"""Phase 1: build literature/references.bib from DOIs.

Reads literature/dois.txt (lines: citekey,DOI), downloads the complete BibTeX
entry for every DOI from doi.org (Crossref metadata), replaces the citation key
with yours, and writes literature/references.bib.

Run from the project root:  python scripts/11_make_bib.py
ALWAYS open the result and check each entry (authors, year, journal, pages).
"""
import re
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DOIS = ROOT / "literature" / "dois.txt"
OUT = ROOT / "literature" / "references.bib"


def read_dois(path: Path) -> list[tuple[str, str]]:
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, doi = (part.strip() for part in line.split(",", 1))
        pairs.append((key, doi))
    return pairs


def set_key(bibtex: str, key: str) -> str:
    """Replace the citation key in the first line, e.g. '@article{Old_2017,'."""
    return re.sub(r"^(@\w+\s*\{)[^,]+,", rf"\g<1>{key},", bibtex.strip(), count=1)


def fetch_bibtex(doi: str) -> str:
    r = requests.get(
        f"https://doi.org/{doi}",
        headers={"Accept": "application/x-bibtex; charset=utf-8"},
        timeout=30,
        allow_redirects=True,
    )
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text


def main() -> None:
    entries, failed = [], []
    for key, doi in read_dois(DOIS):
        try:
            entries.append(set_key(fetch_bibtex(doi), key))
            print(f"  OK   {key}")
        except Exception as exc:  # noqa: BLE001
            failed.append(key)
            print(f"  FAIL {key} ({doi}): {exc}")
        time.sleep(0.5)

    OUT.write_text("\n\n".join(entries) + "\n", encoding="utf-8")
    print(f"\nWrote {len(entries)} entries to {OUT}")
    if failed:
        print("Failed (add these by hand or fix the DOI):", ", ".join(failed))


if __name__ == "__main__":
    main()
