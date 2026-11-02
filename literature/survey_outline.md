# Survey outline: State of the Art / Literature Review

Structure follows the six-block flow from the course material ("Structure of the SoTA"). The six survey questions (Q1-Q6, see `survey_questions.md`) are the analysis tool that fills blocks 2 and 3.

Status legend: [ ] not started, [~] in progress, [x] done

## Block 1: General overview and context [ ]
**Purpose:** introduce the domain, relevant works and citations, narrowing gradually to the specific theme.
**Content for this thesis:**
- Parkinson's disease and why objective diagnostic markers are of interest
- Brain imaging in Parkinson's disease: structural MRI vs. functional MRI
- Resting-state fMRI and functional connectivity (what is measured, in one paragraph)
- Machine learning applied to neuroimaging, narrowing to PD classification from resting-state fMRI
**Sources in the repo:** `wang2025review`, `szewczykkrolikowski2014basalganglia`
**Missing, to be searched:** 1-2 background sources on Parkinson's diagnosis; 1-2 sources on resting-state fMRI and functional connectivity basics.

## Block 2: Theoretical foundation [ ]
**Purpose:** concepts, models, theories and frameworks; position the work within existing approaches.
**Content for this thesis (answers Q1-Q4):**
- Concepts: BOLD signal, brain atlases, functional connectivity matrices
- Datasets used in earlier work and their properties (Q1)
- Preprocessing and features (Q2)
- Machine learning models: logistic regression, SVM, random forest, deep models (Q3)
- Evaluation framework: cross-validation, participant-level splits, metrics, data leakage (Q4)
- Comparison table of the key studies
**Sources in the repo:** `badea2017reproducibility`, `donisi2025connectomes`, `li2024pdarnet`, `xu2023topological`, `shi2022radiomics`, `rubbert2019networks`, `qin2025stn`, `solanalavalle2024causalforest`, `boutet2021dbs`, `patil2024scannerbias`, `germani2025replication`, `nguyen2021trajectory`
**Missing, to be searched:** 1-2 methodological sources on cross-validation and data leakage in neuroimaging machine learning; official citations for Nilearn and scikit-learn.

## Block 3: Research aim: the gap [ ]
**Purpose:** identify what is missing in the literature, why it matters, and the space the thesis addresses.
**Content for this thesis (answers Q5 and Q6):**
- Reliability problems in earlier work (small samples, scanner differences, imbalance, leakage), supported by evidence from the papers read
- Whether early-stage detection or prediction has been attempted and with which data (`guo2022lstm`, `donisi2025connectomes`)
- A short statement of the gap, written only after the matrix is complete

## Block 4: Objectives, research questions, hypotheses [ ]
**Purpose:** clarify what is asked, what is tested, and how the thesis contributes.
**DRAFT for discussion with the teacher (not final):**
- Objectives: the six objectives from the teacher's brief (literature review, dataset exploration, preprocessing and features, model development, evaluation, interpretation)
- RQ1: Do resting-state functional connectivity features allow distinguishing Parkinson's patients from healthy controls better than chance under participant-level validation?
- RQ2: How do logistic regression, SVM and random forest compare under identical conditions?
- RQ3: How sensitive are the results to evaluation choices (for example, feature selection inside vs. outside cross-validation)?
- H1: Connectivity-based models achieve a balanced accuracy significantly above chance level.
- H2 (exploratory): The ranking of models changes when evaluation becomes stricter.
- Scope note: early-stage classification only if the dataset provides reliable stage labels; early prediction requires longitudinal data and is out of scope unless the data allow it.

## Block 5: Justification of relevance [ ]
**Purpose:** theoretical and practical importance, benefits, and why now.
**Content for this thesis:**
- Theoretical: evidence of reproducibility and bias problems in the field (to be supported by the papers once read)
- Practical: an objective, imaging-based signal could support diagnosis in the future; the thesis is an experimental study, not a clinical tool
- Why now: public datasets and mature open tools (Nilearn, scikit-learn) make reproducible work possible for a bachelor's thesis

## Block 6 (optional): Bibliographic search method [~]
Appendix. Content already exists in `survey_questions.md` (databases, search terms, inclusion and exclusion criteria, limitations). Complete the search record after the extra searches.

## Quick checklist (from the course material)
- [ ] Have you covered relevant and recent works?
- [ ] Have you defined a clear theoretical foundation?
- [ ] Is the purpose you are addressing visible?
- [ ] Are the objectives and questions precise?
- [ ] Have you justified the relevance (theoretically and practically)?
- [ ] (Optional) Have you described the search method?
