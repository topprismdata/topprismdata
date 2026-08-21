#!/usr/bin/env python3
"""Derive small, publishable TopPrism logo assets from an approved SVG board.

The private brand-guide boards are intentionally not part of this repository.
This utility extracts only the approved vector logo artwork and normalizes it
into transparent, compact SVGs suitable for a GitHub profile README.
"""

from __future__ import annotations

import argparse
import copy
import xml.etree.ElementTree as ET
from pathlib import Path


SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def tag(name: str) -> str:
    return f"{{{SVG_NS}}}{name}"


def find_logo_group(root: ET.Element) -> ET.Element:
    for element in root.iter(tag("g")):
        clip = element.get("clip-path", "")
        if "master_svg1_" in clip:
            return element
    raise ValueError("approved logo group was not found")


def elements_for_mode(group: ET.Element, mode: str, gradient_ids: set[str]) -> list[ET.Element]:
    selected: list[ET.Element] = []
    for element in group.iter():
        if element.tag not in {tag("path"), tag("ellipse")}:
            continue
        fill = element.get("fill", "")
        if mode == "gradient" and fill.startswith("url(#"):
            referenced = fill.removeprefix("url(#").removesuffix(")")
            if referenced in gradient_ids:
                selected.append(element)
        elif mode == "dark" and fill.upper() == "#000000":
            selected.append(element)
        elif mode == "light" and fill.upper() == "#FFFFFF":
            selected.append(element)
    if not selected:
        raise ValueError(f"no logo artwork found for mode {mode}")
    return selected


def render_asset(source: Path, destination: Path, mode: str) -> None:
    root = ET.parse(source).getroot()
    group = find_logo_group(root)
    gradients = [e.get("id") for e in root.iter(tag("linearGradient")) if e.get("id")]
    # The first gradient is the colored presentation panel; the remaining
    # gradients are the individual approved logo paths.
    logo_gradient_ids = set(gradients[1:])
    artwork = elements_for_mode(group, mode, logo_gradient_ids)

    # These are the three logo rows in the approved "logo usage" board.
    ybase = {"gradient": 190.0, "dark": 370.0, "light": 550.0}[mode]
    out = ET.Element(
        tag("svg"),
        {
            "version": "1.1",
            "viewBox": "0 0 400 140",
            "role": "img",
            "aria-labelledby": "title desc",
        },
    )
    ET.SubElement(out, tag("title"), {"id": "title"}).text = "TopPrism logo"
    ET.SubElement(out, tag("desc"), {"id": "desc"}).text = (
        "TopPrism gradient wordmark derived from the approved brand identity."
    )
    defs = ET.SubElement(out, tag("defs"))
    if mode == "gradient":
        gradient = ET.SubElement(
            defs,
            tag("linearGradient"),
            {"id": "topprism-gradient", "x1": "0%", "y1": "50%", "x2": "100%", "y2": "50%"},
        )
        for offset, color in (
            ("0%", "#13AAFD"),
            ("34.22%", "#5267FD"),
            ("67.03%", "#9255FE"),
            ("100%", "#DC75CE"),
        ):
            ET.SubElement(gradient, tag("stop"), {"offset": offset, "stop-color": color})

    artwork_group = ET.SubElement(out, tag("g"), {"transform": f"translate(-828 {-ybase:g})"})
    for original in artwork:
        element = copy.deepcopy(original)
        if mode == "gradient":
            element.set("fill", "url(#topprism-gradient)")
        else:
            element.set("fill", "#000000" if mode == "dark" else "#FFFFFF")
        element.set("fill-opacity", "1")
        artwork_group.append(element)

    destination.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(out).write(destination, encoding="utf-8", xml_declaration=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="approved logo-usage SVG board")
    parser.add_argument("destination", type=Path, help="directory for derived assets")
    args = parser.parse_args()
    for mode, filename in (
        ("gradient", "topprism-wordmark-gradient.svg"),
        ("dark", "topprism-wordmark-dark.svg"),
        ("light", "topprism-wordmark-light.svg"),
    ):
        render_asset(args.source, args.destination / filename, mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
