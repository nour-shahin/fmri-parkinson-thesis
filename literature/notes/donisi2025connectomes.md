# donisi2025connectomes: ML on multi-scale graph features of functional connectomes classifies early drug-naive PD

**Reference:** Donisi, L., De Micco, R., Pirozzi, M. A., Siciliano, M., Franza, F., Pisani, N., Zamir, B., Cirillo, M., Tessitore, A., & Esposito, F. (2025). Early classification of functional connectomes in Parkinson's disease: a comparison of machine learning classifiers using multiscale topological features. _BMC Medical Informatics and Decision Making_, 25, 455. (full entry in `references.bib`)
**DOI / link:** https://doi.org/10.1186/s12911-025-03303-1
**Type:** research article (open access, CC BY-NC-ND 4.0)
**Read on:** 2026-11-17
**PDF in repo:** yes (`literature/pdfs/donisi2025connectomes.pdf`, CC BY-NC-ND)

## Main idea

Resting-state fMRI functional connectomes of early, drug-naive PD patients differ topologically from healthy controls, and a comparison of nine ML classifiers on network graph theory (NGT) features asks (i) which features (global vs. lobar, cortical vs. subcortical) are most informative and (ii) which classifier performs best (pp. 1, 3). The answer: tree-based ensembles win, with the extra-tree classifier at F1 = 95.8% and AUCROC = 99.3%, and basal ganglia, parietal cortex, and thalamus carry the most informative features (pp. 1, 8-9). The authors explicitly concede that generalization to unseen samples remains unaddressed because the minority class was synthetically augmented (p. 13).

## Method

- Preprocessing: fMRIPrep 23.2.0 (T1 bias correction, skull-stripping; rs-fMRI motion estimation, slice-timing correction, susceptibility distortion correction from field maps, nuisance regression of 24 Friston motion parameters, framewise-displacement outliers, WM/CSF global signals), then bandpass filtering 0.01-0.1 Hz (p. 5).
- Connectome: Brainnetome atlas (246 regions: 210 cortical, 36 subcortical), Pearson correlations of mean BOLD time series, Fisher r-to-z, proportional thresholding keeping the top 10% strongest edges; NGT metrics via the Brain Connectivity Toolbox in MATLAB (p. 5).
- Three feature sets: Dataset 1 = 59 multi-scale features (10 global + 49 lobar: 5 cortical lobes + basal ganglia + thalamus); Dataset 2 = 10 global only (CPL, GE, TRA, ASS, mean BC/CC/DC/ECC/LE/MOD/NS); Dataset 3 = 49 lobar only (p. 6).
- Class imbalance: SMOTE augmented the 17 HC to n = 112 (k = 5 neighbors); ADASYN and a GAN were tested as alternatives, Mahalanobis/Ledoit-Wolf found no HC outliers; all three augmentations gave similar results (p. 6, Supplementary Tables).
- Pipeline before training: VIF filtering (threshold 10, iterative removal of the most collinear feature) and min-max normalization (pp. 6-7).
- Nine classifiers with default hyperparameters, explicitly no tuning: DT, ETC (300 trees), RF (300 trees), XGB, KNN (k = 3), SVM (RBF), NB, LR, MLP (pp. 7, 11).
- Validation: repeated stratified 10-fold CV, 10 repetitions. Metrics: accuracy, sensitivity, specificity, F1, AUCROC, PD as reference class (p. 7). Feature importance: information gain (mutual information), univariate (p. 8).

## Data

- Single-center (University of Campania, Naples), 3T GE Discovery MR750, consecutively recruited: 112 drug-naive PD patients (mH&Y <= 2.5, no dopaminergic or centrally acting medication ever, UPDRS-III 23.3 +/- 9.7, disease duration 1.6 +/- 0.9 y, mH&Y 1.7 +/- 0.5) and 17 HC matched for age and gender (p = 0.68 / 0.81) (pp. 3-4, Table 1).
- rs-fMRI: TR 1500 ms, 320 volumes, 8 min, 2 x 2 x 3 mm (pp. 3-4).
- Data not publicly available, on reasonable request from the corresponding author; code availability not stated (only standard tools named: fMRIPrep, ANTs, BCT, scikit-learn, imbalanced-learn) (p. 14).

