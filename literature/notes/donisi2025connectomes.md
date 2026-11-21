# donisi2025connectomes

**Reference:** Donisi, L., De Micco, R., Pirozzi, M. A., Siciliano, M., Franza, F., Pisani, N., Zamir, B., Cirillo, M., Tessitore, A., & Esposito, F. (2025). Early classification of functional connectomes in Parkinson's disease: a comparison of machine learning classifiers using multiscale topological features. _BMC Medical Informatics and Decision Making_, 25, 455.
**DOI:** https://doi.org/10.1186/s12911-025-03303-1
**Type:** ML study | **License:** CC BY-NC-ND 4.0 (sharing unchanged for non-commercial use is allowed; no adaptations) | **Read on:** 2026-11-17 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/donisi2025connectomes.pdf`; keep unmodified, attribute)

## Main idea

Multi-scale graph-theory (NGT) features of rs-fMRI functional connectomes discriminate early drug-naive PD patients from healthy controls. Nine ML classifiers are compared at default settings; tree ensembles win (extra-tree classifier F1 95.8%, AUCROC 99.3%). Feature-importance analysis locates the discriminative information in basal ganglia, parietal cortex and thalamus, but the authors concede that generalization to unseen real samples is unaddressed (pp. 1, 8-9, 13).

## Method

- fMRIPrep 23.2.0: motion estimation, slice-timing, susceptibility correction; nuisance regression (24 Friston parameters, FD outliers, WM/CSF signals); bandpass 0.01-0.1 Hz (p. 5)
- Brainnetome atlas (246 regions: 210 cortical, 36 subcortical); Pearson FC, Fisher r-to-z, top-10% proportional thresholding; Brain Connectivity Toolbox metrics (p. 5)
- Dataset 1 = 59 features (10 global + 49 lobar: 7 nodal metrics x 5 cortical lobes + basal ganglia + thalamus); Dataset 2 = 10 global; Dataset 3 = 49 lobar (p. 6)
- Processing order as described (pp. 6-7, Fig. 1): z-score (then transformed back) -> SMOTE up to n = 112 HC (k = 5; ADASYN and GAN tested as alternatives) -> VIF filtering (threshold 10) -> min-max normalization -> classifiers
- Nine classifiers with default hyperparameters, no tuning: DT, ETC (300 trees), RF (300), XGB, KNN (k = 3), SVM (RBF), NB, LR, MLP (1 hidden layer, 100 units) (pp. 7, 11)
- Validation: repeated stratified 10-fold CV, 10 repetitions; accuracy, sensitivity, specificity, F1, AUCROC; PD is the reference class (p. 7)

## Data

- 112 drug-naive PD (mH&Y <= 2.5, UPDRS-III 23.3 +/- 9.7, duration 1.6 +/- 0.9 y) vs. 17 HC, age- and sex-matched (age 61.4 vs. 60.7) (pp. 3-4)
- Single center (University of Campania, Naples), 3 T GE Discovery MR750, rs-fMRI TR 1.5 s, 320 volumes, 8 min (pp. 3-4)
- Labels: clinical MDS-criteria PD diagnosis vs. HC
- Data private (on request from the corresponding author); code availability not stated (p. 14)

## Results

All results are internal CV; no external held-out test.

- Feature importance (Dataset 1, Table 2, p. 8): parietal CC 21.9%, thalamic MOD 21.6%, global CPL 19.7% are the top 3; the top 10 contain 4 lobar/cortical, 4 lobar/subcortical, 2 global
- Areas by cumulative IG (p. 9): basal ganglia 18.5% > parietal 17.7% > thalamus 15.6% > occipital 15.5% > temporal 15.0% > sensorimotor 10.4% > fronto-insular 7.4%
- Classification (Dataset 1, Table 3, p. 8): ETC F1 95.8 +/- 3.8, accuracy 96.7 +/- 3.7, sensitivity 95.6 +/- 6.2, specificity 97.8 +/- 4.4, AUCROC 99.3 +/- 1.8, with "7 out of 224 instances misclassified"; RF F1 95.7; XGB 95.2; DT 90.0; SVM 75.3; NB 77.8; LR 77.8; KNN 70.6; MLP 62.3 +/- 29.6
- KNN (Table 3): sensitivity 55.1, specificity 98.9, i.e. it labels most test points HC
- Lobar-only features (Dataset 3) outperformed the combined set (exact values in the supplement only) (p. 11)

## Evaluation and leakage check

- Feature selection / preprocessing before the split? Normalization, VIF filtering and information-gain analysis are described at dataset level, not as refit inside folds (pp. 6-8). SMOTE is applied to the dataset to "balance" it before the CV is introduced, and the best model is described as misclassifying 7 of 224 instances, which means all 224 (112 PD + 112 HC, of which 95 HC are synthetic) were evaluated. This strongly implies SMOTE ran before the split, so synthetic HC points interpolated from the same real subjects can sit in both train and test folds. The authors never state the ordering explicitly
- Same participant in train and test? One scan per subject (pp. 3-5), but see the SMOTE point
- Tuning on test data? No: all classifiers kept default settings deliberately, nested CV avoided on purpose (p. 11)
- Independent test set? Not reported; internal CV only (pp. 3, 7)
- Confounds: motion nuisance-regressed (p. 5); age/sex matched (p. 3); medication excluded by design (p. 3); group head-motion difference not reported
- Metrics beyond accuracy: sensitivity, specificity, F1, AUCROC all reported (p. 7)
- Code and data: data private (p. 14); code not stated

## Limitations

- Admitted: small control group and severe imbalance, which "warrants extreme caution"; SMOTE "does not generate any new authentic biological information"; models "might still have been overfitted" to interpolated patterns; generalization "remains to be addressed"; univariate IG ranking possibly unstable; no test-retest or multicenter validation (p. 13)
- Not admitted: the SMOTE-before-CV ordering (implied by the 7/224 count); the preprocessing (VIF, min-max, IG) being fit on all data; no code release; classifier rankings reflect defaults, not tuned models (p. 11)

## Connection to my thesis

- Relevant: recent PD-vs-HC connectome classifier with a full metric panel and a candid augmentation caveat; concrete instance of the rigor-accuracy tension
- Chapter: Related Work (PD diagnosis from functional connectomes); Discussion (paired with badea2017reproducibility)
- Role: evidence and comparison point (this is the patient vs. healthy task, in drug-naive early PD); method idea (multi-scale NGT features) to weigh, not copy. Its SMOTE handling and internal-only validation are the two choices to do better

## My own thoughts and criticism

- The 95.8% F1 / 99.3% AUCROC are an upper bound, not an estimate: only 17 real HC, about 85% of the "HC" test instances are synthetic, no external test, and SMOTE appears to precede CV. Cite the numbers as internal-CV figures with this caveat
- Real-data-only performance is unknown. The KNN pattern (98.9% specificity, 55.1% sensitivity) is what you would expect if test points land near dense clusters of synthetic HC
- Internal inconsistencies to avoid quoting: the abstract/Methods list "10 global" features but the text names 11 metrics (pp. 1, 6); the text gives mean eccentricity IG as 20.3% (p. 9) while Table 4 gives 4.8%; LR F1 is 73.7 in the text (pp. 11-12) vs. 77.8 in Table 3 (p. 8). Cite the tables
- The neurobiological coherence of the importance map (basal ganglia/thalamus/parietal; MOD informative subcortically but not globally) makes it useful as a biomarker-mapping reference even if the classifier numbers do not generalize
- Concrete instance of what badea2017reproducibility predicts: high single-cohort numbers are unlikely to survive cross-dataset testing

## Quotes

- "does not generate any new authentic biological information" (p. 13)
- "strictly keeping all default settings (i.e., no hyperparameter optimization)" (p. 11)
