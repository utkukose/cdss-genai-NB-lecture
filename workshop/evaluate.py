"""
evaluate.py
The evaluation checklist from the lecture, implemented once so that the workshop can
apply it to any model without rewriting it.

Six things are reported, in this order, because the order matters pedagogically:

    1. Discrimination, with a confidence interval rather than a point estimate
    2. Calibration, which discrimination cannot tell you about
    3. The operating point, chosen from the clinical cost asymmetry
    4. Clinical translation, meaning alerts per hundred patients
    5. Subgroup breakdown, refusing to report where the sample cannot support it
    6. A null comparison, so that a model which learned nothing cannot look impressive

Every function refuses to produce a number it cannot support. A metric computed on
eleven patients is worse than no metric, because it carries the same authority on a
slide.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    brier_score_loss,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)

MIN_SUBGROUP_N = 20
MIN_SUBGROUP_POSITIVES = 10
EPS = 1e-6


# ------------------------------------------------------------------ 1. discrimination


def bootstrap_auc(y_true, y_score, n_boot: int = 2000, seed: int = 0) -> dict:
    """ROC AUC with a percentile bootstrap interval, plus average precision.

    The interval is the point of this function. A small cohort produces an interval wide
    enough to include 0.5, and seeing that is the intended outcome.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    rng = np.random.default_rng(seed)

    point = roc_auc_score(y_true, y_score)
    draws = []
    n = len(y_true)

    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        if len(np.unique(y_true[idx])) < 2:
            continue
        draws.append(roc_auc_score(y_true[idx], y_score[idx]))

    if len(draws) < n_boot * 0.5:
        lo = hi = float("nan")
    else:
        lo, hi = np.percentile(draws, [2.5, 97.5])

    return {
        "auc": float(point),
        "ci_low": float(lo),
        "ci_high": float(hi),
        "average_precision": float(average_precision_score(y_true, y_score)),
        "prevalence": float(np.mean(y_true)),
        "n_bootstrap_usable": len(draws),
    }


# -------------------------------------------------------------------- 2. calibration


def calibration_report(y_true, y_prob, n_bins: int = 5) -> dict:
    """Calibration slope, intercept, Brier score and a binned table.

    A slope below one means the model is over-confident: its high probabilities are too
    high and its low probabilities too low. A slope above one means the opposite.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.clip(np.asarray(y_prob, dtype=float), EPS, 1 - EPS)

    logit = np.log(y_prob / (1 - y_prob)).reshape(-1, 1)
    recalibrator = LogisticRegression(C=1e12, solver="lbfgs", max_iter=1000)
    recalibrator.fit(logit, y_true)
    slope = float(recalibrator.coef_[0][0])
    intercept = float(recalibrator.intercept_[0])

    edges = np.quantile(y_prob, np.linspace(0, 1, n_bins + 1))
    edges = np.unique(edges)
    bins = np.clip(np.digitize(y_prob, edges[1:-1]), 0, len(edges) - 2)

    rows = []
    for b in range(len(edges) - 1):
        mask = bins == b
        if not mask.any():
            continue
        rows.append({
            "bin": b + 1,
            "n": int(mask.sum()),
            "mean_predicted": float(y_prob[mask].mean()),
            "observed_rate": float(y_true[mask].mean()),
        })

    return {
        "slope": slope,
        "intercept": intercept,
        "brier": float(brier_score_loss(y_true, y_prob)),
        "table": pd.DataFrame(rows),
        "verdict": (
            "over-confident, predictions are too extreme" if slope < 0.9
            else "under-confident, predictions are too flat" if slope > 1.1
            else "close to well calibrated on this sample"
        ),
    }


# ---------------------------------------------------------------- 3. operating point


def operating_point(y_true, y_prob, threshold: float) -> dict:
    """Sensitivity, specificity and predictive values at one threshold."""
    y_true = np.asarray(y_true)
    predicted = (np.asarray(y_prob) >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, predicted, labels=[0, 1]).ravel()

    def ratio(num, den):
        return float(num / den) if den else float("nan")

    return {
        "threshold": float(threshold),
        "tp": int(tp), "fp": int(fp), "fn": int(fn), "tn": int(tn),
        "sensitivity": ratio(tp, tp + fn),
        "specificity": ratio(tn, tn + fp),
        "ppv": ratio(tp, tp + fp),
        "npv": ratio(tn, tn + fn),
    }


def threshold_for_sensitivity(y_true, y_prob, target: float = 0.80) -> float:
    """Lowest threshold that still reaches the target sensitivity.

    Used when a miss is more costly than a false alarm, which is the usual case for a
    screening or escalation system. When the cost asymmetry runs the other way, choose
    the threshold from specificity instead.
    """
    fpr, tpr, thresholds = roc_curve(y_true, y_prob)
    reachable = thresholds[tpr >= target]
    return float(reachable.max()) if len(reachable) else 0.0


# ----------------------------------------------------------- 4. clinical translation


def ppv_at_prevalence(sensitivity: float, specificity: float, prevalence: float) -> float:
    """Positive predictive value from Bayes theorem.

    With the Epic Sepsis Model values reported by Wong et al. (2021), sensitivity 0.33
    and specificity 0.83 at a prevalence of 0.07 returns 0.127, reproducing the 12
    percent reported in that paper.
    """
    true_positive = sensitivity * prevalence
    false_positive = (1 - specificity) * (1 - prevalence)
    denominator = true_positive + false_positive
    return float("nan") if denominator == 0 else true_positive / denominator


def alerts_per_hundred(sensitivity: float, specificity: float, prevalence: float) -> dict:
    """Translate an operating point into what a clinician sees on a shift."""
    true_alerts = sensitivity * prevalence * 100
    false_alerts = (1 - specificity) * (1 - prevalence) * 100
    return {
        "alerts_fired": round(true_alerts + false_alerts, 1),
        "true_alerts": round(true_alerts, 1),
        "false_alerts": round(false_alerts, 1),
        "missed_cases": round((1 - sensitivity) * prevalence * 100, 1),
        "ppv": round(ppv_at_prevalence(sensitivity, specificity, prevalence), 3),
    }


def prevalence_table(sensitivity: float, specificity: float,
                     prevalences=(0.01, 0.02, 0.05, 0.07, 0.10, 0.15, 0.20)) -> pd.DataFrame:
    """The lecture's prevalence curve, as a table, for any operating point."""
    rows = []
    for prevalence in prevalences:
        row = alerts_per_hundred(sensitivity, specificity, prevalence)
        row["prevalence"] = prevalence
        rows.append(row)
    order = ["prevalence", "ppv", "alerts_fired", "true_alerts", "false_alerts", "missed_cases"]
    return pd.DataFrame(rows)[order]


