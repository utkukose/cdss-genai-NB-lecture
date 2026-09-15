"""
mimic_web.py
Web-callable loader for the shared workshop scenario.

The MIMIC-IV Clinical Database Demo (v2.2) is open access under the Open Data Commons
Open Database License. No credentialing is required, and the files can be read directly
over HTTPS, which is what this module does. Nothing is stored beyond an optional local
cache inside the runtime.

    Johnson, A., Bulgarelli, L., Pollard, T., Horng, S., Celi, L. A., & Mark, R. (2023).
    MIMIC-IV Clinical Database Demo (version 2.2). PhysioNet.
    https://doi.org/10.13026/dp1f-ex47

Shared scenario
---------------
Target      Prolonged ICU stay, defined as length of stay greater than three days.
Decision    At the moment of ICU admission, six hours after arrival.
User        The intensivist or bed manager planning capacity and escalation.
Inputs      Demographics, admission context, and the first six hours of vitals and labs.

The cohort is small. One hundred patients is not enough to train a deployable model, and
the evaluation step is expected to show that.
"""

from __future__ import annotations

import os
import warnings

import numpy as np
import pandas as pd

BASE_URL = "https://physionet.org/files/mimic-iv-demo/2.2"
CACHE_DIR = "mimic_demo_cache"

# Chart item identifiers used by the MIMIC-IV MetaVision export. Each is validated
# against d_items at load time rather than trusted blindly.
VITAL_ITEMS = {
    "heart_rate": [220045],
    "sbp": [220179, 220050],
    "dbp": [220180, 220051],
    "map": [220181, 220052],
    "resp_rate": [220210],
    "spo2": [220277],
    "temp_c": [223762],
    "temp_f": [223761],
}

# Laboratory tests are resolved by label rather than by hard-coded identifier, because
# label lookup fails loudly while a wrong identifier fails silently.
LAB_LABELS = {
    "creatinine": "Creatinine",
    "wbc": "White Blood Cells",
    "hematocrit": "Hematocrit",
    "sodium": "Sodium",
    "potassium": "Potassium",
    "bicarbonate": "Bicarbonate",
    "bun": "Urea Nitrogen",
    "glucose": "Glucose",
    "platelets": "Platelet Count",
    "lactate": "Lactate",
}

OBSERVATION_HOURS = 6
TARGET_LOS_DAYS = 3.0


# --------------------------------------------------------------------------- loading


def load_table(module: str, table: str, use_cache: bool = True, **kwargs) -> pd.DataFrame:
    """Read one MIMIC-IV demo table straight from PhysioNet.

    module is 'hosp' or 'icu'. table is the file stem, for example 'patients'.
    """
    url = f"{BASE_URL}/{module}/{table}.csv.gz"
    cache_path = os.path.join(CACHE_DIR, f"{module}__{table}.csv.gz")

    if use_cache and os.path.exists(cache_path):
        return pd.read_csv(cache_path, compression="gzip", low_memory=False, **kwargs)

    frame = pd.read_csv(url, compression="gzip", low_memory=False, **kwargs)

    if use_cache:
        os.makedirs(CACHE_DIR, exist_ok=True)
        frame.to_csv(cache_path, index=False, compression="gzip")

    return frame


def check_connection() -> bool:
    """Fetch the smallest file in the archive to confirm the network path works.

    Run this first in a workshop. It fails in under a second if the venue blocks the
    host, which leaves time to switch to the synthetic track.
    """
    try:
        ids = pd.read_csv(f"{BASE_URL}/demo_subject_id.csv")
        print(f"PhysioNet reachable. Demo contains {len(ids)} subject identifiers.")
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"PhysioNet not reachable: {type(exc).__name__}: {exc}")
        print("Use the synthetic cohort track instead (prompt 2a).")
        return False


# ----------------------------------------------------------------- feature assembly


def _first_window_stats(
    events: pd.DataFrame,
    index: pd.DataFrame,
    value_col: str,
    time_col: str,
    key: str,
    name: str,
) -> pd.DataFrame:
    """Summarise one measurement over the first observation window of each stay.

    The window is closed on both sides at admission and admission plus
    OBSERVATION_HOURS. Anything recorded later is dropped, because it would not be
    available at the decision point.
    """
    merged = events.merge(index[[key, "intime"]], on=key, how="inner")
    elapsed = (merged[time_col] - merged["intime"]).dt.total_seconds() / 3600.0
    within = merged[(elapsed >= 0) & (elapsed <= OBSERVATION_HOURS)]

    if within.empty:
        return pd.DataFrame(columns=[key, f"{name}_min", f"{name}_max", f"{name}_mean", f"{name}_n"])

    stats = (
        within.groupby(key)[value_col]
        .agg(["min", "max", "mean", "count"])
        .rename(
            columns={
                "min": f"{name}_min",
                "max": f"{name}_max",
                "mean": f"{name}_mean",
                "count": f"{name}_n",
            }
        )
        .reset_index()
    )
    return stats


