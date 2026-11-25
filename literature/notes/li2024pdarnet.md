# Li et al. 2024, PD-ARnet: a deep learning approach for Parkinson's disease diagnosis from resting-state fMRI

**1. Header**
- Reference: Li G, Song Y, Liang M, Yu J, Zhai R. PD-ARnet: a deep learning approach for Parkinson's disease diagnosis from resting-state fMRI. J Neural Eng 2024; 21: 056016.
- DOI: 10.1088/1741-2552/ad788b
- Type: ML classification study (deep learning, rs-fMRI, ALFF + ReHo)
- License: (c) 2024 IOP Publishing Ltd, all rights reserved; no open license stated in the PDF
- Read date: 23 Nov 2026
- PDF: yes (`literature/pdfs/li2024pdarnet.pdf`)
- Page refs below are PDF pages (PDF page 1 is the IOP cover sheet; journal page = PDF page - 1). Published 18 Sep 2024.

**2. Main idea**
Clinical PD diagnosis is subjective and insensitive, and rs-fMRI ALFF/ReHo measures are a possible auxiliary biomarker. The approach is a dual-branch 3D ResNet (PD-ARnet) that takes ALFF and ReHo maps as two inputs, weights them with a Correlation-Driven weighting module (CWM) to exploit their complementarity, fuses them with an Attention-Enhanced fusion module (AFM), and classifies PD vs HC through an FC + softmax layer. The claim: PD-ARnet outperforms single-input and ablation baselines and reaches 91.6% accuracy on PPMI, with potential as a clinical auxiliary diagnostic tool.

**3. Method**
- Preprocessing (DPABI): remove first 10 time points, slice-timing correction, head-motion correction, spatial normalisation to the EPI template, linear + quadratic detrending (p. 4).
- ALFF: filtered time series, FFT, power spectrum, square root, average over 0.01-0.1 Hz per voxel. ReHo: band-pass 0.01-0.1 Hz, Kendall's coefficient of concordance over a 27-voxel neighbourhood (p. 4).
- Data augmentation: HC samples only, random scaling of ALFF and ReHo images by a factor 1.2-1.5, motivated by PD > HC in the training set (p. 4). The paper does not state explicitly whether this is applied after the split.
- Backbone: two parallel 3D ResNet branches (one per metric); each has a 3D conv block (7x7x7 conv, BN, ReLU, MaxPool) and four 3D residual blocks (each with two residual units of 3x3x3 conv, BN, ReLU) (p. 5). The CWM sits after the second residual block, and two further residual blocks follow it (Fig. 1, p. 6).
- CWM: channel-wise correlation between ALFF and ReHo feature maps (mean, centring, covariance, std, correlation) used as multiplicative weights on both maps (p. 5).
- AFM: adaptive average pooling, 1x1x1 conv for inter-channel relations, softmax channel-attention weights, then concatenation of the ALFF and ReHo channels (p. 6).
- Classifier: FC + softmax; cross-entropy loss; Adam, lr 1e-4 reduced to 90% every 5 epochs, batch size 32 (pp. 6-7).
- Interpretability: 3D Grad-CAM (pp. 6-7).
- Ablation: PD-net-A (ALFF only), PD-net-R (ReHo only), PD-funet (dual branch + AFM), PD-ARnet (adds CWM) (p. 7).

**4. Data**
- Public dataset: PPMI (www.ppmi-info.org); 145 samples: 101 PD, 44 HC (p. 3). Access requires an application and authorisation (p. 3).
- Split: random 70/30, training n = 102 (71 PD, 31 HC), testing n = 43 (30 PD, 13 HC); 290 3D images in total (ALFF + ReHo per subject), split 204 train / 86 test (pp. 3-4).
- Demographics: PD 63.0 +/- 9.7 y, M66/F35; HC 63.6 +/- 11.1 y, M31/F13; age t = 0.30, p = 0.77; sex chi2 = 0.17, p = 0.68 (p. 4, Table 1).
- Scanner parameters: SIEMENS, 3.0 T, EP sequence, TR 2400 ms, TE 25 ms, flip angle 80 deg, 3.3 mm, 40 slices, 210 time points (p. 4). Multiple global PPMI sites (p. 3); the number of scanner models is not reported.
- Labels: PD vs HC grouping from PPMI; not defined further. Disease stage/severity (UPDRS, Hoehn & Yahr, duration, medication): not reported.

