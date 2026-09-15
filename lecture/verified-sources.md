# Verified Sources

Every factual claim made in the Session 1 lecture deck is listed below with its primary
source, the exact figure asserted, and the verification date. Claims were checked against
the originating document or an authoritative secondary record (peer-reviewed journal,
official gazette, government agency publication) rather than aggregator summaries.

Verification date: 14 September 2026.

---

## 1. Turkish national policy

**Claim.** The Türkiye Yapay Zekâ Eylem Planı (2026–2030) entered into force through
Presidential Circular No. 2026/9, published in the Official Gazette dated 18 August 2026,
issue 33344. It replaces the Ulusal Yapay Zekâ Stratejisi (2021–2025), which had been put
into force by Circular No. 2021/18 (Official Gazette, 20 August 2021, issue 31574). The
plan is built on the principles of human-centricity, trustworthiness, ethical
responsibility, digital sovereignty and sustainable development, under the framework
"Fark Et, İstifade Et, Üret ve Yönet".

- Primary source: Resmî Gazete, 18.08.2026, No. 33344.
  https://www.resmigazete.gov.tr/eskiler/2026/08/20260818-8.pdf
- Corroboration: Anadolu Ajansı news report, 18 August 2026.
- Corroboration: Koyuncuoğlu & Köksal Hukuk Bürosu circular note, 21 August 2026.
- Note: The circular was signed on 17 August 2026 and published the following day. The
  plan itself was first presented publicly at the Türkiye Yapay Zekâ Zirvesi on
  13 June 2026.

**Claim.** The plan includes a National AI Literacy Programme covering all 81 provinces.

- Source: T.C. Sanayi ve Teknoloji Bakanlığı, Türkiye Yapay Zekâ Eylem Planı (2026–2030),
  human capital objectives.
- Caution: Secondary reports additionally cite a target of five million people trained
  within two years, alongside 10,000 advanced AI specialists and 100,000 AI application
  professionals. These figures come from press coverage of the plan rather than from the
  circular text. The deck states the 81-province programme only; if the numeric targets
  are used verbally, attribute them to the ministry's plan document.

---

## 2. Epic Sepsis Model — the central case study

**Claim.** External validation at Michigan Medicine covered 27,697 patients across 38,455
hospitalisations between 6 December 2018 and 20 October 2019. The model achieved an AUC of
0.63 (95% CI 0.62–0.64), sensitivity 33%, specificity 83%, positive predictive value 12%,
negative predictive value 95%. The manufacturer had cited an AUC range of 0.76–0.83.

- Primary source: Wong A, Otles E, Donnelly JP, Krumm A, McCullough J, DeTroyer-Cooley O,
  Pestrue J, Phillips M, Konye J, Penoza C, Ghous M, Singh K. External Validation of a
  Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients.
  *JAMA Internal Medicine*. 2021;181(8):1065–1070.
  doi:10.1001/jamainternmed.2021.2626 · PMID 34152373
- Corroboration: Habib AR, Lin AL, Grant RW. The Epic Sepsis Model Falls Short — The
  Importance of External Validation. *JAMA Internal Medicine*. 2021;181(8):1040–1041.
  doi:10.1001/jamainternmed.2021.3333 · PMID 34152360. This accompanying editorial
  restates the same performance figures independently.

**Claim.** A 2024 replication across two county emergency departments covering 145,885
encounters during 2023 reported sensitivity 14.7%, specificity 95.3%, PPV 7.6%, NPV 97.7%,
using the Sepsis-3 definition and the manufacturer's recommended alerting threshold of 6.

- Primary source: Ostermayer DG, Braunheim B, Mehta AM, Ward J, Andrabi S, Sirajuddin AM.
  External validation of the Epic sepsis predictive model in 2 county emergency
  departments. *JAMIA Open*. 2024;7(4):ooae133. doi:10.1093/jamiaopen/ooae133
  · PMC11560849

**Derived figure — prevalence curve (deck slide 13).** The PPV-versus-prevalence curve is
computed, not cited. Holding sensitivity at 0.33 and specificity at 0.83 and applying
Bayes' theorem, PPV = (sens x prev) / (sens x prev + (1 - spec) x (1 - prev)). At a
prevalence of 7%, this yields 12.7%, which reproduces the 12% figure reported by Wong et
al. and confirms the parameters are internally consistent. The slide labels the curve as
calculated.

---

## 3. Definition of clinical decision support

