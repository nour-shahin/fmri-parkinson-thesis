# Rubbert et al. 2019, Machine-learning identifies Parkinson's disease patients based on resting-state between-network functional connectivity

**1. Header**
- Reference: Rubbert C, Mathys C, Jockwitz C, Hartmann CJ, Eickhoff SB, Hoffstaedter F, et al. Machine-learning identifies Parkinson's disease patients based on resting-state between-network functional connectivity. Br J Radiol 2019; 92(1101): 20180886.
- DOI: 10.1259/bjr.20180886
- Type: ML classification study (rs-fMRI, between-network connectivity)
- License: (c) 2019 The Authors, published by the British Institute of Radiology; no license text in the PDF (check the publisher page for the exact terms)
- Read date: 23 Nov 2026
- PDF: yes (`literature/pdfs/rubbert2019ml.pdf`)
- Page refs below are PDF pages, which equal the journal's "x of 9" page numbers.

**2. Main idea**
The paper asks whether whole-brain resting-state fMRI can separate idiopathic PD patients from healthy controls without any hand-picked region. The approach is a data-driven, model-based classifier built on between-network functional connectivity, using canonical network atlases from two external cohorts (HCP and 1000BRAINS) at several granularities. The claim is that rs-fMRI between-network connectivity is a promising, non-invasive neuroimaging biomarker for PD, with very good accuracy and high sensitivity, potentially useful in screening.

**3. Method**
- rs-fMRI pre-processing in FSL v5.0: discard first 5 volumes, motion correction (six rigid-body parameters kept for denoising), BET2 brain extraction, 5 mm FWHM smoothing, intensity normalisation, 150 s high-pass filter, FIX (ICA-based) denoising, co-registration to T1, non-linear normalisation to MNI152 (p. 3).
- Atlas / features: canonical group-ICA network maps from HCP (15/25/50/100/200 networks; 300 excluded for computational reasons) and 1000BRAINS (15/25/50/70 networks, 267 healthy older adults in the same age range); Dual Regression step 1 to get subject-specific network time series, variance-normalised (p. 3).
- Connectivity measures: FSLNets v0.6.3, full (Pearson) and L2-regularised partial correlations (ridge rho = 0.01), Fisher z-transformed; upper triangle of each matrix used as features (p. 3).
- Model: boosted logistic regression, 100 boosting iterations; nested CV with 10 outer / 10 inner folds; atlas source + granularity and correlation type treated as hyperparameters tuned in the inner folds (pp. 1, 4).
- Feature importance: separate non-nested stratified 10-fold CV with 20 repeats on the whole dataset; per-feature ROC/AUC filter importance, scaled 0-1, features > 0.8 examined (p. 4).

**4. Data**
- Participants: 42 PD patients (idiopathic PD, medical OFF: at least 12 h dopaminergic withdrawal) and 47 healthy controls (p. 1 abstract; p. 2 Table 1).
- Age/sex: HC 60.2 +/- 8.9 y, 22 F / 25 M; PD 61.8 +/- 9.6 y, 15 F / 27 M; matched on age and gender, p > 0.1 (p. 2 Table 1, p. 3).
- PD details: disease duration 9.7 +/- 5.5 y; Hoehn & Yahr median 2.75 (IQR 2-3); UPDRS-III OFF median 34, ON median 16.5; LED 1062.8 +/- 364.2 mg; MDRS median 140 (41 of 42 patients); symptom lateralisation right/left 16/26; motor type akinetic-rigid/tremor-dominant/mixed 14/6/22 (p. 2 Table 1).
- Site/scanner: one Siemens Trio 3T; EPI TR 2.2 s, TE 30 ms, 3.1 mm isotropic, 300 time points, about 11 min; MPRAGE T1 (p. 3).
- Private data (local PD/HC pool); labels = clinical diagnosis by a board-certified neurologist using UK Brain Bank criteria, no autopsy confirmation (pp. 2-3, 6).

**5. Results** (all CV, no separate held-out test set)
- Nested CV (the unbiased estimate), outer folds, p. 4: mean accuracy 76.2% (median 77.8%, SD 18.2, IQR 69.4-87.1); mean sensitivity 81% (median 80%, SD 21.1, IQR 75-100); mean specificity 72.7% (median 75%, SD 20.4, IQR 66.7-80). Not reported: AUC, F1, balanced accuracy, PPV/NPV.
- Outer-fold accuracies range from 33.3% (fold 1, HCP-25 partial) to 100% (fold 7, 1000BRAINS-70 full) (p. 4 Table 2).
- Best inner-fold configuration: 1000BRAINS 50-network parcellation with full correlations; partial correlations were weaker overall (best: HCP 25) (p. 4).
- Non-nested 20-repeat 10-fold CV on the whole dataset (optimistic, used for feature importance), p. 5: mean accuracy 80.3% (SD 3.7), sensitivity 84.5% (SD 4.3), specificity 75.7% (SD 5.7).
- Top features (scaled importance > 0.8, p. 5, Fig. 2): (1) right vs left subpart of the sensorimotor network (SMN), including (pre)SMA, primary sensorimotor cortex, thalamus, cerebellum; (2) dorsal visual network - auditory network; (3) dorsal visual network - inferior SMN; (4) right SMN - dorsal midline primary motor/premotor network.
- Of 9 repeatedly misclassified patients, 6 (66.6%) had right-lateralised symptom onset vs 38.1% in the whole PD sample (p. 5).