## Main results

- Feature importance (Dataset 1, Table 2, p. 8): top features are lobar clustering coefficient of parietal cortex (IG 21.9%), lobar modularity of thalamus (21.6%), and global characteristic path length (19.7%); of the top 10, four are lobar/cortical, four lobar/subcortical, two global. Among global metrics only (Table 4, p. 9): CPL 20.3%, GE 14.1%, mean LE 13.7%; modularity least informative globally (2.4%) but highly informative subcortically.
- Brain areas by cumulative IG (p. 9): basal ganglia 18.5% > parietal 17.7% > thalamus 15.6% > occipital 15.5% > temporal 15.0% > sensorimotor 10.4% > fronto-insular 7.4%. Consistent with cortico-striato-thalamo-cortical circuit involvement; sensorimotor cortex surprisingly uninformative at this early stage.
- Classification (Dataset 1, Table 3, p. 8): tree-based models dominate. ETC best (F1 95.8 +/- 3.8, accuracy 96.7 +/- 3.7, sensitivity 95.6 +/- 6.2, specificity 97.8 +/- 4.4, AUCROC 99.3 +/- 1.8; 7 of 224 instances misclassified), RF F1 95.7 +/- 4.5, XGB 95.2 +/- 5.2, DT 90.0 +/- 7.3. Non-tree models far behind: SVM 75.3, NB 77.8, LR 77.8, KNN 70.6, MLP worst 62.3 +/- 29.6 (F1).
- Lobar-only features (Dataset 3) outperformed the combined set, suggesting low-ranked global features add some noise (p. 11); exact numbers are in the supplementary tables only.
- MLP's poor performance is attributed to small n vs. high dimensionality without hyperparameter optimization (p. 11).

## Evaluation and leakage check

Evaluation: internal validation only, repeated stratified 10-fold x 10 CV on a single-center sample; no external or held-out test set. Full metric panel reported (accuracy, sensitivity, specificity, F1, AUCROC), an improvement over most of the literature (p. 7).

