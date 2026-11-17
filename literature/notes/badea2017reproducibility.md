# badea2017reproducibility: rs-fMRI functional connectivity changes in PD are not reproducible across datasets

**Reference:** Badea, L., Onu, M., Wu, T., Roceanu, A., & Bajenaru, O. (2017). Exploring the reproducibility of functional connectivity alterations in Parkinson's disease. _PLoS ONE_, 12(11), e0188196. (full entry in `references.bib`)
**DOI / link:** https://doi.org/10.1371/journal.pone.0188196
**Type:** research article (open access, CC BY)
**Read on:** 2026-11-17
**PDF in repo:** yes (`literature/pdfs/badea2017reproducibility.pdf`, CC BY)

## Main idea

Resting-state fMRI functional connectivity (FC) changes reported in Parkinson's disease contradict each other across studies. This paper tests reproducibility directly: it compares PD-related FC changes across three independent datasets processed with one uniform workflow, and finds them non-reproducible (pp. 1, 11). Using replicate scans of the same subjects, it then shows that random splits of a single dataset are also frequently non-reproducible, so functional heterogeneity of the disease, not technical differences, dominates (pp. 1, 12). Classifiers trained on one dataset fail on the others, and even fail on random splits of the same dataset (pp. 1, 15-16).

## Method

- Preprocessing (uniform for all datasets, FSL): dcm2nii conversion, motion correction (MCFLIRT), brain extraction (BET), 5 mm FWHM smoothing (SUSAN), high-pass filtering (0.01 Hz), BBR registration of BOLD to T1, then linear+nonlinear registration to 2 mm MNI152 (nonlinear resampling at 4 mm) (p. 5).
- Variants tested: global signal regression (GSR), bandpass filter 0.01-0.1 Hz, low-motion subsets (suffix '0'), single PPMI center (suffix 'center32') (pp. 5, 8).
- Features: FC = Fisher z-transformed correlation between ROI timecourse pairs, computed on 13 parcellations built independently of the data (AAL 116 regions, Craddock 130/260/500/950, Shen 100/200/300, OASIS 97, Power 264, Gordon 333, Talairach 695, Stanford 90). Group-ICA parcellations from the analyzed data were deliberately avoided to prevent overfitting the training dataset (pp. 5-6, 13).
- Reproducibility measure: R = correlation between the vectors of PD-vs-NC t-values of all ROI pairs in two datasets (or two splits), with permutation significance (1000 permutations) (pp. 6, 8).
- Heterogeneity test on replicate scans (NEUROCON, 2 scans/subject): (a) "split subjects", different subjects per split with all replicate scans together (heterogeneous); (b) "split replicates", replicates of the same subject placed in different splits (homogeneous, identical technical conditions). Ns = 2510 heterogeneous and Ns = 325 homogeneous random splits (pp. 7-9, 12).
- Classifiers: linear SVM and Gaussian Naive Bayes on FC features, N = 10, 50, 100, 500, 5000 ROI pairs selected by univariate t-tests on the training data (AAL has 6670 pairs in total); balanced average accuracy Aacc = (acc(NC)+acc(PD))/2, chance = 0.5. Cross-dataset: train on one dataset, test on the other two; plus 10,000 random train/test splits of each same dataset (pp. 10, 16).
- Exploratory: consensus NMF clustering of PD FC changes, k = 2..18 (p. 16).

## Data

- Three independent datasets (Table 1, p. 4):
  - NEUROCON (Bucharest): 27 PD (16 M), 16 NC (5 M), 2 replicate scans per subject (54 PD + 31 NC scans), Siemens Avanto 1.5T, TR 3.48 s, ~8 min (137 volumes). Mean H&Y 1.92, disease duration 4.6 y.
  - Tao Wu (Beijing): 20 PD (11 M), 20 NC (12 M), Siemens Magnetom 3T, TR 2 s, 8 min (239 volumes).
  - PPMI (US, multicenter): 91 PD (63 M), 18 NC (14 M) (134 PD + 19 NC scans), Siemens Tim Trio 3T, TR 2.4 s, 8.4 min (210 volumes). Patients diagnosed <= 2 years, not yet on PD medication, scanned eyes open; the other two cohorts are mostly treated (pp. 3-4).
