# boutet2021dbs: fMRI + machine learning to predict optimal deep brain stimulation settings

- **Reference:** Boutet, Madhavan et al., 2021, Nature Communications 12:3043 (full entry in `references.bib`)
- **DOI / link:** https://doi.org/10.1038/s41467-021-23311-9
- **Type:** research article (open access)
- **Read on:** (fill in)  **PDF in repo:** yes, if you add `literature/pdfs/boutet2021dbs.pdf` (open access)

## Main idea
fMRI recorded while deep brain stimulation (DBS) is switched on and off shows brain response patterns that differ between clinically optimal and non-optimal stimulation settings. A classifier learns to tell them apart.

## Method or algorithm
Preprocessing with slice-time and motion correction, normalization to a standard brain space and smoothing (SPM12). Statistical maps per setting, mean values from 16 regions of interest (32 features), linear discriminant analysis (LDA).

## Data used
67 Parkinson's patients with implanted DBS, 3 T fMRI, 203 sessions. Private data (not public).

## Main results
88% cross-validated accuracy on 39 patients; tested on two unseen groups of 9 patients each, reaching 76% on stimulation-naive patients.

## Evaluation
5-fold cross-validation plus two independent test sets. Test sets are very small (n = 9).

## Limitations
Small sample, private data, one hospital and one DBS hardware model. The authors state that models with many features overfit on small samples and that they restricted the number of regions for this reason.

## Connection to my thesis: what is relevant, and for what?
- Relevant information: a published example of fMRI + ML in Parkinson's with held-out test sets, and an explicit statement about overfitting with few participants.
- Used in chapter / section: Related Work; Discussion (small-sample limitation).
- Used as: related work (NOT a baseline, because the task is DBS setting prediction and not patient vs. healthy classification).

## My own thoughts and criticism
(write your own)
