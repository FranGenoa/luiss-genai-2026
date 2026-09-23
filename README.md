# AI and GenAI for Management — Presentation Day

**Wine Business Program 2026 · LUISS / Italia del Vino**
Tool used throughout: **Microsoft 365 Copilot Chat** — `https://m365.cloud.microsoft/chat`

The day has two distinct halves, and they work very differently.

| Folder                           | What it is                                | Format                        | When                        |
| -------------------------------- | ----------------------------------------- | ----------------------------- | --------------------------- |
| [`00_exercise/`](00_exercise/) | Three short, standalone AI exercises      | 10-15 minutes each, individually | **During** the presentation |
| [`01_case_study_handouts/`](01_case_study_handouts/) | One long team case study (English) | ~2 hours, five teams          | After the presentation      |
| [`02_case_study_handouts_ita/`](02_case_study_handouts_ita/) | The same case study in Italian | ~2 hours, five teams          | After the presentation      |

Every guide and handout is provided as `.md` and as a print-ready `.pdf` with the same name, in the same folder.

***

## `00_exercise/` — live exercises during the presentation

Three **independent** exercises, run one at a time as the lecture reaches the
relevant topic. Each is self-contained: they share no state, no chat history
and no data, so a student who misses one can still do the next. Exercises 1 and 2
run on a **10-minute timer**, exercise 3 on **15 minutes**, and each is worked
**individually** — every student at their own
machine, in their own chat, running Copilot *and* checking its output against
the source. The verification is not delegated to anyone else.

All three use **GPT-5.6-Think** in Copilot Chat Basic. No extra subscription,
no Excel, no PowerPoint, no coding tools.

| # | Guide                                                                                                                                | PDF                                                                                        | Topic                                       | Inputs                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------- | -------------------------------------------- |
| 1 | [Esercizio_01_Italia_AI_Guida_studenti.md](00_exercise/Esercizio_01_Italia_AI_Guida_studenti.md)                                   | [PDF](00_exercise/Esercizio_01_Italia_AI_Guida_studenti.pdf)                               | From charts to an executive summary         | 3 PNG screenshots (2 required, 1 optional)   |
| 2 | [Esercizio_02_ROCCA_Confronto_Critica_Guida_studenti.md](00_exercise/Esercizio_02_ROCCA_Confronto_Critica_Guida_studenti.md)       | [PDF](00_exercise/Esercizio_02_ROCCA_Confronto_Critica_Guida_studenti.pdf)                 | Generic prompt vs. ROCCA brief vs. critique | None — three prompts in the guide            |
| 3 | [Esercizio_03_Dati_Dashboard_Presentazione_Guida_studenti.md](00_exercise/Esercizio_03_Dati_Dashboard_Presentazione_Guida_studenti.md) | [PDF](00_exercise/Esercizio_03_Dati_Dashboard_Presentazione_Guida_studenti.pdf)            | Raw CSV → analysis → dashboard → slides     | 1 CSV, 1,500 Italian wine reviews            |

**What each one actually teaches**

* **Esercizio 1** — students analyse Anthropic Economic Index screenshots for
  Italy (plus an optional France comparison) and produce an Italian-language
  report opening with an executive summary. The point is *not* to have Copilot
  confirm a pre-formed conclusion, but to work out what the images actually show.
* **Esercizio 2** — the same commercial decision (a fictional €25,000 choice at
  *Tenuta San Giorgio*) is put to Copilot three ways: a generic prompt, a
  structured **ROCCA** brief, and a self-critique-and-revise pass. Students judge
  the *difference*. A longer, more confident answer is not automatically better.
* **Esercizio 3** — a CSV becomes an analysis, then a standalone HTML dashboard,
  then a slide draft. The test is whether each step **preserves the underlying
  data**. A beautiful dashboard built on invented numbers is a liability.

### Attachments

```
00_exercise/data/
├── README.md                         index of what belongs to which exercise
├── esercizio_01_dati/
│   ├── README.md                     what each screenshot shows, and its limits
│   ├── 01_italia_panoramica_e_attivita.png      required
│   ├── 02_italia_most_distinctive.png           required
│   └── 03_francia_confronto_facoltativo.png     optional comparison
└── esercizio_03_dati/
    ├── README.md                     column dictionary, caveats, provenance
    ├── vini_italiani_recensioni.csv  1,500 reviews, 14 columns
    └── _build_dataset.py             regenerates the CSV from the public source
```

**Students download these before the timer starts.** Exercise 2 needs no
attachment. The dataset is derived from the public Wine Enthusiast reviews
released via TidyTuesday; `_build_dataset.py` filters to Italian wines with a
price and a score, extracts the vintage, and takes a seeded stratified sample by
region — so the file is reproducible.

***

## `01_case_study_handouts/` — the case study

The long-form team activity. Five teams take **Tenuta Corte Aurelia**, a Chianti
Classico estate, into **one export market each**, with a €120,000 first-year
budget. They must tell the CEO what they would earn, what it really costs, and
how she would know within twelve months whether it is working.

Unlike the exercises, this is **one continuous piece of work** over roughly two
hours, in a single Copilot conversation, ending in a live pitch.

```
01_case_study_handouts/
├── README.md                          workshop landing page + facilitator notes
├── Handout_Team-1_Japan.md / .pdf     🇯🇵  0% duty (EU–Japan EPA)
├── Handout_Team-2_USA.md / .pdf       🇺🇸  three-tier system, tariff 0% or 15%
├── Handout_Team-3_UK.md / .pdf        🇬🇧  €3.30 flat excise per bottle
├── Handout_Team-4_Germany.md / .pdf   🇩🇪  lowest price ladder, organic claim
├── Handout_Team-5_Brazil.md / .pdf    🇧🇷  55% of landed value
└── case_study_helper_info/
    ├── README.md
    ├── 01_Prompting-Guide.md / .pdf   7 phases, 16 starter prompts, in order
    ├── 02_If-You-Get-Stuck.md / .pdf  rescue method + the three core calculations
    └── 99_Indicative-Submission_Deck.pptx   market-neutral 8-slide skeleton
```

[`02_case_study_handouts_ita/`](02_case_study_handouts_ita/) has the identical structure and
file names, with every document (including the deck) translated into Italian. Figures are
unchanged and written in Italian number format.

**One handout per team, and it is self-contained** — company, CEO brief, Data
Pack, that team's market pack, cost line, exchange rate and deliverables in a
single file, so one upload gives Copilot the full context. The five handouts sit
side by side, so teams can read each other's markets: the numbers are fictional
and the learning is in the analysis.

**Deliverables:** a board deck (max 10 slides), one generated positioning image
that works in *that* market, a 5-minute pitch and a 2-minute reflection on
working with the AI.

The markets are deliberately not equally winnable. Brazil's tax stack and the
UK's flat excise are built to force a different answer from the obvious one.
