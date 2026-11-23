# shi2022radiomics

**Reference:** Shi, D., Yao, X., Li, Y., Zhang, H., Wang, G., Wang, S., & Ren, K. (2022). Classification of Parkinson's disease using a region-of-interest- and resting-state functional magnetic resonance imaging-based radiomics approach. _Brain Imaging and Behavior_, 16, 2150-2163.
**DOI:** https://doi.org/10.1007/s11682-022-00685-y
**Type:** ML classification (radiomics + SVM) | **License:** Springer, "exclusive licence", not open access (published 1 June 2022) | **Read on:** 2026-11-18 | **Checked against PDF:** 2026-11-21
**PDF:** keep the local copy only (`literature/pdfs/shi2022radiomics.pdf`); do not commit it to a public repo (not CC BY); link the DOI instead

## Main idea

Applies oncology-style radiomics to rs-fMRI: 11 intensity-histogram features per ROI from mean ALFF maps over the Brainnetome 246 atlas (2706 features), reduced by t-tests + SVM-RFE inside nested cross-validation, to classify PD vs. HC. Claims good performance (78.07% accuracy, AUC 0.860), robustness across atlases and CV schemes, and 7 discriminative subregions (pp. 1, 4-6).

## Method

- Preprocessing: DPABI. Dataset 1 was downloaded already preprocessed (pipeline from Hu 2015); Datasets 2 and 3 were processed "similarly": first 6 (Dataset 2) or 10 (Dataset 3) volumes dropped, slice-timing, realignment, DARTEL to MNI (EPI template for Dataset 3, which has no T1), 3 mm resampling, 6 mm smoothing; linear trend + WM + CSF + global signal + Friston-24 regression (pp. 2-3)
- Features: 11 histogram statistics per Brainnetome 246 ROI (CERR code) = 2706 features; min-max normalization, motivated by the heterogeneity of centers and protocols (pp. 3-4)
- Feature selection: two-sample t-tests (P < 0.01, about 215 features) then SVM-RFE (optimal 60 features, chosen by inner-loop accuracy) (pp. 4-6, 8)
- Model: SVM, nested 10-fold CV (inner loop selects the feature count), repeated 20 times; permutation tests (1000); validation reruns with AAL 90 and 5-fold (pp. 4-6)

## Data

- 123 PD / 90 HC from three public datasets (p. 2, Table 1): Dataset 1 (Hu 2015: 59/41; the cited paper is on depressed PD, and HDRS-17 is 11.44 vs. 2.41, p < 0.001), Dataset 2 (NEUROCON: 27/16), Dataset 3 (Wei 2014: 37/33, no T1)
- Scanners (Table 2, p. 3): Siemens Verio 3T (TR 2 s, 140 vol), Avanto 1.5T (TR 3.48 s, 137 vol), Tim Trio 3T (TR 2 s, 240 vol); different voxel sizes and scan lengths
- Labels: PD vs. HC; age/sex matched within each dataset. Medication state during scanning is not reported (Dataset 2 lists UPDRS off/on but not the scan state). PD share per dataset is similar (59%, 63%, 53%)
- Public data; code availability not stated. The cerebellum was not fully covered in some scans and is excluded throughout (p. 11)

## Results

- Tenfold CV, Brainnetome 246: accuracy 78.07%, AUC 0.860 (abstract: 0.8597), sensitivity 78.80%, specificity 76.08%, permutation p < 0.001 (pp. 6-7, Table 3). Fivefold: 76.55%, AUC 0.838
- AAL 90: 72.79% (tenfold) / 71.67% (fivefold), AUC 0.804 / 0.798 (Table 3, p. 7)
- Seven discriminative subregions, selected in > 95% of 2000 iterations (Table 4, p. 7): right IFG (minimum), right PhG (kurtosis), right STG (10th percentile), left PoG (kurtosis), left PrG (minimum), left MFG (median), left SFG (kurtosis). Three of the seven are kurtosis, a distribution-shape statistic that is hard to interpret physiologically
- All results are cross-validated on the pooled 213 subjects; no held-out external test. Calibration and PPV/NPV: not reported

## Evaluation and leakage check

- Feature selection before the split? The text says "We only performed the feature selection in the inner loop" (p. 5) and normalization is described as independent per training/test split. Fig. 2 (p. 5) draws feature selection inside the outer training branch and applies it to the test fold, which implies the t-test screen and SVM-RFE are fold-wise. The text never separately states that the t-test screen is fold-wise, so confirm before calling the 78.07% leak-free
- Same participant in train and test: no (independent datasets, one scan each); subject-level folds assumed but not stated
- Tuning on test data: no; nested CV with 20 repeats and permutation nulls
- Independent test set: no; all evaluation is CV on the pooled data
- Confounds: Dataset 1 is a depressed-PD cohort (HDRS confound); site/scanner differences handled only by min-max normalization, no harmonization; three different TRs/field strengths/scan lengths feed an ALFF measure that depends on them
- Metrics beyond accuracy: AUC, sensitivity, specificity, permutation p-values

## Limitations

- Admitted: moderate sample size; limited clinical information; ALFF-only in Dataset 1; cerebellum coverage gap (pp. 10-11)
- Not admitted: the Dataset 1 depression confound; no demographic-only or plain-mean-ALFF baseline, so the radiomics increment is unquantified; no external validation; "different atlas / different k" is presented as generalizability (pp. 6, 9), which it is not; the text calls p < 0.001 "perfect discriminative power" (p. 6), conflating significance with performance

## Connection to my thesis

- Relevant: honest-performance reference point for classical ML on public PD rs-fMRI; template for nested CV + permutation testing; concrete non-connectivity feature set (ALFF histograms)
- Chapter: Related Work (classical ML baselines); Discussion (evaluation hygiene; what honest pipelines achieve)
- Role: background/evidence for the PD-vs-HC classification question; methodology citable alongside germani2025replication

## My own thoughts and criticism

- The 72-78% accuracy range from a nested-CV pipeline is the useful number. The majority-class rate is 57.7% (123/213), so the margin is about 20 points. It makes the headline numbers of papers with weaker designs (e.g. 97.6% in solanalavalle2024causalforest, a confounded 94.7% in patil2024scannerbias's baseline) look inflated, but note those are different designs, not proof that each is flawed
- The t-test pre-screen is plausibly fold-wise (Fig. 2) but not stated; ask or check before citing 78.07% as leak-free
- Dataset 1's depressed-PD cohort means part of the separation may be depression-related ALFF, not PD
- The radiomics framing adds 11 standard histogram statistics; without a plain-mean-ALFF control, the "radiomics" label is mostly branding
- Only NEUROCON overlaps with other notes in this set (Dataset 2 = the same 27/16 as in qin2025stn and badea2017reproducibility), so results across these papers are not independent evidence

## Quotes

- "We only performed the feature selection in the inner loop" (p. 5)
