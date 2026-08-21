#!/usr/bin/env python3
"""Validate the profile's public assets, links and registry-derived content."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

from render_profile import ROOT, check, load_registry


MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SECRET_PATTERNS = (
    re.compile(r"(?:ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN (?:OPENSSH|RSA|EC|PGP) PRIVATE KEY-----"),
    re.compile(r"(?:sk-[A-Za-z0-9_-]{20,})"),
)
FORBIDDEN_TEXT = ("/Users/", "\\Users\\", "ghkey.txt", "codex-clipboard")
SVG_LIMIT = 150_000


def check_markdown_links() -> list[str]:
    problems: list[str] = []
    for path in (ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "PORTFOLIO.md", ROOT / "PORTFOLIO.zh-CN.md"):
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().split(" ", 1)[0]
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).exists():
                problems.append(f"broken local link: {path.relative_to(ROOT)} -> {target}")
    return problems


def check_assets() -> list[str]:
    problems: list[str] = []
    assets = sorted((ROOT / "assets").rglob("*.svg"))
    if not assets:
        return ["no SVG assets found"]
    for path in assets:
        if path.stat().st_size > SVG_LIMIT:
            problems.append(f"SVG exceeds {SVG_LIMIT} bytes: {path.relative_to(ROOT)}")
        raw = path.read_text(encoding="utf-8")
        if "base64," in raw:
            problems.append(f"embedded base64 is not allowed: {path.relative_to(ROOT)}")
        try:
            root = ET.fromstring(raw)
        except ET.ParseError as exc:
            problems.append(f"invalid SVG XML {path.relative_to(ROOT)}: {exc}")
            continue
        if root.tag.rsplit("}", 1)[-1] != "svg":
            problems.append(f"root element is not svg: {path.relative_to(ROOT)}")
        if not root.get("viewBox"):
            problems.append(f"SVG has no viewBox: {path.relative_to(ROOT)}")
    return problems


def check_public_text() -> list[str]:
    problems: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".yml", ".yaml", ".py", ".svg", ".txt"}:
            continue
        # This validator necessarily contains the markers it is checking for.
        if path.resolve() == Path(__file__).resolve():
            continue
        raw = path.read_text(encoding="utf-8", errors="ignore")
        for marker in FORBIDDEN_TEXT:
            if marker in raw:
                problems.append(f"private/local marker {marker!r} found in {path.relative_to(ROOT)}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(raw):
                problems.append(f"possible secret material found in {path.relative_to(ROOT)}")
                break
    return problems


def check_live(data: dict) -> list[str]:
    problems: list[str] = []
    owner = data["owner"]
    for project in data["projects"]:
        repo = project["repo"]
        result = subprocess.run(
            ["gh", "api", f"repos/{owner}/{repo}"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            problems.append(f"GitHub repository lookup failed: {owner}/{repo}")
            continue
        payload = json.loads(result.stdout)
        if payload.get("private"):
            problems.append(f"catalog repository is private: {owner}/{repo}")
        if payload.get("archived"):
            problems.append(f"catalog repository is archived: {owner}/{repo}")
        if project["portfolio_status"] == "flagship" and payload.get("fork"):
            problems.append(f"flagship cannot be an upstream fork: {owner}/{repo}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="also verify public GitHub repository metadata")
    args = parser.parse_args()
    data = load_registry()
    problems = check(data) + check_markdown_links() + check_assets() + check_public_text()
    if args.live:
        problems.extend(check_live(data))
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1
    print("profile validation passed")
    if args.live:
        print("live GitHub repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
