#!/usr/bin/env python3
"""
FL-04 automation: incoming-notes digest builder.

Reads every .md / .txt file in an "incoming" folder, classifies each note
with simple keyword rules, extracts explicit action lines, and writes a
dated Markdown digest summarising counts and actions.

This is a scripted workflow (Python + cron/Task Scheduler friendly) — the
free path — not a paid no-code automation tool.

Usage:
    python digest.py --incoming incoming --output runs/run_01_digest.md
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

# --------------------------------------------------------------------------
# CONFIGURATION — every prompt/rule used by this workflow lives here.
# Classification: first matching category wins, in the order listed.
# Matching is a case-insensitive substring check against the whole note.
# --------------------------------------------------------------------------
CLASSIFICATION_RULES: dict[str, list[str]] = {
    "kaggle": [
        "kaggle", "leaderboard", "submission", "rank ", "competition",
        "notebook", "public lb", "private lb",
    ],
    "report": [
        "report", "pbl", "jury", "annexure", "paper", "documentation",
        "dashboard", "streamlit",
    ],
    "content": [
        "linkedin", "post draft", "social", "content idea", "caption",
    ],
}
DEFAULT_CATEGORY = "other"

# Action lines: explicit markers only, so extraction is auditable.
ACTION_PATTERN = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\[ \]\s*)?(TODO|ACTION|NEXT STEP)\s*[:\-]\s*(.+)$",
    re.IGNORECASE,
)
CHECKBOX_PATTERN = re.compile(r"^\s*-\s*\[ \]\s*(.+)$")


def classify(text: str) -> str:
    low = text.lower()
    for category, keywords in CLASSIFICATION_RULES.items():
        if any(kw in low for kw in keywords):
            return category
    return DEFAULT_CATEGORY


def extract_actions(text: str) -> list[str]:
    actions: list[str] = []
    for line in text.splitlines():
        m = ACTION_PATTERN.match(line)
        if m:
            actions.append(m.group(2).strip())
            continue
        m = CHECKBOX_PATTERN.match(line)
        if m:
            actions.append(m.group(1).strip())
    return actions


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
        if line:
            return line[:80]
    return fallback


def build_digest(incoming: Path, now: datetime) -> str:
    files = sorted(p for p in incoming.iterdir() if p.suffix.lower() in {".md", ".txt"})
    rows = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        rows.append(
            {
                "file": path.name,
                "title": first_heading(text, path.stem),
                "category": classify(text),
                "actions": extract_actions(text),
                "words": len(text.split()),
            }
        )

    counts = Counter(r["category"] for r in rows)
    total_actions = sum(len(r["actions"]) for r in rows)

    out: list[str] = []
    out.append(f"# Daily Digest — {now.strftime('%Y-%m-%d %H:%M')}")
    out.append("")
    out.append(f"Source folder: `{incoming}`  ")
    out.append(f"Notes processed: **{len(rows)}** · Action lines found: **{total_actions}**")
    out.append("")
    out.append("## Counts by category")
    out.append("")
    out.append("| Category | Notes |")
    out.append("|---|---:|")
    for cat in ["kaggle", "report", "content", "other"]:
        out.append(f"| {cat} | {counts.get(cat, 0)} |")
    out.append("")
    out.append("## All actions")
    out.append("")
    if total_actions:
        for r in rows:
            for a in r["actions"]:
                out.append(f"- [{r['category']}] ({r['file']}) {a}")
    else:
        out.append("- None found.")
    out.append("")
    out.append("## Notes")
    out.append("")
    for r in rows:
        out.append(f"### {r['title']}")
        out.append(f"- File: `{r['file']}` · Category: **{r['category']}** · Words: {r['words']}")
        if r["actions"]:
            for a in r["actions"]:
                out.append(f"  - Action: {a}")
        else:
            out.append("  - Action: —")
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Build a digest from incoming notes.")
    ap.add_argument("--incoming", default="incoming", help="Folder of .md/.txt notes")
    ap.add_argument("--output", default=None, help="Digest .md to write (default: digest_<date>.md)")
    args = ap.parse_args()

    incoming = Path(args.incoming)
    if not incoming.is_dir():
        raise SystemExit(f"Incoming folder not found: {incoming}")
    now = datetime.now()
    output = Path(args.output) if args.output else Path(f"digest_{now.strftime('%Y-%m-%d_%H%M')}.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    digest = build_digest(incoming, now)
    output.write_text(digest, encoding="utf-8")
    print(f"Wrote {output} ({len(digest.splitlines())} lines, {len(digest)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
