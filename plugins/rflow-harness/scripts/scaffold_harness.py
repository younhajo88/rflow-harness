#!/usr/bin/env python3
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
ASSETS = PLUGIN_ROOT / "assets"
COMMON = ASSETS / "common"


def copy_file_if_missing(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install an Rflow harness snapshot into a project.")
    parser.add_argument("--target", default=".", help="Target project root")
    parser.add_argument("--prd", default="docs/prd/00_product_requirements.md", help="Repo-relative PRD path")
    parser.add_argument("--force", action="store_true", help="Overwrite generated harness files")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    prd_path = target / args.prd
    if not prd_path.is_file():
        raise SystemExit(f"PRD not found: {args.prd}")

    (target / ".codex").mkdir(parents=True, exist_ok=True)
    (target / ".codex" / "roles").mkdir(parents=True, exist_ok=True)
    (target / ".codex" / "skills").mkdir(parents=True, exist_ok=True)
    (target / "docs" / "prd").mkdir(parents=True, exist_ok=True)
    (target / "docs" / "plans").mkdir(parents=True, exist_ok=True)
    (target / "_workspace" / "reports").mkdir(parents=True, exist_ok=True)

    files = {
        COMMON / "AGENTS.template.md": target / "AGENTS.md",
        COMMON / "HARNESS.template.md": target / ".codex" / "HARNESS.md",
        COMMON / "project-status.template.md": target / "_workspace" / "00_project_status.md",
        COMMON / "decision-log.template.md": target / "_workspace" / "01_decision_log.md",
        COMMON / "verification-log.template.md": target / "_workspace" / "02_verification_log.md",
    }
    for src, dst in files.items():
        if args.force and dst.exists():
            shutil.copy2(src, dst)
        else:
            copy_file_if_missing(src, dst)

    lock = {
        "plugin": "rflow-harness",
        "pluginVersion": "0.1.0",
        "commonHarnessVersion": "0.1.0",
        "prdSource": args.prd,
        "generationStatus": "pending-prd-analysis",
        "generatedArtifacts": [],
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "snapshotMode": "install-not-live-link",
    }
    lock_path = target / ".codex" / "harness.lock.json"
    lock_path.write_text(json.dumps(lock, indent=2), encoding="utf-8")

    print(f"Installed Rflow common harness in {target}")
    print(f"PRD: {args.prd}")
    print("Next: analyze the PRD and generate DOMAIN.md, roles, and skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
