---
name: r5-run
description: "Use to execute one selected phase plan with implementation, verification, phase report, and project status update."
---

# R5 Run

## Goal

Execute one phase, or a small explicitly selected set of phase units, using the phase plan as the primary handoff document.

## Required Reads

- Selected `docs/plans/phase-XX-*.md`
- `.codex/HARNESS.md`
- `.codex/DOMAIN.md`
- `_workspace/00_project_status.md`
- Any source files named by the phase plan

## Procedure

1. Confirm selected phase or units.
2. Read the phase plan and required context.
3. Implement only in scope.
4. Run verification required by the phase plan.
5. Fix blocking failures that are in scope.
6. Write `_workspace/reports/phase-XX-run-YYYY-MM-DD.md`.
7. Update `_workspace/00_project_status.md` and `_workspace/02_verification_log.md`.

## Run Report Required Sections

- Phase
- Completed units
- Changed files
- Verification performed
- Results
- Failed or blocked items
- Follow-up required
- Status updates made
- Recommendation for next phase

## Guardrails

- Default to one phase per run.
- Do not silently broaden scope.
- Do not claim completion without verification evidence.
- If the phase plan is not independently executable, stop and recommend `r3-make-phase-plans` or `r4-audit`.
