# patil2024scannerbias

**Reference:** Patil, P., & Ford, W. R. (2024). Parkinson's disease recognition using decorrelated convolutional neural networks: Addressing imbalance and scanner bias in rs-fMRI data. _Biosensors_, 14(5), 259.
**DOI:** https://doi.org/10.3390/bios14050259
**Type:** ML study (bias mitigation) | **License:** CC BY 4.0 (MDPI) | **Read on:** 2026-11-18 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/patil2024scannerbias.pdf`)

## Main idea

PD vs. healthy control classification from rs-fMRI is distorted by class imbalance (PPMI: 164 PD vs. 19 controls) and scanner/acquisition bias when datasets are combined. The authors minimize the distance correlation between CNN features and a bias variable (a dummy class label, or scanner variables), producing a decorrelated CNN (DcCNN). Claim: better balanced accuracy on imbalanced PPMI and scanner-invariant features on PPMI + NIFD with little accuracy loss (pp. 1, 6).

## Method

- Preprocessing: FSL v6.0 (BET, MCFLIRT, 5 mm smoothing, 0.01 Hz high-pass); first 10/last 5 slices dropped for PPMI (first 5/last 6 and the first 30 volumes for NIFD); each scan becomes 25 slices x 210 volumes of 66 x 66 images; slices and volumes are used as independent 2D images (pp. 9, 11)
- Features: raw image slices (no atlas, no ROIs); class-bias variable = dummy uniform variable; scanner-bias variables = slice thickness + pixel spacing, features of a scanner classifier (FE model), or temporal SD (pp. 9-12)
- Imbalance handling: random oversampling/SMOTE/stratified sampling tested; the "fusion" method = oversampling + weighted cross-entropy + decorrelation loss (p. 9-10). Oversampling is applied to the training images (Table 2)
- Model: custom CNN with loss = weighted cross-entropy + lambda x DC^2 + L2; variants DcCNN, FE-DcCNN, ConvGRU-DcCNN; RMSprop, minibatch 4000; lambda pairs differ per variant (0.5/5.0, 0.05/0.95, 0.2/0.6) (pp. 10-13)

## Data

- PPMI 183 subjects (164 PD / 19 controls, with follow-up visits); NIFD 215 controls only (follow-up visits). Combined: 398 subjects (183 + 215; the earlier note's 397 is not in the paper) and 2,346,750 slice images, which equals 447 scans of 5,250 images each (my calculation), i.e. more scans than subjects because follow-up scans are counted separately (pp. 8, 11, Table 3)
- Sites/scanners: both Siemens TrioTim 3T; two acquisition protocols (PPMI: TR 2400 ms, TE 25, 3.3 mm slices; NIFD: TR 2000 ms, TE 27, 3.0 mm slices) (pp. 8, 11). The authors call this "multiscanner"
- Public data (PPMI, NIFD); data availability "not applicable", code availability not stated (p. 20). Labels: PD vs. HC; follow-up scans are treated as independent because they were taken at different times (p. 8)
- Diagnosis is confounded with dataset: all PD are from PPMI, and 215 of the 234 controls are from NIFD

## Results

- Imbalanced PPMI, slice-level, held-out test split: fusion method BA 59.42% (sensitivity 58.47%, specificity 60.37%, precision 93.07%) vs. baseline CNN BA 50.01% (100% sensitivity, 0.01% specificity) (Table 4, p. 15). Subject-level after max-wins voting: BA 66.67% (Table 5, p. 16)
- Multiscanner, subject-level, held-out test: baseline CNN/ConvGRU-CNN 94.7% accuracy with 100% scanner-classification accuracy; DcCNN 80.47% (scanner 83.10%); FE-DcCNN 77.80% (80.43%); ConvGRU-DcCNN 65.77% (63.13%) (Tables 6-7, pp. 17-18)
- No cross-validation anywhere; every number is a single 70/15/15 split (p. 9). The reported 95% CIs are across three random initializations of the same split, not across data splits (Tables 5, 7). AUC: not reported (ROC curves plotted, p. 15)

## Evaluation and leakage check

- Selection before the split / on test: lambda pairs, feature layers and the choice among DcCNN / FE-DcCNN / ConvGRU-DcCNN were compared on the held-out results and FE-DcCNN highlighted as "optimal" (pp. 12-13, 17-19); validation-only selection is not stated
- Split level: the Table 3 image counts per split are exact multiples of 5,250 (PD 155/27/36 scans, controls 156/34/39 scans; my calculation), which indicates that the 70/15/15 split was applied to whole scans, not to individual slices. So the leakage route I had assumed (slices of one scan across train and test) most likely did not occur
- Same participant in train and test? Possible through follow-up visits: scans of one subject are treated as independent (p. 8) and the paper does not say follow-ups were kept in the same split. Not discussed by the authors
- Independent test set: none beyond the single hold-out split; no external dataset
- Confounds: age/sex in Table 1 but not modeled (p. 8); medication not reported; PD and controls come from different studies (PPMI vs. NIFD), so diagnosis is confounded with dataset; "multiscanner" is two protocols on the same scanner model
- Metrics beyond accuracy: sensitivity, specificity, precision, F1, balanced accuracy, scanner-classification accuracy, t-SNE (pp. 14-18)

## Limitations

- Admitted: ConvGRU-DcCNN loses accuracy; larger datasets needed; future work on interpretability and larger data (pp. 19-20)
- Not admitted: follow-up visits treated as independent subjects; no comparison with ComBat or domain adaptation, explicitly declined (p. 19); the Discussion states the method is "designed for rs-fMRI data collected from a single scanner with identical acquisition protocols and a single site" (p. 19), which sits oddly with the multiscanner claims; the claim that "a multiscanner and larger dataset results in significantly better performance" compares accuracy in a dataset-confounded design with balanced accuracy in the imbalanced one (p. 20)
- The novelty claim "used for the first time to train CNN models for PD classification" (p. 20) is specific to CNNs. Their own prior-work section cites an LSTM on rs-fMRI (ref. 6, guo2022lstm), so the novelty is the CNN/decorrelation combination, not rs-fMRI deep learning

## Connection to my thesis

- Relevant: scanner-classification accuracy as an operational bias check; a demonstration that 94.7% accuracy can be entirely scanner/dataset-driven
- Chapter: Related Work (bias mitigation in rs-fMRI ML); Discussion (scanner bias / generalization)
- Role: evidence, not a baseline (diagnosis on raw slices, no atlas or connectivity features)

## My own thoughts and criticism

- The quotable contrast is 94.7% accuracy at 100% scanner classification vs. 77.8% at 80.4%: headline accuracy in a confounded multi-protocol design is uninformative without the scanner check
- The same shortcut plausibly operates in solanalavalle2024causalforest (all PD from PPMI, most controls from FCP); cite them together
- The class-bias gain is modest: BA 50.01% -> 59.42% (slice) and 66.67% (subject) is improvement over a broken baseline, not strong diagnosis
- Follow-up scans as independent samples is the remaining subject-leakage risk and should be flagged, but scan-level splitting means the slice-leakage criticism does not apply
- "Multiscanner" is protocol bias on one scanner model; cross-vendor transfer is untested

## Quotes

- "classification of control subjects are almost based on random chance" (p. 14)
- "all PD subjects in the dataset were scanned on one scanner" (p. 17)
