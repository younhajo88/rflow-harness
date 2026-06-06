import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"


class MarketplaceLayoutTests(unittest.TestCase):
    def test_repository_contains_supported_marketplace_layout(self):
        payload = json.loads(MARKETPLACE.read_text(encoding="utf-8"))

        self.assertEqual(payload["name"], "rflow-harness-marketplace")
        self.assertEqual(len(payload["plugins"]), 1)

        plugin = payload["plugins"][0]
        self.assertEqual(plugin["name"], "rflow-harness")
        self.assertEqual(plugin["source"]["source"], "local")
        self.assertEqual(plugin["source"]["path"], "./plugins/rflow-harness")
        self.assertEqual(plugin["policy"]["installation"], "AVAILABLE")
        self.assertEqual(plugin["policy"]["authentication"], "ON_INSTALL")

        plugin_root = ROOT / plugin["source"]["path"]
        self.assertTrue((plugin_root / ".codex-plugin" / "plugin.json").is_file())
        self.assertTrue((plugin_root / "skills").is_dir())


if __name__ == "__main__":
    unittest.main()