- All data publicly available in de-identified form at FCP/INDI (p. 1). Code availability is not stated in the paper.

## Main results

- Global PD-related FC changes are non-reproducible in all three dataset pairs (Fig 2, p. 11; Table 3, p. 11). Example: NEUROCON vs Tao Wu R = -0.146, p = 0.949 (AAL, standard preprocessing). The result holds with GSR, bandpass filtering, low-motion subsets, and a single PPMI center.
- Heterogeneity, not technique: in random splits of NEUROCON, 88% of heterogeneous "split subjects" splits are non-reproducible at p > 0.01 and 42% at p > 0.05, while all homogeneous "split replicates" splits are reproducible at p < 10^-3; median R = 0.21 (heterogeneous) vs 0.71 (homogeneous) (p. 12).
- Control contrast (eyes open vs eyes closed in healthy subjects): reproducible even in heterogeneous splits (only 6% non-reproducible at p > 0.05), so the PD result is not a generic property of noisy FC analysis (p. 12, Table 4).
- Technical factors are exonerated: good reproducibility when doubling TR, changing linear/nonlinear registration, or applying GSR (Fig 4, p. 13); ICA-FIX and WM/CSF regression do not change the non-reproducibility; regressing out age, gender, disease duration does not improve it either (p. 13).
- Parcellation does not rescue it: no reproducibility for any of the 13 parcellations (90-950 regions), Table 5 (p. 13).
- Individual ROI pairs: only 2 of 13 parcellations yield marginally consistent significant pairs (Power264 p = 0.033, Talairach p = 0.032; Shen100 p = 0.055), involving visual-sensorimotor and visual-parietal pairs such as left postcentral/precentral gyrus with right cuneus (pp. 14-15, Tables 6-8).
- Cross-dataset classification: average accuracies 0.225-0.7 (mean 0.497, SD 0.073) across all train-test pairs, feature counts, and both classifiers; aggregated per training dataset 0.336-0.591 (mean 0.497, SD 0.052), i.e. chance level (pp. 15-16, Figs 6-7).
- Same-dataset random splits (10,000 per dataset): mean accuracies only 0.51-0.66, still weak, directly substantiating disease heterogeneity as the bottleneck (p. 16, Fig 8).

## Evaluation and leakage check

Evaluation: the paper's evaluation design is itself the contribution. External validation across two independent datasets for each training set, plus the replicate-scan split logic. Metrics: balanced average accuracy only; no AUC, sensitivity, or specificity (p. 10).

- Feature selection before the split? In the cross-dataset setting, yes: the N best-discriminating ROI pairs were selected by t-tests on the training dataset only (p. 10). For the 10,000 random splits of the same dataset, it is not stated whether feature selection was redone within each training half, so mild optimism cannot be excluded there.
- Same participant in train and test? Cross-dataset: no, different subjects. Random same-dataset splits: not stated whether splits were by subject or by scan; with 2 replicate scans per subject, scan-level splits could place replicates of one subject in both halves.
- Hyperparameters tuned on test data? Feature count N and preprocessing variants were all reported rather than tuned to maximize test performance; results are uniformly low, so no test-informed selection is apparent (pp. 10, 16).
- Independent test set? Yes, this is the strongest point: two external datasets per training set (p. 10).
- Confounds checked? Motion (low-motion subsets and comparisons, pp. 5, 11), GSR/bandpass/denoising variants (pp. 8, 13), age/gender/disease duration regression (p. 13). Medication status and eyes-open condition differ between PPMI and the other cohorts and are acknowledged but not fully controlled (p. 3).
- Metrics reported: balanced average accuracy only (p. 10); no AUC.
- Code and data available? Data yes, public at FCP/INDI (p. 1); code availability not stated.

## Limitations

