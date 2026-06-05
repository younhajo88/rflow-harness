# AGENTS.md

## Rflow Harness

This project uses an Rflow harness snapshot.

Always follow:

1. PRD defines what to build.
2. `.codex/HARNESS.md` defines the common lifecycle.
3. `.codex/DOMAIN.md` defines domain-specific rules.
4. `docs/plans/00_master_implementation_plan.md` defines phase order.
5. `docs/plans/phase-XX-*.md` defines phase-level implementation handoffs.
6. `_workspace/00_project_status.md` is the current state board.

## Lifecycle

brainstorm -> PRD -> harness -> master plan -> phase plans -> audit -> phase run -> verification -> release review -> observation

## Status Rule

Update `_workspace/00_project_status.md` whenever phase status, verification results, blockers, deployment state, or next action changes.

## Implementation Rule

For large work, implement one phase at a time. A phase is complete only when its exit criteria and verification requirements are satisfied.
