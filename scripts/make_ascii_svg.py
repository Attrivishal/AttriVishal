"""
====================================================
Generate ASCII SVG Portrait
Author : Vishal Attri
====================================================

Converts a profile image into ASCII art
and exports it as an SVG.
"""

from PIL import Image
from utils import *

# ==================================================
# ASCII SETTINGS
# ==================================================

ASCII_CHARS = "@%#*+=-:. "
ASCII_WIDTH = 120

FONT_SIZE = 10
LINE_HEIGHT = 12

# ==================================================
# IMAGE PROCESSING
# ==================================================

def resize_image(image: Image.Image) -> Image.Image:
    """
    Resize image while maintaining aspect ratio.
    """

    width, height = image.size
    aspect_ratio = height / width

    new_height = int(ASCII_WIDTH * aspect_ratio * 0.55)

    return image.resize((ASCII_WIDTH, new_height))


def grayscale(image: Image.Image) -> Image.Image:
    """
    Convert image to grayscale.
    """

    return image.convert("L")


def image_to_ascii(image: Image.Image) -> str:
    """
    Convert grayscale pixels into ASCII characters.
    """

    pixels = image.getdata()

    ascii_string = "".join(
        ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        for pixel in pixels
    )

    return ascii_string


# ==================================================
# SVG GENERATOR
# ==================================================

def build_svg(ascii_image: str, width: int, height: int) -> str:

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{width*7}"
height="{height*LINE_HEIGHT}"
style="background:{BACKGROUND}">

<style>
text {{
    fill:{BLUE};
    font-family:{FONT};
    font-size:{FONT_SIZE}px;
    white-space:pre;
}}
</style>
"""

    y = LINE_HEIGHT

    for line in ascii_image.split("\n"):

        svg += f'<text x="5" y="{y}">{line}</text>\n'

        y += LINE_HEIGHT

    svg += "</svg>"

    return svg


# ==================================================
# MAIN
# ==================================================

def main():

    print("Loading profile image...")

    image = Image.open(PROFILE_IMAGE)

    image = resize_image(image)

    image = grayscale(image)

    ascii_string = image_to_ascii(image)

    pixel_count = len(ascii_string)

    ascii_image = "\n".join(
        ascii_string[index:index + ASCII_WIDTH]
        for index in range(0, pixel_count, ASCII_WIDTH)
    )

    svg = build_svg(
        ascii_image,
        ASCII_WIDTH,
        len(ascii_image.split("\n"))
    )

    with open(ASCII_OUTPUT, "w") as file:
        file.write(svg)

    print(f"✅ Generated: {ASCII_OUTPUT}")


if __name__ == "__main__":
    main()