"""Phase 1: download open-access PDFs for the sources in literature/dois.txt.

Uses the free Unpaywall API. A PDF is saved ONLY when the paper has an open
license (for example CC BY), because this repository is public. Papers that are
free to read but have no open license, and paywalled papers, are skipped: keep
their DOI, bib entry and notes only.

Run from the project root:
    python scripts/13_fetch_pdfs.py --email your.name@example.com
Output: literature/pdfs/<citekey>.pdf
"""
import argparse
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
DOIS = ROOT / "literature" / "dois.txt"
PDFS = ROOT / "literature" / "pdfs"


def read_dois(path: Path) -> list[tuple[str, str]]:
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, doi = (part.strip() for part in line.split(",", 1))
        pairs.append((key, doi))
    return pairs


def pick_open_pdf(data: dict) -> tuple[str | None, str | None]:
    """Return (pdf_url, license) for an openly licensed PDF, else (None, reason)."""
    if not data.get("is_oa"):
        return None, "not open access"
    locations = [data.get("best_oa_location") or {}] + (data.get("oa_locations") or [])
    saw_free_without_license = False
    for loc in locations:
        pdf_url = loc.get("url_for_pdf")
        if not pdf_url:
            continue
        if loc.get("license"):
            return pdf_url, loc["license"]
        saw_free_without_license = True
    if saw_free_without_license:
        return None, "free to read but no open license"
    return None, "open access, but no direct PDF link"


def download(url: str, target: Path) -> bool:
    r = requests.get(url, timeout=60, headers={"User-Agent": "thesis-literature-script"})
    r.raise_for_status()
    if not r.content.startswith(b"%PDF"):
        return False
    target.write_bytes(r.content)
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", required=True, help="your email (required by Unpaywall)")
    args = parser.parse_args()

    PDFS.mkdir(parents=True, exist_ok=True)
    skipped = []
    for key, doi in read_dois(DOIS):
        target = PDFS / f"{key}.pdf"
        if target.exists():
            print(f"  have {key}")
            continue
        try:
            r = requests.get(f"https://api.unpaywall.org/v2/{doi}",
                             params={"email": args.email}, timeout=30)
            r.raise_for_status()
            url, info = pick_open_pdf(r.json())
            if url and download(url, target):
                print(f"  OK   {key}  (license: {info})")
            else:
                reason = info if not url else "download did not return a PDF"
                skipped.append((key, doi, reason))
                print(f"  skip {key}: {reason}")
        except Exception as exc:  # noqa: BLE001
            skipped.append((key, doi, str(exc)))
            print(f"  FAIL {key}: {exc}")
        time.sleep(0.5)

    if skipped:
        print("\nNo PDF stored for these (keep DOI + bib entry + notes; open the paper through the DOI link or your university access):")
        for key, doi, reason in skipped:
            print(f"  {key}  https://doi.org/{doi}  [{reason}]")


if __name__ == "__main__":
    main()
