#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
VALIDATOR = Path.home() / ".codex" / "skills" / ".system" / "plugin-creator" / "scripts" / "validate_plugin.py"
PLUGIN_NAME = "rflow-harness"


def run(command: list[str], cwd: Path = PLUGIN_ROOT) -> None:
    print("+ " + " ".join(command))
    subprocess.run(command, cwd=str(cwd), check=True)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def with_cachebuster(version: str, token: str) -> str:
    prefix = version.split("+", 1)[0]
    return f"{prefix}+codex.{token}"


def sanitize_token(value: str) -> str:
    token = re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")
    token = re.sub(r"-{2,}", "-", token)
    if not token:
        raise ValueError("cachebuster token must contain a letter or digit")
    return token


def update_cachebuster(token: str | None) -> str:
    manifest = read_json(MANIFEST)
    old_version = manifest["version"]
    cachebuster = sanitize_token(token or datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"))
    manifest["version"] = with_cachebuster(old_version, cachebuster)
    write_json(MANIFEST, manifest)
    print(f"version: {old_version} -> {manifest['version']}")
    return manifest["version"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Update local Rflow Harness install from the Git checkout.")
    parser.add_argument("--pull", action="store_true", help="Run git pull before validation and registration")
    parser.add_argument("--no-cachebuster", action="store_true", help="Skip plugin version cachebuster update")
    parser.add_argument("--cachebuster", help="Explicit cachebuster token")
    args = parser.parse_args()

    if args.pull:
        run(["git", "pull", "--ff-only"])

    if not VALIDATOR.exists():
        raise FileNotFoundError(f"missing Codex plugin validator: {VALIDATOR}")

    run(["python", str(VALIDATOR), str(PLUGIN_ROOT)])
    run(["python", str(PLUGIN_ROOT / "scripts" / "register_personal_marketplace.py")])

    if not args.no_cachebuster:
        update_cachebuster(args.cachebuster)
        run(["python", str(VALIDATOR), str(PLUGIN_ROOT)])

    print("")
    print("Local marketplace is ready.")
    print("Next install/reinstall command:")
    print(f"  codex plugin add {PLUGIN_NAME}@personal")
    print("Start a new Codex thread after reinstalling so the updated skills load.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
