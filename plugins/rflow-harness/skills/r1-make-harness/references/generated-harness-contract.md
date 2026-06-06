# Generated Harness Contract

## `.codex/DOMAIN.md`

Include:

- Project mission derived from the PRD
- Domain boundaries and important subdomains
- Required expert perspectives
- Project-specific guardrails
- Evidence and verification standards
- Release review concerns
- Explicit non-goals
- Traceability table mapping each role and skill to PRD requirements or risks

## `.codex/roles/*.md`

Create only roles that contribute distinct expertise. Each role must define:

- Responsibility
- Questions it must answer
- Inputs it reads
- Outputs or decisions it contributes
- Boundaries and prohibited claims

## `.codex/skills/*/SKILL.md`

Create focused workflows that the project will repeatedly need. Each skill must include valid YAML frontmatter and define:

- When it triggers
- Required inputs
- Procedure
- Verification or evidence requirements
- Outputs
- Guardrails

## `.codex/harness.lock.json`

After generation, preserve the existing fields and set:

```json
{
  "generationStatus": "complete",
  "domainSummary": "Concise PRD-derived description",
  "generatedArtifacts": [
    ".codex/DOMAIN.md",
    ".codex/roles/example.md",
    ".codex/skills/example/SKILL.md"
  ]
}
```

Do not claim generation is complete when roles or skills are placeholders.
