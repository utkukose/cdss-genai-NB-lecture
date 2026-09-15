"""
safety.py
Three guardrails placed between a model and a clinician.

    Abstention          The system may decline to answer.
    Drift detection     The system may notice that this patient is unlike its training set.
    Input validation    The system may refuse an impossible value instead of predicting on it.

One design decision runs through this module and should be read before the code.

Every bound used here is derived from the training data, never asserted from memory. A
physiological range typed into a source file without a citation is the first anti-pattern
in the workshop list, and a module that teaches against that pattern cannot practise it.
Where a clinician supplies sourced limits, PhysiologicalValidator uses them and records
the source. Where nobody has, it says so in its own report rather than pretending the
data-derived envelope is clinical knowledge.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

ABSTAIN = "abstain, clinician review required"
ALERT = "alert"
NO_ALERT = "no alert"


# --------------------------------------------------------------------- abstention


def choose_band(y_true, y_prob, threshold: float, max_abstain: float = 0.20,
                steps: int = 200) -> dict:
    """Widen a band around the threshold until the abstention budget is spent.

    The band is chosen from the data rather than picked. It is then audited: the report
    compares accuracy inside the band against accuracy outside it. If the two are
    similar, the band is not isolating genuine uncertainty and should be abandoned
    rather than kept for appearances.
    """
    y_true = np.asarray(y_true)
    y_prob = np.asarray(y_prob)
    predicted = (y_prob >= threshold).astype(int)

    best = 0.0
    for delta in np.linspace(0, 0.5, steps):
        inside = np.abs(y_prob - threshold) <= delta
        if inside.mean() > max_abstain:
            break
        best = delta

    inside = np.abs(y_prob - threshold) <= best
    outside = ~inside

    def accuracy(mask):
        return float((predicted[mask] == y_true[mask]).mean()) if mask.any() else float("nan")

    return {
        "threshold": float(threshold),
        "band": float(best),
        "low": float(threshold - best),
        "high": float(threshold + best),
        "abstain_fraction": float(inside.mean()),
        "accuracy_inside_band": accuracy(inside),
        "accuracy_outside_band": accuracy(outside),
        "verdict": _band_verdict(accuracy(inside), accuracy(outside)),
    }


def _band_verdict(inside: float, outside: float) -> str:
    if np.isnan(inside) or np.isnan(outside):
        return "not assessable on this sample"
    gap = outside - inside
    if gap > 0.15:
        return "the band isolates genuinely uncertain cases and is worth keeping"
    if gap > 0.05:
        return "the band helps modestly"
    return ("the band is not isolating uncertainty on this sample, so abstaining here "
            "costs coverage without buying reliability")


class AbstentionPolicy:
    """Turn a probability into one of three answers rather than two."""

    def __init__(self, threshold: float, band: float):
        self.threshold = float(threshold)
        self.band = float(band)

    def decide(self, probability: float) -> str:
        if abs(probability - self.threshold) <= self.band:
            return ABSTAIN
        return ALERT if probability >= self.threshold else NO_ALERT

    def decide_many(self, probabilities) -> np.ndarray:
        return np.array([self.decide(float(p)) for p in np.asarray(probabilities)])


# ------------------------------------------------------------ distribution checks


class DriftDetector:
    """Flag a case that does not resemble the training population.

    Robust statistics are used because a cohort this small is easily dominated by a few
    extreme values. Each numeric feature gets a median and a median absolute deviation,
    and a case is scored by how many of its features sit far outside that envelope.
    """

    def __init__(self, z_limit: float = 4.0, feature_fraction: float = 0.10):
        self.z_limit = z_limit
        self.feature_fraction = feature_fraction
        self.medians_ = None
        self.scales_ = None
        self.columns_ = None

    def fit(self, X: pd.DataFrame) -> "DriftDetector":
        numeric = X.select_dtypes(include="number")
        self.columns_ = list(numeric.columns)
        self.medians_ = numeric.median()
        mad = (numeric - self.medians_).abs().median() * 1.4826
        # A zero scale means the feature is constant in training, so any deviation at
        # all is out of distribution. Fall back to a small positive value.
        self.scales_ = mad.replace(0, np.nan).fillna(numeric.std().replace(0, 1e-6))
        return self

    def score(self, X: pd.DataFrame) -> pd.DataFrame:
        numeric = X[self.columns_]
        z = (numeric - self.medians_).abs() / self.scales_
        far = (z > self.z_limit)
        return pd.DataFrame({
            "features_out_of_range": far.sum(axis=1).values,
            "fraction_out_of_range": far.mean(axis=1).values,
            "max_robust_z": z.max(axis=1).values,
            "out_of_distribution": (far.mean(axis=1) > self.feature_fraction).values,
        }, index=X.index)

    def explain(self, X_row: pd.DataFrame, top: int = 5) -> pd.DataFrame:
        """Which features put this case outside the envelope."""
        numeric = X_row[self.columns_]
        z = ((numeric - self.medians_).abs() / self.scales_).iloc[0]
        frame = pd.DataFrame({
            "feature": z.index,
            "value": numeric.iloc[0].values,
            "training_median": self.medians_.values,
            "robust_z": z.values,
        })
        return frame.sort_values("robust_z", ascending=False).head(top).reset_index(drop=True)


# ------------------------------------------------------------- input validation


class PhysiologicalValidator:
    """Reject impossible values before they reach the model.

    Two sources of bounds are kept separate on purpose.

    Data-derived bounds come from a wide quantile envelope of the training set. They
    catch transcription errors such as a heart rate of 8000, and nothing more. They are
    not clinical knowledge and the report says so.

    Clinician bounds are supplied by a person, with a source recorded alongside. Only
    these carry clinical authority. Until they are supplied, the validator reports the
    gap rather than filling it.
    """

    def __init__(self, lower_quantile: float = 0.001, upper_quantile: float = 0.999,
                 slack: float = 3.0):
        self.lower_quantile = lower_quantile
        self.upper_quantile = upper_quantile
        self.slack = slack
        self.data_bounds_ = None
        self.clinician_bounds_ = {}
        self.sources_ = {}

    def fit(self, X: pd.DataFrame) -> "PhysiologicalValidator":
        numeric = X.select_dtypes(include="number")
        low = numeric.quantile(self.lower_quantile)
        high = numeric.quantile(self.upper_quantile)
        span = (high - low).replace(0, 1.0)
        self.data_bounds_ = pd.DataFrame({
            "low": low - self.slack * span,
            "high": high + self.slack * span,
        })
        return self

    def set_clinician_bounds(self, feature: str, low: float, high: float, source: str):
        """Record a sourced clinical limit. The source string is required."""
        if not source or not str(source).strip():
            raise ValueError(
                "A source is required. An unsourced clinical bound is the first "
                "anti-pattern in this workshop."
            )
        self.clinician_bounds_[feature] = (float(low), float(high))
        self.sources_[feature] = source
        return self

    def validate(self, X_row: pd.DataFrame) -> dict:
        problems = []
        row = X_row.iloc[0]

        for feature, (low, high) in self.clinician_bounds_.items():
            value = row.get(feature)
            if value is not None and not pd.isna(value) and not (low <= value <= high):
                problems.append({
                    "feature": feature, "value": float(value),
                    "bound": f"{low} to {high}", "basis": f"clinician, {self.sources_[feature]}",
                })

        for feature in self.data_bounds_.index:
            if feature in self.clinician_bounds_:
                continue
            value = row.get(feature)
            if value is None or pd.isna(value):
                continue
            low = self.data_bounds_.loc[feature, "low"]
            high = self.data_bounds_.loc[feature, "high"]
            if not (low <= value <= high):
                problems.append({
                    "feature": feature, "value": float(value),
                    "bound": f"{low:.1f} to {high:.1f}",
                    "basis": "data-derived envelope, not a clinical limit",
                })

        return {"valid": not problems, "problems": problems}

    def coverage_report(self) -> str:
        total = len(self.data_bounds_.index)
        sourced = len(self.clinician_bounds_)
        lines = [
            f"Numeric features: {total}",
            f"With sourced clinical bounds: {sourced}",
            f"Relying on the data-derived envelope only: {total - sourced}",
        ]
        if sourced < total:
            lines += [
                "",
                "The data-derived envelope catches transcription errors and nothing more.",
                "It cannot detect a value that is possible in arithmetic but impossible in",
                "a patient. Supplying sourced bounds for the clinically important features",
                "is a task for a clinician, not for this module and not for a language model.",
            ]
        return "\n".join(lines)


# --------------------------------------------------------------- assembled system


class GuardedModel:
    """A fitted model behind all three guardrails."""

    def __init__(self, model, policy: AbstentionPolicy,
                 drift: DriftDetector, validator: PhysiologicalValidator):
        self.model = model
        self.policy = policy
        self.drift = drift
        self.validator = validator

    def predict_one(self, X_row: pd.DataFrame) -> dict:
        check = self.validator.validate(X_row)
        if not check["valid"]:
            return {"decision": "rejected, implausible input", "probability": None,
                    "reason": check["problems"]}

        drift = self.drift.score(X_row).iloc[0]
        probability = float(self.model.predict_proba(X_row)[0, 1])

        if bool(drift["out_of_distribution"]):
            return {"decision": "withheld, patient unlike the training population",
                    "probability": probability,
                    "reason": self.drift.explain(X_row).to_dict("records")}

        return {"decision": self.policy.decide(probability), "probability": probability,
                "reason": None}


def red_team(guarded: "GuardedModel", X: pd.DataFrame, seed: int = 0) -> pd.DataFrame:
    """Five constructed cases that push the system, including a plausible one.

    The clinically plausible case matters most. A system that only fails on obviously
    broken input has not been tested, because obviously broken input rarely reaches a
    production model.
    """
    rng = np.random.default_rng(seed)
    numeric = list(X.select_dtypes(include="number").columns)
    base = X.iloc[[int(rng.integers(0, len(X)))]].copy()
    # Integer columns cannot hold the values constructed below, so widen them first.
    for column in numeric:
        base[column] = base[column].astype(float)

    cases = {"typical case, unchanged": base.copy()}

    if numeric:
        impossible = base.copy()
        impossible.loc[impossible.index[0], numeric[0]] = 1e6
        cases[f"impossible value in {numeric[0]}"] = impossible

        extreme = base.copy()
        for column in numeric[: max(1, len(numeric) // 3)]:
            extreme.loc[extreme.index[0], column] = (
                float(X[column].median()) + 8 * float(X[column].std() or 1)
            )
        cases["many features far from the training median"] = extreme

        # The case that matters. Nothing here is broken or impossible: one feature sits
        # at the far edge of what the training set contains, which is exactly the kind
        # of patient a deployed system meets and a synthetic test never covers.
        plausible = base.copy()
        edge_feature = numeric[min(1, len(numeric) - 1)]
        plausible.loc[plausible.index[0], edge_feature] = float(X[edge_feature].quantile(0.99))
        cases[f"clinically plausible, {edge_feature} at the 99th percentile"] = plausible

    empty = base.copy()
    empty.loc[empty.index[0], :] = np.nan
    cases["every value missing"] = empty

    rows = []
    for name, case in cases.items():
        try:
            result = guarded.predict_one(case)
            probability = result["probability"]
            rows.append({
                "case": name,
                "decision": result["decision"],
                "probability": None if probability is None else round(probability, 3),
            })
        except Exception as exc:  # noqa: BLE001
            rows.append({"case": name, "decision": f"crashed: {type(exc).__name__}",
                         "probability": None})

    return pd.DataFrame(rows)