**Claim.** The "five rights" framing — right information, right person, right format,
right channel, right time.

- Source: Osheroff JA, Teich JM, Levick D, Saldana L, Velasco FT, Sittig DF, Rogers KM,
  Jenders RA. *Improving Outcomes with Clinical Decision Support: An Implementer's Guide*,
  2nd edition. HIMSS, 2012.
- Corroboration: Campbell R. The five rights of clinical decision support.
  *Journal of AHIMA*. 2013;84(10):42–47.

---

## 4. United States regulatory position

**Claim.** Approximately 1,450 AI-enabled devices have received FDA marketing
authorisation since the first in 1995, the majority in radiology, cardiology and
neurology, most via the 510(k) pathway. No generative-AI-enabled device has been
authorised to date. In March 2026 the FDA granted breakthrough device designation to a
patient-facing clinical generative AI application.

- Primary source: Congressional Research Service. *FDA Regulation of AI-Enabled Devices*.
  In Focus IF13245. https://www.congress.gov/crs-product/IF13245
- Corroboration: FDA Artificial Intelligence-Enabled Medical Device List. Most recent
  final decision date shown at review was 30 March 2026; database last updated 4 March
  2026 per MedTech Dive's 11 May 2026 download.
- Caution: The FDA states explicitly that this list is not a comprehensive inventory of
  AI-enabled devices; it is compiled from AI-related terminology in public authorisation
  summaries. Third-party snapshots vary between roughly 1,400 and 1,525 entries depending
  on download date. The deck uses "approximately 1,450" and attributes it to CRS. Do not
  present any of these figures as an exact count.
- First authorised AI-enabled device, 1995: PAPNET, a cervical cytology rescreening
  system.

**Claim.** FDA finalised its Predetermined Change Control Plan guidance in December 2024,
allowing specified future modifications to an AI-enabled device software function to be
pre-authorised within the original marketing submission.

- Source: FDA. *Marketing Submission Recommendations for a Predetermined Change Control
  Plan for Artificial Intelligence-Enabled Device Software Functions*. Final guidance,
  4 December 2024.

**Claim.** Under FD&C Act Section 520(o)(1)(E), added by the 21st Century Cures Act,
certain clinical decision support software functions fall outside the device definition
only if four statutory criteria are met, including that the software enables the health
care professional to independently review the basis for the recommendation.

- Source: FD&C Act Section 520(o)(1)(E).
- Corroboration: FDA. *Clinical Decision Support Software: Guidance for Industry and Food
  and Drug Administration Staff*. Final guidance, September 2022.

**Related, not used in the deck but useful in Q&A.**
- FDA draft guidance, *Artificial Intelligence-Enabled Device Software Functions:
  Lifecycle Management and Marketing Submission Recommendations*, issued 7 January 2025,
  docket FDA-2024-D-4488. Still in draft as of mid-2026; listed on FDA's FY-2026 "B" list
  for finalisation. Do not describe it as final.
- Good Machine Learning Practice for Medical Device Development: Guiding Principles.
  FDA, Health Canada and MHRA, October 2021; adopted in final form by IMDRF, January 2025.
- FDA final guidance, *Cybersecurity in Medical Devices: Quality Management System
  Considerations and Content of Premarket Submissions*, 3 February 2026.
- The amended Quality Management System Regulation (21 CFR Part 820) took effect
  2 February 2026.

---

## 5. European Union regulatory position

**Claim.** The EU AI Act (Regulation (EU) 2024/1689) entered into force on 1 August 2024.
Regulation (EU) 2026/1744, the Digital Omnibus on AI, was published in the Official
Journal on 24 July 2026 and entered into force on 27 July 2026. It deferred high-risk
obligations for standalone Annex III systems from 2 August 2026 to 2 December 2027, and
for AI embedded in products already covered by EU product-safety law under Annex I —
which includes AI inside medical devices regulated under MDR and IVDR — from
2 August 2027 to 2 August 2028. Article 50 transparency obligations were not deferred and
applied from 2 August 2026. Two new Article 5 prohibitions, together with the Article
50(2) watermarking obligation for systems already on the market, apply from
2 December 2026.

- Primary sources: Regulation (EU) 2024/1689, OJ 12.07.2024; Regulation (EU) 2026/1744,
  OJ 24.07.2026.
- Corroboration: Gibson Dunn client alert on the Omnibus agreement; DLA Piper knowledge
  note recording entry into force on 27 July 2026; Cloud Security Alliance research note
  on the deferral. Three independent legal-practice sources agree on all five dates.