# ------------------------------------------------------------ 5. subgroup breakdown


def subgroup_report(y_true, y_prob, groups, threshold: float) -> pd.DataFrame:
    """Per-subgroup metrics, with a refusal where the sample is too small.

    A subgroup below MIN_SUBGROUP_N patients or MIN_SUBGROUP_POSITIVES positive cases
    gets the string 'insufficient sample' instead of a number. Reporting a figure there
    would give a coin flip the same authority as an estimate.
    """
    frame = pd.DataFrame({
        "y": np.asarray(y_true),
        "p": np.asarray(y_prob),
        "group": np.asarray(groups, dtype=object),
    })

    rows = []
    for name, part in frame.groupby("group", dropna=False):
        n = len(part)
        positives = int(part["y"].sum())
        entry = {"group": name, "n": n, "positives": positives}

        if n < MIN_SUBGROUP_N or positives < MIN_SUBGROUP_POSITIVES or part["y"].nunique() < 2:
            entry.update({"auc": "insufficient sample", "sensitivity": "insufficient sample",
                          "specificity": "insufficient sample", "ppv": "insufficient sample"})
        else:
            point = operating_point(part["y"], part["p"], threshold)
            entry.update({
                "auc": round(roc_auc_score(part["y"], part["p"]), 3),
                "sensitivity": round(point["sensitivity"], 3),
                "specificity": round(point["specificity"], 3),
                "ppv": round(point["ppv"], 3),
            })
        rows.append(entry)

    return pd.DataFrame(rows).sort_values("n", ascending=False).reset_index(drop=True)


# -------------------------------------------------------------- 6. null comparison


def null_comparison(y_true, threshold_free: bool = True) -> dict:
    """What a model that always predicts the majority class would achieve."""
    y_true = np.asarray(y_true)
    prevalence = float(np.mean(y_true))
    majority = 1 if prevalence > 0.5 else 0

    return {
        "strategy": f"always predict {majority}",
        "accuracy": float(max(prevalence, 1 - prevalence)),
        "auc": 0.5,
        "sensitivity": 1.0 if majority == 1 else 0.0,
        "specificity": 0.0 if majority == 1 else 1.0,
        "note": "Any model must beat these numbers before it is worth discussing.",
    }


# ------------------------------------------------------------------ orchestration


