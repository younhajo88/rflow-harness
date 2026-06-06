import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "rflow-harness"
SCRIPT = PLUGIN_ROOT / "scripts" / "scaffold_harness.py"


class ScaffoldHarnessTests(unittest.TestCase):
    def test_scaffold_installs_only_common_project_structure(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)
            prd = target / "docs" / "prd" / "00_product_requirements.md"
            prd.parent.mkdir(parents=True)
            prd.write_text("# PRD\n\nBuild a scheduling product.", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--target",
                    str(target),
                    "--prd",
                    "docs/prd/00_product_requirements.md",
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / "AGENTS.md").exists())
            self.assertTrue((target / ".codex" / "HARNESS.md").exists())
            self.assertTrue((target / ".codex" / "roles").is_dir())
            self.assertTrue((target / ".codex" / "skills").is_dir())
            self.assertFalse((target / ".codex" / "DOMAIN.md").exists())
            self.assertEqual(list((target / ".codex" / "roles").iterdir()), [])
            self.assertEqual(list((target / ".codex" / "skills").iterdir()), [])

            lock = json.loads(
                (target / ".codex" / "harness.lock.json").read_text(encoding="utf-8")
            )
            self.assertNotIn("domainHarness", lock)
            self.assertNotIn("domainHarnessVersion", lock)
            self.assertEqual(lock["generationStatus"], "pending-prd-analysis")

    def test_scaffold_rejects_missing_prd(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--target",
                    temp_dir,
                    "--prd",
                    "docs/prd/missing.md",
                ],
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("PRD not found", result.stderr + result.stdout)

    def test_scaffold_has_no_domain_argument(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--help"],
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("--domain", result.stdout)


if __name__ == "__main__":
    unittest.main()
