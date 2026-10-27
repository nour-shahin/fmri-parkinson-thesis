# Thesis: ML on resting-state fMRI for Parkinson's disease

Bachelor's thesis project. Pipeline: dataset -> QC -> preprocessing -> connectivity features -> ML -> evaluation -> interpretation.

## Setup
    python -m venv .venv
    source .venv/bin/activate          # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python scripts/00_check_env.py

## Literature
See `literature/README.md` for sources, notes and the bibliography (`literature/references.bib`).

## Layout
    data/         raw + processed data (git-ignored)
    literature/   papers.csv (reading table), search results, notes
    scripts/      numbered scripts, one per step, run in order
    results/      tables and figures
