# boutet2021dbs

**Reference:** Boutet, A., Madhavan, R., Elias, G. J. B., Joel, S. E., Gramer, R., Ranjan, M., Paramanandam, V., Xu, D., Germann, J., Loh, A., Kalia, S. K., Hodaie, M., Li, B., Prasad, S., Coblentz, A., Munhoz, R. P., Ashe, J., Kucharczyk, W., Fasano, A., & Lozano, A. M. (2021). Predicting optimal deep brain stimulation parameters for Parkinson's disease using functional MRI and machine learning. _Nature Communications_, 12, 3043.
**DOI:** https://doi.org/10.1038/s41467-021-23311-9
**Type:** ML study | **License:** CC BY 4.0 | **Read on:** 2026-11-17 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/boutet2021dbs.pdf`)

## Main idea

fMRI recorded during DBS ON/OFF cycling (30 s blocks, six cycles, 6.5 min) shows distinct brain response patterns for clinically optimal vs. non-optimal stimulation settings. An LDA classifier trained on 39 already-optimized patients classifies a setting as optimal or not, and is tested on two unseen groups of 9 patients each. The fMRI response is proposed as an objective biomarker to assist DBS programming (pp. 1-2).

## Method

- SPM12/MATLAB: slice-time + motion correction, T1/MNI registration, 6 mm smoothing (p. 11)
- Motion: volumes > 1.5 mm removed (max 6 per patient, 3.3%); 6 motion regressors; motion not correlated with the ON/OFF design (p. 11)
- Features: 16 a priori ROIs (motor circuit + side-effect areas), 16 positive + 16 negative t-values = 32 features per setting, normalized by t-values in areas tied to non-optimal stimulation (visual cortex/operculum for contacts, right motor cortex for voltages) (pp. 2, 11)
- Model: LDA, 5-fold cross-validation (pp. 4, 11). Hyperparameters: none reported
- Unilateral left stimulation, Medtronic 3387 leads, mostly monopolar settings (43/57 patients) (p. 10)

## Data

- 67 PD patients with Medtronic DBS (62 STN, 5 GPi), 203 fMRI sessions, single site (Toronto Western), 3 T GE HDx (pp. 2, 10)
- Labels: neurologist-defined optimal vs. non-optimal contacts/voltages (Toronto Western algorithms) (pp. 2, 10)
- Train 39 patients (contact n = 20, voltage n = 19; 35 STN + 4 GPi); held-out test 1 = 9 a priori optimized (9 STN); test 2 = 9 stimulation-naive (8 STN + 1 GPi), labeled afterwards by a neurologist blinded to fMRI (pp. 2, 4, 11). Frequency data (n = 10) were acquired with a different paradigm and not used in the model
- Medication: last dose the night before; DBS off ~15 min before scanning (p. 10)
- Data private (on request; only the Fig. 3A/B data are public); code public (GitHub/Zenodo) (p. 11)
- Competing interests: three authors are GE employees (GE Research also funded the work and contributed to design, acquisition, analysis and writing); five authors, including the senior author, hold IP related to the manuscript (p. 13)

## Results

- 88% training accuracy = 5-fold CV on n = 39 (pp. 1, 4). Motor-only ROIs 67%; excluding the 4 GPi patients gives "86% to 81%" (p. 4; the text gives 86%, not 88%, as the reference value)
- Test 1 (held-out, n = 9): combined model best, with the lowest false-positive rate; the exact accuracy is only in Fig. 5E (about 80%+), not in the text. Contact-only 63%, voltage-only 71% (p. 4)
- Test 2 (held-out, n = 9, stimulation-naive): 76% agreement with the blinded neurologist's settings, determined over ~1-1.5 years of programming (p. 6). From the Fig. 5E bars, the contact-only and voltage-only models are near chance on this cohort (roughly 55% and 50%, read off the figure)
- Fig. 5 matrices: rows sum to 100%. In test 2 (Fig. 5B) only 42.9% of settings predicted "optimal" fall in the observed-optimal column, so the 76% hides many false positives. The normalization is not explained; check Source Data before quoting
- Pattern: BOLD decrease in ipsilateral primary motor cortex, increase in ipsilateral thalamus, contralateral cerebellar changes; non-optimal settings recruit non-motor areas (visual cortex, operculum) (pp. 2-3, 7)
- Voltage: ipsilateral M1 BOLD did not significantly separate optimal from non-optimal voltage (p > 0.05, p. 4)

## Evaluation and leakage check

- Feature selection before the split? ROIs chosen a priori from PET/SPECT literature (pp. 2, 11), but the normalization regions were "chosen based on initial data exploration" (p. 11), on unspecified data
- Same participant in train and test? Not across train/test groups, but "optimized patients were randomly assigned to the train and test datasets" (p. 11), so test 1 is a random hold-out from the same cohort and site. Within the 5-fold CV it is not stated whether folds split by patient or by setting (p. 11)
- Tuning on test data? No hyperparameter tuning; model variants (combined / contact-only / voltage-only) were compared on test set 1 and the combined model highlighted as best (p. 4)
- Independent test set? Yes, two groups of 9, same institution and hardware (pp. 2, 11)
- Confounds: motion checked (p. 11); medication timed (p. 10); age/sex in Table 1 but not modeled (p. 4); the clinically optimal contact was usually scanned first, no washout (p. 9)
- Metrics beyond accuracy: ">80% sensitivity" stated once (p. 9); no AUC or specificity in the text; confusion matrices in Fig. 5 (p. 8)
- Code and data: code public, data private (p. 11)

## Limitations

- Admitted: small samples, overfitting controlled by restricting ROIs (p. 9); acquisition order not fully randomized, no washout (p. 9); one hardware family (Medtronic 3387), 3 T (p. 9); frequency/pulse-width unexamined (p. 9); immediate clinical improvement as a possible BOLD confound (argued away with anesthetized-patient and animal evidence) (p. 9)
- Not admitted: CV fold level (patient vs. setting) never stated; binary labels only cover pre-screened candidate settings, not the full programming space; n = 9 test sets give wide uncertainty on 76%; the number of classified settings per test set is not given in the text; GE/IP conflicts are declared but not discussed as a limitation

## Connection to my thesis

- Relevant: published fMRI + ML in PD with held-out test sets and blinded naive-cohort labeling; explicit small-sample overfitting statement (p. 9)
- Chapter: Related Work; Discussion (small-sample limitation)
- Role: background/evidence. NOT a baseline for PD-vs-healthy or early-prediction work: the task is DBS-setting prediction within patients
- Cited in qin2025stn's introduction as an SVM study, but Boutet used LDA (p. 11)

## My own thoughts and criticism

- Quote 88% only as CV training accuracy; the honest generalization numbers are the two n = 9 test results
- Strongest design element: the blinded naive cohort approximates prospective use, but n = 9 and an unstated number of settings mean 76% carries wide uncertainty
- Feature normalization bakes domain knowledge (non-optimal-response areas) into the features: interpretable, hard to transfer
- Table 1 is internally consistent (the 18 STN + 2 GPi row is the n = 20 contact group). Real inconsistencies: Methods say 59 chronically stimulated + 9 stimulation-naive patients (= 68) for a 67-patient cohort (p. 10), and the GPi-exclusion baseline is 86% in the text vs. 88% headline (p. 4)
- Unstated CV fold level (patient vs. setting) is a real open leakage question with multiple settings per patient

## Quotes

- "the number of features are much greater than the number of independent samples" (p. 9)
- "correctly predicted which DBS settings were deemed clinically optimal" (p. 6)
