# Rflow Project Harness

## Harness Sources

- common lifecycle: rflow-common@0.1.0
- domain harness: see `.codex/DOMAIN.md`
- lockfile: `.codex/harness.lock.json`

## Mission

Preserve project direction, execution quality, and progress state across Codex sessions by using durable documents and phase-scoped implementation.

## Common Lifecycle

1. Brainstorm and write PRD.
2. Install project harness.
3. Write master implementation plan.
4. Write phase plans.
5. Audit planning documents.
6. Run one phase at a time.
7. Verify each phase.
8. Run release review before readiness claims.
9. Observe production data before growth claims.

## Document Roles

- PRD: product and scope truth.
- Master plan: phase sequence and dependencies.
- Phase plan: implementation handoff packet.
- Project status: current state and next action.
- Verification log: evidence of checks performed.
- Run report: what happened during a phase execution.

## Invariants

- Domain harnesses add expertise but do not override this lifecycle.
- Project files contain a snapshot of the harness.
- Updates to common harness rules require explicit user request.
- Completion requires verification evidence.
- Large implementation should default to one phase per run.

## Release Readiness

Do not claim release readiness while blocking verification or release-review failures remain.
