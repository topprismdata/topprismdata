#!/usr/bin/env python3
"""Report drift between the reviewed registry and manually managed GitHub Pins."""

from __future__ import annotations

import argparse
import json
import subprocess

from render_profile import load_registry


QUERY = """
query($login: String!) {
  user(login: $login) {
    pinnedItems(first: 6, types: REPOSITORY) {
      nodes {
        ... on Repository { name }
      }
    }
  }
}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="return non-zero when Pins differ")
    args = parser.parse_args()
    registry = load_registry()
    expected = [p["repo"] for p in registry["projects"] if p["pin"]]
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={QUERY}", "-F", f"login={registry['owner']}"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        print("ERROR: unable to read GitHub Pins; authenticate with gh and retry")
        if result.stderr:
            print(result.stderr.strip())
        return 1
    payload = json.loads(result.stdout)
    actual = [node["name"] for node in payload["data"]["user"]["pinnedItems"]["nodes"]]
    missing = [repo for repo in expected if repo not in actual]
    extra = [repo for repo in actual if repo not in expected]
    order_drift = not missing and not extra and actual != expected
    print(f"expected Pins: {', '.join(expected) or '(none)'}")
    print(f"actual Pins:   {', '.join(actual) or '(none)'}")
    if missing:
        print(f"missing: {', '.join(missing)}")
    if extra:
        print(f"extra: {', '.join(extra)}")
    if order_drift:
        print("order drift: actual Pin order differs from registry order")
    if missing or extra or order_drift:
        print("ACTION: update Pins manually in the topprismdata GitHub profile after the reviewed change is merged.")
        return 1 if args.strict else 0
    print("GitHub Pins match the reviewed registry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
