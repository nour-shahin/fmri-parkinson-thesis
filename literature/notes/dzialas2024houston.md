# dzialas2024houston

**Reference:** Dzialas, V., Doering, E., Eich, H., Strafella, A. P., Vaillancourt, D. E., Simonyan, K., van Eimeren, T., & International Parkinson Movement Disorders Society-Neuroimaging Study Group. (2024). Houston, We Have AI Problem! Quality Issues with Neuroimaging-Based Artificial Intelligence in Parkinson's Disease: A Systematic Review. _Movement Disorders_, 39(12), 2130-2143.
**DOI:** https://doi.org/10.1002/mds.30002
**Type:** review (systematic, quality/bias assessment) | **License:** CC BY-NC-ND | **Read on:** 2026-11-23
**PDF in repo:** yes (`literature/pdfs/dzialas2024houston.pdf`)
**Page refs below are PDF pages** (journal page = PDF page + 2129). Published online 5 Sep 2024.

## Main idea

First systematic quality assessment of neuroimaging-based AI studies in PD: of 244 included studies (from 810 PubMed hits), only 20% passed all five minimal quality criteria (MQC: train/test split, no data leakage, minimal model complexity, generalizability reporting, biological plausibility). Studies with data leakage reported higher accuracies (87.5% vs. 84.6%), but this was P = 0.035 one-tailed and not significant after multiple-comparison correction (p. 8), even though the abstract calls it a "significant inflation". External test sets were rare (8% of studies in the abstract, 7% of aims in the results) and external accuracy was about 5% lower. The field's effort is misaligned with clinical need: 54% of studies do PD vs. HC, a task of questionable clinical relevance (pp. 1, 5, 8-9).

## Method (of the review)

- PubMed search on 1 January 2024, broad term (PD + AI + neuroimaging modalities), 810 articles; two independent raters with consensus; not registered (pp. 2-3)
- Exclusions: not original research, not English, retracted, non-human, PD not stand-alone (no "parkinsonian syndromes" grouping), neuroimaging not the primary input, no clinically relevant aim (pp. 2-3)
- Categorization: diagnosis (6 subcategories: PD vs HC, PD vs APS, subtypes, staging/severity, cognitive impairment, FOG), prognosis (4), intervention (2, incl. DBS) (p. 4)
- Five MQC rated passed/failed/NA/unclear: (1) train/test split or CV; (2) no data leakage (incl. feature selection on the full dataset and same subject in train and test); (3) minimal model complexity (features < individuals; not applicable to deep learning); (4) generalizability (test or average CV performance reported without selective reporting); (5) biological plausibility (feature contribution explained) (p. 4)
- Statistics: weighted t tests for model/modality accuracy differences (PD vs HC subcategory, n = 113 studies reporting accuracy); 1-tailed t test for leakage vs no-leakage accuracy (pp. 4-5, 8)
- Bias assessment beyond MQC: imbalance handling, external test sets, reproducibility details (scanner, tracer, field strength, eye status) (p. 5)

## Main conclusions

- 244 studies; 86% diagnostic, 8% prognostic, 9% interventional; PD vs HC is the largest subcategory (54%, n = 131), PD vs APS second (25%, n = 60) (p. 5)
- Models: SVM 46%, CNN 17%, ensemble 14%; 88% of subcategory entries used unimodal input (p. 6)
- PD vs HC studies reached accuracies of up to 100%; sample-size-weighted means: ensemble 94.1%, [123I]-FP-CIT SPECT 97.4% (pp. 6-8)
- The SPECT result is circular: 15 of 17 SPECT studies used PPMI, where dopaminergic (ab)normality is an inclusion criterion for both groups (p. 8)
- Quality: only 20% passed all MQC; MQC 2 (no leakage) passed by 49%, MQC 5 (plausibility) 57%, MQC 3 (complexity) 57%, MQC 1 95%, MQC 4 92% (p. 8)
- Leakage: 87.5 +/- 10.9% (leakage) vs. 84.6 +/- 12.1% (no leakage), P = 0.035 one-tailed, not significant after correction (alpha = 0.017) (p. 8)
- External test sets: only 7% of aims (n = 22); external performance lower by a mean of 5% (t = 3.1, P < 0.01) (p. 8)
- Imbalance not addressed: 16% of classification aims (n = 49) in the results (p. 8); the abstract says 19% of studies (p. 1)
- Reproducibility gaps: 46% of PET/SPECT and 20% of structural MRI studies omitted scanner type (91% and 87% of those used PPMI); 44% of fMRI studies did not report eye status (pp. 8-9)
- Quality did not improve over the years despite rising publication counts, and stayed low across journal impact-factor bins (pp. 8-9)
- Key recommendations: clinician-engineer collaboration, imbalance-aware metrics, external test sets or permutation testing, nested CV or a plain train-test split for n < 1000, multiple splits, graphical pipeline diagrams in publications (pp. 10-11)

