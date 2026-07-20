"""
====================================================
Generate GitHub Contribution Heatmap
Author : Vishal Attri
====================================================

Creates a fake GitHub-style contribution heatmap.
This is used as a visual element inside the README.
"""

import random
import svgwrite

from utils import *

# ==================================================
# GRID SETTINGS
# ==================================================

ROWS = 7
COLUMNS = 26

CELL_SIZE = 18
CELL_GAP = 4

PADDING = 30

# GitHub contribution colors
LEVELS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

SVG_WIDTH = PADDING * 2 + COLUMNS * (CELL_SIZE + CELL_GAP)
SVG_HEIGHT = PADDING * 2 + ROWS * (CELL_SIZE + CELL_GAP)


# ==================================================
# CREATE SVG
# ==================================================

dwg = svgwrite.Drawing(
    str(HEATMAP_OUTPUT),
    size=(f"{SVG_WIDTH}px", f"{SVG_HEIGHT}px"),
)

# Background

dwg.add(
    dwg.rect(
        insert=(0, 0),
        size=(SVG_WIDTH, SVG_HEIGHT),
        fill=BACKGROUND,
        rx=15,
        ry=15,
    )
)

# ==================================================
# TITLE
# ==================================================

dwg.add(
    dwg.text(
        "GitHub Contribution Heatmap",
        insert=(25, 20),
        fill=TEXT,
        font_family=FONT,
        font_size="15px",
        font_weight="bold",
    )
)

# ==================================================
# DRAW GRID
# ==================================================

for column in range(COLUMNS):

    for row in range(ROWS):

        x = PADDING + column * (CELL_SIZE + CELL_GAP)

        y = 35 + row * (CELL_SIZE + CELL_GAP)

        level = random.choice(LEVELS)

        dwg.add(
            dwg.rect(
                insert=(x, y),
                size=(CELL_SIZE, CELL_SIZE),
                rx=3,
                ry=3,
                fill=level,
            )
        )

# ==================================================
# LEGEND
# ==================================================

legend_x = SVG_WIDTH - 140
legend_y = SVG_HEIGHT - 20

dwg.add(
    dwg.text(
        "Less",
        insert=(legend_x - 35, legend_y + 11),
        fill=GRAY,
        font_family=FONT,
        font_size="10px",
    )
)

for i, color in enumerate(LEVELS):

    dwg.add(
        dwg.rect(
            insert=(legend_x + i * 16, legend_y),
            size=(12, 12),
            rx=2,
            ry=2,
            fill=color,
        )
    )

dwg.add(
    dwg.text(
        "More",
        insert=(legend_x + 90, legend_y + 11),
        fill=GRAY,
        font_family=FONT,
        font_size="10px",
    )
)

# ==================================================
# SAVE
# ==================================================

dwg.save()

print(f"✅ Generated: {HEATMAP_OUTPUT}")