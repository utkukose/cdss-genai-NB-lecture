# Anti-patterns · Errors generative AI makes in clinical code

This list is the reference used when auditing generated code during the workshop. Every
item describes a failure mode encountered in practice, and all of them share one property:
the code runs, raises no error, and looks correct when read.

The check cells in the notebooks and the contracts at the end of each prompt are designed
to catch the errors listed here. This document explains why the checks look where they do.

---

## 1. The fabricated clinical threshold

**What happens.** The model writes a cut-off value with no traceable source into the code
in confident language. Values such as 2 mmol/L for lactate, 1.2 mg/dL for creatinine or a
two point rise in SOFA are sometimes correct, sometimes approximate and sometimes entirely
invented. All three arrive in the same register.

**Why it is dangerous.** Correct values and invented ones cannot be told apart by their
form. A comment reading "standard clinical cutoff" does not mean the cut-off exists.

**How it is caught.** Ask for the source of every constant in the generated code. Values
with no source are marked `UNSOURCED` in the code and remain so until a clinician confirms
them.

**Example.**

```python
# As produced by the model
LACTATE_THRESHOLD = 2.0  # standard clinical cutoff for sepsis

# After the audit
LACTATE_THRESHOLD = 2.0  # UNSOURCED: verify. Lactate above 2 mmol/L is a component of
                         # the Sepsis-3 definition of septic shock, but it is being used
                         # here for a different purpose in a different population.
```

---

## 2. Silent leakage: preprocessing fitted before the split

**What happens.** A scaler, imputer or encoder is fitted across the whole dataset before
the training and test split. The mean or median of the test set is carried into training.

**Why it is dangerous.** No warning is raised. Performance improves, and the order of the
steps looks sensible when the code is read.

**How it is caught.** The whole preprocessing chain is placed inside a `Pipeline`, which
makes the error structurally impossible. The model check in NB3 tests whether a Pipeline
was used.

**Example.**

```python
# Leaking
X = SimpleImputer().fit_transform(X)
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Correct
X_train, X_test, y_train, y_test = train_test_split(X, y)
pipe = Pipeline([("impute", SimpleImputer()), ("scale", StandardScaler()), ("clf", model)])
pipe.fit(X_train, y_train)
```

---

## 3. Target leakage: a consequence of the outcome becomes a feature

**What happens.** A variable recorded after the outcome is given to the model as an input.
An antibiotic order in a sepsis model, an intensive care bed number in a transfer model or
a discharge type in a mortality model are all instances.

**Why it is dangerous.** Performance rises dramatically and the rise looks like success at
first sight. Once the model is deployed, the variable is not yet populated at the decision
moment and the system does not work.

**How it is caught.** One question is asked of every feature: was this value present in the
record at the decision moment? The contracts in NB2 make this explicit. The six hour window
in the data module, and the removal of the `los` and `outtime` columns, exist for this
reason.

**Warning sign.** An area under the curve above 0.95 on a genuinely difficult clinical
problem is almost always the signature of an error. Look for leakage before celebrating.

---

## 4. Splitting at row level rather than patient level

**What happens.** Where a patient has more than one record, `train_test_split` divides rows
at random by default and one record of a patient falls into training while another falls
into test.

**Why it is dangerous.** The model recognises the patient. Test performance rises and the
rise does not repeat on a new patient.

**How it is caught.** The patient identifier is passed as the split group, using
`GroupShuffleSplit` or `StratifiedGroupKFold`. The model does not do this of its own
accord; it has to be requested.

The same error appears at window level in time series work, and across different slices of
the same patient in imaging.

---

## 5. The hallucinated citation

**What happens.** A citation is given to a paper, guideline or standard that does not
exist. The author names are real, the journal is real, the year is plausible and the format
is flawless.

**Why it is dangerous.** Correctness of form suggests correctness of content. Once such a
citation reaches a model card or a manuscript it is difficult to remove.

**How it is caught.** A DOI or official document number is requested for every citation.
Where none can be given, the citation is removed. Where one is given, it is opened and
checked; there is no identifier that fails to resolve through doi.org.

---

## 6. Accuracy presented as the headline figure

**What happens.** Accuracy is reported on an imbalanced clinical problem.

**Why it is dangerous.** At a prevalence of seven percent, a rule that always predicts the
negative class is ninety three percent accurate. Accuracy in that setting measures how rare
the condition is rather than what the model does.

**How it is caught.** A null comparison belongs in every report. The `null_comparison`
function in the evaluation module provides it.

---

## 7. Calibration never reported

**What happens.** The area under the curve is reported and calibration is omitted.

**Why it is dangerous.** Where a threshold is set for a clinical decision, the probability
the model returns has to correspond to reality. An over-confident model places the
clinician's chosen threshold somewhere other than where it appears to be.

**How it is caught.** A calibration curve and slope are requested. A slope markedly below
one indicates over-confidence.

---

## 8. Subgroup breakdowns omitted or invented

**What happens.** There are two forms. The first is that no subgroup analysis is carried
out at all. The second is that a sensitivity value is reported to three decimal places for
a subgroup of eight patients.

**Why it is dangerous.** The second is more dangerous than the first, because it gives the
appearance of scrutiny. On a slide or in a model card, a figure derived from eight patients
carries the same authority as one derived from eight hundred.

**How it is caught.** A sample size floor is set in advance and subgroups below it carry
the words insufficient sample instead of a figure. The evaluation module does this. That
wording is a finding rather than a shortcoming: a system cannot be shown to be fair for a
group it was never tested on.

---

## 9. Point estimates presented without a confidence interval

**What happens.** An area under the curve of 0.78 is reported with no interval.

**Why it is dangerous.** On small cohorts the interval can include 0.5, in which case the
model is not distinguishable from chance, and the point estimate conceals that fact.

**How it is caught.** Every performance figure is requested with its interval. The
`bootstrap_auc` function in the evaluation module produces it.

---

## 10. Confident invention on regulatory questions

**What happens.** Asked whether software qualifies as a medical device, or which compliance
date applies, the tool returns a definite and outdated answer.

**Why it is dangerous.** The dates in this area changed in July 2026. Regulation (EU)
2026/1744, the Digital Omnibus, deferred the compliance date for embedded systems under
Annex I to 2 August 2028. The change is recent enough that many tools still return the
superseded timetable.

**How it is caught.** The regulatory triage note produced in NB5 is audited separately. A
confidence level, and the point a lawyer would need to check, is requested for every
regulatory claim.

---

## The order of the audit

The following order is used for every piece of generated code.

1. Have the tool list every constant in the code.
2. Read the list and mark the values with no source.
3. Find where the split happens, with your own eyes.
4. Filter the feature list against the decision moment.
5. Open any citations through doi.org.
6. Only then look at the results.

The results come last. Once a figure that looks good has been seen, the error behind it
becomes considerably harder to find.