**5. Results** (test-set metrics over 10 random 70/30 re-splits; no CV in the usual sense)
- PD-ARnet on the test set (p. 7): accuracy 0.916 +/- 0.012 (95% CI 0.909-0.924); precision 0.947 +/- 0.007 (0.942-0.951); recall 0.862 +/- 0.020 (0.849-0.874); F1 0.902 +/- 0.014 (0.893-0.911); AUC 0.928 +/- 0.031 (0.911-0.950).
- Ablation on the test set (p. 8, Table 2): PD-net-A acc 0.851, prec 0.907, rec 0.756, F1 0.824, AUC 0.851; PD-net-R acc 0.853, prec 0.886, rec 0.777, F1 0.826, AUC 0.872; PD-funet acc 0.888, prec 0.928, rec 0.818, F1 0.869, AUC 0.890.
- PD-ARnet vs PD-funet: significant on all five metrics (paired t-tests, p1 < 0.001 to 0.005) (p. 8).
- Comparison to published PPMI methods (p. 11, Table 3): cmcRVFL+ acc 0.819; LLCFS 0.875 (AUC 0.900); EKM+SPL 0.853 (AUC 0.842); Cross-GNN 0.849 (recall 0.866); BrainMass 0.845. PD-ARnet is best on accuracy, precision, F1 and AUC; Cross-GNN recall is 0.004 higher. These are numbers copied from other papers, not re-run on the same splits.
- Grad-CAM: attention shifts with depth from a small prefrontal area to broader motor cortex (p. 9); the full model covers a broader frontal area than any ablation (p. 10).

**6. Evaluation and leakage check**
- Feature selection before the split: no explicit feature selection (the network learns features), so this risk does not apply. The order of the split and the HC augmentation is not stated explicitly.
- Same participant in train and test: the split is at subject level (a subject's ALFF and ReHo images stay together). The split is re-randomised 10 times (Monte-Carlo-style repeated hold-out). This is fine as long as each experiment retrains from scratch, which is not stated, but all 10 re-splits come from one 145-subject cohort, so the CIs reflect split variance only.
- Tuning on test data: Fig. 5 shows test-set accuracy/loss across training epochs (p. 7), which suggests that epoch selection or training monitoring may have used the test set. The paper does not say whether hyperparameters or the stopping epoch were chosen on test performance.
- Independent test set: none (same PPMI cohort, re-randomised); no external cohort.
- Confounds: age and sex tested (p = 0.77 / 0.68, Table 1); medication, disease duration, UPDRS, site/scanner distribution and head motion not reported. HC-only random scaling (1.2-1.5x) is an unusual transformation of exactly the quantity ALFF measures and could act as a shortcut.
- Metrics beyond accuracy: precision, recall, F1 and AUC with 95% CIs over 10 runs; good.
- Code and data: data stated as openly available (PPMI, data availability statement, p. 12), but access needs an application (p. 3). No public code repository mentioned.

**7. Limitations**
- Admitted: small sample size may limit generalisability; larger heterogeneous datasets needed; future work on other architectures (ConvNeXt, RepVGG) and multimodal biomarkers (p. 12).
- Not admitted: no true independent test set; possible test-set-informed monitoring (Fig. 5); the HC-only scaling augmentation is physiologically unmotivated and could be a shortcut (no control experiment such as augmenting PD too or no augmentation); the test set is 70% PD (30 of 43), so a majority-class classifier would already score about 70% accuracy and recall (0.862) is the more informative number; the paired t-tests and CIs treat ten overlapping re-splits as independent, which makes them optimistic; the Table 3 comparison is not like-for-like (different subsets and protocols); sample size of 145 is small for a 3D ResNet; the frontal-lobe Grad-CAM is discussed against the basal-ganglia literature only qualitatively (p. 12), with no quantitative regional analysis; no multi-scanner robustness test.

**8. Connection to my thesis (Leveraging fMRI Data for Early Prediction of Parkinson's Disease)**
- Role: method idea and comparison baseline; a target to reproduce or benchmark against.
- Relevant for: Methods chapter (ALFF + ReHo as complementary rs-fMRI metrics; dual-branch architecture; attention fusion; Grad-CAM for interpretability); Experiments chapter (what a 2024 deep learning model reaches on PPMI: acc 0.916, AUC 0.928 under repeated re-splits); Discussion (supports rs-fMRI functional metrics as diagnostic; frontal-lobe focus complements the basal-ganglia-centric view).
- Directly reusable idea: two complementary functional metrics as parallel inputs with a correlation-driven fusion module instead of raw concatenation; 3D Grad-CAM for interpretability.
- Caveat: their task is established-diagnosis classification, not early prediction; PPMI has de novo / prodromal / longitudinal data that suit early prediction better, which this paper does not use.

**9. My own thoughts and criticism**
- The architecture is reasonable but the evaluation is the weak point: re-randomising one PPMI cohort 10 times and reporting mean test metrics is not independent validation, and the CIs (e.g. AUC 0.911-0.950) understate real between-cohort variance.
- The HC-only scaling augmentation changes the amplitude distribution of one class, which is what ALFF measures. If the model learns the scaling artefact, part of the reported performance may not be PD biology; there is no control experiment.
- Reporting test-set curves over epochs (Fig. 5) is a red flag for test-set leakage in model selection.
- The ablations are informative (each module adds a measurable gain), which makes the paper more trustworthy than many deep learning papers; the largest step (0.888 -> 0.916) comes from the CWM, whose mechanism is shown only through heatmaps.
- The frontal-lobe Grad-CAM focus is argued from the literature (p. 12) but not tested against basal-ganglia regions or quantified regionally.
- For my thesis: a good target to beat on PPMI, but its numbers are an optimistic reference rather than a realistic benchmark.

**10. Quotes (max 2, with page)**
- The authors note that "the relatively small sample size may limit the generalizability of the findings" (p. 12, Limitations and future directions).
