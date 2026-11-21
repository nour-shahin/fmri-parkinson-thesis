# germani2025replication

**Reference:** Germani, E., Bhagwat, N., Dugre, M., Gau, R., Montillo, A. A., Nguyen, K. P., Sokolowski, A., Sharp, M., Poline, J.-B., & Glatard, T. (2025). Predicting Parkinson's disease trajectory using clinical and functional MRI features: A reproduction and replication study. _PLOS ONE_, 20(2), e0317566.
**DOI:** https://doi.org/10.1371/journal.pone.0317566
**Type:** reproducibility/replication study | **License:** CC BY 4.0 (PLOS ONE, 21 Feb 2025) | **Read on:** 2026-11-18 | **Checked against PDF:** 2026-11-21
**PDF in repo:** yes (`literature/pdfs/germani2025replication.pdf`)

## Main idea

Reproduces and replicates Nguyen et al. (2021), which predicted MDS-UPDRS total scores (current and up to 4 years ahead) from regional rs-fMRI ReHo/fALFF plus clinical and demographic features on PPMI. Phase 1 replicates from paper + code only; Phase 2 reproduces after author contact (own preprocessing, and a partial reproduction on the authors' derived maps). Success criteria: R2 > 0 and above permutation chance, and |R2 difference| < 0.15 from the original (pp. 1, 3-4, 14).

## Method

- Cohort: PPMI PD with rs-fMRI + ON-medication MDS-UPDRS III at the same visit, database queried 21 Aug 2023; replication cohort 102/67/61/46 subjects at Baseline/Year 1/2/4; closest-to-original 82/51/41/30 (pp. 5-8)
- Preprocessing: Nipype + FSL 6.0.6.1 + AFNI 23.3.01 + ANTs 2.3.4 in Docker (MCFLIRT, 3dAutomask, ANTs to MNI152NLin6Asym 2 mm); denoising with 6 motion parameters + ICA-AROMA + WM/CSF (AFNI segmentation, "arbitrarily chosen"); variations: FSL FAST, template masks, fMRIprep (pp. 8-10)
- Features: fALFF/ReHo (C-PAC, authors' code), z-scored; regional means over a custom 135-ROI Schaefer + cerebellar + striatal atlas, BASC197, BASC444 (pp. 10-11)
- Models: ElasticNet, linear SVM, Random Forest, Gradient Boosting (scikit-learn 1.3.0); nested CV with an inner 10-fold (RMSE) and an outer leave-one-out (pp. 12-14)
- Null: 1,000 label permutations, but each permutation used a 5-fold inner and 5-fold outer loop rather than the 10-fold/LOO scheme of the real models (p. 14), so the null and the real estimates are not computed identically

## Data

- PD only (no HC arm); labels = MDS-UPDRS total scores at 4 time points
- Single database (PPMI); public on application. Code public (GitHub notebook, Docker, Zenodo); data not reshareable under the PPMI DUA (pp. 2, 30)
- Motion: 80 of 102 participants had at least one frame with FD > 0.5 mm; mean FD 0.258 mm; all participants and volumes were kept, following the original (p. 18)

## Results

- All results are cross-validated (nested LOO); no held-out external test (the original's PDBP validation was not re-run, p. 26)
- Baseline: original ReHo R2 = 0.304, fALFF 0.242; best default workflow ReHo 0.124, fALFF 0.205 (p. 19). With the paper's nested scheme (E.1): fALFF 0.049, ReHo -0.164; with the original's published best model (E.2): fALFF -0.039, ReHo -0.102 (Table 4, p. 23)
- Year 1: fALFF 0.717 vs. orig 0.558; ReHo 0.535 vs. 0.453. Year 2: fALFF 0.529 vs. 0.463, ReHo 0.344 vs. 0.471. Year 4: fALFF 0.411 vs. 0.152, ReHo 0.312 vs. 0.255. Chance level about -0.04 to -0.14 (Table 3, p. 19)
- Partial reproduction on the authors' derived maps: close to the original except Year 4 fALFF (pp. 20, 25)
- Secondary high/low-severity classification: AUC 0.805 (fALFF), 0.767 (ReHo) at Year 1 (default workflow, p. 22)
- D.2/D.4 (no Baseline MDS-UPDRS; imaging only): R2 drops by more than 0.2 at Year 1 and Year 2 (p. 20)

## Evaluation and leakage check

- Feature selection before the split: no; models and features fixed per workflow, hyperparameters in the inner loop (pp. 12-13)
- Same participant in train and test: no; LOO over participants
- Tuning on test data: no; but the default reporting picks the best model x parcellation on the same LOO results it reports; the authors quantify the inflation themselves via E.1/E.2 (pp. 22-23)
- Independent test set: no external one; the "replication" is analytic, not external validation
- Confounds: the unversioned PPMI database (2 original images unavailable; visit mismatches) affects even the closest-to-original cohort (pp. 7-8, 27); high motion kept (p. 18); the Baseline MDS-UPDRS input makes Year 1/2 prediction largely clinical autocorrelation (p. 20)
- Metrics beyond accuracy: R2, RMSE, AUC, PPV, NPV, sensitivity, specificity; permutation nulls; a 0.15 difference threshold tied to the original's lowest R2 (p. 14)

## Limitations

- Admitted: cohort retrieval failed even with author lists (102 vs. 82); pipeline guesses; single dataset; small Year-4 n; PPMI limitations inherited (Caucasian bias, medication effects) (pp. 26-29)
- Not stated plainly: that under the original's own evaluation scheme (E.1/E.2) Baseline prediction is at or below chance, even though the abstract says the replication is "consistent with its findings"; the E.1/E.2 numbers are in Table 4 and the text but not drawn out as a conclusion

## Connection to my thesis

- Relevant: quantified best-model-reporting inflation (0.205 -> 0.049 at Baseline for fALFF); feature importance not replicating while R2 does (p. 24); imaging-only vs. baseline-score ablations (D.2/D.4, drops > 0.2, p. 20)
- Chapter: Related Work (reproducibility in rs-fMRI ML); Discussion (evaluation practice, what "progression prediction" means)
- Role: evidence and method idea (honest nested CV + permutation nulls as a template)

## My own thoughts and criticism

- The abstract's "consistent with its findings" is technically true, but the sharpest finding is the E.1 contrast: under honest nested selection, Baseline signal vanishes
- Year 1/2 R2 of 0.4-0.7 mostly reflects predicting next year's score from this year's score; cite the D.2/D.4 ablations, not the headline R2
- Clean methodological opposite of patil2024scannerbias in the same data domain: subject-level LOO, permutation nulls, explicit leakage discussion. Caveat: the permutation null uses a different CV scheme from the real models
- No demographic-only control (age, sex, education) is run, so the imaging contribution at Baseline is not isolated
- Feature-importance non-replication supports my argument against over-reading model weights in this literature
- Task differs from diagnosis (severity regression in PD only); use it for evaluation practice, not as a diagnostic baseline

## Quotes

- "similar R2 is attained, though through different sets of features" (p. 24)
- "reproducing the experiments made in existing papers remains extremely challenging" (p. 30)
