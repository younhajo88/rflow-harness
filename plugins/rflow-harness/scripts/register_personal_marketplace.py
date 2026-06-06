#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path


PLUGIN_NAME = "rflow-harness"
DEFAULT_MARKETPLACE_ROOT = Path.home() / ".agents" / "plugins"


def load_marketplace(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {
        "name": "personal",
        "interface": {"displayName": "Personal"},
        "plugins": [],
    }


def write_marketplace(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def sync_copy(src: Path, dst: Path) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        shutil.rmtree(dst)
    ignore = shutil.ignore_patterns(".git", "__pycache__", "*.pyc")
    shutil.copytree(src, dst, ignore=ignore)
    return "copy"


def main() -> int:
    parser = argparse.ArgumentParser(description="Register this plugin in the default personal marketplace.")
    parser.add_argument("--plugin-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--marketplace-root", default=str(DEFAULT_MARKETPLACE_ROOT))
    args = parser.parse_args()

    plugin_root = Path(args.plugin_root).resolve()
    marketplace_root = Path(args.marketplace_root).resolve()
    marketplace_path = marketplace_root / "marketplace.json"
    plugin_link = marketplace_root / "plugins" / PLUGIN_NAME

    mode = sync_copy(plugin_root, plugin_link)

    payload = load_marketplace(marketplace_path)
    plugins = payload.setdefault("plugins", [])
    entry = {
        "name": PLUGIN_NAME,
        "source": {"source": "local", "path": f"./plugins/{PLUGIN_NAME}"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }

    for index, existing in enumerate(plugins):
        if isinstance(existing, dict) and existing.get("name") == PLUGIN_NAME:
            plugins[index] = entry
            break
    else:
        plugins.append(entry)

    write_marketplace(marketplace_path, payload)

    print(f"registered: {PLUGIN_NAME}")
    print(f"marketplace: {marketplace_path}")
    print(f"source: {plugin_link} ({mode})")
    print("install command: codex plugin add rflow-harness@personal")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
