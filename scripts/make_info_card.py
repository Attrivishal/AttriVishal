"""
====================================================
Generate GitHub Profile Information Card
====================================================
"""

import svgwrite

from utils import *

# ==================================================
# CREATE DRAWING
# ==================================================

dwg = svgwrite.Drawing(
    str(INFO_CARD_OUTPUT),
    size=(f"{WIDTH}px", f"{HEIGHT}px"),
)

# ==================================================
# BACKGROUND
# ==================================================

dwg.add(
    dwg.rect(
        insert=(0, 0),
        size=(WIDTH, HEIGHT),
        rx=CARD_RADIUS,
        ry=CARD_RADIUS,
        fill=BACKGROUND,
    )
)

# ==================================================
# HEADER
# ==================================================

dwg.add(
    dwg.rect(
        insert=(0, 0),
        size=(WIDTH, HEADER_HEIGHT),
        rx=CARD_RADIUS,
        ry=CARD_RADIUS,
        fill=HEADER,
    )
)

# Header Fix

dwg.add(
    dwg.rect(
        insert=(0, 20),
        size=(WIDTH, HEADER_HEIGHT),
        fill=HEADER,
    )
)

# ==================================================
# macOS BUTTONS
# ==================================================

for index, color in enumerate(BUTTON_COLORS):

    dwg.add(
        dwg.circle(
            center=(22 + index * 20, 21),
            r=6,
            fill=color,
        )
    )

# ==================================================
# TITLE
# ==================================================

dwg.add(
    dwg.text(
        TITLE,
        insert=(90, 27),
        fill=GRAY,
        font_family=FONT,
        font_size="15px",
    )
)

# ==================================================
# NAME
# ==================================================

dwg.add(
    dwg.text(
        NAME,
        insert=(35, 80),
        fill=BLUE,
        font_family=FONT,
        font_size="28px",
        font_weight="bold",
    )
)

# ==================================================
# DIVIDER
# ==================================================

dwg.add(
    dwg.line(
        start=(35, 95),
        end=(720, 95),
        stroke=BORDER,
        stroke_width=1,
    )
)

# ==================================================
# PROFILE INFORMATION
# ==================================================

y = 130

for key, value in ROWS:

    # Left Column

    dwg.add(
        dwg.text(
            key,
            insert=(35, y),
            fill=GREEN,
            font_family=FONT,
            font_size="18px",
            font_weight="bold",
        )
    )

    # Right Column

    dwg.add(
        dwg.text(
            value,
            insert=(250, y),
            fill=TEXT,
            font_family=FONT,
            font_size="18px",
        )
    )

    y += 35

# ==================================================
# FOOTER
# ==================================================

dwg.add(
    dwg.text(
        "Generated with Python + svgwrite",
        insert=(35, HEIGHT - 20),
        fill=GRAY,
        font_family=FONT,
        font_size="12px",
    )
)

# ==================================================
# SAVE
# ==================================================

dwg.save()

print(f"✅ Generated: {INFO_CARD_OUTPUT}")