def _resolve_lab_itemids(d_labitems: pd.DataFrame) -> dict:
    """Map friendly names to itemids, preferring blood specimens."""
    resolved = {}
    for name, label in LAB_LABELS.items():
        match = d_labitems[d_labitems["label"].astype(str).str.strip().str.lower() == label.lower()]
        if "fluid" in match.columns:
            blood = match[match["fluid"].astype(str).str.lower() == "blood"]
            if not blood.empty:
                match = blood
        if match.empty:
            warnings.warn(f"Lab not found in d_labitems and skipped: {label}", stacklevel=2)
            continue
        resolved[name] = match["itemid"].tolist()
    return resolved


def _validate_vital_itemids(d_items: pd.DataFrame) -> dict:
    """Keep only chart itemids that actually exist in this release."""
    available = set(d_items["itemid"].tolist())
    resolved = {}
    for name, ids in VITAL_ITEMS.items():
        present = [i for i in ids if i in available]
        if not present:
            warnings.warn(f"Vital sign not found in d_items and skipped: {name}", stacklevel=2)
            continue
        resolved[name] = present
    return resolved


def build_cohort(use_cache: bool = True, verbose: bool = True) -> pd.DataFrame:
    """Assemble the shared cohort, one row per ICU stay.

    Every feature is restricted to the first OBSERVATION_HOURS after ICU admission, so
    no column can carry information from after the decision point. The outcome column is
    named 'prolonged_stay'.
    """
    icustays = load_table("icu", "icustays", use_cache)
    patients = load_table("hosp", "patients", use_cache)
    admissions = load_table("hosp", "admissions", use_cache)

    icustays["intime"] = pd.to_datetime(icustays["intime"])
    icustays["outtime"] = pd.to_datetime(icustays["outtime"])

    # A stay shorter than the observation window has no window to observe, so the
    # decision point never arrives and the stay cannot be included.
    cohort = icustays[icustays["los"] >= OBSERVATION_HOURS / 24.0].copy()
    cohort["prolonged_stay"] = (cohort["los"] > TARGET_LOS_DAYS).astype(int)

    demographic_cols = ["subject_id", "gender", "anchor_age"]
    cohort = cohort.merge(patients[demographic_cols], on="subject_id", how="left")

    context_cols = [c for c in ["hadm_id", "admission_type", "admission_location",
                               "insurance", "marital_status", "race"] if c in admissions.columns]
    cohort = cohort.merge(admissions[context_cols], on="hadm_id", how="left")

    # ---- vital signs
    d_items = load_table("icu", "d_items", use_cache)
    vitals = _validate_vital_itemids(d_items)
    wanted_ids = [i for ids in vitals.values() for i in ids]

    chartevents = load_table("icu", "chartevents", use_cache)
    chartevents = chartevents[chartevents["itemid"].isin(wanted_ids)].copy()
    chartevents["charttime"] = pd.to_datetime(chartevents["charttime"])
    chartevents = chartevents.dropna(subset=["valuenum"])

    for name, ids in vitals.items():
        subset = chartevents[chartevents["itemid"].isin(ids)]
        if subset.empty:
            continue
        stats = _first_window_stats(subset, cohort, "valuenum", "charttime", "stay_id", name)
        cohort = cohort.merge(stats, on="stay_id", how="left")

    # ---- laboratory results
    d_labitems = load_table("hosp", "d_labitems", use_cache)
    labs_map = _resolve_lab_itemids(d_labitems)
    lab_ids = [i for ids in labs_map.values() for i in ids]

    labevents = load_table("hosp", "labevents", use_cache)
    labevents = labevents[labevents["itemid"].isin(lab_ids)].copy()
    labevents["charttime"] = pd.to_datetime(labevents["charttime"])
    labevents = labevents.dropna(subset=["valuenum"])

    stay_index = cohort[["stay_id", "hadm_id", "intime"]]
    for name, ids in labs_map.items():
        subset = labevents[labevents["itemid"].isin(ids)]
        if subset.empty:
            continue
        joined = subset.merge(stay_index[["stay_id", "hadm_id"]], on="hadm_id", how="inner")
        stats = _first_window_stats(joined, cohort, "valuenum", "charttime", "stay_id", f"lab_{name}")
        cohort = cohort.merge(stats, on="stay_id", how="left")

    # Columns that describe the stay after it has finished must not reach the model.
    leaky = ["outtime", "los", "last_careunit"]
    cohort = cohort.drop(columns=[c for c in leaky if c in cohort.columns])

    if verbose:
        describe(cohort)

    return cohort


