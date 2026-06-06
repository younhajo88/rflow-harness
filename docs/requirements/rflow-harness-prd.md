# Rflow Harness PRD

## Purpose

Create a Codex plugin that helps large projects preserve direction and execution state across sessions by installing a common harness, composing a domain harness, creating implementation plans, auditing planning artifacts, and running phase-scoped implementation handoffs.

## Primary User

A solo builder using Codex across multiple sessions who needs repeatable project setup, durable planning documents, and reliable status tracking.

## Core Workflow

1. Start with a PRD produced by brainstorming.
2. Generate a project harness from the PRD.
3. Generate a master implementation plan from the PRD and harness.
4. Generate phase plans from the master plan and harness.
5. Audit the documents before implementation.
6. Run one phase at a time, with implementation, verification, report, and status update.

## Requirements

- Install a versioned common lifecycle snapshot into the target project.
- Generate a project-specific domain harness, expert roles, skills, guardrails, and verification standards from the PRD.
- Keep domain generation open-ended rather than selecting from bundled domain packs.
- Create `_workspace/00_project_status.md`, decision log, verification log, and reports directory.
- Create a `harness.lock.json` file that records source versions.
- Keep phase plans independent enough for a fresh session to implement and verify.
- Provide audit checks for PRD, harness, master plan, phase plans, and status freshness.
- Keep implementation phase-scoped by default.

## Non-Goals

- Do not build a fully autonomous deployment system in v0.1.
- Do not live-link project harness files to plugin templates.
- Do not maintain a catalog of fixed domain templates in the core plugin.
- Do not make domain harnesses override the common lifecycle.

## Success Criteria

- A new project can run r1 through r5 using only local files.
- A fresh session can execute a phase from its phase plan without needing the full conversation.
- The project status file clearly shows current phase, completed units, blockers, and next action.
