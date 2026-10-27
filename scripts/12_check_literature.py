"""Phase 1: check that every source in references.bib is documented.

For each citation key it reports whether a notes file exists
(literature/notes/<key>.md) and whether a PDF exists (literature/pdfs/<key>.pdf).
Run from the project root:  python scripts/12_check_literature.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "literature" / "references.bib"
NOTES = ROOT / "literature" / "notes"
PDFS = ROOT / "literature" / "pdfs"


def bib_keys(text: str) -> list[str]:
    return re.findall(r"^@\w+\s*\{\s*([^,\s]+)\s*,", text, flags=re.MULTILINE)


def main() -> None:
    if not BIB.exists():
        print("references.bib not found. Run scripts/11_make_bib.py first.")
        return
    keys = bib_keys(BIB.read_text(encoding="utf-8"))
    print(f"{'citekey':<32} {'notes':<7} {'pdf':<5}")
    missing_notes = 0
    for key in keys:
        has_notes = (NOTES / f"{key}.md").exists()
        has_pdf = (PDFS / f"{key}.pdf").exists()
        missing_notes += not has_notes
        print(f"{key:<32} {'yes' if has_notes else 'NO':<7} {'yes' if has_pdf else '-':<5}")
    print(f"\n{len(keys)} sources, {missing_notes} without notes.")
    print("Bachelor target: roughly 15-30 relevant, recent sources.")
    print("A missing PDF is fine for paywalled papers: keep DOI + notes only.")


if __name__ == "__main__":
    main()
