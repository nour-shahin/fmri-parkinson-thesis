# guo2022lstm

**Reference:** Guo, X., Tinaz, S., & Dvornek, N. C. (2022). Characterization of Early Stage Parkinson's Disease From Resting-State fMRI Data Using a Long Short-Term Memory Network. _Frontiers in Neuroimaging_, 1, 952084.
**DOI:** https://doi.org/10.3389/fnimg.2022.952084
**Type:** ML study | **License:** CC BY | **Read on:** 2026-11-17 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/guo2022lstm.pdf`)

## Main idea

Instead of PD vs. controls, this paper classifies disease stage within PD: Hoehn and Yahr stage 1 vs. 2, using raw rs-fMRI ROI time series fed directly to an LSTM, preserving temporal information that FC pipelines discard. The LSTM reaches 71.63% subject-level accuracy under 5-times repeated 10-fold stratified CV, beating FC-based ML and a CNN, and its output correlates with MDS-UPDRS-III motor severity (pp. 1, 6). Learned weights and a post-hoc FC analysis implicate motor, visual, limbic, and default-mode regions; all stage-discriminating edges weaken from stage 1 to 2 (pp. 6-8).

## Method

- CONN toolbox v17: motion correction, outlier detection (FD > 0.9 mm or global signal > 5 SD), MNI normalization, 8 mm smoothing, AAL-116 ROIs; CompCor (WM/CSF), motion/outlier regression, detrending, no GSR; bandpass 0.008-0.09 Hz (p. 3)
- Augmentation: crops of w = 50 time points (2 min), stride 1, 156 per subject, 13,104 total; applied in training and testing (p. 3)
- LSTM: ROI time series in, hidden states pooled to a dense layer, dropout 0.5, sigmoid; L2 = 0.01, early stopping (patience 10, max 50 epochs); Adam lr 1e-4, batch 200; hidden size tuned in [16, 32, 64, 128] on a validation fold (pp. 4-5)
- Baselines: linear SVC, RF, LR on FC matrices (Ledoit-Wolf, upper triangle); 1-D CNN on the same time series (p. 4)
- Split per fold: 80/10/10 train/validation/test, stratified; class imbalance handled with inverse-ratio sample weights; final model retrained on train + validation (p. 5)

## Data

- PPMI (public, 24 sites in the US/Europe/Australia): 84 subjects after excluding 6 of 90 (poor normalization or motion): 56 stage 2 (41 M/15 F, 62.5 +/- 9.6 y) and 28 stage 1 (16 M/12 F, 58.2 +/- 9.5 y). Called "age-matched" because the t-test gave p > 0.05, although the stage means differ by about 4 years; sex and onset side also p > 0.05 (p. 3)
- rs-fMRI: 8.5 min, TR 2.4 s, 206 frames after dropping 4; head motion not significantly different between stages (Table 2, p. 3)
- Labels: clinical H&Y stage 1 vs. 2; MDS-UPDRS-III 14.00 +/- 5.57 vs. 23.69 +/- 10.70 (p. 5)
- Data via PPMI application; code availability not stated (pp. 9-10)

## Results

All results are internal CV (5-times repeated 10-fold, subject-level majority vote); no external held-out test.

- LSTM accuracy 0.7163 +/- 0.1318, F1 0.7912 +/- 0.1050, precision 0.7794, recall 0.8226, specificity 0.5833 +/- 0.2948 (Table 3, p. 6). Accuracy of the others: CNN 0.6007, RF 0.5862, SVC 0.5811, LR 0.5664
- LSTM significantly better than all models in accuracy, F1, recall (corrected repeated k-fold test, alpha = 0.05, df = 49); in precision/specificity only vs. SVC (p. 6)
- LSTM output vs. MDS-UPDRS-III r = 0.4270 +/- 0.0595 (p = 0.00003), highest of all models (Table 4, p. 6)
- Top-weight ROIs (Table 5, p. 7): cerebellar vermis 10, orbital inferior/middle frontal gyri, bilateral calcarine, right insula, right caudate, superior occipital gyri, left amygdala, right postcentral, cerebellar regions, SMA, posterior cingulate, right lenticular nucleus
- Stage 1 vs. 2 FC (Table 6, p. 7): 11 edges, all weaker in stage 2, mostly between non-motor nodes. The text states the FDR outcome only for the regression analysis below, so whether Table 6 edges survive FDR is unclear
- Elastic net on MDS-UPDRS-III (Table 7, pp. 7-8): 13 edges with permutation p between 0.0004 and 0.043. After FDR at q = 0.2 only the top three edges survive, all "decreased" with impairment (calcarine L/R and superior occipital R to right postcentral). The vermis edges that "increase" with impairment (p = 0.022-0.033) do not survive
- Whole-brain FC control: no edge survived FDR in either analysis, read by the authors as overfitting of the whole-brain analysis (pp. 7, 9)

## Evaluation and leakage check

- Feature selection before the split? None for the LSTM (raw ROI time series) or the baselines (full FC upper triangle) (p. 4)
- Same participant in train and test? No: subject-level splits and subject-level outputs (p. 5); 156 heavily overlapping crops per subject raise effective-sample-size concerns, not leakage
- Tuning on test data? No: tuning on the 10% validation fold, then retraining on train + validation. Exception: window length w = 50 was chosen "on a random cross-validation fold" before the protocol (p. 5), a mild selection on CV data
- Independent test set? Not reported: internal CV only, no cross-cohort replication (pp. 5-6)
- Confounds: head motion reported per stage, no difference (Table 2, p. 3); age (4-year mean gap, p > 0.05), sex and onset side tested (p. 3); medication status not discussed for this cohort
- Metrics beyond accuracy: precision, recall, specificity, F1 (p. 5) plus MDS-UPDRS-III correlation as a validity check (p. 6); no AUC
- Code and data: data public via PPMI (p. 9); code not stated

## Limitations

- Admitted: single preprocessing pipeline without GSR; rs-fMRI only, multimodal data left to future work (p. 9)
- Not admitted: small sample for deep learning (84 subjects, 28 stage 1); low specificity (0.5833) means stage-1 detection is barely above chance, with huge fold variance; no sensitivity analysis of the crop augmentation; no external validation despite multicenter PPMI; the restricted-ROI FC analysis is circular (see below)

## Connection to my thesis

- Relevant: first LSTM on raw rs-fMRI for early-stage PD staging; evidence that temporal modeling beats FC-based ML at modest n; subject-level evaluation of overlapping crops; correlation with a continuous clinical scale as an external-validity check
- Chapter: Related Work (deep learning on rs-fMRI time series, within-PD staging); Discussion (modest within-PD staging accuracy; note it is a different task from donisi2025connectomes' PD vs. HC numbers)
- Role: related work + method idea (windowed time series with subject-level voting; corrected repeated k-fold comparison test)

## My own thoughts and criticism

- The 71.63% needs its baseline: stage 2 is 56/84 = 66.7% of subjects, so always predicting stage 2 gives 66.7% accuracy, recall 1.0 and F1 0.80 (my calculation). The LSTM's F1 (0.791) is not above that trivial rule and its accuracy gain is about 5 points. Report it as modestly above the majority-class rate, not as "credible because unimpressive"
- Recall 0.82 vs. specificity 0.58: the model over-predicts stage 2 (the majority class); part of the LSTM's advantage over the baselines may be better imbalance handling rather than richer temporal features (the CNN's specificity 0.33 shows how badly small imbalanced data distorts per-class rates)
- Abstract vs. Table 3 mismatch: it claims 13.52% above the "best traditional ML method", but the best baseline by accuracy is RF (0.5862), a gap of 13.01%; 13.52% corresponds to SVC. Quote the table
- The weights -> top ROIs -> restricted FC analysis is a sensible template, but circular: ROIs are chosen by a model trained on the stage labels of the same subjects, then FC is tested against those labels. Edges surviving FDR there while the whole-brain analysis finds nothing is partly a selection effect, not independent confirmation. Input-weight magnitude is also a crude importance measure
- The vermis "increases with impairment" and the cerebellar-shift interpretation rest on uncorrected p-values
- H&Y labels are coarse and partly subjective; r = 0.43 with MDS-UPDRS-III is a good validity check but shows the ceiling: imaging explains about 18% of motor-score variance (my calculation, r^2)

## Quotes

- "did not survive correction" (p. 9, on the whole-brain FC analysis)
- "significant improvement in accuracy, F1, and recall compared to all other models" (p. 6)
