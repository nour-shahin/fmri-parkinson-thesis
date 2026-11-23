# solanalavalle2024causalforest

**Reference:** Solana-Lavalle, G., Cusimano, M. D., Steeves, T., Rosas-Romero, R., & Tyrrell, P. N. (2024). Causal Forest Machine Learning Analysis of Parkinson's Disease in Resting-State Functional Magnetic Resonance Imaging. _Tomography_, 10(6), 894-911.
**DOI:** https://doi.org/10.3390/tomography10060068
**Type:** ML study | **License:** CC BY | **Read on:** 2026-11-20 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/solanalavalle2024causalforest.pdf`)

## Main idea

PD vs. control classification from rs-fMRI with an explicit interpretability pipeline: 11,600 hand-crafted features per participant (voxel intensity, frequency-band, connectivity features from 200 Schaefer cortical regions), reduced by Causal Forest (CF) then wrapper feature subset selection (WFSS), classified with logistic regression and XGBoost under nested CV. Headline: 97.6% accuracy in the mixed population with fewer than 300 features (pp. 1, 8). Second contribution: Multiple Correspondence Analysis (MCA) maps which brain regions associate with four sex-by-diagnosis groups and with UPDRS-III thresholds (pp. 6, 11-12).

## Method

- Eight-stage pipeline (Fig. 1, p. 2): preprocessing, time-series extraction, 10-band filtering, feature extraction, CF selection, WFSS selection, classification, MCA
- fMRIPrep 21.0.2 + Nipype 1.6.1 (FSL/FreeSurfer/AFNI); PPMI converted to BIDS (p. 4). Schaefer 200 is a cortical atlas, so basal ganglia, thalamus and cerebellum are not represented (p. 4)
- Features per region (58 x 200 = 11,600): gray intensity 6 (mean, variance, skewness, kurtosis, autocorrelation, wave height) = 1200; frequency 42 (ten 0.014 Hz bands within 0.01-0.15 Hz with four features each, plus 2 whole-spectrum) = 8400; connectivity 10 (band-vs-baseline-sinusoid correlation) = 2000 (p. 4)
- CF (Microsoft EconML) run at five reduction levels (96-99.9%); run ten times for stability (features ranked highly in at least four runs); top 4% kept; then WFSS per classifier (pp. 5, 8). The outcome/treatment definition for the "causal" forest is not spelled out; it works as a split-frequency feature ranker
- Classifiers: logistic regression, XGBoost (pp. 5-6)
- Nested k-fold CV, outer loop for performance, inner for selection; all scans of one patient are kept in the same fold (p. 6)
- MCA: 2D projection of regions and groups (83.78% inertia); a second MCA with UPDRS-III split at 23.7, taken as the H&Y stage 2 threshold (pp. 6, 11-12)

## Data

- Table 1 (p. 3) counts images (scans), not patients: PPMI PD 70 F + 147 M = 217 images from 68 patients (46 M, 22 F); PPMI controls 4 F + 18 M images; 1000 Functional Connectomes Project (33 sites) controls 103 F + 101 M images, age 19-65; total about 443 images. The Discussion then calls the 70 F / 147 M images "patients" (p. 13), which is the source of the apparent contradiction with 46 M + 22 F
- PPMI participants are aged 38-77 (Table 1 row, includes PPMI controls); FCP controls 19-65. PPMI TR 2.4 s vs. FCP 2-2.3 s; voxel size 3-4 mm; 175-265 frames per scan (pp. 3-4)
- Balanced per-sex sets (p. 13): women = 22 PPMI patients + 4 PPMI and 18 FCP controls; men = 46 PPMI patients + 18 PPMI and 28 FCP controls. Every patient comes from PPMI; 18/22 (82%) of the female and 28/46 (61%) of the male controls come from FCP. What the "mixed" model uses is not stated
- Labels: clinical PD vs. control
- Data public (PPMI, 1000FCP); code public on GitHub (github.com/GabrielSolana29/fmri_causalForest) (pp. 3, 15)

## Results

All results are internal nested CV; external held-out test not reported (the authors call it "a proof of concept that remains to be validated", p. 14).

- Best accuracies (Table 2, p. 8; each is the best over the five CF reduction levels): mixed XGBoost 97.6% (192 features), mixed LR 97.6% (26), female XGBoost 95.7% (445), female LR 95.6% (55), male XGBoost 93.0% (16), male LR 96.5% (37). Abstract: 97.6% accuracy, 97.5% F1, 97.9% precision, 97.7% recall, mixed population (p. 1)
- After CF + WFSS the selected features are 56%/60.4% gray intensity, 39.2%/36.3% frequency, 4.8%/3.3% connectivity (XGBoost/LR) (p. 7). CF alone ranked gray intensity highest; WFSS favored frequency features (pp. 7-8, 13)
- Table 3 (p. 8), family shares of the CF-selected features: frequency features dominate in male controls (65.5%), female PD (56.5%) and male PD (64.8%); only female controls are mostly gray intensity (59.2%). There is no consistent "controls = frequency, patients = gray intensity" pattern, and Table 3 conflicts with the text's statement that CF ranked gray intensity highest (pp. 7-8, 13)
- MCA (Fig. 5, p. 11): male PD associated with left visual extrastriate, right lateral dorsal PFC, left temporal-parietal regions; female PD with bilateral limbic temporal pole, right lateral dorsal PFC, bilateral somatomotor regions
- UPDRS-III MCA (Fig. 6, p. 12): regions differ above/below the 23.7 threshold (p. 14)
- Comparison table (Table 4, pp. 13-14): Kazeminejad 2017 (95%, LOO, n = 37), Guo 2022 (71.63%), Nguyen 2020 (PPV up to 71%), Cao 2020 (100%, private data, n = 120), Rubbert 2019 (76.2%, private), Haq 2020 (sensitivity 94%) and this work

## Evaluation and leakage check

- Feature selection before the split? Not stated: CF ranking and WFSS are described as dataset-level steps (pp. 5, 8), "during the PD detection evaluation". WFSS selects features by classification performance, so it must be refit inside training folds to be leakage-free; the paper does not claim this
- Selection on the outer result: the CF reduction level (96-99.9%) with the best performance is the one reported (Table 2), i.e. a configuration choice made on the evaluation numbers
- Same participant in train and test? Explicitly handled: all scans from one patient in the same fold (p. 6); the paper's strongest methodological point
- Tuning on test data? Nested CV separates selection (inner) from estimation (outer) (p. 6), but see the reduction-level point
- Independent test set? Not reported: internal CV only (p. 14)
- Confounds: diagnosis is almost perfectly confounded with source dataset (all PD from PPMI; most controls from FCP), with age (controls 19-65 vs. PPMI 38-77; the authors admit this, p. 14), and with TR/scan length (PPMI 2.4 s vs. FCP 2-2.3 s). 8400 of the 11,600 features are frequency-band features, which depend directly on TR and scan duration, and WFSS favors them. No age-matched or age-regressed analysis
- Metrics beyond accuracy: F1, precision, recall (pp. 1, 6); no specificity, no AUC, no confusion matrices in the main text
- Code and data: both public (pp. 3, 15)

## Limitations

- Admitted: nested CV alone may not reveal generalizing patterns; the age gap between controls and patients could dominate the signal; "this is a proof of concept that remains to be validated" (p. 14)
- Not admitted: CF's "causal" framing oversells (feature ranking by split frequency, not causal effects); no comparison of CF selection against a simple univariate baseline; MCA group-region associations unvalidated (no stability or permutation analysis); a cortical-only atlas misses the basal ganglia; the abstract's precision (97.9%) differs from Table 4's (97.4%), and Table 4's per-population metrics appear (from Fig. 2) to combine values from different classifiers (e.g. women: precision from XGBoost, recall and F1 from LR)

## Connection to my thesis

- Relevant: PD-vs-control classifier on public data with released code, patient-level fold control, and a candid limitations section naming the missing external validation and the age confound
- Chapter: Related Work (engineered-feature pipelines); Discussion (cautionary example of dataset-shift confounds: 97.6% is inseparable from age/site/acquisition differences)
- Role: evidence + cautionary tale for evaluation; also a baseline-adjacent comparison for the PD vs. healthy task, with the caveat that its numbers are not comparable to age-matched single-cohort results

## My own thoughts and criticism

- The 97.6% is the least informative number in the paper: with controls about 20 years younger on average, from different sites/scanners/TRs, a classifier can reach the mid-90s by learning dataset and age, not disease. This is the same shortcut patil2024scannerbias demonstrates for scanner differences. The authors admit the age issue yet keep 97.6% as the abstract headline
- Strongest elements: explicit patient-level fold assignment and the code release, which makes the CF/WFSS-inside-folds question empirically checkable
- CF is used as a heterogeneity-aware feature ranker, nothing more; cite the feature-selection ensemble idea, not "causal biomarkers"
- The paper's own comparison table mixes tasks: Guo 2022 is H&Y stage 1 vs. 2 and Nguyen 2020 is progression prediction, so it cannot support a claim that "accuracy tracks rigor" for PD-vs-HC work; use Kazeminejad (n = 37, 95%) and Cao (private, 100%) as the small-n, optimistic end only
- MCA visualizations are attractive but unvalidated; no evidence the group-region associations replicate in held-out data
- Table 1 is not garbled; it simply counts images. Cite the abstract/Section 2.1 numbers (68 patients, 46 M + 22 F) for patients

## Quotes

- "this is a proof of concept that remains to be validated" (p. 14)
- "substantially younger than the patients" (p. 14, on the controls)
