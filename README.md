<div align="center">

# Clinical Decision Support Systems with Generative AI

### Lecture and Hands-on Workshop Material

*Technology and Artificial Intelligence Literacy Training in Health Sciences*
*Akdeniz University, Antalya, Türkiye · 16 and 18 September 2026*

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-0E7C7B.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Open in Colab](https://img.shields.io/badge/Start%20with-NB1%20in%20Colab-C2185B.svg)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB1_Problem_Definition.ipynb)
[![Notebooks](https://img.shields.io/badge/Notebooks-12-16213C.svg)](notebooks/)
[![Language](https://img.shields.io/badge/Material-English-6B7590.svg)](README.md)
[![Turkce](https://img.shields.io/badge/Ders%20notu-T%C3%BCrk%C3%A7e-6B7590.svg)](README.tr.md)

**Prof. Dr. Utku Köse**

Süleyman Demirel University, Department of Computer Engineering, Isparta, Türkiye<br>
Director, Artificial Intelligence Application and Research Center (YAZEM)<br>
University of North Dakota, Grand Forks, United States<br>
Universidad Panamericana, Mexico City, Mexico<br>
Vel Tech University, Chennai, India<br>
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

The two sessions are designed as one argument. The lecture sets out the thirteen stages
through which such a system is built and the criteria by which each stage is judged; the
workshop walks through those same stages, one notebook at a time. A participant who attends
only the workshop can still follow it, and a participant who attends only the lecture still
leaves with the stage list the workshop is built around.

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
│   └── cdss_kit.py                     Carries code between notebooks and runs the checks
├── notebooks/
│   ├── en/                             The English set, NB1 to NB6
│   └── tr/                             The Turkish set, NB1 to NB6
├── prompts/
│   ├── en/anti-patterns.md             What generated clinical code gets wrong
│   └── tr/anti-patterns.md             The same, in Turkish
├── templates/
│   ├── en/                             Model card and regulatory triage, reference for NB5
│   └── tr/                             The same two, in Turkish
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
readers who prefer Turkish should follow [README.tr.md](README.tr.md). The two do not
cross-reference each other, and a participant follows one of them from beginning to end.

| | Notebook | What is added |
|---|---|---|
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB1_Reaching_the_Data.ipynb) | **NB1** Reaching the data | Preparation, loading the data, a first look |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB2_Preparing_the_Data.ipynb) | **NB2** Preparing the data | Cleaning, patient level split, conversion for the model |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB3_Building_and_Measuring.ipynb) | **NB3** Building and measuring | Model, predictions and a nine value honest measurement |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB4_Justifying_the_Decision.ipynb) | **NB4** Justifying the decision | Overall and per patient reasoning, and its critique |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB5_Safety_and_Compliance.ipynb) | **NB5** Safety and compliance | Three guardrails, red team, printed compliance report |
| [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/utkukose/cdss-genai-NB-lecture/blob/main/notebooks/en/NB6_Web_Interface.ipynb) | **NB6** The web interface | A browser interface and the complete program |

### Datasets

Six openly accessible datasets are prepared, and the participant selects one in NB1. Every
later step follows the choice.

| Code | Type | Dataset | Access |
|---|---|---|---|
| `mimic-icu` | table | MIMIC-IV Clinical Database Demo, 100 patients | HTTPS, no credentialing |
| `wisconsin` | table | Breast Cancer Wisconsin, 569 samples | Bundled with scikit-learn |
| `pneumonia-mnist` | image | PneumoniaMNIST, 5,856 chest radiographs | `pip install medmnist` |
| `breast-mnist` | image | BreastMNIST, 780 ultrasound images | `pip install medmnist` |
| `mimic-ecg` | signal | MIMIC-IV-ECG Demo, 659 ECGs from 92 patients | HTTPS, no credentialing |
| `synthetic-notes` | text | Generated clinical notes | Produced by the code |

The ECG set covers the same 92 patients as the clinical demo, so that route predicts the
same outcome from the signal and the two are directly comparable. The MedMNIST sets carry
no patient identifier, which the notebook states rather than conceals. No credential-free
clinical note collection exists, so the text route generates its data.

### How the notebooks work

**No Python knowledge is required, and you do not write the code.** Each step gives you a
prompt written in plain clinical language. You pass it to a generative AI tool, paste the
code it returns into the blank cell below the prompt, and run it.

Every prompt ends with a section headed EXPECTED RESULT stating what the code must
produce. The check cell that follows tests exactly that, and reports what is missing. You
return the report to the AI tool and have the code regenerated. Not succeeding on the first
attempt is normal.

Understanding the code is expected, and a short Python note follows each step. The notes
assume nothing and explain what you have just seen: what a library is, what a table is,
what a function and a docstring are, printing against returning, dictionaries, loops,
objects and methods, early returns, callbacks.

### Code carries forward

The first line of each paste cell reads `#@cdss step_name`. At the end of a notebook,
`kit.export()` gathers every marked cell into one block. You copy that block into the first
cell of the next notebook, so the program you are writing accumulates as you go. Correcting
a step and running it again replaces the earlier version in place.

By the end of NB6 the accumulated code is a complete clinical decision support system
running behind a web interface, saved as `cdss_system.py`.

### What is supplied

One module, `workshop/cdss_kit.py`. It carries the code forward and runs the checks. It
contains no clinical decision support logic; that is what you write.

**One requirement.** The notebooks fetch that module from `raw.githubusercontent.com`, so
the repository must be public. In a private repository the fetch returns 404 and the module
has to be uploaded into the Colab session by hand.

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

Across six notebooks the participant writes a working clinical decision support system. No
Python knowledge is required and no code is hand written: each step supplies a prompt in
plain clinical language, the participant passes it to a generative AI tool, pastes the code
that comes back and runs it. A check cell then tests the result against the expected result
stated at the end of the prompt.

| Notebook | Layer added |
|---|---|
| NB1 | Reaching the data and taking a first look |
| NB2 | Cleaning, patient level split, conversion for the model |
| NB3 | Building the model, teaching it, measuring it honestly |
| NB4 | The layer that justifies the decision |
| NB5 | Safety guardrails and the compliance report |
| NB6 | An interface used from a web browser |

The code carries forward. At the end of each notebook every step written so far is
collected into one block and pasted into the first cell of the next notebook. By the end of
NB6 the accumulated code is a complete system running behind a web interface, saved as
`cdss_system.py`.

The participant chooses one of the six datasets listed above in NB1, and that choice drives
everything afterwards. Where a step genuinely differs by data type, the prompt branches
inside itself; everywhere else it reads the constants declared in NB1 and works unchanged.
Nothing is downloaded in advance and no dataset is redistributed here.

**The datasets are too small to support a deployable model, and the evaluation says so.**
Participants build a system, evaluate it honestly, and reach the conclusion that it should
not be deployed.

---

## How to use this material

**As a participant.** No preparation is needed. Come with a browser and an account for a
generative AI tool; which tool does not matter. If you want to prepare, open NB1, look at
the dataset catalogue and decide which set to work with. If you have a clinical problem of
your own and want to go beyond the catalogue, bring it written down in one sentence.

**As an instructor reusing the material.** Three items in the lecture are time sensitive
and should be rechecked before any later delivery: the European Union artificial
intelligence timetable, the United States device count, and the position on national
legislation. Each is dated in `lecture/verified-sources.md` for that reason.

**A note on what this material is not.** Nothing here is a validated clinical tool. The
systems built during the workshop are teaching artefacts. Using any of them on real patient
data, or deploying them in a care setting, would require the entire apparatus the lecture
describes: external validation, calibration assessment, subgroup analysis, regulatory
classification and post deployment monitoring.

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

Süleyman Demirel University, Department of Computer Engineering<br>
Director, Artificial Intelligence Application and Research Center (YAZEM)<br>
Isparta, Türkiye

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) · [www.utkukose.com](https://www.utkukose.com) · [ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) · [github.com/utkukose](https://github.com/utkukose)

</div>
