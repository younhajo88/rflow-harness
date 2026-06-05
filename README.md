# Rflow Harness

Rflow Harness is a Codex plugin for PRD-driven projects. It installs a versioned common lifecycle harness, composes a domain harness and project overlay, creates master and phase plans, audits the documents, and runs implementation one phase at a time.

## Workflow

1. `r1-make-harness`: install common lifecycle, domain harness, project overlay, status board, and lockfile from a PRD.
2. `r2-make-plan`: create the master implementation plan from the PRD and harness.
3. `r3-make-phase-plans`: create phase handoff packets from the master plan and harness.
4. `r4-audit`: review PRD, harness, master plan, and phase plans for consistency.
5. `r5-run`: execute one selected phase plan, verify it, report results, and update status.

## MVP Domain

- SEO

## Design Rule

The common lifecycle is installed as a project snapshot, not live-linked. Domain harnesses may add roles, checks, and constraints, but they must not override the common lifecycle.
