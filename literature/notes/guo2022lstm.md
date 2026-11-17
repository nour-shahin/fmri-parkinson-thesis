# guo2022lstm: LSTM on raw rs-fMRI time series classifies early-stage PD (stage 1 vs 2) in PPMI

**Reference:** Guo, X., Tinaz, S., & Dvornek, N. C. (2022). Characterization of Early Stage Parkinson's Disease From Resting-State fMRI Data Using a Long Short-Term Memory Network. _Frontiers in Neuroimaging_, 1, 952084. (full entry in `references.bib`)
**DOI / link:** https://doi.org/10.3389/fnimg.2022.952084
**Type:** research article (open access, CC BY)
**Read on:** 2026-11-17
**PDF in repo:** yes (`literature/pdfs/guo2022lstm.pdf`, CC BY)

## Main idea

Instead of classifying PD vs. healthy controls, this paper classifies disease stage *within* PD: Hoehn and Yahr stage 1 vs. stage 2, using raw rs-fMRI ROI time series fed directly into an LSTM, which keeps temporal information that FC-based pipelines discard (pp. 1-2). The LSTM reaches 71.63% subject-level accuracy under repeated 10-fold stratified CV, beating FC-based traditional ML and a CNN baseline, and its output scores correlate with MDS-UPDRS-III motor severity (pp. 1, 6). Learned weights and post-hoc FC analysis highlight motor, visual, limbic, and default-mode regions; all stage-discriminating edges weaken from stage 1 to 2 (pp. 6-8).

## Method

- Preprocessing (CONN toolbox v17): motion correction, outlier detection (framewise displacement > 0.9 mm or global signal > 5 SD), MNI normalization, 8 mm FWHM smoothing, AAL-116 atlas ROI extraction; denoising with CompCor (WM/CSF principal components), motion/outlier regression, linear detrending; no global signal regression; bandpass 0.008-0.09 Hz; ROI mean time series standardized by temporal SD (p. 3).
- Data augmentation by cropping: window w = 50 time points (2 min), stride s = 1, 156 crops per subject, total 13,104 sequences; applied to all subjects in training and testing (p. 3).
- LSTM: ROI time series input, hidden states from every time step pooled into a dense layer (1 node), dropout 0.5, sigmoid output = probability of stage 2; L2 regularization (lambda = 0.01) and early stopping (patience 10 epochs, max 50); Adam, lr 1e-4, batch 200; PyTorch, 1 GPU (pp. 4-5). Architecture follows the authors' earlier autism LSTM (Dvornek et al. 2017).
- Baselines: linear SVC, RF, logistic regression on FC matrices (Ledoit-Wolf covariance, upper triangle only), and a 1-D CNN (kernel sizes 7/5/3, channels 16/32/32) on the same ROI time series (p. 4).
- Hyperparameter tuning: within each CV split, a 10% validation set selects hyperparameters (LSTM hidden size from [16, 32, 64, 128]; LR C in [1e-9, 10]; SVC C in [0.01, 10]; RF trees [10-500], depth 2-6, etc.); the final model is then retrained on train + validation (p. 5). The LSTM input length w = 50 was chosen "based on initial testing on a random cross-validation fold" (p. 5, details in supplementary).
- Training split per fold: 80% train / 10% validation / 10% test, stratified by stage; class imbalance handled by inverse-ratio sample weights (p. 5).

## Data

- PPMI (public, 24 sites in US/Europe/Australia): 90 subjects curated, 6 excluded (poor normalization or excessive motion), leaving 84 subjects: 56 stage 2 (41 M / 15 F, age 62.5 +/- 9.6) and 28 stage 1 (16 M / 12 F, age 58.2 +/- 9.5); age (p > 0.05), sex, and onset side matched (p. 3, Table 1).
- rs-fMRI: 8.5 min, TR 2400 ms, 206 frames after discarding the first 4 (p. 3).
- Head motion not different between stages (Table 2, p. 3). MDS-UPDRS-III: stage 1 = 14.00 +/- 5.57, stage 2 = 23.69 +/- 10.70 (p. 5).
- Data available from PPMI under a Data Use Agreement and online application; no code availability statement (pp. 9-10).

