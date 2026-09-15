# Regulatory Triage

This document is not legal advice and does not substitute for it. It is used to establish
which questions have been answered and which remain open before approaching a lawyer or a
regulatory specialist.

The dates hold as of September 2026. This area moves; all four sections should be refreshed
before the document is reused.

---

## 0. Note on use

The second prompt in NB5 produces a draft of this document. That draft **must** be audited
separately. Regulatory questions invite confident invention, and the compliance dates in
this area changed in July 2026. The change is recent enough that many tools still return
the superseded timetable.

Each item carries two fields: the answer, and **the point a lawyer would need to check**.
The second may not be left blank.

---

## 1. Is this a medical device?

In the European Union the assessment is made under the Medical Device Regulation (EU)
2017/745, and in particular under Rule 11 of Annex VIII, which classifies software.

| Question | Answer |
|---|---|
| What intended purpose does the manufacturer declare | |
| Is that purpose diagnostic or therapeutic | |
| Does the output present a decision or a justification | |
| What class applies under Rule 11 | |
| **Point for the lawyer to check** | |

The declared purpose is itself decisive. The same software may fall into a different
regulatory position under a different statement of purpose.

---

## 2. The European Union Artificial Intelligence Act

The Act entered into force through Regulation (EU) 2024/1689 on 1 August 2024. Regulation
(EU) 2026/1744, the Digital Omnibus on Artificial Intelligence, was published on 24 July
2026, entered into force on 27 July 2026, and changed the application dates for the
high-risk obligations.

| Scope | Compliance date |
|---|---|
| Article 50 transparency obligations | 2 August 2026, not deferred |
| New Article 5 prohibitions and watermarking for systems already on the market | 2 December 2026 |
| Standalone high-risk systems under Annex III | 2 December 2027, previously 2 August 2026 |
| Embedded systems under Annex I, including AI within medical devices | 2 August 2028, previously 2 August 2027 |

| Question | Answer |
|---|---|
| Which annex does the system fall under | |
| What is the operative compliance date | |
| How will the Article 13 transparency requirements be met | |
| How will human oversight be documented | |
| **Point for the lawyer to check** | |

Note that deferral of the date does not defer the preparation. The conformity assessment,
the technical file and the human oversight design have to be complete when the date
arrives.

---

## 3. United States

Section 520(o)(1)(E) of the Federal Food, Drug, and Cosmetic Act, added by the 21st Century
Cures Act, sets four criteria under which decision support software falls outside the
device definition.

| Criterion | Met | Reasoning |
|---|---|---|
| Does not acquire, process or analyse a medical image, signal or specimen | | |
| Displays, analyses or prints medical or patient information | | |
| Offers options to a health care professional rather than imposing a single decision | | |
| **Enables the professional to independently review the basis for the recommendation** | | |

The fourth criterion is the legal counterpart of explainability and the reason the system
built in this workshop displays a contribution breakdown.

| Question | Answer |
|---|---|
| If it is a device, which pathway applies | |
| Where a learning component exists, is a predetermined change control plan required | |
| **Point for the lawyer to check** | |

Note that no device powered by generative artificial intelligence or a large language model
has been authorised to date on the list published by the FDA.

---

## 4. Data protection

Health data is a special category of personal data in most jurisdictions, including under
the EU General Data Protection Regulation and under Turkish Law No. 6698.

| Question | Answer |
|---|---|
| Which lawful basis applies to the processing | |
| Is explicit consent required, or does another basis apply | |
| How is data minimisation ensured | |
| Is there any transfer of data outside the jurisdiction | |
| Does the use of the system fall within the scope of informed consent | |
| Where liability rests in the event of an error | |
| **Point for the lawyer to check** | |

Where a cloud based or foreign hosted language model is used, whether patient data is sent
to that service must be answered separately and explicitly. No real patient data is sent to
a language model in the systems built during this workshop. Do not assume the same holds in
your own institution.

---

## 5. Conclusion

| | |
|---|---|
| Can this system be deployed at present | |
| If not, what is missing | |
| Next step | |
| Assessment made by | |
| Date | |

---

## 6. Statement of confidence

Which of the answers above are settled and which are estimates? Estimates are marked here.
An unmarked estimate is read as a certainty by whoever reads the document.
