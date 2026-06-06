import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCAFFOLD = ROOT / "scripts" / "scaffold_harness.py"
AUDIT = ROOT / "scripts" / "audit_harness.py"


def run(*args):
    return subprocess.run(
        [sys.executable, *map(str, args)],
        capture_output=True,
        text=True,
    )


class AuditHarnessTests(unittest.TestCase):
    def scaffold(self, target: Path) -> None:
        prd = target / "docs" / "prd" / "00_product_requirements.md"
        prd.parent.mkdir(parents=True)
        prd.write_text("# PRD\n\nBuild a scheduling product.", encoding="utf-8")
        result = run(
            SCAFFOLD,
            "--target",
            target,
            "--prd",
            "docs/prd/00_product_requirements.md",
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_pending_prd_generation_is_a_failure(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)
            self.scaffold(target)

            result = run(AUDIT, "--target", target)
            payload = json.loads(result.stdout)
            checks = {finding["check"] for finding in payload["findings"]}

            self.assertEqual(result.returncode, 1)
            self.assertIn("prd_harness_generation_complete", checks)
            self.assertIn("generated_roles_exist", checks)
            self.assertIn("generated_skills_exist", checks)

    def test_generated_domain_harness_passes_generation_checks(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)
            self.scaffold(target)

            (target / ".codex" / "DOMAIN.md").write_text(
                "# Scheduling Domain Harness", encoding="utf-8"
            )
            (target / ".codex" / "roles" / "scheduling-architect.md").write_text(
                "# Scheduling Architect", encoding="utf-8"
            )
            skill = target / ".codex" / "skills" / "schedule-validation" / "SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text(
                "---\n"
                "name: schedule-validation\n"
                'description: "Validate scheduling rules."\n'
                "---\n\n"
                "# Schedule Validation\n",
                encoding="utf-8",
            )

            lock_path = target / ".codex" / "harness.lock.json"
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            lock["generationStatus"] = "complete"
            lock["domainSummary"] = "Scheduling and conflict resolution"
            lock["generatedArtifacts"] = [
                ".codex/DOMAIN.md",
                ".codex/roles/scheduling-architect.md",
                ".codex/skills/schedule-validation/SKILL.md",
            ]
            lock_path.write_text(json.dumps(lock), encoding="utf-8")

            result = run(AUDIT, "--target", target)
            payload = json.loads(result.stdout)
            failed_checks = {
                finding["check"]
                for finding in payload["findings"]
                if finding["status"] == "FAIL"
            }

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertNotIn("prd_harness_generation_complete", failed_checks)
            self.assertNotIn("generated_roles_exist", failed_checks)
            self.assertNotIn("generated_skills_exist", failed_checks)


if __name__ == "__main__":
    unittest.main()