## Main results

- Classification (subject-level, Table 3, p. 6): LSTM accuracy 0.7163 +/- 0.1318, F1 0.7912 +/- 0.1050, precision 0.7794 +/- 0.1047, recall 0.8226 +/- 0.1579, specificity 0.5833 +/- 0.2948. CNN 0.6007 accuracy; RF 0.5862; SVC 0.5811; LR 0.5664.
- Statistical comparison (corrected repeated k-fold test, k = 10, r = 5): LSTM significantly better than all other models in accuracy, F1, and recall; in precision and specificity only vs. SVC (p. 6).
- Severity correlation (Table 4, p. 6): LSTM output vs. MDS-UPDRS-III r = 0.4270 +/- 0.0595 (p = 0.00003), highest of all models; SVC r = 0.1748 not significant (p = 0.12).
- Interpretation (Table 5, p. 7): top ROIs by input-hidden weight magnitude: cerebellar vermis 10, right orbital inferior frontal gyrus, bilateral calcarine sulcus, orbital middle frontal gyri, right insula, right caudate, superior occipital gyri, left amygdala, right postcentral gyrus, cerebellar regions, right SMA, posterior cingulate, right lenticular nucleus.
- FC analysis on top ROIs (Table 6, p. 7): all 11 significant stage-1 vs. stage-2 edges weaker in stage 2 (e.g. right postcentral - left superior occipital, p = 0.0022), i.e. progression involves FC decrease, mostly between non-motor nodes.
- Elastic net regression on MDS-UPDRS-III (FDR q = 0.2, Table 7, p. 8): vermis-sensorimotor and vermis-visual edges increase with motor impairment; most other significant edges decrease.
- Whole-brain FC control analysis: no edge survived FDR correction, which the authors read as overfitting of conventional whole-brain analysis in small samples (p. 7).

## Evaluation and leakage check

Evaluation: 5-times repeated 10-fold stratified CV, subject-level outputs by majority vote over crops; five metrics reported; corrected repeated k-fold significance test (alpha = 0.05) (pp. 5-6).

- Feature selection before the split? No feature selection step: the LSTM consumes raw ROI time series, and baselines use the full FC upper triangle (6670 values for AAL-116) with no univariate preselection (p. 4). No leakage from feature selection.
- Same participant in train and test? No. Splits are at subject level and metrics are computed on subject-level majority votes (p. 5). Crops of one subject never straddle folds, though 156 heavily overlapping crops per subject make effective sample size an issue, not leakage.
- Hyperparameters tuned on test data? Not directly: tuning uses the 10% validation fold inside training, then the model is retrained on train + validation and evaluated on test (p. 5). Exception: the sequence length w = 50 was chosen on "a random cross-validation fold" before the protocol (p. 5), a mild form of selection on CV data.
- Independent test set? No external dataset; all evaluation is internal CV on PPMI. No cross-cohort replication.
- Confounds checked? Head motion reported per stage with no significant difference (Table 2, p. 3); age, sex, onset side matched (p. 3); medication status not discussed for this cohort in the paper.
- Metrics reported: accuracy, precision, recall (sensitivity), specificity, F1 (p. 5); plus correlation with MDS-UPDRS-III as external validity check (p. 6). No AUC.
- Code and data available? Data public via PPMI application (p. 9); no code release stated.

## Limitations

- Authors' own limitations (p. 9): a single preprocessing pipeline without GSR (results could differ with GSR); rs-fMRI only, multimodal data (task fMRI, cognitive/behavioral, biomarkers) left for future work.
- Small sample for deep learning (84 subjects, 28 in stage 1); the LSTM's low specificity (0.5833 +/- 0.2948) means stage 1 detection is barely above chance on average, with very high variance across folds.
- Internal CV only; no external validation, although PPMI is multicenter, which partially mitigates single-scanner bias.
- Class imbalance 2:1 handled by sample weights; no sensitivity analysis of the augmentation (crop length/stride) on results.