- Feature selection before the split? Not resolved. VIF filtering, z-score/min-max normalization, and IG analysis are described as dataset-level preprocessing steps (pp. 6-8) before the CV is introduced (p. 7); the paper does not state that these were fitted inside each training fold. If fitted on the full data, this is mild leakage; the authors note the IG ranking itself may not be stable (p. 13).
- Same participant in train and test? No subject duplication within the CV (one scan per subject, pp. 3-5). The critical open question is the order of SMOTE and CV splitting: if synthetic HC samples were generated before the 10-fold split (the paper's description suggests the augmented dataset of 224 instances was what was cross-validated, p. 8), training folds contain interpolations between real HC samples that may include test-fold HCs as nearest neighbors. The paper does not state that SMOTE was applied within training folds only.
- Hyperparameters tuned on test data? No. All classifiers kept default settings deliberately, stated as a reproducibility choice; the authors explain they avoided nested CV on purpose (p. 11).
- Independent test set? No. No external cohort; the only out-of-sample evidence is internal CV (pp. 3, 7).
- Confounds checked? Motion handled by nuisance regression and FD spike regression (p. 5); age and gender matched between groups (p. 3); medication confound excluded by design (drug-naive, p. 3). Group differences in head motion are not reported.
- Metrics reported: accuracy, sensitivity, specificity, F1, AUCROC (p. 7).
- Code and data available? Data private (on request, p. 14); no code availability statement.

## Limitations

- Authors' own limitations (p. 13): small control group (n = 17) with severe class imbalance; SMOTE "does not generate any new authentic biological information" and models "might still have been overfitted to the highly correlated, interpolated patterns inherent in the synthetic data"; generalization to new, unseen real-world samples "remains to be addressed". This is unusually candid.
- Univariate IG importance may be unstable under strong feature correlation; the feature ranking needs replication (p. 13).
- No test-retest assessment, no multicenter validation, single scanner and pipeline; atlas and parcellation choices may matter in multicenter data (pp. 13-14).
- No hyperparameter optimization (deliberate), so classifier rankings reflect defaults, not tuned models (p. 11).

## Connection to my thesis: what is relevant, and for what?

- Relevant information: a recent, methodically transparent example of PD vs. HC classification from rs-fMRI connectomes with multi-scale graph features, a full metric panel, and a rare authors' admission that synthetic augmentation may cap generalization (p. 13).
- Used in chapter / section: Related Work (PD diagnosis from functional connectomes); Discussion (paired with badea2017reproducibility: high internal CV accuracy vs. chance-level cross-dataset generalization).
- Used as: related work AND a potential comparison point, since this is exactly the patient vs. healthy classification task. NOT a method to copy uncritically: the SMOTE imbalance handling and internal-only validation are the two design choices my thesis should do better.

## My own thoughts and criticism

- The headline numbers (F1 95.8%, AUCROC 99.3%) should be read as an upper bound, not an estimate. The combination of 17 real HC, SMOTE interpolation, no external test set, and an unstated SMOTE/CV ordering leaves real-data generalization open, as the authors themselves say (p. 13). This paper is the concrete instance of exactly what badea2017reproducibility warns about: single-cohort results this high are unlikely to survive cross-dataset testing.
- The SMOTE-before-CV question is the single most important thing to check in the supplementary material or code before citing any number from Table 3. Applying SMOTE before the split is a known way to inflate CV results by leaking interpolated test-class structure into training folds.
- Internal inconsistencies in the paper: the abstract says "17 HC subjects" (p. 1), Dataset 2 is described as "10 features" while listing 11 global metrics (p. 6), and the discussion reports LR F1 as 73.7 +/- 10.6% (p. 12) while Table 3 gives 77.8 +/- 9.4% (p. 8). Cite Table 3 numbers and note the text discrepancy.
- Per-class rates reveal what aggregate F1 hides: KNN reaches 98.9% sensitivity but only 55.1% specificity (Table 3, p. 8), i.e. near-degenerate prediction of the majority-shaped class in some models. Always read the confusion structure, not the headline.
- The feature-importance story is neurobiologically coherent (basal ganglia, thalamus, parietal dominance; modularity informative subcortically but not globally), which makes the paper useful as a biomarker-mapping reference even if the classifier numbers do not generalize.

## Relevant quotes

- "the core mechanism of any data augmentation techniques does not generate any new authentic biological information. Consequently, any of the models trained here might still have been overfitted to the highly correlated, interpolated patterns inherent in the synthetic data, rather than learning the true and diverse biological characteristics of the minority class." (p. 13)
- "all classifiers were here trained by strictly keeping all default settings (i.e., no hyperparameter optimization)." (p. 11)

## Reading questions

1. **How can I use this?** As related work for PD-vs-HC classification from rs-fMRI connectomes, as a benchmark for which NGT features matter (basal ganglia, thalamus, parietal), and in the Discussion as the single-cohort counterpart to badea2017reproducibility's cross-dataset negative result.
2. **Does it do what the authors claim?** Partly. The classifier comparison and feature-importance mapping are internally sound and well reported; the early-diagnosis claim is qualified by the authors themselves, because the performance estimates depend on synthetic controls and have never left the single cohort.
3. **Do I understand the results?** Yes: 59 multi-scale graph features from a 246-node Brainnetome connectome, SMOTE-balanced to 224 instances, nine default classifiers under repeated stratified 10-fold CV; tree ensembles (ETC, RF, XGB) above 95% F1, everything else 62-78%, and subcortical plus parietal features carrying the discriminative information.
