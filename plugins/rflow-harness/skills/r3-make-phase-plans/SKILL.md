---
name: r3-make-phase-plans
description: "Use after r2-make-plan to create phase-specific handoff plans from the master implementation plan and harness."
---

# R3 Make Phase Plans

## Goal

Create independent phase plans under `docs/plans/phase-XX-*.md`.

Each phase plan is a handoff packet. A fresh session should be able to read it and implement plus verify that phase without needing the original conversation.

## Required Reads

- `docs/plans/00_master_implementation_plan.md`
- `.codex/HARNESS.md`
- `.codex/DOMAIN.md`
- PRD
- Existing phase reports, if any

## Depth Rule

Create a skeleton for every phase, but deeply specify only the current phase and the next one unless the user asks for more. This avoids stale over-planning.

## Required Sections

- Objective
- Source documents
- Required context
- Scope
- Non-scope
- Dependencies and prerequisites
- Implementation units
- Expected files or areas to inspect/change
- Verification requirements
- Exit criteria
- Phase run report schema
- Status update instructions

## Rules

- Do not hide unresolved decisions. Mark them as blockers or assumptions.
- Verification must be concrete enough to execute.
- Update `_workspace/00_project_status.md` with generated phase plans and next action.

## Output

List generated phase plan files and identify which phases are deep plans.