## Connection to my thesis: what is relevant, and for what?

- Relevant information: the first use of an LSTM on raw rs-fMRI for early-stage PD staging; evidence that temporal modeling beats FC-based ML at modest sample size; subject-level evaluation of overlapping crops via majority vote; correlation of model output with a continuous clinical scale as a validity check (pp. 1, 5-6).
- Used in chapter / section: Related Work (deep learning on rs-fMRI time series; stage staging rather than diagnosis); Discussion (what moderate, honestly-reported accuracy looks like: 71.6% with wide fold-to-fold variance, vs. donisi2025connectomes' 95%+ under internal CV with synthetic controls).
- Used as: related work. NOT a baseline for PD vs. HC classification: the task is stage 1 vs. stage 2 within patients, a different (and arguably harder, subtler) discrimination, and the input is raw time series rather than FC or graph features.

## My own thoughts and criticism

- The 71.63% headline is credible precisely because it is unimpressive: near 70% with honest variance, on a subtle within-disease task, with a real (non-synthetic) public cohort and subject-level voting. This is the kind of number that survives external validation, unlike the 95%+ internal results of donisi2025connectomes.
- The specificity problem deserves more attention than the paper gives it: recall 0.82 vs. specificity 0.58 means the model over-predicts stage 2 (the majority class), so part of the LSTM's advantage over baselines may be better calibration of the imbalance weighting rather than richer temporal features. The CNN's even lower specificity (0.3266) shows how badly imbalanced small data distorts per-class rates.
- The abstract's claimed margins do not match Table 3: it says 13.52% above the best traditional ML method, but the best traditional model in Table 3 is RF (0.5862), giving a real gap of 13.01%; the 13.52% corresponds to SVC (0.5811), which is not the best baseline. Small, but quote the table.
- The interpretation pipeline (weights -> top ROIs -> restricted FC analysis) is a sensible template: restricting FC analysis to model-selected ROIs let edges survive FDR where the whole-brain analysis found nothing (p. 7). But LSTM input-weight magnitude is a crude importance measure; gradients or attention would be stronger, and the authors' own supplementary picks w = 50 the same informal way.
- Stage labels come from clinical Hoehn and Yahr ratings, which are coarse and partly subjective; correlating model output with MDS-UPDRS-III (r = 0.43) is a good validity check but also shows the ceiling: the imaging signal explains only ~18% of motor-score variance.
- Directly relevant to my evaluation design: this paper shows the corrected repeated k-fold test (Bouckaert and Frank) for comparing classifiers under repeated CV, a cheap upgrade over reporting means alone.

## Relevant quotes

- "the current work focuses on the usage of only rs-fMRI data in early stage PD classification... the LSTM model showed significant improvement in accuracy, F1, and recall compared to all other models." (pp. 6, 9)
- "the very large number of connections in the whole-brain FC analysis not only hinders interpretation but also did not survive correction... given the relatively smaller number of subjects, the whole-brain FC analysis could result in overfitting." (p. 9)

## Reading questions

1. **How can I use this?** As related work for temporal deep learning on rs-fMRI in PD, as a realistic accuracy benchmark for within-PD staging on public data, and as a methodological reference for subject-level evaluation of windowed time series and the corrected repeated k-fold comparison test.
2. **Does it do what the authors claim?** Largely yes for the comparison claims (statistically tested against baselines under a corrected repeated CV test), with two soft spots: the best-baseline margin is overstated in the abstract (RF vs. SVC, 13.01% vs. 13.52%), and the low specificity shows stage 1 is hard to detect, which the framing underplays.
3. **Do I understand the results?** Yes: 84 PPMI subjects, AAL-116 ROI time series cropped into 156 overlapping windows each, LSTM vs. CNN vs. FC-based LR/RF/SVC under 5 x 10-fold stratified CV; LSTM 71.6% subject-level accuracy, highest MDS-UPDRS-III correlation (r = 0.43); top-weight ROIs span motor, visual, limbic, and default-mode systems; stage 2 shows FC weakening, mostly between non-motor nodes.
