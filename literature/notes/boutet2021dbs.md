# boutet2021dbs: fMRI + machine learning to predict optimal deep brain stimulation settings

- **Reference:** Boutet, A., Madhavan, R., et al. (2021). Predicting optimal deep brain stimulation parameters for Parkinson's disease using functional MRI and machine learning. *Nature Communications*, 12, 3043. (full entry in `references.bib`)
- **DOI / link:** https://doi.org/10.1038/s41467-021-23311-9
- **Type:** research article (open access, CC BY 4.0)
- **Read on:** 2026-11-17
- **PDF in repo:** yes (`literature/pdfs/boutet2021dbs.pdf`, CC BY 4.0)

## Main idea
fMRI recorded while deep brain stimulation (DBS) is cycled ON/OFF (30 s blocks, six cycles, 6.5 min per session) shows brain response patterns that differ between clinically optimal and non-optimal stimulation settings (electrode contact or voltage). A linear classifier trained on patients whose settings were already optimized predicts optimal vs. non-optimal settings and is tested on two unseen groups. The authors propose the fMRI response as an objective biomarker of DBS efficacy (pp. 1-2).

## Method
- Preprocessing (SPM12/MATLAB): slice-time and motion correction, registration to T1 and MNI space, 6 mm smoothing (p. 11).
- Motion: volumes with motion >1.5 mm removed (at most 6 volumes, 3.3%, per patient); six motion parameters used as regressors; motion was not correlated with the ON/OFF design (p. 11).
- Features: mean t-values (GLM with 30 s ON/OFF design, canonical HRF, unthresholded) from 16 a priori ROIs, 16 positive + 16 negative = 32 features per tested setting. Normalized by t-values in areas tied to non-optimal stimulation: visual cortex and operculum (contact data), right motor cortex (voltage data) (pp. 2, 11).
- Classifier: linear discriminant analysis (LDA), 5-fold cross-validation (pp. 4, 11).

## Data
- 67 PD patients with implanted Medtronic DBS (62 STN, 5 GPi), 3 T fMRI, 203 sessions, one hospital (Toronto Western) (pp. 2, 10). Observational trial NCT03153670.
- Train: 39 patients with a priori optimized settings (20 contact, 19 voltage). Test 1: 9 a priori optimized patients. Test 2: 9 stimulation-naive patients, programmed afterwards by a neurologist blinded to the fMRI results (pp. 2, 4, 11).
- Medication: last dose the night before; DBS off for ~15 min before scanning (p. 10).
- Data private (available on reasonable request); code public on GitHub/Zenodo (p. 11).

## Main results
- 88% cross-validated **training** accuracy (n = 39) (pp. 1, 4). Motor-only ROIs: 67%. Without the 4 GPi patients: 86% to 81% (p. 4).
- Test 1 (n = 9): combined model about 80-82% (approximate, read from the Fig. 5E bar chart; not stated in the text). Contact-only 63%, voltage-only 71% (pp. 4, 8).
- Test 2 (stimulation-naive, n = 9): 76% agreement with the settings the blinded neurologist judged optimal over ~1-1.5 years (p. 6).
- Optimal pattern: BOLD decrease in ipsilateral primary motor cortex, increase in ipsilateral thalamus, changes in contralateral cerebellum; non-optimal settings also recruit non-motor areas such as visual cortex and operculum (pp. 2-3, 8).

## Evaluation and leakage check
- Evaluation: 5-fold CV on the training set plus two independent test sets (n = 9 each). Accuracy is the headline metric; ">80% sensitivity" is stated once (p. 9); confusion matrices in Fig. 5 (p. 8). No AUC.
- Feature selection before the split? ROIs were chosen a priori from PET/SPECT literature (pp. 2, 11), but the normalization regions "were chosen based on initial data exploration" (p. 11), without stating on which data.
- Same participant in train and test? The two test sets are different patients. Inside the CV it is not stated whether folds split by patient or by setting (p. 11 only says patients were randomly assigned to train/test).
- Hyperparameters tuned on test data? None described, but model variants were compared on test set 1 and the combined model highlighted as best (p. 4).
- Confounds: motion checked (p. 11); medication timing controlled (p. 10); age and sex reported in Table 1 but not modeled; scan order not fully randomized, no washout (p. 9).

## Limitations
Small sample and very small test sets; one hospital, one scanner family, one DBS lead model; private data; one fixed canonical HRF; only contact and voltage studied; binary labels simplify real multi-parameter programming (pp. 9-10). The authors say they limited overfitting by restricting features to 16 ROIs (p. 9).

## Connection to my thesis: what is relevant, and for what?
- Relevant information: a published example of fMRI + simple ML in Parkinson's with held-out tests, a blinded stimulation-naive cohort, and an explicit statement about overfitting with few participants (p. 9).
- Used in chapter / section: Related Work; Discussion (small-sample limitation).
- Used as: related work. **Not a baseline**: the task is DBS setting prediction, the features are stimulation-driven activation t-values (not resting-state connectivity), and there is no patient vs. healthy classification.

## My own thoughts and criticism
- Quote the 88% only as cross-validated training accuracy. The generalization evidence is the two n = 9 test results. The paper itself gives the training baseline as 88% and as 86% in neighboring sentences (p. 4).
- Strongest design element: the naive cohort, labeled after scanning by a blinded neurologist (p. 6), which approximates prospective use. But n = 9 and the number of settings classified is not stated, so 76% carries wide uncertainty.
- The Fig. 5B matrix (naive cohort) contains a 42.9% cell for optimal settings (p. 8) that the 76% overall accuracy hides. Check how the matrix is normalized before interpreting; per-class rates matter more than accuracy here.
- Open leakage questions: patient-level vs. setting-level CV folds, normalization regions chosen from data exploration, and mild test-informed model choice.
- Features are domain-engineered (a priori ROIs, normalization by non-optimal areas): good for interpretability, hard to transfer to a diagnosis task.

## Relevant quotes
- "Typically, in neuroimaging data, the number of features are much greater than the number of independent samples, leading frequently to model overfitting." (p. 9)
- "...correctly predicted which DBS settings were deemed clinically optimal... with 76% accuracy..." (p. 6)

## Reading questions
1. How can I use this? As related work and as a citable source for the small-sample overfitting argument.
2. Does it do what the authors claim? Partly. The pattern and the naive-cohort design are credible, but the biomarker claim rests on two n = 9 test sets, and the 88% is training accuracy.
3. Do I understand the results? Yes: optimal stimulation gives a motor-circuit-specific pattern, non-optimal settings add non-motor responses, and 32 normalized ROI values per setting feed an LDA.
