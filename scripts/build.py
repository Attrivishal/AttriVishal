"""
============================================================
GitHub Profile Generator - Build System
Author : Vishal Attri

Description:
------------
Runs all SVG generators in sequence while performing
pre-build validation, timing, and detailed logging.

Usage:
------
python scripts/build.py
============================================================
"""

from pathlib import Path
import subprocess
import sys
import time
import shutil

# ==========================================================
# PROJECT PATHS
# ==========================================================

ROOT = Path(__file__).resolve().parent.parent

ASSETS = ROOT / "assets"
GENERATED = ROOT / "generated"

PROFILE_IMAGE = ASSETS / "profile.jpg"

# ==========================================================
# BUILD CONFIGURATION
# ==========================================================
SCRIPTS = [
    "scripts/make_info_card.py",
    "scripts/make_ascii_svg.py",
    "scripts/make_heatmap.py",
]

# ==========================================================
# COLORS
# ==========================================================

class Color:
    RESET = "\033[0m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"

    BOLD = "\033[1m"


# ==========================================================
# PRINT HELPERS
# ==========================================================

def banner():

    print()

    print(Color.CYAN + "=" * 65)
    print("        GitHub Profile Generator Build System")
    print("=" * 65 + Color.RESET)

    print()


def info(message):

    print(f"{Color.BLUE}[INFO]{Color.RESET} {message}")


def success(message):

    print(f"{Color.GREEN}[SUCCESS]{Color.RESET} {message}")


def warning(message):

    print(f"{Color.YELLOW}[WARNING]{Color.RESET} {message}")


def error(message):

    print(f"{Color.RED}[ERROR]{Color.RESET} {message}")


# ==========================================================
# PRE BUILD CHECKS
# ==========================================================

def check_python():

    info("Checking Python version...")

    if sys.version_info < (3, 10):
        error("Python 3.10 or newer is required.")
        sys.exit(1)

    success(
        f"Python {sys.version.split()[0]}"
    )


def check_assets():

    info("Checking assets...")

    if not PROFILE_IMAGE.exists():
        error("assets/profile.jpg not found.")
        sys.exit(1)

    success("Profile image found.")


def create_directories():

    info("Checking output directory...")

    GENERATED.mkdir(exist_ok=True)

    success("Output directory ready.")


def check_dependencies():

    info("Checking dependencies...")

    if shutil.which(sys.executable) is None:
        error("Python executable not found.")
        sys.exit(1)

    success("Dependencies look good.")


# ==========================================================
# RUN SCRIPT
# ==========================================================

def run_script(index, total, script):

    script_path = ROOT / script

    print()

    print(
        Color.BOLD +
        f"[{index}/{total}] Running {script}" +
        Color.RESET
    )

    start = time.perf_counter()

    result = subprocess.run(
        [sys.executable, str(script_path)]
    )

    elapsed = time.perf_counter() - start

    if result.returncode != 0:

        error(f"{script} failed.")

        sys.exit(1)

    success(f"Completed in {elapsed:.2f} sec")


# ==========================================================
# BUILD SUMMARY
# ==========================================================

def summary(total_time):

    print()

    print(Color.CYAN + "=" * 65)

    print("BUILD SUMMARY")

    print("=" * 65 + Color.RESET)

    print(f"Scripts Executed : {len(SCRIPTS)}")

    print(f"Total Time       : {total_time:.2f} sec")

    print()

    success("All SVG files generated successfully!")

    print()


# ==========================================================
# MAIN
# ==========================================================

def main():

    total_start = time.perf_counter()

    banner()

    check_python()

    create_directories()

    check_assets()

    check_dependencies()

    total = len(SCRIPTS)

    for index, script in enumerate(SCRIPTS, start=1):

        run_script(index, total, script)

    total_time = time.perf_counter() - total_start

    summary(total_time)


if __name__ == "__main__":
    main()