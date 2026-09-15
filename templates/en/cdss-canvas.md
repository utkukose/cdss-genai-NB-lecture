# Decision Support Card

Complete this card for your own clinical problem before the workshop. The answers form the
input to every prompt written during the session. The card is entered in the first cell of
NB1 and carried from there into every step that follows.

---

## How to complete it

All seven questions should be answered. Where a question cannot be answered, this does not
mean the system cannot be designed; it means that question is the point to work on during
the session. Rather than leaving it blank, write what is unknown and why.

Three cautions. An estimated figure in question five is better than no figure, provided it
is labelled as an estimate. If both errors in question six appear equally costly, the
clinical consequence of the decision has probably not yet been considered closely enough.
Question seven is the one most often skipped and the one that matters most.

---

## The card

### 1. Which clinical decision?

The decision the system targets, and the exact moment at which it intervenes.

> *Your answer:*

---

### 2. Who will use it?

A physician, nurse, technician or the patient directly, and what that user is doing at the
moment of use.

> *Your answer:*

---

### 3. Which type of data?

Routine hospital data, medical images, physiological time series or clinical text. Where
more than one applies, which is the principal source. This answer determines which data
track you follow in the workshop.

> *Your answer:*

---

### 4. What is the outcome?

The precise definition of the outcome to be predicted, its time window, and how it would be
identified in routine records. Deterioration is not an outcome variable; transfer to
intensive care within 48 hours of admission is.

> *Your answer:*

---

### 5. What is the prevalence?

The frequency of the target condition in your own patient group. Where it is not known
precisely, give the estimate and what it rests on. Positive predictive value cannot be
interpreted without this figure.

> *Your answer:*

---

### 6. Which error is more costly?

A miss or a false alarm. State the answer together with its clinical consequence. This
answer determines the direction in which the threshold is set during the workshop.

> *Your answer:*

---

### 7. What happens when it is wrong?

A concrete harm scenario and an escalation rule. Under what circumstances does the decision
pass to a human?

> *Your answer:*

---

## Worked example

The shared scenario of the workshop was built by completing this card. Answers at this
level of detail are sufficient.

**1. Which clinical decision?**
Early prediction of whether a patient admitted to intensive care will have a prolonged
stay. The system intervenes six hours after admission and provides input to bed capacity
planning and to early escalation decisions.

**2. Who will use it?**
The intensive care consultant and the nurse responsible for bed management, during the
morning round as the patient list is reviewed.

**3. Which type of data?**
Routine hospital data. Demographics, admission context, and vital signs and laboratory
results from the first six hours.

**4. What is the outcome?**
Intensive care length of stay exceeding three days. It is computed from admission and
discharge times and is directly available in routine records.

**5. What is the prevalence?**
About one third in this cohort. It will differ in your own unit; use your own figure.

**6. Which error is more costly?**
A miss. Failing to identify a patient who will stay long fills capacity without a plan and
delays the admission of another patient. The cost of a false alarm is an unnecessary
planning meeting. The threshold is therefore set from sensitivity.

**7. What happens when it is wrong?**
On a false negative the capacity plan falls short and the transfer decision is delayed. The
escalation rule is as follows: where the system abstains, or where the patient does not
resemble the training population, the decision passes to the responsible clinician and no
system output is displayed.

---

## First use of the card

The completed card is used in NB1. The prompt there produces a specification from the card,
and every notebook that follows works from that specification.

The prompt is written so that it reports where your answers are incomplete or internally
inconsistent. Read the open questions list in the specification it produces. The weak points
of your card will be the weak points of the system you build.
