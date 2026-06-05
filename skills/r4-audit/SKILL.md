---
name: r4-audit
description: "Use before implementation or release to audit PRD, harness, master plan, phase plans, status board, and verification expectations for consistency."
---

# R4 Audit

## Goal

Review documents for execution readiness before implementation starts or continues.

## Required Checks

- PRD exists and has clear requirements.
- `.codex/HARNESS.md`, `.codex/DOMAIN.md`, and `.codex/harness.lock.json` exist.
- Master plan maps PRD requirements to phases.
- Every active phase has a phase plan.
- Each phase plan is independently executable.
- Verification requirements are concrete and runnable.
- Domain guardrails do not conflict with the common lifecycle.
- `_workspace/00_project_status.md` reflects the latest phase and next action.
- Existing FAIL findings are not ignored.

## Procedure

1. Run `scripts/audit_harness.py` from the plugin root when available for structural checks.
2. Read the PRD, harness, master plan, and current phase plan.
3. Produce findings ordered by severity: FAIL, WARN, PASS.
4. Write or update `_workspace/reports/audit-YYYY-MM-DD.md`.
5. Update `_workspace/00_project_status.md` if the audit changes readiness.

## Output

Lead with blocking findings. If no blockers exist, state that implementation may proceed and name the recommended phase for `r5-run`.
