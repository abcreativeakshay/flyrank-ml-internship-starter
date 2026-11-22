#!/usr/bin/env python3
"""
FL-05 — a minimal MCP (Model Context Protocol) filesystem server.

Written by hand with the official `mcp` Python SDK (FastMCP) because the
reference `mcp-server-filesystem` package is distributed via npm/npx, not
pip (verified: `pip install mcp-server-filesystem` -> "No matching
distribution found"). This server exposes three tools over stdio and is
hard-limited to one sandbox folder: every path is resolved and checked
to stay inside the root before any file is touched.

Tools:
    list_files(subdir="")          -> names + sizes of files in the sandbox
    read_file(name)                -> full text of one sandbox file
    count_lines(term)              -> per-file + total count of lines
                                      containing `term` across the sandbox

Run standalone (for an MCP host/client to spawn):
    python filesystem_server.py [sandbox_dir]
"""

from __future__ import annotations

import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

SANDBOX = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).parent.joinpath("sandbox").resolve()
TEXT_SUFFIXES = {".md", ".txt"}

mcp = FastMCP("fl05-filesystem-sandbox")


def _safe_path(name: str) -> Path:
    """Resolve `name` inside the sandbox; refuse anything that escapes it."""
    target = (SANDBOX / name).resolve()
    if SANDBOX not in target.parents and target != SANDBOX:
        raise ValueError(f"Path escapes the sandbox: {name!r}")
    return target


@mcp.tool()
def list_files(subdir: str = "") -> str:
    """List files (name and size in bytes) inside the sandbox folder."""
    folder = _safe_path(subdir) if subdir else SANDBOX
    if not folder.is_dir():
        return f"Not a directory: {subdir or '.'}"
    lines = []
    for p in sorted(folder.iterdir()):
        kind = "dir " if p.is_dir() else "file"
        size = p.stat().st_size if p.is_file() else 0
        lines.append(f"{kind}  {p.name}  ({size} bytes)")
    return "\n".join(lines) if lines else "(empty)"


@mcp.tool()
def read_file(name: str) -> str:
    """Read and return the full text of one file inside the sandbox."""
    target = _safe_path(name)
    if not target.is_file():
        return f"Not a file: {name}"
    return target.read_text(encoding="utf-8", errors="replace")


@mcp.tool()
def count_lines(term: str) -> str:
    """Count, per file and in total, how many lines contain `term` (case-insensitive)."""
    total = 0
    out = []
    for p in sorted(SANDBOX.rglob("*")):
        if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES:
            hits = sum(1 for line in p.read_text(encoding="utf-8", errors="replace").splitlines()
                       if term.lower() in line.lower())
            out.append(f"{p.relative_to(SANDBOX)}: {hits}")
            total += hits
    out.append(f"TOTAL lines containing {term!r}: {total}")
    return "\n".join(out)


if __name__ == "__main__":
    SANDBOX.mkdir(parents=True, exist_ok=True)
    mcp.run(transport="stdio")
