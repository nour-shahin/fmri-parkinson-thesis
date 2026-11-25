# Xu et al. 2023, PD Diagnosis beyond Clinical Features: A Biomarker using Topological Machine Learning of rs-fMRI

**1. Header**
- Reference: Xu N, Zhou Y, Patel A, Zhang N, Liu Y. Parkinson's Disease Diagnosis beyond Clinical Features: A Bio-marker using Topological Machine Learning of Resting-state Functional Magnetic Resonance Imaging. Neuroscience 2023; 509: 43-50.
- DOI: 10.1016/j.neuroscience.2022.11.022
- Type: ML classification study (rs-fMRI, fractal features + manifold learning)
- License: not stated in PDF (Elsevier, (c) 2022 IBRO, all rights reserved)
- Read date: 23 Nov 2026
- PDF: yes (`literature/pdfs/xu2023topological.pdf`)
- Page refs below are PDF pages (journal page = PDF page + 42). Online 24 Nov 2022, volume year 2023.

**2. Main idea**
The problem: PD diagnosis relies on clinical features; patient- and region-specific imaging biomarkers are missing. The approach: compute Generalized Hurst Exponents (GHE, fractal analysis) of BOLD signals per voxel in extracted resting-state network regions, embed them in 2D with UMAP (topological/manifold learning), then classify PD vs HC with SVM / Gradient Boosting / a 2-layer DNN. Claim: region-specific classifiability up to ~1.00 in some regions of small datasets, and 96.4% accuracy for a multi-region DNN, presented as a quantifiable, verifiable biomarker for early detection (pp. 1-2, 5-7). The paper does not state which dataset the 96.4% was computed on (see section 5).

**3. Method**
- Preprocessing: Methods cite DPABI (Yan 2016); Resource availability says DPARSF v4.3 in MATLAB 2020a, so the paper is inconsistent about the tool. Steps: slice timing, realignment, co-registration to T1, DARTEL normalisation to MNI, smoothing (pp. 3, 7).
- Region extraction: resting-state network (RSN) regions via group statistical analysis, p < 0.05 (p. 3). Five regions are shown; "other regions have been done but not presented" (p. 4).
- Features: Generalized Hurst Exponent (GHE) per voxel in each region (Eq. 1-2) (p. 3).
- Dimension reduction: UMAP v0.4, cosine metric, a = 100, b = 0.9 (p. 7). UMAP is non-deterministic, so scores are averaged over 5 runs (p. 4).
- Classifiers: SVM and Gradient Boost Classifier (region analysis, p. 4); 2-layer DNN binary classifier on multi-region embeddings: the "four regions in Fig. 3" are combined as an 8-D input (p. 5).
- Region-level accuracy is NOT standard accuracy: Acc = min(correct-health / true-health, correct-PD / true-PD), i.e. the minimum of the two class recalls (Eq. 3, p. 4).

**4. Data**
- Three public datasets (p. 2, Table 1):
  - PPMI: 92 PD + 22 HC; PD males 66 / females 26, age 45-83, median 66; HC males 16 / females 6, age 39-79, median 63.
  - OpenNeuro ds001354 (Tessa 2019): 14 de novo parkinsonian syndrome + 14 age/gender-matched HC; 11 M / 3 F in each group; HC age 38-76 (median 67), PD age 36-77 (median 69).
  - OpenNeuro ds000245 (Yoneyama 2018): 15 PD + 15 matched HC; 7 M / 8 F in each group; HC age 58-69 (median 63), PD age 66-76 (median 71). Tremor-dominant PD patients were excluded to minimise motion artifact (p. 3), so these PD patients are non-tremor-dominant. The 8-year median age gap is not discussed.
- Sites/scanners: multi-source (PPMI multi-site, OpenNeuro); scanner parameters not reported. Class imbalance in PPMI (92 vs 22).
- Labels: PD vs HC clinical grouping; stage/severity/medication not reported.

**5. Results**
- Region-level accuracies (SVM / GBC, 5-run averages, Table 2, p. 5): PPMI best Region 5 0.73/0.80, Region 4 0.84/0.82; ds001354 best Region 3 0.94/0.97; ds000245 best Region 4 1.00/1.00. Many regions near chance (e.g. PPMI Region 3 0.12/0.22; Region 2 0.35/0.56). [CHECK against the table image: Table 2 is not in the PDF text layer.] The protocol behind these scores (held-out split vs in-sample) is not described.
- Top four regions averaged over the three datasets (Table 3, p. 6): 0.91, 0.87, 0.72, 0.54 (temporal lobe, parieto-occipital, motor region, occipital).
- Patient-specific analysis, single region, 5-fold CV: 87.8% average accuracy (p. 4). For the illustrated example the embedding is obtained from training data and test subjects are projected into it (Fig. 5, p. 4).
- Multi-region DNN, 5-fold CV (Table 4, p. 7): DNN 0.964, Gradient Boost 0.914, SVM 0.837 [CHECK against the table image]. The paper does not say which dataset this is. The only pointer is "four regions in Fig. 3", and Fig. 3 is the ds000245 figure (n = 30 in total). Do not cite 96.4% as a PPMI result.
- Not reported: sensitivity/specificity/precision/recall/F1/AUC, CIs, per-fold variance, confusion matrices. No external test set.

