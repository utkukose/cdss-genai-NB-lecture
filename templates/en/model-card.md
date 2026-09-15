# Model Card

The document produced in NB5 is compared against this template. Every heading present here
and absent from that document is an unanswered question. Every field left blank is a
question a clinician ought to ask.

One rule applies throughout. Nothing unmeasured is written here optimistically. "Not
tested" is a valid answer and is preferable to an invented figure.

---

## 1. Identification

| | |
|---|---|
| System name | |
| Version | |
| Date | |
| Responsible person and institution | |
| Contact | |

---

## 2. Intended use

**Which clinical decision is supported?**

**Who will use it?**

**At what moment does it intervene?**

**In what form is the output presented?** A probability, a ranking, a binary alert or a
marking on an image.

---

## 3. Out-of-scope uses

What the system does not do and must not be used to do. This section should not be left
blank; an empty out-of-scope list means the scope was never considered.

- Cannot be used for screening, because
- Does not hold for the following patient group, because
- Cannot serve as the sole justification for a decision, because

---

## 4. Training data and its limitations

| | |
|---|---|
| Source | |
| Number of centres | |
| Number of patients | |
| Recording period | |
| Outcome prevalence | |
| Missing data rate | |
| Access and licence | |

**Representation gaps.** Which patient groups are under-represented in this data? What
effect do those gaps have on the population where the system will be used?

**Artefacts of the record.** Could measurement frequency, coding practice or device
differences be influencing what the model has learned?

---

## 5. Evaluation

### Discrimination

| Metric | Value | 95% confidence interval |
|---|---|---|
| ROC AUC | | |
| Average precision | | |
| Null model comparison | | |

### Calibration

| Metric | Value |
|---|---|
| Calibration slope | |
| Intercept | |
| Brier score | |
| Interpretation | |

### Operating point

| | |
|---|---|
| Threshold | |
| Who chose the threshold | |
| Reasoning for the choice | |
| Sensitivity | |
| Specificity | |
| Positive predictive value | |
| Negative predictive value | |
| Alerts per hundred patients | |
| How many of those are true | |

### Subgroup breakdown

| Subgroup | n | Positives | AUC | Sensitivity | PPV |
|---|---|---|---|---|---|
| | | | | | |

Subgroups that could not be evaluated for want of sample size are recorded here. That is a
finding rather than a shortcoming: a system cannot be shown to be fair for a group it was
never tested on.

### External validation

Was it carried out? If not, every figure in this card belongs to a single centre and does
not hold elsewhere.

---

## 6. Known failure modes

For each item: what happens, in which patient, and with what consequence.

1.
2.
3.

---

## 7. Abstention and escalation

| | |
|---|---|
| Abstention band | |
| How the band was chosen | |
| Proportion of cases abstained | |
| Result of the band audit | |
| Drift detection method | |
| Missing data guard | |
| Escalation rule | |

---

## 8. Input validation

| Feature | Lower bound | Upper bound | Source |
|---|---|---|---|
| | | | |

No clinical bound without a source is entered in this table. A data-derived envelope is not
a clinical limit and cannot be presented as one.

---

## 9. Post-deployment monitoring

**What will be monitored?** Performance drift, shifts in the input distribution, alert
volume, clinician acceptance rate.

**At what frequency?**

**At what threshold will intervention occur?**

**Who is responsible for monitoring?**

If this section is empty the system should not be deployed. Performance drift goes unnoticed
unless it is measured.

---

## 10. Regulatory position

See `regulatory-triage.md` for the detail. Only the conclusion is entered here.

| | |
|---|---|
| Is it a medical device | |
| Applicable legislation | |
| Operative compliance date | |
| Has a data protection assessment been made | |
| Has legal advice been obtained | |
