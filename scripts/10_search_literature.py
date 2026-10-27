"""Phase 1: search PubMed and save the results to a CSV you can screen.

Uses the free NCBI E-utilities API (no key needed for light use).
Run from the project root:
    python scripts/10_search_literature.py
    python scripts/10_search_literature.py --query "your own query" --max 50
Output: literature/search_results.csv
"""
import argparse
import csv
import time
from pathlib import Path

import requests

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

DEFAULT_QUERIES = [
    '(Parkinson Disease[MeSH]) AND (resting state fMRI) AND (machine learning OR classification)',
    '(Parkinson*) AND (functional connectivity) AND (support vector machine OR deep learning)',
    '(Parkinson*) AND (resting-state) AND (early stage OR drug-naive) AND (classification)',
]


def search_ids(query: str, retmax: int) -> list[str]:
    r = requests.get(
        f"{BASE}/esearch.fcgi",
        params={"db": "pubmed", "term": query, "retmax": retmax,
                "sort": "relevance", "retmode": "json"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["esearchresult"]["idlist"]


def fetch_summaries(ids: list[str]) -> list[dict]:
    rows = []
    for i in range(0, len(ids), 100):
        chunk = ids[i:i + 100]
        r = requests.get(
            f"{BASE}/esummary.fcgi",
            params={"db": "pubmed", "id": ",".join(chunk), "retmode": "json"},
            timeout=30,
        )
        r.raise_for_status()
        result = r.json()["result"]
        for pmid in chunk:
            item = result.get(pmid)
            if not item:
                continue
            doi = next((a["value"] for a in item.get("articleids", [])
                        if a.get("idtype") == "doi"), "")
            authors = ", ".join(a["name"] for a in item.get("authors", [])[:3])
            if len(item.get("authors", [])) > 3:
                authors += " et al."
            rows.append({
                "pmid": pmid,
                "year": item.get("pubdate", "")[:4],
                "authors": authors,
                "title": item.get("title", ""),
                "journal": item.get("fulljournalname", ""),
                "doi": doi,
                "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "keep": "",   # fill in by hand: yes / no / maybe
            })
        time.sleep(0.4)  # be polite to the API
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="custom PubMed query (otherwise defaults are used)")
    parser.add_argument("--max", type=int, default=40, help="results per query")
    args = parser.parse_args()

    queries = [args.query] if args.query else DEFAULT_QUERIES
    seen, all_rows = set(), []
    for q in queries:
        print(f"Searching: {q}")
        ids = [i for i in search_ids(q, args.max) if i not in seen]
        seen.update(ids)
        all_rows.extend(fetch_summaries(ids))
        time.sleep(0.4)

    if not all_rows:
        print("No results found.")
        return
    all_rows.sort(key=lambda row: row["year"], reverse=True)
    out = Path(__file__).resolve().parents[1] / "literature" / "search_results.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"Saved {len(all_rows)} unique papers to {out}")


if __name__ == "__main__":
    main()
