#!/usr/bin/env python3
"""Render the public profile README sections from the versioned portfolio registry."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "portfolio" / "portfolio.yml"
MARKER_RE = re.compile(
    r"(?P<start><!-- GENERATED:(?P<name>[A-Z0-9_-]+):START -->)\n.*?\n(?P<end><!-- GENERATED:(?P=name):END -->)",
    re.DOTALL,
)
STATUS = {"flagship", "catalog", "candidate", "retired"}


def load_registry() -> dict[str, Any]:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("portfolio registry must be a mapping")
    validate_registry(data)
    return data


def validate_registry(data: dict[str, Any]) -> None:
    if data.get("schema_version") != 1:
        raise ValueError("unsupported portfolio schema_version")
    if not data.get("owner"):
        raise ValueError("portfolio owner is required")
    sections = data.get("portfolio_sections")
    if not isinstance(sections, list) or not sections or len(set(sections)) != len(sections):
        raise ValueError("portfolio_sections must be a non-empty unique list")
    pillars = data.get("pillars")
    projects = data.get("projects")
    if not isinstance(pillars, list) or not pillars:
        raise ValueError("at least one pillar is required")
    if not isinstance(projects, list) or not projects:
        raise ValueError("at least one project is required")
    pillar_ids = {p.get("id") for p in pillars}
    for pillar in pillars:
        for key in ("id", "title_en", "title_zh", "description_en", "description_zh", "flow_en", "flow_zh"):
            if not pillar.get(key):
                raise ValueError(f"pillar missing {key}: {pillar}")
    repos: set[str] = set()
    pin_count = 0
    for project in projects:
        if not isinstance(project, dict):
            raise ValueError("each project must be a mapping")
        for key in ("repo", "pillar", "portfolio_section", "portfolio_status", "summary_en", "summary_zh"):
            if not project.get(key):
                raise ValueError(f"project missing {key}: {project}")
        repo = project["repo"]
        if repo in repos:
            raise ValueError(f"duplicate repository: {repo}")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", repo):
            raise ValueError(f"invalid repository name: {repo}")
        repos.add(repo)
        if project["pillar"] not in pillar_ids:
            raise ValueError(f"unknown pillar for {repo}: {project['pillar']}")
        if project["portfolio_section"] not in sections:
            raise ValueError(f"unknown portfolio section for {repo}: {project['portfolio_section']}")
        if project["portfolio_status"] not in STATUS:
            raise ValueError(f"invalid portfolio_status for {repo}")
        if not isinstance(project.get("pin"), bool):
            raise ValueError(f"pin must be boolean for {repo}")
        pin_count += int(project["pin"])
    if pin_count > 6:
        raise ValueError(f"GitHub supports at most six pins; registry has {pin_count}")
    for pillar in pillars:
        selected = [p for p in projects if p["pillar"] == pillar["id"] and p["portfolio_status"] == "flagship"]
        if not selected:
            raise ValueError(f"pillar has no flagship: {pillar['id']}")
    if any(p["pin"] and p["portfolio_status"] != "flagship" for p in projects):
        raise ValueError("only flagship projects may be marked pin: true")


def project_url(owner: str, repo: str) -> str:
    return f"https://github.com/{owner}/{repo}"


def tags(project: dict[str, Any]) -> str:
    return " · ".join(
        f"`{project[key].replace('-', ' ')}`" for key in ("purpose", "maturity", "evidence")
    )


def flagship_block(data: dict[str, Any], language: str) -> str:
    owner = data["owner"]
    projects = data["projects"]
    lines: list[str] = []
    for pillar in data["pillars"]:
        pillar_projects = sorted(
            (p for p in projects if p["pillar"] == pillar["id"] and p["portfolio_status"] == "flagship"),
            key=lambda p: p["display_order"],
        )
        title = pillar["title_en"] if language == "en" else pillar["title_zh"]
        description = pillar["description_en"] if language == "en" else pillar["description_zh"]
        flow_key = "flow_en" if language == "en" else "flow_zh"
        lines.extend([f"## {title}", "", description, "", "```text", pillar[flow_key], "```", "", "<table>", "<tr>"])
        for index, project in enumerate(pillar_projects):
            summary_key = "summary_en" if language == "en" else "summary_zh"
            summary = html.escape(project[summary_key])
            repo = html.escape(project["repo"])
            url = project_url(owner, project["repo"])
            lines.extend(
                [
                    f'<td width="50%"><strong><a href="{url}">{repo}</a></strong><br>',
                    f"<sub>{summary}</sub><br><br>{tags(project)}</td>",
                ]
            )
            if index == 0 and len(pillar_projects) == 1:
                lines.append('<td width="50%">&nbsp;</td>')
        lines.extend(["</tr>", "</table>", ""])
    return "\n".join(lines).rstrip()


def portfolio_block(data: dict[str, Any], language: str) -> str:
    owner = data["owner"]
    projects = data["projects"]
    lines: list[str] = []
    for section in data["portfolio_sections"]:
        section_projects = sorted(
            (p for p in projects if p["portfolio_section"] == section),
            key=lambda p: p["display_order"],
        )
        if not section_projects:
            continue
        lines.extend([f"### {section}", "", "| Project | Summary | Status | Evidence |", "| --- | --- | --- | --- |"])
        for project in section_projects:
            summary_key = "summary_en" if language == "en" else "summary_zh"
            repo = project["repo"]
            summary = project[summary_key].replace("|", "\\|")
            status = project["portfolio_status"]
            evidence = project["evidence"].replace("-", " ")
            lines.append(
                f"| [{repo}]({project_url(owner, repo)}) | {summary} | `{status}` | `{evidence}` |"
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_block(text: str, name: str, content: str) -> str:
    pattern = re.compile(
        rf"<!-- GENERATED:{re.escape(name)}:START -->\n.*?\n<!-- GENERATED:{re.escape(name)}:END -->",
        re.DOTALL,
    )
    replacement = f"<!-- GENERATED:{name}:START -->\n{content}\n<!-- GENERATED:{name}:END -->"
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise ValueError(f"controlled marker block not found exactly once: {name}")
    return updated


def expected_files(data: dict[str, Any]) -> dict[Path, dict[str, str]]:
    return {
        ROOT / "README.md": {"FLAGSHIPS": flagship_block(data, "en")},
        ROOT / "README.zh-CN.md": {"FLAGSHIPS": flagship_block(data, "zh")},
        ROOT / "PORTFOLIO.md": {"PORTFOLIO": portfolio_block(data, "en")},
        ROOT / "PORTFOLIO.zh-CN.md": {"PORTFOLIO": portfolio_block(data, "zh")},
    }


def check(data: dict[str, Any]) -> list[str]:
    problems: list[str] = []
    for path, blocks in expected_files(data).items():
        if not path.exists():
            problems.append(f"missing generated target: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for name, content in blocks.items():
            try:
                expected = replace_block(text, name, content)
            except ValueError as exc:
                problems.append(str(exc))
                continue
            if expected != text:
                problems.append(f"generated block is stale: {path.relative_to(ROOT)}::{name}")
    return problems


def write(data: dict[str, Any]) -> None:
    for path, blocks in expected_files(data).items():
        text = path.read_text(encoding="utf-8")
        for name, content in blocks.items():
            text = replace_block(text, name, content)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true", help="update controlled marker blocks")
    group.add_argument("--check", action="store_true", help="fail when generated blocks are stale")
    args = parser.parse_args()
    data = load_registry()
    if args.write:
        write(data)
        print("profile blocks rendered")
        return 0
    problems = check(data)
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1
    print("profile blocks are current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