- Note on sequence: A provisional political agreement was reached on 6–7 May 2026,
  confirmed by Council representatives on 13 May 2026, with final Council approval on
  29 June 2026. This history matters only if a participant recalls the earlier
  uncertainty; the deferral is now enacted law.

**Claim.** Software intended for a diagnostic or therapeutic purpose falls under the
Medical Device Regulation (EU) 2017/745, with software classification governed by Rule 11
of Annex VIII.

- Source: Regulation (EU) 2017/745 (MDR), Annex VIII, Rule 11.

---

## 6. Model quality and reporting standards

| Standard | Full citation |
|---|---|
| TRIPOD+AI | Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024;385:e078378. doi:10.1136/bmj-2023-078378 |
| PROBAST+AI | Moons KGM, Damen JAA, Kaul T, Hooft L, Andaur Navarro C, Dhiman P, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. *BMJ*. 2025;388:e082505. doi:10.1136/bmj-2024-082505 |
| DECIDE-AI | Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. *Nature Medicine*. 2022;28(5):924–933. doi:10.1038/s41591-022-01772-9 |
| CONSORT-AI | Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. *BMJ*. 2020;370:m3164 |
| SPIRIT-AI | Cruz Rivera S, Liu X, Chan AW, Denniston AK, Calvert MJ. Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. *BMJ*. 2020;370:m3210 |

The TRIPOD+AI record carries a correction notice, *BMJ* 2024;385:q902, which amended
author affiliations only. Cite e078378 as the article of record.

---

## 7. Explainability

**Claim.** Rudin argues that for high-stakes decisions, post-hoc explanation of black-box
models should be replaced by inherently interpretable models.

- Source: Rudin C. Stop explaining black box machine learning models for high stakes
  decisions and use interpretable models instead. *Nature Machine Intelligence*.
  2019;1:206–215. doi:10.1038/s42256-019-0048-x

The deck presents this as a live and unresolved debate rather than a settled position,
which is the accurate characterisation of the clinical literature.

---

## 8. Datasets referenced for the workshop

| Resource | Access | Citation |
|---|---|---|
| MIMIC-IV Clinical Database Demo v2.2 | Open, no credentialing; 100 patients; PhysioNet states it is suitable for running workshops | PhysioNet. doi:10.13026/dp1f-ex47 |
| MIMIC-IV (full) | Credentialed access only, not usable inside a two-hour workshop | Johnson A, Bulgarelli L, Pollard T, Horng S, Celi LA, Mark R. MIMIC-IV v2.2. PhysioNet. doi:10.13026/6mm1-ek67 |
| MIMIC-IV-ECG Demo | Open; 659 diagnostic ECGs across 92 patients | PhysioNet |
| Synthea | Open-source synthetic patient generator | Walonoski J, Kramer M, Nichols J, Quina A, Moesel C, Hall D, et al. Synthea: an approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record. *JAMIA*. 2018;25(3):230–238. doi:10.1093/jamia/ocx147 |
| PhysioNet platform | Repository of record for the above | Pollard T, Moody BE, Lehman L, Gow B, Fernandes C, Xie C, Johnson A, Mark RG, Heldt T. PhysioNet as a global platform for biomedical research. *Nature Health*. 2026;1(8):792–795. doi:10.1038/s44360-026-00096-z |

---

## 9. Claims deliberately excluded

The following were considered and left out because they could not be traced to a source
that meets the standard applied here.

- Aggregate alert-override percentages for clinical decision support. Published figures
  range very widely across institutions and alert types, and no single number is
  defensible as a general statistic. The deck describes alert fatigue mechanistically
  instead, without a numeric claim.
- Any figure for the number of CDSS deployments in Turkish hospitals. No authoritative
  national dataset was located.
- Vendor-specific performance claims other than the Epic Sepsis Model, which is included
  precisely because independent peer-reviewed external validations exist.
- The status of TİTCK guidance specific to clinical decision support software. Secondary
  sources describe work in progress but no primary document was verified, so the deck
  refers to medical device legislation generally rather than to a named guideline.

---

## Standing caution for delivery

Three items on these slides are time-sensitive and should be re-checked shortly before any
future delivery of this lecture: the EU AI Act timetable, the FDA device count and
generative-AI authorisation status, and the Turkish legislative position. Each is dated on
its slide for exactly this reason.
