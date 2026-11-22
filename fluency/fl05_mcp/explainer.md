# FL-05 — Agents and MCP, explained from a workflow I actually built

*Akshay Biradar · FlyRank AI Fluency · Nov 2026*

## What is an agent?

An agent is a program that pursues a goal in a loop: it observes the
current state of the world, decides what to do next, acts through tools,
observes the result, and repeats until the goal is met or it is told to
stop. The modern version puts a large language model in the decision
seat. The model supplies judgement — reading messy, human input and
choosing sensible next steps — while ordinary code supplies the hands:
APIs, files, browsers, databases.

Three things separate an agent from a chatbot. First, **tools**: it can
do things, not just say things. Second, **a loop**: it checks the effect
of its own actions and corrects course, rather than firing one answer
and stopping. Third, **a goal with latitude**: you specify the outcome
and the boundaries, not every step. That latitude is exactly why agents
are powerful and why they need guardrails, covered below.

My FL-04 digest workflow is deliberately *not* an agent. It is a fixed
script: same steps, same order, every run. That predictability is a
feature for a task whose rules I can state exactly. An agent earns its
keep when the rules cannot be stated exactly — which, as the FL-04
walkthrough admits, is already true of one part of my workflow.

## What is MCP?

MCP — the Model Context Protocol — is an open standard, released by
Anthropic in November 2024, for connecting AI applications to external
tools and data. Before MCP, every tool integration was bespoke: each
app needed custom glue code for each service, in each language. MCP
defines one protocol instead, often summarised as "USB-C for AI": build
a tool once as an **MCP server**, and any **MCP client** (the host
application, such as an assistant or IDE) can discover and call it.

The moving parts are small. A server advertises capabilities —
**tools** (actions it can perform), **resources** (data it can expose)
and **prompts** (reusable templates). Client and server exchange
JSON-RPC messages over a transport: stdio for a local subprocess, or
HTTP/SSE for a remote service. The client begins with a handshake,
asks the server to list its tools, and then issues tool calls with
structured arguments, receiving structured results.

The evidence beside this explainer is a real instance, not a diagram:
a 70-line filesystem server I wrote with the official Python SDK,
exposing `list_files`, `read_file` and `count_lines` over a sandboxed
folder, and a client that connects over stdio, lists those tools, and
performs all three tasks. Nothing in the client knows how the server
reads a disk — that separation is the entire point.

## What would FL-04 need to become an agent?

Four additions, in order of importance.

**1. Tools, exposed through MCP.** The digest script would stop reading
files directly. A filesystem MCP server (like the one in this folder)
would serve the notes folder; a messaging tool would deliver the
finished digest; a calendar tool could attach deadlines. Each tool is
swappable and independently testable, and the agent's reachable world
is exactly the tool list I grant it — nothing more.

**2. A decision loop with a model inside.** Today's classifier is
first-match keywords, and it demonstrably fails: my LinkedIn note is
filed under "kaggle" because it quotes Kaggle scores. A model in the
loop would read each note, classify by meaning, merge duplicate
actions, spot the deadline inside an action line, and decide what
deserves escalation. The loop matters as much as the model: read notes,
draft digest, re-check the draft against the sources, then deliver —
verifying its own output before acting on it.

**3. Guardrails, because latitude without them is just risk.** The
filesystem server here already shows the pattern: every path is
resolved and refused if it escapes the sandbox. An agent version would
add: read-only access by default; human approval before anything is
*sent* (a digest may be drafted freely, never dispatched freely); no
spending capability at all; a complete log of tool calls, so every
action can be audited and replayed; and a hard stop the moment a tool
returns something the plan did not predict.

**4. State and triggers.** An agent needs a reason to wake up — a
schedule, a new file arriving, a deadline approaching — and a memory
of yesterday's digest so "new since last time" is a fact, not a guess.

None of this requires rebuilding FL-04. The script stays as the
reliable core; MCP tools wrap its inputs and outputs, a model replaces
its weakest rule, and guardrails fence in the difference. That is the
honest path from automation to agent: not a rewrite, but a promotion —
granted only to the parts that have earned the latitude.