**6. Evaluation and leakage check**
- Feature (region) selection before the split: regions are chosen for high classifiability (five shown out of more, others "not presented", p. 4; top four in Table 3) on the same data later used for the multi-region classifier. No evidence this was done inside CV folds. Leakage risk: moderate to high.
- Same participant in train and test: 5-fold CV is stated, but the paper does not say how folds were formed; points in the figures appear to be one per subject, but this is not stated.
- Tuning on test data: UMAP hyperparameters (metric, a, b) are reported but the paper does not say how they were chosen. In Figs 2-4 all subjects are embedded together, so those cluster plots are not out-of-sample predictions. The paper does not say whether labels were used by UMAP.
- Independent test set: none. No dataset is held out for the final model.
- Confounds: no motion covariate (ds000245 excluded tremor-dominant PD to limit motion artifact, p. 3, an implicit acknowledgement of the issue); age/sex distributions reported but not controlled in the PPMI analysis (HC median 63 vs PD 66); medication, site, scanner not reported.
- Metrics beyond accuracy: none. The custom min-of-recalls metric makes comparison with plain accuracy in other papers unreliable.
- Code and data: data public (OpenNeuro ds000245, ds001354; PPMI on request); code released at the GitHub address printed on p. 7 (the URL breaks across a line in the PDF, so copy it from the PDF and check it resolves).

**7. Limitations**
- Admitted (p. 7): data quality limits training; scanner/parameter effects on the embedding not investigated (critical for cross-site validation); binary classification only, PD staging unknown; multimodal diagnosis would help.
- Not admitted: imbalance in PPMI (92 vs 22) is handled only through the choice of metric (Eq. 3), with no resampling or weighting described; region selection and final evaluation use the same data; no standard metrics (AUC, sens/spec); the dataset behind the headline 96.4% is not stated; scores of 1.00 on the n = 30 datasets are very likely inflated (tiny n, protocol unstated); UMAP embeddings of full datasets are descriptive, not predictive validation; the "first time" novelty claim (p. 2) is not substantiated with a literature check; the SVM/GBC/DNN comparison is on one unstated dataset and not benchmarked against published baselines on identical splits.

**8. Connection to my thesis (Leveraging fMRI Data for Early Prediction of Parkinson's Disease)**
- Role: method idea + background; weak comparison point (dataset behind the headline number is unclear).
- Relevant for: Methods chapter (GHE/fractal features as an alternative temporal feature family to ALFF/ReHo; UMAP as dimension reduction/visualisation, with caution); Discussion (region-specific biomarker idea: temporal, parieto-occipital and motor regions are linked by the authors to known PD symptoms).
- Directly reusable idea: per-region biomarkers with region-wise classifiability ranking; their code is public, so the pipeline could be re-run with subject-level splits and standard metrics as one of my baselines.
- Caveat: established diagnosis, not early prediction (despite "early detection" wording in the abstract); the 96.4% is not comparable to Li 2024's PPMI re-split results.

**9. My own thoughts and criticism**
- The GHE + UMAP pipeline is an interesting nonlinear alternative to correlation-based features, and code availability makes it reproducible; worth re-implementing under a stricter protocol.
- The min-of-recalls metric (Eq. 3) is unusual. It is probably chosen for robustness to imbalance, but it is not comparable to the plain accuracy other papers report, so the paper's cross-paper comparisons are shaky.
- Region selection on the same data as evaluation is a real leakage concern for the 96.4% claim; a nested design would settle it.
- The near-chance and below-chance region scores in PPMI (0.12, 0.22) show how dataset-dependent the embedding is; CIs are missing.
- UMAP on full datasets is descriptive, not predictive; the paper sometimes conflates visual cluster separation with diagnostic accuracy.
- The 96.4% appears to come from the "four regions in Fig. 3" input, which is the ds000245 figure with 30 subjects; if so it is a small-sample result.

**10. Quotes (max 2, with page)**
- Scanner/parameter effects on the embedding were not investigated, which the authors call "critical for a wide range of validation across different sites" (p. 7, Limitation and Future Work).
