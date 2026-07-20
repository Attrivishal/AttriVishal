"""
====================================================
GitHub Profile Generator - Shared Utilities
Author : Vishal Attri
====================================================

This file contains all shared constants used by
every generator script.

If you ever want to change colors, fonts,
dimensions or your profile information,
you only need to edit this file.
"""

from pathlib import Path

# ==================================================
# PROJECT PATHS
# ==================================================

ROOT = Path(__file__).resolve().parent.parent

ASSETS = ROOT / "assets"
GENERATED = ROOT / "generated"

GENERATED.mkdir(exist_ok=True)

PROFILE_IMAGE = ASSETS / "profile.jpg"

ASCII_OUTPUT = GENERATED / "ascii.svg"
INFO_CARD_OUTPUT = GENERATED / "info-card.svg"
HEATMAP_OUTPUT = GENERATED / "contrib-heatmap.svg"

# ==================================================
# SVG SETTINGS
# ==================================================

WIDTH = 760
HEIGHT = 420

CARD_RADIUS = 18
HEADER_HEIGHT = 42

# ==================================================
# COLORS
# ==================================================

BACKGROUND = "#0d1117"
HEADER = "#161b22"

TEXT = "#c9d1d9"
GRAY = "#8b949e"

BLUE = "#58a6ff"
GREEN = "#7ee787"

BORDER = "#30363d"

BUTTON_RED = "#ff5f56"
BUTTON_YELLOW = "#ffbd2e"
BUTTON_GREEN = "#27c93f"

BUTTON_COLORS = [
    BUTTON_RED,
    BUTTON_YELLOW,
    BUTTON_GREEN,
]

# ==================================================
# FONT
# ==================================================

FONT = "Menlo, Monaco, monospace"

# ==================================================
# PROFILE INFORMATION
# ==================================================

NAME = "Vishal Attri"

USERNAME = "Attrivishal"

TITLE = f"{USERNAME}@github"

ROLE = "Cloud & DevOps Engineer"

STATUS = "Building Cloud Projects..."

ROWS = [
    ("Role", ROLE),
    ("Cloud", "Amazon Web Services (AWS)"),
    ("IaC", "Terraform"),
    ("Containers", "Docker"),
    ("Orchestration", "Kubernetes (Learning)"),
    ("Operating System", "Linux"),
    ("Editor", "Visual Studio Code"),
    ("Status", STATUS),
]