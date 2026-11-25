# szewczykkrolikowski2014basal

**Reference:** Szewczyk-Krolikowski, K., Menke, R. A. L., Rolinski, M., Duff, E., Salimi-Khorshidi, G., Filippini, N., Zamboni, G., Hu, M. T. M., & Mackay, C. E. (2014). Functional connectivity in the basal ganglia network differentiates PD patients from controls. _Neurology_, 83(3), 208-214.
**DOI:** https://doi.org/10.1212/WNL.0000000000000592
**Type:** case-control rs-fMRI study with threshold-based classification (ROC cutoff on one averaged feature, not a trained ML model) | **License:** (c) AAN, no open license stated | **Read on:** 2026-11-23
**PDF in repo:** yes (`literature/pdfs/szewczykkrolikowski2014basal.pdf`)
**Page refs below are PDF pages** (journal page = PDF page + 207). Published online 11 Jun 2014.

## Main idea

ICA-derived basal ganglia network (BGN) connectivity is reduced in early, cognitively normal PD and separates PD (off medication) from matched controls with 100% sensitivity / 89.5% specificity in the discovery cohort. The derived threshold, applied to a separate validation cohort of 13 PD patients, flags 85% of them. Dopaminergic medication normalizes the deficit, and 4 of 5 drug-naive validation patients also show it, which the authors take to speak against a simple medication-withdrawal effect (pp. 1, 4-5).

## Method

- FSL MELODIC v3.03: motion correction + fieldmap unwarping, a previously described ICA-based denoising approach for motion (their ref 18), MNI registration (p. 3)
- Template: group ICA on 80 elderly HC (19 OPDC + 61 from 3 prior studies, same scanner/protocol); BGN = one of 50 components; dual regression to individual maps (p. 3). The 19 OPDC controls in the template are the same controls used in the discovery comparison (pp. 2-3)
- Group comparison: PD-off vs HC unpaired t test, Randomise with TFCE, p < 0.05 FWE; medication effect via paired t test within that significant mask, FDR-corrected (p. 3)
- Classification: participant-averaged parameter estimates within the significant clusters, with an ROC-derived cutoff (no ML model beyond a one-feature threshold) (p. 3)

## Data

- Discovery: 19 early PD (sex ratio 10:9, age 58.9 +/- 10.8, UPDRS-III 23.9 +/- 9.6, H&Y 1.8, duration 30.7 months, LEDD 382 mg) vs 19 age/sex-matched HC (sex ratio 8:11, age 60.6 +/- 7.7) (Table 1, p. 2). Table 1 does not label which side of the sex ratio is male.
- Validation: 13 PD (sex ratio 5:8, age 66.8 +/- 11.4, UPDRS-III 29.7 +/- 14.7), 5 drug-naive + 8 medicated, all scanned off medication (pp. 1-2). The validation cohort contains patients only; no controls were scanned for validation.
- Single site (Oxford OPDC), one 3T Siemens Trio; TR 2 s, 180 volumes, 6 min, 3 x 3 x 3.5 mm (p. 3)
- Medication states: discovery scanned off (12-17 h withdrawal) and on (60-90 min after the dose); validation off only (pp. 2-3)
- Labels: clinical PD (UK Brain Bank criteria; patients with physician-rated diagnostic certainty < 90%, more than mild tremor in the on state, or dyskinesia/dystonia were excluded) vs HC (p. 2)
- Data and code availability: not reported

## Results

