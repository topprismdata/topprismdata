import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_profile import check, load_registry  # noqa: E402


class ProfileContractTest(unittest.TestCase):
    def test_registry_has_reviewed_flagships_for_each_pillar(self):
        registry = load_registry()
        projects = registry["projects"]
        self.assertEqual(len(projects), 25)
        self.assertEqual(sum(project["pin"] for project in projects), 3)
        for pillar in registry["pillars"]:
            self.assertTrue(
                any(
                    project["pillar"] == pillar["id"] and project["portfolio_status"] == "flagship"
                    for project in projects
                )
            )

    def test_generated_pages_are_current(self):
        self.assertEqual(check(load_registry()), [])


if __name__ == "__main__":
    unittest.main()
