"""
pipeline.py
The baseline built in NB3, packaged so that the later notebooks can rebuild it without
repeating the code.

NB3 writes this pipeline out in full, because seeing where the split happens and where
the preprocessing is fitted is the point of that notebook. From NB4 onward the model is
scaffolding rather than subject matter, so it is rebuilt with one call.

The guarantees carried over from NB3 are unchanged and worth restating.

    The split is by patient, not by stay, so no patient appears on both sides.
    Every preprocessing step lives inside the pipeline, so nothing is fitted on the
    test set.
    The outcome and the identifier columns never reach the model.
"""

from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

import mimic_web as mw


def split_by_patient(cohort: pd.DataFrame, test_size: float = 0.30, seed: int = 42):
    """Hold out whole patients, never individual stays."""
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    train_idx, test_idx = next(
        splitter.split(cohort, cohort["prolonged_stay"], groups=cohort["subject_id"])
    )
    return cohort.iloc[train_idx].copy(), cohort.iloc[test_idx].copy()


def build_baseline(train: pd.DataFrame, features: list) -> Pipeline:
    """Fit the NB3 baseline: median and mode imputation, scaling, one hot, logistic."""
    numeric = train[features].select_dtypes(include="number").columns.tolist()
    categorical = [c for c in features if c not in numeric]

    blocks = []
    if numeric:
        blocks.append(("num", Pipeline([
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]), numeric))
    if categorical:
        blocks.append(("cat", Pipeline([
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("encode", OneHotEncoder(handle_unknown="ignore")),
        ]), categorical))

    model = Pipeline([
        ("prepare", ColumnTransformer(blocks)),
        ("clf", LogisticRegression(max_iter=2000, class_weight="balanced")),
    ])
    model.fit(train[features], train["prolonged_stay"])
    return model


def prepare(test_size: float = 0.30, seed: int = 42, verbose: bool = True) -> dict:
    """Call the data, split it, fit the baseline, and return everything downstream needs."""
    cohort = mw.build_cohort(verbose=verbose)
    features = mw.feature_columns(cohort)
    train, test = split_by_patient(cohort, test_size, seed)
    model = build_baseline(train, features)
    probabilities = model.predict_proba(test[features])[:, 1]

    if verbose:
        print()
        print(f"Baseline rebuilt. Train {len(train)} stays, test {len(test)} stays, "
              f"{len(features)} features.")

    return {
        "cohort": cohort,
        "features": features,
        "train": train,
        "test": test,
        "model": model,
        "probabilities": probabilities,
        "y_test": test["prolonged_stay"].values,
    }