def honest_report(y_true, y_prob, groups=None, target_sensitivity: float = 0.80,
                  label: str = "model") -> dict:
    """Run the whole checklist and print it with plain language interpretation."""
    y_true = np.asarray(y_true)
    y_prob = np.asarray(y_prob)
    n = len(y_true)
    positives = int(y_true.sum())

    print("=" * 72)
    print(f"HONEST EVALUATION · {label}")
    print("=" * 72)
    print(f"Test set: {n} cases, {positives} positive ({positives / n:.1%})")
    if positives < 25:
        print()
        print("WARNING. Fewer than 25 positive cases in the test set. Every figure below")
        print("is an illustration of the method, not an estimate of performance. Read the")
        print("confidence interval, not the point estimate.")
    print()

    print("1. DISCRIMINATION")
    disc = bootstrap_auc(y_true, y_prob)
    print(f"   ROC AUC            {disc['auc']:.3f}  (95% CI {disc['ci_low']:.3f} to {disc['ci_high']:.3f})")
    print(f"   Average precision  {disc['average_precision']:.3f}  (no-skill value {disc['prevalence']:.3f})")
    if not np.isnan(disc["ci_low"]) and disc["ci_low"] <= 0.5:
        print("   The interval includes 0.5, so this model is not distinguishable from chance.")
    print()

    print("2. CALIBRATION")
    cal = calibration_report(y_true, y_prob)
    print(f"   Slope {cal['slope']:.2f}, intercept {cal['intercept']:.2f}, Brier {cal['brier']:.3f}")
    print(f"   Verdict: {cal['verdict']}")
    print()
    print(cal["table"].to_string(index=False))
    print()

    print("3. OPERATING POINT")
    threshold = threshold_for_sensitivity(y_true, y_prob, target_sensitivity)
    point = operating_point(y_true, y_prob, threshold)
    print(f"   Threshold chosen for sensitivity >= {target_sensitivity:.0%}: {threshold:.3f}")
    print(f"   Sensitivity {point['sensitivity']:.3f}   Specificity {point['specificity']:.3f}")
    print(f"   PPV         {point['ppv']:.3f}   NPV         {point['npv']:.3f}")
    print(f"   Counts: TP {point['tp']}, FP {point['fp']}, FN {point['fn']}, TN {point['tn']}")
    print()

    print("4. CLINICAL TRANSLATION")
    shift = alerts_per_hundred(point["sensitivity"], point["specificity"], disc["prevalence"])
    print(f"   Per 100 patients: {shift['alerts_fired']} alerts fire, "
          f"{shift['true_alerts']} true, {shift['false_alerts']} false.")
    print(f"   {shift['missed_cases']} cases are missed entirely.")
    print()

    print("5. SUBGROUP BREAKDOWN")
    if groups is None:
        print("   No grouping variable supplied.")
        sub = None
    else:
        sub = subgroup_report(y_true, y_prob, groups, threshold)
        print(sub.to_string(index=False))
        refused = (sub["auc"] == "insufficient sample").sum()
        if refused:
            print(f"   {refused} subgroup(s) too small to evaluate. That absence is a finding:")
            print("   a system cannot be shown to be fair for a group it was never tested on.")
    print()

    print("6. NULL COMPARISON")
    null = null_comparison(y_true)
    print(f"   {null['strategy']}: accuracy {null['accuracy']:.3f}, AUC {null['auc']:.2f}")
    print(f"   {null['note']}")
    print("=" * 72)

    return {"discrimination": disc, "calibration": cal, "operating_point": point,
            "clinical": shift, "subgroups": sub, "null": null, "threshold": threshold}


def plot_curves(y_true, y_prob, calibration_bins: int = 5):
    """ROC curve and calibration curve side by side."""
    import matplotlib.pyplot as plt

    fpr, tpr, _ = roc_curve(y_true, y_prob)
    cal = calibration_report(y_true, y_prob, calibration_bins)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))

    axes[0].plot(fpr, tpr, color="#C2185B", linewidth=2.2)
    axes[0].plot([0, 1], [0, 1], color="#6B7590", linestyle="--", linewidth=1.2)
    axes[0].set_xlabel("1 - specificity")
    axes[0].set_ylabel("sensitivity")
    axes[0].set_title(f"ROC, AUC = {roc_auc_score(y_true, y_prob):.3f}")

    table = cal["table"]
    axes[1].plot(table["mean_predicted"], table["observed_rate"],
                 marker="o", color="#0E7C7B", linewidth=2.2)
    axes[1].plot([0, 1], [0, 1], color="#6B7590", linestyle="--", linewidth=1.2)
    axes[1].set_xlabel("mean predicted probability")
    axes[1].set_ylabel("observed rate")
    axes[1].set_title(f"Calibration, slope = {cal['slope']:.2f}")

    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    return fig