**6. Evaluation and leakage check**
- Feature selection before the split: no univariate pre-selection; atlas and correlation type are chosen inside the inner folds, so hyperparameter selection is properly nested (p. 4). OK.
- Same participant in train and test: not an issue; subjects are split into folds (each outer fold holds about 7-9 subjects: fold accuracies such as 85.7%, 87.5% and 88.9% correspond to 6/7, 7/8 and 8/9). No repeated measures.
- Tuning on test data: avoided in the nested CV. The feature-importance model is non-nested and tuned on the whole dataset, and the authors themselves call its performance "probably too optimistic" (p. 6). The headline 76.2% is the nested number and is the one to cite.
- Independent test set: none. Performance rests on CV of one single-scanner sample; no external validation.
- Confounds: age and sex matched (p > 0.1) (p. 3); motion parameters are used in FIX denoising, but no head-motion QC or covariate is reported; medication partially controlled (scanned OFF) but long-term dopaminergic effects cannot be excluded, as the authors admit (p. 6); a single scanner removes site as a confound but limits generalisability; disease duration/severity not regressed out.
- Metrics beyond accuracy: sensitivity and specificity reported; no AUC, no calibration, no balanced accuracy.
- Code and data: tools named (FSL, FSLNets, R caret/rsample/caTools); no code release and no data sharing mentioned. HCP and 1000BRAINS network maps are public; the PD/HC sample is not.

**7. Limitations**
- Admitted by authors: small sample (42 vs 47); clinical (not autopsy-proven) ground truth, and clinical diagnosis itself is about 83.9% accurate even for experts at follow-up (p. 6); long-term medication effects may contribute to the connectivity differences (p. 6); rs-fMRI heterogeneity across sites limits deployment and multi-centre samples are needed (p. 7); comparison with structural-MRI studies is not straightforward because methods differ (p. 7).
- Not admitted: no held-out external test set; no AUC; the sensitivity-specificity gap (81% vs 73%) means about 1 in 4 controls is misclassified, a problem for the screening use the authors propose; the authors say accuracy is "similar to those of clinical experts" (p. 7), but 76.2% is below the 79.6% and 83.9% expert figures they cite (p. 2) and only above the 73.8% for non-experts; the non-nested model is optimistically biased even though used descriptively; no head-motion QC; the 33.3% fold shows instability that the mean hides.

**8. Connection to my thesis (Leveraging fMRI Data for Early Prediction of Parkinson's Disease)**
- Role: baseline / method idea / evidence.
- Relevant for: Methods chapter (atlas granularity justification: the authors suggest 25-70 networks are a reasonable range, p. 6; full vs partial correlation; dual regression + Fisher z pipeline); Experiments chapter (a conservative nested-CV baseline for PD vs HC with between-network features, about 76% at n = 89, single scanner); Related Work / Discussion (supports the PD "disconnection syndrome" framing and SMN features as disease-relevant).
- Directly reusable idea: treat atlas source and granularity as hyperparameters selected in inner CV; report sensitivity separately because screening cares about missed patients.
- Caveat: the cohort is established PD (mean duration 9.7 y, median H&Y 2.75), so it supports PD detection, not early prediction; an early-prediction claim needs prodromal/early-stage data or a longitudinal framing.

**9. My own thoughts and criticism**
- The nested CV design is a real strength. Dzialas et al. report that only about half of PD neuroimaging-AI studies pass the no-leakage criterion (p. 8), so treating the atlas as an inner-fold hyperparameter sets Rubbert apart.
- The SD of 18.2 across outer folds is huge; with n = 89 one fold is only 7-9 subjects, so fold accuracies are very noisy. I would add balanced accuracy and AUC with CIs, and consider repeated nested CV for stability.
- A specificity of about 73% is weak for a screening claim; the abstract sells the sensitivity, but 27% false positives would over-refer heavily, especially at low prevalence.
- The right-lateralised-onset pattern in misclassified patients (6 of 9) is an interesting side finding, explored only descriptively with no statistical test.
- Single scanner plus an almost identical acquisition pipeline for the 1000BRAINS atlas means the 76% may not transfer; Badea et al. (their ref 42) showed global connectivity changes are not reproducible across three datasets (p. 7), which is the reproducibility problem my thesis should design around.

**10. Quotes (max 2, with page)**
- On the non-nested CV used for feature importance, the authors say its results "are probably too optimistic" (p. 6, Discussion).
