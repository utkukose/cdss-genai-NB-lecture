"""
explain.py
Explanation for the workshop prototype, at two levels.

Two methods are used, and the difference between them is part of the teaching.

Permutation importance is model agnostic. It asks what happens to performance when one
feature is shuffled, so it measures how much the model relies on that feature. It works
for any model and needs no extra library.

Linear contribution decomposition is exact rather than approximate. For a logistic
regression the log odds is a sum of coefficient times feature value, so the contribution
of each feature to one prediction can be read off directly. Nothing is estimated.

That exactness is the point. When the workshop moves to a non-linear model, the same
decomposition is no longer available and a post hoc approximation such as SHAP is needed.
Participants should see the exact version first, so that they understand what the
approximation is approximating.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.inspection import permutation_importance


# ------------------------------------------------------------------------ global


def permutation_global(model, X, y, n_repeats: int = 20, scoring: str = "roc_auc",
                       seed: int = 0, top: int = 15) -> pd.DataFrame:
    """Model agnostic global importance, with the spread across repeats.

    The standard deviation column matters as much as the mean. On a small cohort the
    spread is often larger than the difference between neighbouring features, which
    means the ranking itself is unstable and should not be reported as an ordering.
    """
    result = permutation_importance(
        model, X, y, n_repeats=n_repeats, scoring=scoring, random_state=seed
    )
    frame = pd.DataFrame({
        "feature": list(X.columns),
        "importance": result.importances_mean,
        "sd": result.importances_std,
    })
    frame["ranking_is_stable"] = frame["importance"] > 2 * frame["sd"]
    return frame.sort_values("importance", ascending=False).head(top).reset_index(drop=True)


def linear_coefficients(model, top: int = 15) -> pd.DataFrame:
    """Coefficients of a linear final step, on the transformed feature scale."""
    classifier = model[-1]
    if not hasattr(classifier, "coef_"):
        raise TypeError("The final pipeline step is not linear, so it has no coefficients.")

    names = _transformed_names(model)
    frame = pd.DataFrame({"feature": names, "coefficient": classifier.coef_[0]})
    frame["odds_ratio"] = np.exp(frame["coefficient"])
    frame["magnitude"] = frame["coefficient"].abs()
    return frame.sort_values("magnitude", ascending=False).head(top).drop(
        columns="magnitude").reset_index(drop=True)


# ------------------------------------------------------------------------- local


def _transformed_names(model) -> list:
    """Feature names after the preprocessing steps, with a positional fallback."""
    try:
        return list(model[:-1].get_feature_names_out())
    except Exception:  # noqa: BLE001
        width = model[-1].coef_.shape[1]
        return [f"feature_{i}" for i in range(width)]


def linear_contributions(model, X_row: pd.DataFrame, top: int = 12) -> pd.DataFrame:
    """Exact per-feature contribution to the log odds for one case.

    The contributions plus the intercept sum to the log odds of the prediction. This is
    an identity, not an estimate, so there is no approximation error to argue about.
    """
    if X_row.shape[0] != 1:
        raise ValueError("Pass exactly one row.")

    classifier = model[-1]
    transformed = np.asarray(model[:-1].transform(X_row)).ravel()
    coefficients = classifier.coef_[0]
    contributions = coefficients * transformed

    frame = pd.DataFrame({
        "feature": _transformed_names(model),
        "value_after_preprocessing": transformed,
        "coefficient": coefficients,
        "contribution_to_log_odds": contributions,
    })
    frame["magnitude"] = frame["contribution_to_log_odds"].abs()
    frame = frame.sort_values("magnitude", ascending=False).drop(columns="magnitude")
    return frame.head(top).reset_index(drop=True)


def explain_case(model, X: pd.DataFrame, index: int, top: int = 10) -> dict:
    """Everything needed to discuss one prediction with a clinician."""
    row = X.iloc[[index]]
    probability = float(model.predict_proba(row)[0, 1])
    contributions = linear_contributions(model, row, top=top)
    intercept = float(model[-1].intercept_[0])
    total = float(linear_contributions(model, row, top=10**6)["contribution_to_log_odds"].sum())

    return {
        "index": index,
        "probability": probability,
        "log_odds": intercept + total,
        "intercept": intercept,
        "contributions": contributions,
        "raw_values": row.iloc[0],
    }


def pick_cases(y_true, y_prob, threshold: float) -> dict:
    """Find one true positive, one false positive and one false negative.

    The false positive is the important one. An explanation that makes a wrong
    prediction look reasonable is how explanation launders error, and that has to be
    seen rather than described.
    """
    y_true = np.asarray(y_true)
    y_prob = np.asarray(y_prob)
    predicted = (y_prob >= threshold).astype(int)

    def first(mask, order_by, descending=True):
        idx = np.where(mask)[0]
        if len(idx) == 0:
            return None
        ranked = idx[np.argsort(order_by[idx])]
        return int(ranked[-1] if descending else ranked[0])

    return {
        "true_positive": first((y_true == 1) & (predicted == 1), y_prob),
        "false_positive": first((y_true == 0) & (predicted == 1), y_prob),
        "false_negative": first((y_true == 1) & (predicted == 0), y_prob, descending=False),
        "true_negative": first((y_true == 0) & (predicted == 0), y_prob, descending=False),
    }


# ------------------------------------------------------------------------- plots


def plot_global(importance: pd.DataFrame, title: str = "Permutation importance"):
    """Horizontal bars, with the repeat spread drawn as an error bar."""
    import matplotlib.pyplot as plt

    frame = importance.iloc[::-1]
    fig, ax = plt.subplots(figsize=(8, 0.36 * len(frame) + 1.4))
    ax.barh(frame["feature"], frame["importance"],
            xerr=frame.get("sd"), color="#C2185B", ecolor="#6B7590", capsize=3)
    ax.axvline(0, color="#16213C", linewidth=1)
    ax.set_xlabel("drop in ROC AUC when the feature is shuffled")
    ax.set_title(title)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig


def plot_case(explanation: dict, title: str | None = None):
    """Contributions for one case, coloured by direction."""
    import matplotlib.pyplot as plt

    frame = explanation["contributions"].iloc[::-1]
    colours = ["#C2185B" if v > 0 else "#0E7C7B"
               for v in frame["contribution_to_log_odds"]]

    fig, ax = plt.subplots(figsize=(8, 0.36 * len(frame) + 1.6))
    ax.barh(frame["feature"], frame["contribution_to_log_odds"], color=colours)
    ax.axvline(0, color="#16213C", linewidth=1)
    ax.set_xlabel("contribution to log odds")
    ax.set_title(title or f"case {explanation['index']}, "
                          f"predicted probability {explanation['probability']:.3f}")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig
