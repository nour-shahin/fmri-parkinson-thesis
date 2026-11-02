# Literature survey: questions and criteria

Thesis topic: Leveraging fMRI Data for Early Prediction of Parkinson's Disease

> This file doubles as the optional appendix "Bibliographic search method" of the survey (databases, search terms, inclusion/exclusion criteria, limitations). The six questions below are the *analysis questions* used to compare the papers. They are not the thesis research questions; those are defined in `survey_outline.md` (block 4).

## Aim of the survey
To establish which approaches exist for classifying Parkinson's disease (PD) from resting-state fMRI, how reliable the reported results are, and which gap the thesis addresses.

## Survey questions

| ID | Question | Answered in |
|---|---|---|
| Q1 | Which datasets are used for PD vs. healthy-control classification with resting-state fMRI, and how large and how accessible are they? | Datasets section |
| Q2 | How is the data preprocessed, and which features are extracted (atlas, connectivity measure, other)? | Preprocessing and features section |
| Q3 | Which machine learning algorithms are applied, and how do they compare? | Methods section |
| Q4 | How are the models validated (cross-validation type, split by participant, independent test set, metrics)? | Evaluation section |
| Q5 | How large are the reported results, and which factors weaken them (small samples, scanner differences, class imbalance, data leakage)? | Evaluation and reliability section |
| Q6 | Has early-stage detection or prediction of future disease been attempted, and with which data? | Early-stage section |

## Inclusion criteria (a source must meet at least IC1 and IC2, or IC4)
- IC1: Parkinson's disease is the studied condition.
- IC2: Resting-state fMRI (or functional connectivity derived from it) is the main data.
- IC3: Machine learning classification or prediction is applied (patients vs. controls, stages, or progression).
- IC4: The source provides necessary background for the thesis: a dataset description, a review, an evaluation or reproducibility study, or documentation of a tool used in the thesis.
- IC5: Peer-reviewed publication or established preprint. Preferably published in the last 5-10 years; older papers are kept when they are foundational. The quality of the venue (journal reputation, impact factor) is noted for each source.

## Exclusion criteria
- EC1: Other modalities as the main data (EEG, MEG, fNIRS, gait sensors, voice, PET without fMRI).
- EC2: Studies on deep brain stimulation outcomes or drug effects only, without relevance to diagnosis or classification (kept only as related work if the methodology is instructive).
- EC3: Studies of other conditions (for example REM sleep behavior disorder, Alzheimer's) without a PD comparison.
- EC4: Studies focused on symptoms only (depression, freezing of gait, hallucinations) without a classification component.
- EC5: Conference abstracts and proceedings volumes without a full paper.

## Search record
| Date | Source | Query | Results |
|---|---|---|---|
| (fill in) | PubMed | see `scripts/10_search_literature.py` | 87 unique papers |
| (fill in) | Google Scholar / Semantic Scholar | backward and forward snowballing from Donisi 2025 and Wang 2025 | (fill in) |
| (fill in) | oatd.org, openthesis.org | other theses on resting-state fMRI and Parkinson's disease | (fill in) |
| (fill in) | Google Scholar | background: Parkinson's diagnosis, resting-state fMRI basics, cross-validation and leakage in neuroimaging | (fill in) |
| | | | |

Limitations of the search: one main database (PubMed) plus snowballing; English-language sources only; results depend on the search terms used.

## Screening record
Screened by title and journal in `search_results.csv` (column `keep`). 15 sources kept, 8 undecided, remaining papers excluded by EC1-EC5.
