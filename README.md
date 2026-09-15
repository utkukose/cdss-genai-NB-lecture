<div align="center">

# Clinical Decision Support Systems with Generative AI

### Lecture and Hands-on Workshop Material

*Technology and Artificial Intelligence Literacy Training in Health Sciences*
*Akdeniz University, Antalya, Türkiye · 16 and 18 September 2026*

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-0E7C7B.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Open in Colab](https://img.shields.io/badge/Start%20with-NB1%20in%20Colab-C2185B.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB1_Problem_Definition.ipynb)
[![Notebooks](https://img.shields.io/badge/Notebooks-6%20%C3%97%202-16213C.svg)](notebooks/)
[![Language](https://img.shields.io/badge/Material-English-6B7590.svg)](README.md)
[![Türkçe](https://img.shields.io/badge/Ders%20notu-Türkçe-6B7590.svg)](README.tr.md)

**Prof. Dr. Utku Köse**

Süleyman Demirel University, Faculty of Engineering and Natural Sciences, Department of Computer Engineering
Director, Artificial Intelligence Application and Research Center (YAZEM), Isparta, Türkiye
University of North Dakota · Universidad Panamericana · Vel Tech University
IEEE Senior Member · ACM Professional Member

[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--9652--6415-A6CE39.svg)](https://orcid.org/0000-0002-9652-6415)
[![Website](https://img.shields.io/badge/Web-utkukose.com-16213C.svg)](https://www.utkukose.com)
[![GitHub](https://img.shields.io/badge/GitHub-utkukose-181717.svg)](https://github.com/utkukose)

</div>

---

## What this repository is

This repository holds the complete material for two linked sessions on artificial
intelligence based clinical decision support systems. The first is a forty five minute
lecture on what such systems are, why they fail in practice, and what makes them
trustworthy. The second is a two hour workshop in which participants build a working
decision support prototype for their own clinical problem using generative artificial
intelligence tools, with as little direct coding as the task allows.

The two sessions are designed as one argument. The lecture supplies a set of assessment
criteria, and the workshop turns each of those criteria into a prompt. A participant who
attends only the workshop can still follow it, and a participant who attends only the
lecture still leaves with the seven question card that the workshop is built around.

**The workshop requires no prior Python experience and no software installation.**
Everything runs in Google Colab through a browser.

---

## Repository layout

```
cdss-genai-NB-lecture/
├── lecture/
│   ├── CDSS-lecture-notes-EN.pdf       Lecture source text with figures, English
│   ├── KKDS-ders-notlari-TR.pdf        The same text in Turkish
│   └── verified-sources.md             Every factual claim with its primary source
├── slides/                             Decks generated from the notes, added after the session
├── workshop/
│   ├── mimic_web.py                    Calls the MIMIC-IV demo over HTTPS and builds the cohort
│   ├── pipeline.py                     Rebuilds the NB3 baseline for the later notebooks
│   ├── checks.py                       Acceptance tests for the code participants generate
│   ├── evaluate.py                     The six part evaluation checklist from the lecture
│   ├── explain.py                      Permutation importance and exact linear contributions
│   └── safety.py                       Abstention, drift detection and input validation
├── notebooks/
│   ├── en/                             The English set, NB1 to NB6
│   └── tr/                             The Turkish set, NB1 to NB6
├── prompts/
│   ├── en/anti-patterns.md             What generated clinical code gets wrong
│   └── tr/anti-patterns.md             The same, in Turkish
├── templates/
│   ├── en/                             Decision card, model card, regulatory triage
│   └── tr/                             The same three, in Turkish
├── LICENSE                             CC BY-NC-SA 4.0, with third party scope noted
├── CITATION.cff                        Machine readable citation metadata
└── docs/images/
```

---

## Lecture material

| | Document | Language |
|---|---|---|
| [PDF](lecture/CDSS-lecture-notes-EN.pdf) | Lecture notes, full source text with figures | English |
| [PDF](lecture/KKDS-ders-notlari-TR.pdf) | Ders notlari, ayni metnin Turkce surumu | Turkish |
| [PDF](slides/CDSS-lecture-slides-EN.pdf) | Presentation deck | English |
| [PDF](slides/KKDS-ders-sunumu-TR.pdf) | Sunum dosyasi | Turkish |

The lecture notes are written as continuous prose so that they can be used directly as
source documents in NotebookLM or a comparable tool. The decks in `slides/` are generated
from them and are added after the session. Every figure, date and citation in the notes is
traced to a primary source in [lecture/verified-sources.md](lecture/verified-sources.md).

---

## Running the notebooks

The material exists as two complete parallel sets. This page leads to the English set;
readers who prefer Turkish should follow [README.tr.md](README.tr.md), which leads to the
Turkish set. The two do not cross-reference each other, and a participant follows one of
them from beginning to end.

Every notebook opens in Google Colab and runs in a browser. Nothing is installed locally
and no dataset is downloaded in advance.

| | Notebook | What it covers |
|---|---|---|
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB1_Problem_Definition.ipynb) | **NB1** Problem card | Defining the problem through seven questions and turning it into a specification |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB2_Data_Preparation.ipynb) | **NB2** Data | Calling the MIMIC-IV demo, building the cohort, four data tracks |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB3_Model_and_Evaluation.ipynb) | **NB3** Model | Patient level split, baseline model and the honest evaluation report |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB4_Explainability.ipynb) | **NB4** Explainability | Global importance, exact local contributions and the critique of the explanation |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB5_Safety_and_Governance.ipynb) | **NB5** Safety | Abstention, drift detection, red team, governance artefacts |
| [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB6_Web_Interface.ipynb) | **NB6** Interface | A demo interface callable from the web |

### How the notebooks work

You do not write the code. Each step supplies a prompt. The prompt is copied into a
generative AI tool, the code that tool returns is pasted into the blank cell below the
prompt, and that cell is run.

Every paste cell is followed by a check cell. Each prompt ends with a section headed
CONTRACT stating which variables the code must produce and under which names, and the
check cell tests exactly that. This is the substance of the workshop rather than a
convenience: when a task is delegated to a language model, defining the interface is the
user's responsibility, and a prompt without a contract produces code that cannot be
checked.

Check density falls as the notebooks progress. NB2 carries eleven checks and NB6 carries
one, so verification passes to the participant as the material advances.

The cells that evaluate, plot and red team what you built are fixed.

**One requirement.** The notebooks fetch the `workshop/` modules from
`raw.githubusercontent.com`, which means the repository must be public. In a private
repository that fetch returns 404 and the modules have to be uploaded into the Colab
session by hand.

**One thing to check before teaching.** Run the first two cells of NB2. The connection
test fails within a second if the venue blocks PhysioNet, which leaves time to move the
session onto the synthetic data track.

---

## Session 1 — Lecture, 16 September 2026

**AI Based Clinical Decision Support Systems**

The lecture is organised around an independently validated failure. The Epic Sepsis Model,
deployed in hundreds of hospitals, was externally validated on 38,455 hospitalisations and
returned an area under the curve of 0.63 against a vendor claim of 0.76 to 0.83, with a
positive predictive value of 12 percent. A second validation three years later, across
145,885 emergency department encounters, returned a sensitivity of 14.7 percent. From
these two studies the lecture derives three lessons that carry directly into the workshop:
external validation is not optional, positive predictive value cannot be interpreted
without local prevalence, and a system that fires too often causes harm of its own.

The remaining sections cover calibration against discrimination, what explainability does
and does not provide, the reporting standards that make a claim auditable, and the
regulatory position in the European Union, the United States and Türkiye as of September
2026.

Source texts for the lecture are in `lecture/`. They are written as continuous prose so
that they can be used directly as source documents in NotebookLM or a comparable tool to
generate slides. Every figure, date and citation in them is traced in
`lecture/verified-sources.md`.

---

## Session 2 — Workshop, 18 September 2026

**Building Clinical Decision Support Systems with Generative AI Tools**

The workshop builds a decision support system in seven prompts. Participants begin on a
shared scenario and, roughly one hour in, switch the same prompt chain to their own
clinical problem. Participants who have no data of their own generate a synthetic cohort
that matches their problem; participants who want real data use open datasets that require
no credentialing.

| Notebook | What happens |
|---|---|
| NB1 | The seven questions are answered and converted into a written specification |
| NB2 | The cohort is built from open data, branching by data type |
| NB3 | A baseline model and, more importantly, an honest report on it |
| **Divergence** | Each participant substitutes their own card into the same chain |
| NB4 | The model is explained, then the explanation is attacked |
| NB5 | Abstention and guardrails, then the model card and regulatory triage |
| NB6 | A web callable interface and the closing discussion |

### Four data tracks

The prompt library carries a variant of each prompt for each type of clinical data, so
that participants working on different problems follow the same sequence.

| Track | Typical problem | Workshop data |
|---|---|---|
| Routine hospital data | Deterioration risk, readmission, triage priority | MIMIC-IV Clinical Database Demo, or a generated cohort |
| Medical imaging | Lesion detection, screening triage | MedMNIST, or a generated image set |
| Physiological time series | Arrhythmia detection, monitoring alarms | MIMIC-IV-ECG Demo, or a generated signal set |
| Clinical text | Report classification, information extraction | Synthetic notes generated to the participant's specification |

### Open data, called rather than downloaded

Only openly accessible resources are used during the session, so that nobody is blocked by
a credentialing process. The MIMIC-IV Clinical Database Demo is published under the Open
Data Commons Open Database License and requires no credentialing, so `workshop/mimic_web.py`
reads the tables straight from PhysioNet over HTTPS at runtime. Nothing is downloaded in
advance and nothing is redistributed here. The full MIMIC-IV database does require
credentialed access and is referenced but not used.

The shared scenario predicts prolonged ICU stay, defined as a length of stay greater than
three days, from the first six hours after ICU admission. Two guards are built into the
loader. Every measurement is restricted to that six hour window, and the columns that
describe the stay after it ended are dropped before the cohort is returned.

**The cohort is too small to support a deployable model.** One hundred patients produce a
confidence interval wide enough to include chance, and most subgroups are too thin to
evaluate at all. Participants build a system, evaluate it honestly, and reach the
conclusion that it should not be deployed.

### Prompts in two languages

Every prompt in `prompts/prompt-library.md` is given in Turkish and in English, and the
difference between them is treated as material rather than as a convenience. After prompt
3, participants run the same prompt in both languages in separate conversations and
compare four things: the model chosen, whether the split was made at patient level,
whether invented numbers appear, and whether clinical terms were mapped correctly. The
recommended working pattern is a canvas written in Turkish inside a technical prompt
written in English, but participants are asked to establish that for their own problem
rather than take it on trust.

---

## How to use this material

**As a participant.** Open `templates/cdss-canvas.md` and answer the seven questions for a
clinical problem you care about before the session. Bring those answers. Everything else
happens in the browser.

**As an instructor reusing the material.** The notebooks are self contained lecture notes
as well as executable material, so they can be read without being run. Three items in the
lecture are time sensitive and should be rechecked before any later delivery: the
European Union artificial intelligence timetable, the United States device count, and the
Turkish legislative position. Each is dated in `lecture/verified-sources.md` for that
reason.

**A note on what this material is not.** Nothing here is a validated clinical tool. The
prototypes built during the workshop are teaching artefacts. Using any of them on real
patient data, or deploying them in a care setting, would require the entire apparatus the
lecture describes: external validation, calibration assessment, subgroup analysis,
regulatory classification and post deployment monitoring.

---

## Citation

```bibtex
@misc{kose2026cdssgenai,
  author       = {K{\"o}se, Utku},
  title        = {Clinical Decision Support Systems with Generative AI:
                  Lecture and Workshop Material},
  year         = {2026},
  howpublished = {\url{https://github.com/utkukose/cdss-genai-NB-lecture}},
  note         = {Technology and Artificial Intelligence Literacy Training in Health Sciences,
                  Akdeniz University}
}
```

## License

Released under the Creative Commons Attribution NonCommercial ShareAlike 4.0 International
license. The material may be shared and adapted for teaching and research with attribution,
and may not be resold or used commercially without permission. See `LICENSE`.

---

## Acknowledgements

These sessions were delivered within the Technology and Artificial Intelligence Literacy
Training project supported by TÜBİTAK and hosted by Akdeniz University. The author thanks
the project coordinators and the organising committee for the invitation and for the
organisation of the programme, and the participants whose clinical questions shaped the
divergence stage of the workshop.

---

<div align="center">

**Prof. Dr. Utku Köse**

Süleyman Demirel University, Department of Computer Engineering
Director, Artificial Intelligence Application and Research Center (YAZEM)
Isparta, Türkiye

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) · [www.utkukose.com](https://www.utkukose.com) · [ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) · [github.com/utkukose](https://github.com/utkukose)

</div>
