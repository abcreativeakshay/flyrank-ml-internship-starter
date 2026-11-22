#!/usr/bin/env python3
"""
FL-05 — MCP client test.

Spawns filesystem_server.py as a subprocess, connects over stdio using the
official `mcp` Python SDK, lists the server's tools, then performs three
real tasks through tool calls:
    TASK 1  list the sandbox folder
    TASK 2  read one file (kaggle_scores.md)
    TASK 3  search/count lines containing "TODO" across all sandbox files

Everything printed here was captured verbatim into evidence_transcript.txt.
"""

from __future__ import annotations

import asyncio
import importlib.metadata as md
import sys
from datetime import datetime
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).resolve().parent
SANDBOX = HERE / "sandbox"


def text_of(result) -> str:
    return "\n".join(c.text for c in result.content if hasattr(c, "text"))


async def main() -> int:
    print("=" * 72)
    print("FL-05 MCP EVIDENCE RUN")
    print(f"Timestamp : {datetime.now().isoformat(timespec='seconds')}")
    print(f"Python    : {sys.version.split()[0]}  ({sys.executable})")
    print(f"mcp SDK   : {md.version('mcp')}")
    print(f"Server    : {HERE / 'filesystem_server.py'}")
    print(f"Sandbox   : {SANDBOX}")
    print("Transport : stdio (server spawned as a subprocess)")
    print("=" * 72)

    params = StdioServerParameters(
        command=sys.executable,
        args=[str(HERE / "filesystem_server.py"), str(SANDBOX)],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            print(f"\n[handshake] initialize() OK — server: "
                  f"{init.serverInfo.name} v{init.serverInfo.version}, "
                  f"protocol: {init.protocolVersion}")

            tools = await session.list_tools()
            print(f"\n[tools] list_tools() returned {len(tools.tools)} tools:")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description.splitlines()[0]}")

            print("\n--- TASK 1: list_files() — list the sandbox folder ---")
            r1 = await session.call_tool("list_files", {})
            print(text_of(r1))

            print("\n--- TASK 2: read_file('kaggle_scores.md') — read one file ---")
            r2 = await session.call_tool("read_file", {"name": "kaggle_scores.md"})
            print(text_of(r2))

            print("\n--- TASK 3: count_lines('TODO') — search/count across all files ---")
            r3 = await session.call_tool("count_lines", {"term": "TODO"})
            print(text_of(r3))

    print("\n[done] All three tasks completed through MCP tool calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
