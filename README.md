# Thesis: ML on resting-state fMRI for Parkinson's disease

Bachelor's thesis project. Pipeline: dataset -> QC -> preprocessing -> connectivity features -> ML -> evaluation -> interpretation.

## Setup
    python -m venv .venv
    source .venv/bin/activate          # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python scripts/00_check_env.py

## Literature workflow
    python scripts/10_search_literature.py              # search PubMed
    python scripts/11_make_bib.py                       # build literature/references.bib from dois.txt
    python scripts/13_fetch_pdfs.py --email you@x.com   # open-licensed PDFs only
    python scripts/12_check_literature.py               # which sources still lack notes

## Status
Phase 1 (literature): in progress. Sources, notes and bibliography are in `literature/`.

## AI assistance
An AI assistant (Claude, Anthropic) was used to plan the project structure and to help write the helper scripts. All sources are read, checked and annotated by the author.

## Literature
See `literature/README.md` for sources, notes and the bibliography (`literature/references.bib`).

## Layout
    data/         raw + processed data (git-ignored)
    literature/   papers.csv (reading table), search results, notes
    scripts/      numbered scripts, one per step, run in order
    results/      tables and figures
