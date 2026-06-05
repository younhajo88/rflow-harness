#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


REQUIRED = [
    "AGENTS.md",
    ".codex/HARNESS.md",
    ".codex/DOMAIN.md",
    ".codex/harness.lock.json",
    "_workspace/00_project_status.md",
    "_workspace/01_decision_log.md",
    "_workspace/02_verification_log.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run structural Rflow harness audit.")
    parser.add_argument("--target", default=".", help="Target project root")
    parser.add_argument("--prd", default=None, help="Optional repo-relative PRD path")
    parser.add_argument("--master-plan", default="docs/plans/00_master_implementation_plan.md")
    args = parser.parse_args()

    root = Path(args.target).resolve()
    findings = []

    for rel in REQUIRED:
        if not (root / rel).exists():
            findings.append({"status": "FAIL", "check": "required_file", "path": rel})

    lock_path = root / ".codex" / "harness.lock.json"
    if lock_path.exists():
        try:
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            prd = args.prd or lock.get("prdSource")
            if prd and not (root / prd).exists():
                findings.append({"status": "WARN", "check": "prd_source_exists", "path": prd})
        except json.JSONDecodeError:
            findings.append({"status": "FAIL", "check": "lockfile_valid_json", "path": ".codex/harness.lock.json"})

    if not (root / args.master_plan).exists():
        findings.append({"status": "WARN", "check": "master_plan_exists", "path": args.master_plan})

    plan_dir = root / "docs" / "plans"
    phase_plans = list(plan_dir.glob("phase-*.md")) if plan_dir.exists() else []
    if not phase_plans:
        findings.append({"status": "WARN", "check": "phase_plans_exist", "path": "docs/plans/phase-*.md"})

    if not findings:
        findings.append({"status": "PASS", "check": "structural_audit", "path": str(root)})

    print(json.dumps({"target": str(root), "findings": findings}, indent=2))
    return 1 if any(f["status"] == "FAIL" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
