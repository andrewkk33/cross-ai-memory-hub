---
name: cross-ai-memory-hub
description: "This skill should be used when a user wants to avoid re-introducing themselves to every new AI office agent (Doubao Work, TraeWork, WorkBuddy, Qwen Office, Yuanbao, etc.) by establishing a shared local memory hub on their own machine that all agents read and write. Triggers include requests like make a cross-AI memory prompt, stop making me re-introduce myself to new AIs, shared memory for multiple AI assistants, portable AI onboarding prompt, or any discussion of AI office-agent memory isolation or switching between multiple agents. It provides a zero-edit unboxing prompt plus a cross-platform scaffold script that creates an EMPTY .ai-memory-hub directory under the user home directory, e.g. C:\\Users\\YOUR_USERNAME\\.ai-memory-hub on Windows or ~/.ai-memory-hub on macOS/Linux."
agent_created: true
---

# Cross-AI Memory Hub

## Overview

Users increasingly run several AI office agents (数字员工 / 办公智能体) at once and switch
between them. Each agent keeps its own private memory, so the user must re-state "who I am,
where I am, what I do, what I prefer" every time they open a new one. This skill solves that
by setting up a single **local hidden folder** (`.ai-memory-hub`) as the *single source of
truth* for the user's profile, preferences, context, and habits. A portable "unboxing prompt"
tells any new agent to read/write that folder automatically — so onboarding becomes a
copy-paste, not an interview.

## When To Use

- User complains about re-introducing themselves to new AI agents.
- User asks for a reusable prompt to "carry my memory across AIs".
- User is switching between Doubao Work / TraeWork / WorkBuddy / Qwen Office and wants continuity.
- User wants to build a shareable onboarding prompt for friends or a team.

## How It Works

1. A hidden directory `.ai-memory-hub` lives in the user's **home directory**
   (`C:\Users\YOUR_USERNAME\.ai-memory-hub` on Windows, `~/.ai-memory-hub` on macOS/Linux).
2. It holds plain-markdown files: `profile.md`, `preferences.md`, `context.md`,
   `habits.md`, `agent-log.md`, `README.md`.
3. The **unboxing prompt** (see `references/unboxing-prompt.md`) is pasted into a new agent's
   first message. The agent then:
   - locates/creates `.ai-memory-hub`;
   - if `profile.md` exists, reads all files and works from memory (no re-introduction);
   - if not, scaffolds the skeleton and asks a few generic onboarding questions, then continues;
   - writes incremental updates back after each session, appending to `agent-log.md`.

## Workflow

### Step 1 — Scaffold the hub (optional, one-time)

Run the bundled script to create an **empty** hub on the current machine:

```bash
python scripts/scaffold.py
```

The script is cross-platform (Windows / macOS / Linux), idempotent (skips existing files),
and creates only empty/titled skeleton files — it never copies any existing personal data.
After scaffolding, the user may pre-fill `profile.md` or let the first agent ask.

### Step 2 — Use the unboxing prompt

Copy the entire prompt from `references/unboxing-prompt.md` and paste it as the **first
message** to any new AI office agent. No editing required — the agent auto-locates the hub
in the user's home directory. Verify by asking the agent "Who am I and what am I working on
lately?"; a correct answer proves the hub is wired up.

### Step 3 — Ongoing use

Each new agent reads the same hub, so context carries over. The `agent-log.md` file forms a
continuous cross-agent timeline. To share the system with others, send them only
`references/unboxing-prompt.md` (generic, no personal data) — their agent scaffolds its own
empty hub on first run.

## Safety & Privacy Boundaries (MUST enforce)

- The "full permission" granted in the prompt is scoped to **read/write of the hub directory
  + the agent's own built-in tools**. Do NOT grant unknown new agents whole-machine admin,
  format, or shell escalation — untested product sandboxes risk local file leakage.
- Never instruct an agent to upload hub contents to untrusted external services.
- Keep secrets (passwords, keys, ID numbers) OUT of the hub.
- Prerequisite: the target agent must have **local file access** (desktop / virtual-desktop
  class agents such as WorkBuddy, TraeWork, Doubao Work virtual desktop). Pure cloud chat
  bots without file permission cannot create/read the folder and will fail.

## Resources

### scripts/scaffold.py
Cross-platform scaffolder that creates an empty `.ai-memory-hub` under the user's home
directory with the six standard skeleton files.

### references/unboxing-prompt.md
The portable, zero-edit prompt to paste into any new agent. Generic and safe to share
publicly — contains no personal information.
