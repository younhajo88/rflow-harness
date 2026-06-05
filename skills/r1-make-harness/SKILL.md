---
name: r1-make-harness
description: "Use after a PRD exists to install an Rflow project harness: common lifecycle snapshot, domain harness, project overlay, status board, logs, and harness lockfile."
---

# R1 Make Harness

Use this after brainstorming has produced a PRD or requirements document.

## Goal

Install, do not live-link, a project-local harness snapshot. The common lifecycle is fixed by this plugin. The domain harness adds domain roles and checks. The project overlay comes from the PRD.

## Inputs

- PRD path, preferably `docs/prd/00_product_requirements.md`.
- Domain name. Use `seo` when the PRD is about search visibility, indexing, SEO learning, public SEO sites, or Search Console workflows.
- Target project root. Default to the current repository.

## Procedure

1. Read the PRD.
2. Determine the domain. If uncertain, ask the user before installing.
3. Run `scripts/scaffold_harness.py` from the plugin root with `--target`, `--domain`, and `--prd`.
4. Edit `.codex/HARNESS.md` and `.codex/DOMAIN.md` only if the PRD contains project-specific guardrails that are not captured by the templates.
5. Update `_workspace/00_project_status.md` with current phase `Harness Installed` and next action `Create master implementation plan`.

## Guardrails

- Do not redesign the common lifecycle for each project.
- Do not let domain harness rules override the common lifecycle.
- Do not remove an existing project harness unless the user explicitly asks for replacement.
- Preserve existing project files when possible.

## Output

Report installed files, selected domain, lockfile path, and the next command: `r2-make-plan`.
