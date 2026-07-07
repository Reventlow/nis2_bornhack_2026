#!/usr/bin/env python3
"""Generate site/index.html (light) from site/dark.html.

site/dark.html is the editable source of truth. This script maps its
dark terminal palette to a light "Milky Matcha" palette (inspired by
the Omarchy milkmatcha theme) and writes the result as index.html —
the default deck, since the talk runs on a projector in a daylight
tent where dark ink on cream survives far better than neon-on-black.

Run from the repo root after any edit to site/dark.html:

    python3 scripts/make-light.py
"""

from pathlib import Path

SRC = Path("site/dark.html")
DST = Path("site/index.html")

# Dark token -> Milky Matcha light token.
# Text accents use dim matcha (#6b8054) rather than the theme's brighter
# #7a9461 for contrast on cream; alphas of translucent ink are boosted
# slightly since dark-on-light at low alpha reads weaker than the reverse.
COLOR_MAP = {
    # backgrounds & grid
    "#0c0e0c": "#f4f1e8",
    "rgba(120,255,160,0.045)": "rgba(122,148,97,0.14)",
    "rgba(120,255,160,0.03)": "rgba(122,148,97,0.09)",
    # accent green family
    "#4dff88": "#6b8054",
    "rgba(77,255,136,0.85)": "rgba(107,128,84,0.95)",
    "rgba(77,255,136,0.55)": "rgba(107,128,84,0.65)",
    "rgba(77,255,136,0.5)": "rgba(107,128,84,0.6)",
    "rgba(77,255,136,0.3)": "rgba(107,128,84,0.4)",
    "rgba(77,255,136,0.22)": "rgba(107,128,84,0.32)",
    "rgba(77,255,136,0.16)": "rgba(107,128,84,0.24)",
    "rgba(77,255,136,0.08)": "rgba(107,128,84,0.14)",
    # headline / body ink
    "#eef2ee": "#3a4433",
    "rgba(220,235,224,0.88)": "rgba(58,68,51,0.92)",
    "rgba(220,235,224,0.85)": "rgba(58,68,51,0.9)",
    "rgba(220,235,224,0.82)": "rgba(58,68,51,0.88)",
    "rgba(220,235,224,0.75)": "rgba(58,68,51,0.82)",
    "rgba(220,235,224,0.7)": "rgba(58,68,51,0.78)",
    "rgba(220,235,224,0.6)": "rgba(58,68,51,0.7)",
    "rgba(220,235,224,0.55)": "rgba(58,68,51,0.65)",
    "rgba(220,235,224,0.5)": "rgba(58,68,51,0.62)",
    "rgba(220,235,224,0.45)": "rgba(58,68,51,0.58)",
    "rgba(220,235,224,0.4)": "rgba(58,68,51,0.52)",
    "rgba(220,235,224,0.3)": "rgba(58,68,51,0.42)",
    "rgba(220,235,224,0.18)": "rgba(58,68,51,0.28)",
    "rgba(220,235,224,0.12)": "rgba(58,68,51,0.2)",
    "rgba(220,235,224,0.03)": "rgba(58,68,51,0.06)",
    # amber (warning/failure beats) -> darkened golden milk tea
    "#ffc857": "#a8763a",
    # inverted takeaway slide: cream ink (bg handled below)
    "#071008": "#f4f1e8",
    "rgba(7,16,8,0.82)": "rgba(244,241,232,0.92)",
    "rgba(7,16,8,0.75)": "rgba(244,241,232,0.85)",
    "rgba(7,16,8,0.7)": "rgba(244,241,232,0.85)",
    "rgba(7,16,8,0.65)": "rgba(244,241,232,0.8)",
    # terminal prompt colors (Questions slide) + link hover
    "#3f9e5f": "#6b8054",
    "#5a6b5e": "#7a8670",
    "#6ea3d8": "#7a92a5",
    "#cfe8d6": "#3a4433",
    "#8dffb5": "#8fac70",
}


def main() -> None:
    html = SRC.read_text()
    for dark, light in COLOR_MAP.items():
        html = html.replace(dark, light)
    # The inverted slide's solid #4dff88 background became #6b8054 above;
    # deepen it so cream text keeps projector-grade contrast.
    html = html.replace("background:#6b8054;box-sizing", "background:#5c6a53;box-sizing")
    # Theme-matched favicon.
    html = html.replace("favicon-dark.svg", "favicon-light.svg")
    DST.write_text(html)
    print(f"{DST} written ({len(html)} bytes)")


if __name__ == "__main__":
    main()
