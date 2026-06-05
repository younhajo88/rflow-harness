---
name: r2-make-plan
description: "Use after r1-make-harness to create a master implementation plan from the PRD, project harness, domain harness, and current repository context."
---

# R2 Make Plan

## Goal

Create `docs/plans/00_master_implementation_plan.md`.

The master plan controls phase order, dependencies, scope boundaries, and exit criteria. It must not become a giant detailed implementation design.

## Required Reads

- PRD, usually `docs/prd/00_product_requirements.md`
- `.codex/HARNESS.md`
- `.codex/DOMAIN.md`
- `.codex/harness.lock.json`
- Existing source tree and relevant existing docs

## Plan Shape

The master plan must include:

- Problem frame
- Source documents
- Scope and non-scope
- Architecture-level decisions
- Phase overview
- Phase dependencies
- Cross-phase risks
- Verification strategy
- Release review criteria
- Current and next phase pointer

## Rules

- Keep implementation details at phase level.
- Every PRD requirement must map to at least one phase or be explicitly deferred.
- Every phase must have an exit criterion.
- Update `_workspace/00_project_status.md` after writing the plan.

## Output

Write the master plan and report the phase list. Recommend `r3-make-phase-plans`.
