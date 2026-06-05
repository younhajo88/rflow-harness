#!/usr/bin/env python3
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
ASSETS = PLUGIN_ROOT / "assets"
COMMON = ASSETS / "common"
DOMAINS = ASSETS / "domains"


def copy_tree_contents(src: Path, dst: Path) -> None:
    if not src.exists():
        raise FileNotFoundError(src)
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            copy_tree_contents(item, target)
        elif not target.exists():
            shutil.copy2(item, target)


def copy_file_if_missing(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description="Install an Rflow harness snapshot into a project.")
    parser.add_argument("--target", default=".", help="Target project root")
    parser.add_argument("--domain", default="seo", help="Domain harness to install")
    parser.add_argument("--prd", default="docs/prd/00_product_requirements.md", help="Repo-relative PRD path")
    parser.add_argument("--force", action="store_true", help="Overwrite generated harness files")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    domain = args.domain.lower().strip()
    domain_src = DOMAINS / domain
    if not domain_src.exists():
        raise SystemExit(f"Unknown domain harness: {domain}")

    (target / ".codex").mkdir(parents=True, exist_ok=True)
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

    copy_tree_contents(domain_src / "roles", target / ".codex" / "roles")
    copy_tree_contents(domain_src / "skills", target / ".codex" / "skills")
    copy_file_if_missing(domain_src / "domain-harness.template.md", target / ".codex" / "DOMAIN.md")

    lock = {
        "plugin": "rflow-harness",
        "pluginVersion": "0.1.0",
        "commonHarnessVersion": "0.1.0",
        "domainHarness": domain,
        "domainHarnessVersion": "0.1.0",
        "prdSource": args.prd,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "snapshotMode": "install-not-live-link",
    }
    lock_path = target / ".codex" / "harness.lock.json"
    lock_path.write_text(json.dumps(lock, indent=2), encoding="utf-8")

    print(f"Installed Rflow harness in {target}")
    print(f"Domain: {domain}")
    print(f"PRD: {args.prd}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
