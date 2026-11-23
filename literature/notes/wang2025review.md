# wang2025review

**Reference:** Wang, Y.-F., Huang, Y., Chang, X.-Y., Guo, S.-Y., Chen, Y.-Q., Wang, M.-Z., Liu, K.-L., & Huang, F.-F. (2025). Classification of neurodegenerative diseases using brain effective connectivity and machine learning techniques: a systematic review. _Frontiers in Neurology_, 16, 1581105.
**DOI:** https://doi.org/10.3389/fneur.2025.1581105
**Type:** review (systematic) | **License:** CC BY | **Read on:** 2026-11-20 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/wang2025review.pdf`)

## Main idea

PRISMA systematic review (PubMed + Embase, up to 13 June 2024) of classification models for neurodegenerative diseases built on brain effective connectivity (EC), the directed/causal counterpart of functional connectivity (FC), with ML/DL. 16 studies included: 6 AD, 6 MCI, 1 PD, 2 AD+MCI, 1 AD+PD (pp. 1, 4). Conclusions: Granger causality (GCA) dominates EC estimation; multimodal fusion (EC + FC + structural/clinical) consistently outperforms EC alone; and accuracy-only reporting, single-source data, and unvalidated generalizability are the field's core weaknesses (pp. 9-10).

## Method (of the review)

- PRISMA-guided search in PubMed and Embase up to 13 June 2024; two authors screened independently with a third for disagreements; PRISMA flow diagram given (pp. 2-3)
- Search terms combined diseases (AD, PD, MCI, HD, ALS), EC methods (Granger, PDC, DTF, TE, DCM, SEM, OUM, Bayesian networks), modalities (fMRI, EEG, MEG), and classification/ML terms, plus "accuracy" (p. 3)
- Inclusion: original peer-reviewed English articles using EC features + ML/DL for classification; exclusion: EC without classification, no ML/DL, reviews and case reports (p. 3)
- Extraction form: author, year, modality, EC method, classifier, validation, task, accuracy (pp. 3-4)
- PRISMA numbers: 157 retrieved (PubMed 97, Embase 60), 25 duplicates, 105 excluded by title/abstract, 12 excluded at full text, 15 included + 1 by cross-referencing = 16 (p. 4)

## Main conclusions

- EC estimation (p. 5, Fig. 3): GCA 8, TE 1 (EEG), deep-learning GC 3, other 4. 12 fMRI, 3 EEG, 1 MEG studies (p. 4). Representation: about 11 use EC as direct variables, 4 as connectivity matrices, 1 as a directed graph with a GNN (p. 8)
- Selected accuracies (Tables 1-2, pp. 6, 9): AD: SVM on BP_KFGC EC 95.89%; EC + sMRI raises SVM from 78.72% to 91.49% (Hu 2022); dynamic EC 86.24%, +5.53% over static EC (Zhao 2022); DAG network 88.24%, 95.59% with FC added (Qiao 2018). MCI: sparse MVAR EC SVM 91.89%, +5.4% over FC (Li 2014); MCPC (FC + EC + sparse) 87.4%; RF on GRU-GC EC 87.88% (EMCI). Khazaee: NB on directed graph measures 93% (Table 1 labels it MCI vs. HC; the text, p. 8, calls it AD/MCI/HC, 93.3%). PD: EEG EC via FDCCM, NB best, 83.9% (Avvaru 2023); AD vs. PD vs. HC: EEG DSL-GNN, PD vs. HC 94.2%, three-class 93% (Cao 2024)
- Cross-cutting: dynamic EC (sliding window, change-point, RNN/GRU) outperforms static EC; multimodal fusion is the most consistent booster (pp. 9-10)

## What they say about quality (review-specific checklist)

- Validation: Tables 1-2 list LOOCV, 5-/10-fold CV, or an unspecified "validation data" (Guo 2020); none is described as an external-cohort test. The review itself says "generalizability across diverse samples and clinical settings remains to be thoroughly validated" (pp. 6, 9-10)
- Data: 9 of the 12 fMRI studies use ADNI (p. 10), named as a generalizability constraint
- Metrics: accuracy is the near-universal currency (the search string required "accuracy"); the review criticizes this, asking for sensitivity, specificity and predictive values, and warns that "data dependency, overfitting, and inherent biases may lead to inflated performance estimates" (p. 10)
- Atlas sensitivity: EC varies with atlas choice; Khazaee found a 264-region functional atlas outperformed AAL (p. 10)
- The review has no limitations section and no formal risk-of-bias appraisal (e.g. QUADAS). The items below are my critique, not the authors' admissions: two databases only (no IEEE/Scopus/Web of Science); nothing after June 2024; narrative synthesis, no pooling; accuracy-centric extraction

## Limitations

- Authors' own future-work list: larger samples, multi-scale dynamic EC, integrated ML/DL, multimodal fusion (p. 10)
- Two PD-involving studies, both EEG (Avvaru; Cao), so there is effectively no published fMRI-EC ML evidence for PD in this review. DCM/SEM/Bayesian estimators are absent from the included studies and only noted as underused (pp. 8-10)
- Not admitted: the accuracy table spans incomparable tasks/atlases/validation schemes without saying so. Internal inconsistencies: the text says Avvaru and Wang 2024 report "test set validation" accuracy while Table 1 lists LOOCV and 10-fold CV; reference 41 appears in both the GCA and "other methods" lists while Khazaee (39), a multivariate-GC study, appears in neither; the MCPC method is credited to Li (37) in the text but Li (38) in Table 1; the Discussion credits MVGC with modeling "nonlinear dynamic properties" although MVGC is a linear autoregressive method (p. 9)

## Connection to my thesis

- Relevant: current map of the EC + ML field (estimators, classifiers, fusion gains) and an external, published endorsement of the evaluation critique my other notes make independently
- Chapter: Introduction/Related Work (FC vs. EC framing, positioning my work); Discussion (field-level evaluation criticism)
- Role: background + evidence (citation anchor for the evaluation argument); sources to snowball: Avvaru 2023 (PD-EC state of the art) and Cao 2024 (multi-disease GNN)

## My own thoughts and criticism

- The review's own sentence, that accuracy alone is insufficient because inflated estimates arise from data dependency, overfitting and bias (p. 10), repeats in 2025 what badea2017reproducibility showed empirically in 2017 (the review does not cite it): the critique has been standard for eight years without changing practice
- PD coverage is two EEG studies (83.9% and 94.2%); the fMRI-EC ML literature for PD is effectively empty, a gap my thesis can name, and the positive results concentrate in AD/MCI where ADNI provides scale
- The accuracy spread (61.5% to 97.4%) across heterogeneous tasks, atlases, and validation schemes is cross-study incomparable; the review reports it without flagging that, its biggest missed opportunity
- The multimodal-fusion recommendation is supported within this set (+12.77 points from sMRI, +7.35 from FC; my arithmetic from Tables 1-2) but those gains are also internal-CV results, so the caveat applies to the review's own advice
- If my thesis uses FC rather than EC, this review is the citation for why EC is the next step and why its evidentiary base is currently thin

## Quotes

- "accuracy alone does not substantiate model robustness" (p. 10)
- "remains to be thoroughly validated" (p. 10)
