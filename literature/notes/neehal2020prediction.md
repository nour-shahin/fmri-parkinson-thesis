# Neehal et al. 2020, Prediction of Parkinson's Disease by Analyzing fMRI Data and using Supervised Learning

**1. Header**
- Reference: Neehal AH, Azam MN, Islam MS, Hossain MI, Parvez MZ. Prediction of Parkinson's Disease by Analyzing fMRI Data and using Supervised Learning. 2020 IEEE Region 10 Symposium (TENSYMP), 5-7 June 2020, Dhaka, Bangladesh, pp. 362-365.
- DOI: not printed in the PDF. IEEE Xplore document 9230918 (https://ieeexplore.ieee.org/document/9230918/). Confirm the DOI on that page before using it in the .bib.
- Type: ML classification study (rs-fMRI, signal-processing features, SVM), early-stage prediction claim; conference paper
- License: not stated in PDF (IEEE, (c) 2020; ISBN 978-1-7281-7366-5)
- Read date: 23 Nov 2026
- PDF: yes (`literature/pdfs/neehal2020prediction.pdf`)
- Page refs below are PDF pages (journal page = PDF page + 361).
- Related: a longer BRAC University bachelor thesis by the same authors exists ("Detection of early stages of Parkinson's disease by analyzing fMRI data and machine learning approaches", hdl.handle.net/10361/13884). Not read; it might clarify labels, controls and the CV design.

**2. Main idea**
The problem: PD symptoms appear gradually, so early detection could improve treatment. The approach: treat each fMRI voxel's BOLD signal as a time series, extract time-frequency features (STFT, then power spectral density via Welch's method), and classify early-stage PD with an SVM (RBF kernel) using 5-fold CV. The claim: 100% sensitivity, specificity and accuracy for 7 of 8 subjects (one subject 99.76%), presented as a well-structured model for predicting early PD.

**3. Method**
- Voxel time-series extraction from rs-fMRI; zero-valued voxels (outside the brain) removed (p. 2).
- STFT on each voxel time series (p. 3), then PSD estimation with Welch's periodogram method (p. 3).
- Features: PSD-derived feature vectors, shape (420, 2) per subject (412, 2) for one (Table III, p. 3).
- Classifier: SVM with RBF kernel, 5-fold CV (4 folds train, 1 test, random split) (p. 3).
- "Prediction" design: two scan years per subject about 2 years apart; the second year's data are used to train and the first year's data to check the predictor (pp. 3-4).
- No fMRI preprocessing (motion correction, normalisation, smoothing, nuisance regression) is described anywhere in the paper.

**4. Data**
- Public: PPMI database (ppmi-info.org/data) (pp. 1-2).
- Participants: 8 subjects (7 male, 1 female), all described as "prodromal (early stage)" (p. 2). No healthy controls are listed in the analysis set, and what "normal subjects" refers to is not defined.
- Subject IDs / ages (Tables I-III): 60036 F 71/73; 60006 M 82/84; 60035 M 66/68; 60043 M 68/70; 60044 M 73/75; 60073 M 65/67; 60074 M 74/76; 60075 M 66/68.
- Sites/scanners: not reported (PPMI is multi-site; no scanner, TR, TE or voxel size given).
- Labels: "prodromal" and "early stage" are used interchangeably; no clinical criteria or follow-up conversion given. Confounds (age, sex, medication, motion): not reported.
- My reading of Fig. 4 (subject 60006, p. 4): "actual Parkinson's status" is 0 for the first half and 1 for the second half of a feature vector of about 420 entries, labelled "pre stage" and "on-set". The classification target therefore appears to be pre-stage vs on-set scan state within a subject, not PD vs HC. The text does not say this explicitly; check Fig. 4.