# --------------------------------------------------------------------- diagnostics


def describe(cohort: pd.DataFrame) -> None:
    """Print the honest summary that should be read before any modelling."""
    n = len(cohort)
    positives = int(cohort["prolonged_stay"].sum())
    prevalence = positives / n if n else float("nan")

    print("Shared workshop cohort")
    print(f"  ICU stays            {n}")
    print(f"  Unique patients      {cohort['subject_id'].nunique()}")
    print(f"  Prolonged stays      {positives}  ({prevalence:.1%})")
    print(f"  Feature columns      {cohort.shape[1] - 1}")
    print(f"  Observation window   first {OBSERVATION_HOURS} hours after ICU admission")
    print(f"  Outcome definition   ICU length of stay greater than {TARGET_LOS_DAYS} days")
    print()
    print("  Read this before modelling:")
    print("  A cohort of this size cannot support a deployable model. With this many")
    print("  positives, a confidence interval on any performance estimate will be wide")
    print("  enough to include chance. Treat every number produced downstream as a")
    print("  demonstration of the method, never as evidence about the method's result.")

    missing = cohort.isna().mean().sort_values(ascending=False)
    heavy = missing[missing > 0.5]
    if len(heavy):
        print()
        print(f"  {len(heavy)} columns are more than half missing. The highest are:")
        for col, frac in heavy.head(5).items():
            print(f"    {col:<28} {frac:.0%}")


def feature_columns(cohort: pd.DataFrame) -> list:
    """Columns safe to hand to a model, with identifiers and the outcome removed."""
    drop = {"subject_id", "hadm_id", "stay_id", "intime", "prolonged_stay"}
    return [c for c in cohort.columns if c not in drop]


# ------------------------------------------------------- lecture linked calculators


def ppv_at_prevalence(sensitivity: float, specificity: float, prevalence: float) -> float:
    """Positive predictive value from Bayes theorem.

    This is the calculation behind the prevalence curve in the lecture. With the Epic
    Sepsis Model values reported by Wong et al. (2021), sensitivity 0.33 and specificity
    0.83 at a prevalence of 0.07 returns 0.127, which reproduces the 12 percent they
    report.
    """
    true_positive = sensitivity * prevalence
    false_positive = (1 - specificity) * (1 - prevalence)
    denominator = true_positive + false_positive
    return float("nan") if denominator == 0 else true_positive / denominator


def alerts_per_hundred(sensitivity: float, specificity: float, prevalence: float) -> dict:
    """Translate an operating point into what a clinician would see on a shift."""
    true_alerts = sensitivity * prevalence * 100
    false_alerts = (1 - specificity) * (1 - prevalence) * 100
    missed = (1 - sensitivity) * prevalence * 100
    return {
        "alerts_fired": round(true_alerts + false_alerts, 1),
        "true_alerts": round(true_alerts, 1),
        "false_alerts": round(false_alerts, 1),
        "missed_cases": round(missed, 1),
        "ppv": round(ppv_at_prevalence(sensitivity, specificity, prevalence), 3),
    }


def prevalence_table(sensitivity: float, specificity: float,
                     prevalences=(0.01, 0.02, 0.05, 0.07, 0.10, 0.15, 0.20)) -> pd.DataFrame:
    """Reproduce the lecture's prevalence curve as a table for any operating point."""
    rows = []
    for prevalence in prevalences:
        row = alerts_per_hundred(sensitivity, specificity, prevalence)
        row["prevalence"] = prevalence
        rows.append(row)
    columns = ["prevalence", "ppv", "alerts_fired", "true_alerts", "false_alerts", "missed_cases"]
    return pd.DataFrame(rows)[columns]


if __name__ == "__main__":
    if check_connection():
        data = build_cohort()
        print()
        print(data.head())