- Only ROI-pair FC with correlation features is tested; no amplitude-of-fluctuation (ALFF) analysis (the authors' complementary reference found limited reproducibility there too) (p. 18).
- Classifiers are simple (linear SVM, GNB) on t-test-selected features; no nonlinear or regularized alternatives are tried, so "FC cannot classify PD" is really "these FC features cannot" (pp. 10, 16).
- PPMI differs from the other two cohorts in medication status, disease stage, and scan condition (eyes open), so part of the cross-dataset failure is a genuine domain shift rather than pure disease heterogeneity (p. 3). The split-subjects heterogeneity result within NEUROCON is the cleaner evidence.
- NEUROCON is 1.5T with coarse voxels (3.8 x 3.8 x 5 mm) and only 27 patients; the heterogeneity estimate rests mainly on this one dataset (Table 1, p. 4).
- No code availability statement; reproducibility of the reproducibility analysis itself depends on the S1 File.

## Connection to my thesis: what is relevant, and for what?

- Relevant information: a cautionary example that rs-fMRI FC biomarkers and PD-vs-control classifiers reported on single datasets do not generalize, with a quantitative heterogeneity estimate (88% of heterogeneous splits non-reproducible at p > 0.01, p. 12) and the multisite-schizophrenia parallel (multisite < 70% vs published single-site > 80%, p. 18).
- Used in chapter / section: Related Work (reproducibility and generalization of fMRI biomarkers); Discussion (why held-out external validation matters; heterogeneity as an obstacle for diagnostic FC markers).
- Used as: related work AND as an evaluation-standards argument. Unlike boutet2021dbs, this is the patient vs. healthy classification task my thesis relates to, and its negative result motivates cautious claims about single-cohort accuracy.

## My own thoughts and criticism

- The split-replicates design is the cleverest part: replicate scans give a technical-noise floor (all homogeneous splits reproducible, median R = 0.71) against which the heterogeneous splits (median R = 0.21) show heterogeneity rather than hardware as the culprit. This is a transferable evaluation idea for any dataset with repeated scans.
- Chance-level cross-dataset accuracy (mean 0.497) does not prove FC is useless for PD; it proves that group-average FC differences in these feature spaces are not a stable subject-level biomarker. The distinction matters for how I cite it: as evidence for heterogeneity and evaluation rigor, not as "fMRI cannot classify PD".
- The cross-dataset design with a uniform pipeline is the right control, but medication and condition differences in PPMI are a confound the authors wave away somewhat quickly (p. 3). The within-NEUROCON heterogeneity result is therefore the load-bearing finding.
- Possible residual leakage in the random-split classifiers (feature selection or scan-level splits, p. 10) would only make their already-low accuracies optimistic, which strengthens rather than weakens the heterogeneity conclusion.
- Notably, this paper anticipates the current reproducibility debate in neuroimaging ML by several years and is a good anchor citation against papers that report only within-dataset cross-validation.

## Relevant quotes

- "Unfortunately, PD-related functional connectivity changes turned out to be non-reproducible across datasets." (p. 1, Abstract)
- "we still observe non-reproducibility in a significant fraction of random subsamples of each individual dataset (these subsamples being technically homogeneous as they come from the same dataset), suggests that functional heterogeneity may be a dominating factor behind the lack of reproducibility of functional connectivity alterations in different resting state fMRI studies of Parkinson's disease." (p. 18)

## Reading questions

1. **How can I use this?** As related work on the limits of rs-fMRI FC biomarkers in PD, and as the citation justifying external validation and heterogeneity-aware evaluation in my own experiments. It also frames why a within-patient task (like DBS setting prediction in boutet2021dbs) sidesteps one source of variance that between-subject diagnosis cannot.
2. **Does it do what the authors claim?** Yes, the negative reproducibility result is well supported, especially by the replicate-scan split design and the eyes-open/eyes-closed control. The claim is appropriately scoped to ROI-pair FC features and simple classifiers.
3. **Do I understand the results?** Yes: three datasets, one pipeline, near-zero t-value correlations across datasets; heterogeneity confirmed inside a single dataset via replicate scans; classifiers at chance across datasets and only 0.51-0.66 within datasets; a handful of marginally reproducible visual-sensorimotor ROI pairs.