## What they say about quality (review-specific checklist)

- The five MQC are the field's minimal bar, and 80% of the literature fails them; leakage is the most common failure, typically via feature selection before the split or same-subject samples in both train and test (p. 8)
- They cite earlier work (their ref 18) that same-subject train/test contamination can overestimate PD-vs-HC accuracy by about 50% (p. 10); "cross-literature data leakage" through shared databases such as PPMI is flagged as a further risk (p. 10)
- External test sets lower accuracy by about 5% on average; PPMI circularity (diagnosis embedded in the imaging inclusion criteria) is documented for SPECT (p. 8)
- Review limitations (admitted): the broad search may miss new applications; non-imaging biomarkers not covered; MQC rating requires expertise; time lag between analysis and publication; the MQC are a first step, not the whole picture (p. 11)
- Not admitted: PubMed is the only database searched (unlike wang2025review's dual search); no formal risk-of-bias tool (their MQC is custom, not QUADAS/PROBAST); no inter-rater reliability (kappa) is reported for the MQC ratings

## Limitations

- Admitted: see above (p. 11)
- Not admitted: accuracy as the common comparison metric (their own choice) mirrors the field's accuracy-centrism; the leakage-accuracy comparison lost significance after correction, yet the abstract states leakage "was associated with a significant inflation of accuracies" (pp. 1, 8), a stronger claim than the corrected statistic supports

## Connection to my thesis

- Relevant: the quantitative evidence base for my evaluation-rigor argument (80% fail minimal standards; leakage is associated with higher accuracy; external tests drop it; PPMI circularity), and a citable MQC rubric for designing and reporting my own experiments
- Chapter: Discussion (the central citation that the rigor-accuracy pattern in my other notes is field-wide, not anecdotal); Methods (MQC as a reporting checklist)
- Role: evidence (bias/quality assessment) + tool (their MQC and recommendations as my reporting standard). Sources to snowball: ref 18 (same-subject leakage, about 50% inflation), refs 87-88 (permutation testing for overfitting)

## My own thoughts and criticism

- This paper is the field-level version of my case studies: badea2017 (reproducibility), donisi2025 (SMOTE + internal CV), guo2022 (honest ~72%), solanalavalle2024 (97.6% with confound), szewczykkrolikowski2014 (in-sample 100%), boutet2021 (CV-framing) each illustrate a specific MQC failure this review quantifies
- The leakage-accuracy gap (87.5 vs 84.6) is smaller than the narrative implies and nonsignificant after correction (p. 8); the roughly 50% inflation figure comes from an earlier study (their ref 18), not from this review's own data
- The clinical-relevance argument is the sharpest point: PD vs HC on recruited cohorts, and HC who "hardly represent a population likely to consult a neurologist" (p. 9); differential diagnosis, prognosis and treatment prediction are the clinically needed tasks and are rare (pp. 9-10)
- The PPMI circularity finding applies to guo2022lstm and solanalavalle2024causalforest in my set (both PPMI-based), though neither uses the SPECT inclusion criterion, so the circularity is weaker there than in the SPECT studies
- Practical takeaway for my thesis: adopt their MQC explicitly and report a pipeline diagram; passing all five would already place my work above 80% of the field

## Quotes

- The authors conclude that study quality is "alarmingly low, especially at the implementation level" (p. 11).
