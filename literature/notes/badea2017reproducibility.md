# badea2017reproducibility

**Reference:** Badea, L., Onu, M., Wu, T., Roceanu, A., & Bajenaru, O. (2017). Exploring the reproducibility of functional connectivity alterations in Parkinson's disease. _PLoS ONE_, 12(11), e0188196.
**DOI:** https://doi.org/10.1371/journal.pone.0188196
**Type:** reproducibility study | **License:** CC BY | **Read on:** 2026-11-17 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/badea2017reproducibility.pdf`)

## Main idea

PD-related rs-fMRI functional connectivity (FC) changes reported across studies contradict each other. Under one uniform preprocessing pipeline, global PD-related FC changes are non-reproducible across three independent datasets. Random splits of a single dataset with replicate scans show the same non-reproducibility, which the authors read as disease heterogeneity dominating over technical differences (pp. 1, 11-12).

## Method

- Uniform FSL pipeline: MCFLIRT motion correction, BET, 5 mm smoothing (SUSAN), 0.01 Hz high-pass, BBR registration to T1 then linear + nonlinear to MNI152 at 4 mm (p. 5)
- Variants tested: global signal regression, bandpass 0.01-0.1 Hz, low-motion subsets, single PPMI center (pp. 5, 8). Doubling the TR was tested by dropping every second time point of the NEUROCON data (a synthetic TR, not a real acquisition) (p. 8)
- Features: Fisher-z FC of all ROI pairs on 13 externally built parcellations (90-950 regions; group-ICA on the analyzed data deliberately avoided) (pp. 5-6, 13)
- Reproducibility measure: correlation R of PD-vs-NC t-value vectors between two datasets (or splits), permutation-tested, 1000 permutations (pp. 6, 8)
- Heterogeneity test on the NEUROCON replicate scans: "split subjects" (different subjects, all their replicates together; heterogeneous; Ns = 2510 splits) vs. "split replicates" (the replicates of each subject in different halves; homogeneous; Ns = 325) (pp. 7-9)
- Classifiers: linear SVM and Gaussian Naive Bayes on t-test-selected FC features (N = 10-5000); average of per-class accuracies as the metric, chance 0.5 (p. 10)

## Data

- Table 1 (p. 4). NEUROCON (Bucharest): 27 PD (16 M) / 16 NC (5 M), 2 replicate scans per subject (54 + 31 scans), Siemens Avanto 1.5T, TR 3.48 s, 137 volumes; H&Y 1.92, disease duration 4.6 y; most patients treated
- Tao Wu (Beijing): 20 PD (11 M) / 20 NC (12 M), Siemens Magnetom 3T, TR 2 s, 239 volumes; H&Y 1.88, duration 5.4 y; most patients treated
- PPMI (multicenter US): 91 PD (63 M) / 18 NC (14 M) as 134 PD and 19 NC scans (so some subjects have more than one scan), Siemens Tim Trio 3T, TR 2.4 s; disease duration 1.9 y, de novo, unmedicated, eyes open (pp. 3-4)
- Labels: clinical PD vs. NC. Class balance varies by dataset (PPMI 91:18)
- Data public at FCP/INDI (p. 1); code availability not stated

## Results

- Global FC changes non-reproducible in all three dataset pairs [held-out datasets]: e.g. NEUROCON-Tao Wu R = -0.146, p = 0.949 (AAL); holds under GSR, bandpass, low-motion, single-center restriction (Table 3, p. 11)
- Heterogeneity: 88% of heterogeneous splits non-reproducible at p > 0.01, 42% at p > 0.05; all homogeneous splits reproducible at p < 10^-3; median R 0.21 vs. 0.71 (p. 12)
- Control contrast (eyes open vs. closed, healthy): reproducible even in heterogeneous splits (only 6% non-reproducible) (p. 12)
- Technical factors (NEUROCON only): doubling TR (synthetic), linear vs. nonlinear registration, GSR all reproduce well (p. 13). ICA-FIX/WM/CSF denoising and age/gender/duration regression change nothing, but both are reported as "data not shown" (p. 13)
- No parcellation rescues reproducibility (13 tested, Table 5, p. 13)
- Cross-dataset classification [held-out datasets]: average accuracies 0.225-0.7, mean 0.497 (SD 0.073); aggregated per training set 0.336-0.591 (pp. 15-16)
- Same-dataset random splits (10,000 splits in half): means only 0.51-0.66 (p. 16)
- Marginally reproducible ROI pairs: only 2 of 13 parcellations significant (Power264 p = 0.033, Talairach p = 0.032; Shen100 p = 0.055), visual-sensorimotor and visual-parietal pairs (pp. 14-15)

## Evaluation and leakage check

- Feature selection before the split? Cross-dataset: t-tests on the training dataset only (p. 10); random same-dataset splits: not stated
- Same participant in train and test? Cross-dataset: no. Random half-splits for the classifiers: not stated whether by subject or by scan, although NEUROCON has 2 scans per subject and PPMI up to several (p. 10). If by scan, subjects leak across halves, which would make the already-low accuracies optimistic
- Tuning on test data? Feature counts and preprocessing variants are reported rather than tuned to maximize test performance (pp. 10, 16)
- Independent test set? Yes, two external datasets per training set (p. 10)
- Confounds: motion subsets and denoising variants checked (pp. 11, 13); PPMI is de novo, unmedicated and eyes open while the others are mostly treated; the authors argue pairwise comparisons make this irrelevant, but it is not controlled (pp. 3-4)
- Metrics beyond accuracy: not reported (per-class average accuracy only) (p. 10)
- Code and data: data public (p. 1); code not stated

## Limitations

- There is no limitations section. The authors say that whether the marginally consistent ROI pairs are more widely reproducible "will have to await the release of more publicly-available PD datasets" (pp. 15, 17-18)
- Not admitted: only simple classifiers (linear SVM, GNB) tried, so the negative result is about these features; the PPMI cohort differs in medication, stage and scan condition; the heterogeneity estimate rests on one 1.5 T dataset with 27 patients, so each random half holds roughly 13 PD and 8 NC subjects. Low R between such small halves is also what sampling noise alone would produce, so "heterogeneity" and "small groups" are not separated. The "split replicates" control puts the same subjects in both halves, so its high R (0.71) reflects identical individuals as well as technical reliability: it is a ceiling, not a neutral noise floor

## Connection to my thesis

- Relevant: quantitative evidence that single-cohort FC biomarker claims do not generalize; the split-replicates design as a transferable idea (with the caveats above)
- Chapter: Related Work (reproducibility of FC biomarkers); Discussion (justifies external validation requirements)
- Role: evidence (the evaluation-rigor argument my Discussion is built on)

## My own thoughts and criticism

- The replicate-scan design is clever: it separates "same people scanned twice" from "different people", but see the caveat that its two arms differ in more than technical noise
- Chance-level cross-dataset accuracy shows that group-average FC is not a stable subject-level biomarker in this feature space with these linear classifiers, not that "fMRI cannot classify PD"; cite it scoped that way
- The within-NEUROCON result is the load-bearing finding because the cross-dataset design carries PPMI's medication/condition shifts
- Any residual subject leakage in the random-split classifiers would only make their low accuracies optimistic, strengthening the conclusion
- Good anchor citation against papers reporting only within-dataset cross-validation, eight years before the field absorbed the lesson. NEUROCON is the dataset shared with shi2022radiomics and qin2025stn

## Quotes

- "PD-related functional connectivity changes turned out to be non-reproducible across datasets" (p. 1)
- "functional heterogeneity may be a dominating factor" (p. 18)
