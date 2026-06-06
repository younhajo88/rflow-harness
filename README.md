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

## Local Development Install

Register the plugin in the default personal marketplace:

```powershell
python .\scripts\register_personal_marketplace.py
```

Then install it in Codex:

```powershell
codex plugin add rflow-harness@personal
```

Start a new Codex thread after installing so the new skills are loaded.

If the Codex CLI is not on PATH, use the Codex app plugin UI. The personal marketplace is already registered at:

```text
C:\Users\younh\.agents\plugins\marketplace.json
```

If Codex protocol deeplinks are registered on your machine, this may also open the plugin view:

```text
codex://plugins/rflow-harness?marketplacePath=C%3A%5CUsers%5Cyounh%5C.agents%5Cplugins%5Cmarketplace.json
```

From PowerShell, run it with:

```powershell
Start-Process "codex://plugins/rflow-harness?marketplacePath=C%3A%5CUsers%5Cyounh%5C.agents%5Cplugins%5Cmarketplace.json"
```

## Updating From GitHub

Use the GitHub repository as the canonical source, while Codex installs from the local checkout through the personal marketplace.

```powershell
cd C:\work\rflow-harness
python .\scripts\update_local_install.py --pull
```

The update script runs `git pull --ff-only`, validates the plugin, ensures the personal marketplace points at this checkout, updates the plugin version cachebuster, and prints the reinstall command:

```powershell
codex plugin add rflow-harness@personal
```

If the Codex CLI is not available, the script also prints a Codex app deeplink for installing from the plugin UI.

## Design Rule

The common lifecycle is installed as a project snapshot, not live-linked. Domain harnesses may add roles, checks, and constraints, but they must not override the common lifecycle.
