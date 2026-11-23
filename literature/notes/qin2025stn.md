# qin2025stn

**Reference:** Qin, B., Tang, Y., Qin, H., Gao, W., Liao, S., & Yang, M. (2025). Abnormal subthalamic nucleus functional connectivity and machine learning classification in Parkinson's disease: A multisite functional magnetic resonance imaging study. _Frontiers in Aging Neuroscience_, 17, 1695806.
**DOI:** https://doi.org/10.3389/fnagi.2025.1695806
**Type:** ML classification (multisite rs-fMRI FC) | **License:** CC BY (Frontiers; published 3 Dec 2025) | **Read on:** 2026-11-18 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/qin2025stn.pdf`)

## Main idea

Pools rs-fMRI from four public sources to characterize subthalamic nucleus (STN) functional connectivity differences in PD and uses the significant FC values in a linear SVM for PD vs. HC classification. Claims bilateral STN hypoconnectivity with temporal/parietal regions as a possible core PD feature and high diagnostic accuracy of an STN-centric FC classifier with external validation (pp. 1-2).

## Method

- Preprocessing: DPABI + SPM12 (MATLAB 2021a); first 10 time points dropped, slice-timing, motion correction, MNI 3 mm, 4 mm smoothing, Friston-24 + WM/CSF regression, 0.01-0.10 Hz bandpass. Exclusions: mismatched time points/slices, non-right-handedness, poor quality, motion > 1.5 mm or 1.5 degrees (pp. 2-3)
- Features: bilateral STN seeds (Talairach Daemon templates via WFU_PickAtlas); Fisher-z FC maps; the FC values of the significant clusters (five clusters, Table 2) go into the SVM (pp. 3-4)
- Harmonization: subsampling maximum-mean-distance (SMA), DPABI defaults, subsampling ratio 0.8, Euclidean metric (p. 3)
- Model: linear SVM (MVPANI toolkit), C = 1, gamma = 0.1 (unused for a linear kernel); 10-fold CV in training; stated to beat RF, logistic regression, naive Bayes, LDA, k-NN, decision trees "within our dataset" (Supplementary Table 1) (p. 3)

## Data

- 158 PD / 74 HC after exclusions (pp. 1, 4, Table 1): PPMI 96/24 (from 162/52 initially; 58 PD and 18 HC dropped for incomplete/poor data, 8 PD and 10 HC for motion), OpenfMRI ds000245 15/15, NEUROCON 27/16, Tao Wu 20/19 (one HC dropped for motion). NEUROCON and Tao Wu are both inside "FCP/INDI"
- Training = PPMI + OpenfMRI (111 PD / 39 HC); validation = FCP/INDI (47 PD / 35 HC) (p. 4)
- Age matched per site (all p > 0.05); sex difference is borderline at NEUROCON (PD 16 M/11 F vs. HC 5 M/11 F, p = 0.08) (Table 1, p. 4). Scanner details per site not reported. Medication state not reported
- Public data; analysis code availability not stated (p. 6)

## Results

- FC (Table 2, p. 4): decreased connectivity of left STN with left STG (49 voxels) and right supramarginal gyrus (50); of right STN with right STG (67), left MTG (72), left IFG (54) (GRF: voxel p < 0.005, cluster p < 0.05). Only decreases are reported; clusters are small
- Training (PPMI + OpenfMRI), 10-fold CV: accuracy 91.7%, sensitivity 98.8%, specificity 71.3%, AUC 0.920 (p. 4)
- Validation (FCP/INDI): accuracy 89.1%, sensitivity 97.7%, specificity 75.8%, AUC 0.931 (p. 4)
- Confusion matrices and balanced accuracy: not reported. The Discussion reports a different set: "accuracy (85%, AUC = 0.896)", "92% sensitivity", specificity 69% (p. 5), and the key-findings paragraph also says AUC = 0.896 (p. 4); these contradict the Results

## Evaluation and leakage check

- Feature selection before the split: unresolved. The five FC clusters come from a GRF group comparison whose sample is not stated; if it used the pooled 232 participants, the external test sites informed the features. SMA harmonization is also fitted on the pooled multisite data (p. 3), which is a second route for test-set information. Neither is described as training-only
- Same participant in train and test: distinct repositories, no overlap stated; PPMI follow-up visits not discussed
- Tuning on test data: SVM parameters fixed; classifier choice made "within our dataset" (p. 3), i.e. on pooled data
- Independent test set: yes (FCP/INDI sites unseen in training); this is the design strength
- Confounds: medication unreported; class ratio differs by site (PPMI 80% PD, ds000245 50%, NEUROCON 63%, Tao Wu 51%) so site and diagnosis are partly entangled; PD:HC imbalance unaddressed (no class weights); only 24 PPMI controls
- Metrics beyond accuracy: AUC, sensitivity, specificity, ROC; no balanced accuracy, no calibration
- Code/data: data public; analysis code not stated

## Limitations

- Admitted: cross-sectional design cannot separate disease effect from compensation; no subtype/stage analysis (limited phenotypic data in public datasets); heterogeneity; minor specificity limitation (pp. 5-6)
- Not admitted: the numeric inconsistency between Results and Discussion; the probable feature-selection and harmonization leakage into the external test; no comparison with other fMRI classifiers (the "outperforming" claims compare against wearable-sensor studies of other tasks, p. 5); the introduction lists Boutet 2021 as an SVM study predicting DBS response, but Boutet used LDA (p. 2)

## Connection to my thesis

- Relevant: closest published example of a diagnosis-style FC + classical ML classifier on public multisite PD data including PPMI; SMA harmonization as a citable alternative to ComBat; external-dataset validation as good practice
- Chapter: Related Work (FC-based PD classification, multisite harmonization); Methods justification (subject-level splits, external validation)
- Role: background/related work; usable as a soft comparison point for a PD vs. HC task, but not a clean baseline until the leakage question is resolved

## My own thoughts and criticism

- Quote only the Results numbers (91.7/89.1%, AUC 0.920/0.931) and flag the Discussion's contradictory 85%/0.896 set; three inconsistent reports of one model is itself a citable reporting failure
- The validation majority-class rate is about 57% PD (47/82), not the pooled 68%; the training rate is 74% (111/150). So 89.1% validation accuracy is a real but not enormous margin over chance, and the 97.7% sensitivity / 75.8% specificity pattern still shows a PD-leaning classifier
- The reported validation rates do not map onto the stated counts: 97.7% of 47 PD is 45.9 patients and 75.8% of 35 HC is 26.5 controls (my calculation); 97.7% and 75.8% correspond to 43/44 and 25/33, i.e. 77 people, not 82. Something (n, averaging, or rounding) is off
- The external validation is only as clean as the feature selection and harmonization; on the paper's text it probably was not, so treat 89.1% as an upper bound
- The FC finding itself (STN-temporal/parietal hypoconnectivity under a conservative GRF correction) is the more credible part and stands independent of the classifier numbers
- Atlas-defined STN seeds (Talairach Daemon, 3 mm voxels, 4 mm smoothing) are coarse for a nucleus this small; individual anatomy would matter for a true STN biomarker

## Quotes

- "robust accuracy (85%, AUC = 0.896)" (p. 5; conflicts with Results: 91.7% training / 89.1% validation, AUC 0.920/0.931)
- "within our dataset" (p. 3, on how the SVM was chosen over other classifiers)