- Discovery (in-sample): PD-off < HC in 16,273 voxels across 9 clusters (putamen/caudate bilaterally, midbrain, superior temporal gyrus, DLPFC, medial PFC, precuneus), p < 0.05 FWE (pp. 3-4)
- Medication: PD-on > PD-off within the mask (FDR); PD-on vs HC: no significant difference (p. 4)
- ROC [in-sample, discovery]: AUC 0.972 (95% CI 0.921-1.0); cutoff 3.88 gives 100% sensitivity, 89.5% specificity (p. 4). Mean PE: PD-off 1.04 (0.42-1.65) vs HC 7.59 (5.61-9.56) (p. 4)
- Validation [held-out, n = 13 patients]: the threshold flagged 11/13 = 85% as PD; mean PE 1.72 (0.52-2.93); the 2 misses were 1 drug-naive and 1 medicated patient; 4/5 drug-naive were below threshold (p. 4)
- No correlation of BGN connectivity with UPDRS-III, H&Y, disease duration or age (p. 4)

## Evaluation and leakage check

- Feature selection before the split? There is no split-based feature selection (the "model" is one averaged feature), but the averaging mask comes from the discovery PD-off vs HC contrast and the ROC is then computed on the same discovery subjects (double-dipping); the mask and threshold are fixed before validation (pp. 3-4)
- Same participant in train and test? No: the validation cohort is disjoint (p. 2)
- Tuning on test data? No: the threshold is derived on the discovery cohort only, then applied unchanged to the validation cohort (pp. 3-4)
- Independent test set? Yes, but small (n = 13), PD only, and from the same center/scanner. Because it has no controls, the "85% accuracy" is a sensitivity (11 of 13 patients flagged); specificity was never tested on held-out controls. No multi-site external validation.
- Confounds: motion explicitly addressed (ICA denoising; no between-group motion difference, p. 5); age/sex matched in discovery, but the validation cohort is older (66.8 vs 60.6 in HC, p = 0.11) and has lower MMSE vs HC (p = 0.02, Table 1, p. 2); medication state is part of the design (classification shown only off medication)
- Metrics beyond accuracy: sensitivity, specificity and AUC with CI are reported (pp. 1, 4); Class III evidence rating (p. 1)
- Code and data: not reported

## Limitations

- Admitted: small discovery sample (mitigated with a validation cohort); tremor patients excluded, which limits generalizability (p. 6). The authors also discuss that the lack of correlation with severity may mean a trait marker or a floor effect (p. 5).
- Not admitted: single site/scanner; the 100%/89.5% figures are in-sample (mask and cutoff were derived from these same participants), so the held-out figure is the 11/13, which is sensitivity only; classification is shown only for the off-medication state (PD-on is indistinguishable from HC), which limits use in routinely medicated patients; the healthy-elderly template includes the same 19 controls used in the discovery contrast

## Connection to my thesis

- Relevant: early rs-fMRI PD-vs-HC separation with a held-out validation cohort and a drug-state manipulation; the medication-normalization result is direct evidence that FC features are state-dependent
- Chapter: Related Work (early rs-fMRI PD detection); Discussion (state vs trait markers; in-sample vs held-out reporting)
- Role: evidence + method idea (a healthy-cohort ICA template reusable across studies; discovery-validation design). NOT a baseline: one-feature threshold, not a multivariate model

## My own thoughts and criticism

- The 100%/89.5% figures are in-sample ROC numbers and should never be quoted alone. The only held-out number is 11/13 patients flagged (85%, a sensitivity), whose exact 95% CI is wide (roughly 55-98%).
- The medication result cuts both ways: it strengthens the biological claim (dopamine-dependent, functional rather than structural) but means the classifier only works off medication, a major practical constraint the abstract does not flag.
- The healthy-elderly ICA template is a good idea, since networks defined without patient data cannot encode the disease contrast, and it is reusable. It is not completely clean here because the 19 matched controls are part of the 80-subject template.
- No severity correlation plus on-state normalization suggests a trait-like floor effect; citing this as a staging/progression marker would overreach.
- The validation cohort differs from HC in MMSE (p = 0.02, Table 1, p. 2). The authors call it marginal, but a cognitive mismatch is a possible confound in a 13-patient test.

## Quotes

- The authors state that "a major limitation of our study is small sample size of the discovery cohort" (p. 6).
