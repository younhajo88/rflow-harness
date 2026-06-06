---
name: r1-make-harness
description: "Use after a PRD exists to install the common Rflow lifecycle and generate a project-specific domain harness, expert roles, skills, guardrails, and verification standards from that PRD."
---

# R1 Make Harness

Use this after brainstorming has produced a PRD or requirements document.

## Goal

Install a project-local common lifecycle snapshot, then generate the domain and project harness from the PRD. Do not select a bundled domain template. Derive only the expertise and controls this project needs.

## Inputs

- PRD path, preferably `docs/prd/00_product_requirements.md`.
- Target project root. Default to the current repository.

## Procedure

1. Read the PRD.
2. Inspect the repository for stack, constraints, existing instructions, and validation tooling.
3. Run `scripts/scaffold_harness.py` from the plugin root with `--target` and `--prd`. This installs only the common lifecycle and workspace files.
4. Read `references/generated-harness-contract.md`.
5. Derive the project's domain boundaries, required expert perspectives, risks, evidence standards, and release checks from the PRD and repository.
6. Write `.codex/DOMAIN.md`, `.codex/roles/*.md`, and `.codex/skills/*/SKILL.md`.
7. Add project-specific guardrails to `.codex/DOMAIN.md`; do not rewrite the common lifecycle in `.codex/HARNESS.md`.
8. Update `.codex/harness.lock.json` with `generationStatus: complete`, a concise `domainSummary`, and every generated artifact path.
9. Update `_workspace/00_project_status.md` with current phase `Harness Generated` and next action `Create master implementation plan`.

## Guardrails

- Do not redesign the common lifecycle for each project.
- Do not copy a prebuilt domain pack or assume a domain from examples.
- Every generated role and skill must trace to a PRD requirement, project risk, or required verification surface.
- Prefer the smallest sufficient expert team; avoid decorative roles.
- Do not let domain harness rules override the common lifecycle.
- Do not remove an existing project harness unless the user explicitly asks for replacement.
- Preserve existing project files when possible.

## Output

Report the derived domain summary, generated roles and skills, lockfile path, traceability rationale, and the next command: `r2-make-plan`.