**5. Results** (5-fold CV on 8 subjects; no independent test set)
- Per-subject sensitivity / specificity / accuracy (p. 4, Table IV): 7 of 8 subjects 100 / 100 / 100 (60036, 60006, 60035, 60043, 60044, 60074, 60075); subject 60073: sensitivity 99.53, specificity 100, accuracy 99.76.
- Comparison claims (p. 4): vs [10] Kazeminejad et al. 94.6% and vs [3] Prashanth et al. 96.10%, "our proposed method achieved better accuracy".
- Internal inconsistency: the text claims 100% accuracy "in more than 90% of our subjects" (p. 4), but 7 of 8 is 87.5%.
- Not reported: precision, F1, AUC, CIs, confusion matrices, per-fold numbers, how the features were aggregated, hyperparameter search, class balance in the CV folds.

**6. Evaluation and leakage check**
- Feature selection before the split: none described; features are PSD vectors from non-zero voxels.
- Same participant in train and test: HIGH LEAKAGE RISK. Two scans of the same subject are used, with the second year in training and the first year in testing (p. 3-4). Train and test share the participant, so the model can pick up subject-specific signal rather than PD-related patterns. Results are also reported per subject (Table IV), and the unit of CV is unclear (Table III gives a 420 x 2 feature array per subject; if folds split the entries of that array, samples from the same subject land in both train and test).
- Tuning on test data: no hyperparameter search protocol is reported, so any tuning is undocumented.
- Independent test set: none. 8 subjects, 5-fold CV.
- Confounds: none reported or controlled (no age/sex matching, medication state, motion, site/scanner). The "prodromal" label is asserted, not validated.
- Metrics beyond accuracy: only sensitivity, specificity and accuracy; no AUC, no precision/F1, no CIs, no statistical test for the claimed superiority over prior work.
- Code and data: PPMI is public; no code released; subject IDs are listed, so the subset is in principle reproducible.

**7. Limitations**
- Admitted (p. 4 Conclusion): only 8 subjects, so accuracy may drop with more subjects; may perform worse on other datasets.
- Not admitted: (1) same-subject train/test design makes the 100% numbers uninterpretable as generalisation; (2) the effective n is 8, and folds drawn from the same subjects are not independent; (3) no healthy controls are listed, so what "specificity" measures is unclear (and Fig. 4 suggests the label is the scan time point); (4) no fMRI preprocessing is described; (5) "prodromal", "early stage" and de novo PD are conflated, with no criteria or follow-up confirmation; (6) the comparison with prior work (94.6%, 96.1%) is not like-for-like (different cohorts and tasks); (7) no confound control; (8) the ">90% of subjects" claim contradicts Table IV (7/8 = 87.5%).

**8. Connection to my thesis (Leveraging fMRI Data for Early Prediction of Parkinson's Disease)**
- Role: background / negative example; the voxel-level time-frequency idea is worth noting but this is not a valid baseline.
- Relevant for: Related Work (an example of an early-prediction claim with serious evaluation problems, useful when justifying my subject-level split design); Methods (motivates the same-participant leakage check and honest CV reporting; STFT/PSD could be a feature-engineering baseline if done with subject-level splits).
- Directly reusable idea: voxel-wise time-frequency (STFT/PSD) features as an alternative to ALFF/ReHo/connectivity, only with subject-level splits.
- Caveat: do NOT cite the 100% accuracy as a benchmark; cite it as an example of evaluation failure.

**9. My own thoughts and criticism**
- Using two years of the same subject, one in train and one in test, guarantees optimistic results; the 100% says almost nothing about new patients.
- With 8 subjects and no controls the paper cannot support any claim about prodromal PD detection; the labels are undefined.
- The signal-processing angle (STFT + Welch PSD on voxel time series) is an interesting feature idea that deserves a rigorous re-evaluation with subject-level splits and a real control group.
- No described preprocessing is a serious omission for rs-fMRI; motion alone can produce spurious group differences.
- Claiming superiority over Kazeminejad (94.6%) and Prashanth (96.1%) from an n = 8 within-subject design is not a valid comparison.

**10. Quotes (max 2, with page)**
- The authors concede that "the accuracy can get lower for more subjects" (p. 4, Conclusion).
