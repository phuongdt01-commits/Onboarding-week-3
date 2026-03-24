#!/usr/bin/env python3
"""Convert HTML/CSS to WebP image using Playwright.

Usage:
    python html_to_image.py input.html output.webp
    python html_to_image.py --html "<html>...</html>" output.webp

The script renders HTML at 1500x1000px and exports to WebP (<100KB).
It automatically replaces placeholders:
  - {{BACKGROUND_BASE64}} - background image
  - {{FONT_CLASH_DISPLAY}} - Clash Display font-face declarations
"""
import argparse
import base64
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import io


def get_project_root():
    """Get project root directory."""
    return Path(__file__).resolve().parents[4]


def get_background_base64():
    """Get background image as base64 data URL."""
    root = get_project_root()
    bg_path = root / "data" / "templates" / "background.png"

    if bg_path.exists():
        with open(bg_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{data}"
    else:
        return "linear-gradient(135deg, #06038D 0%, #5750FE 100%)"


def get_background_thumbnail_base64():
    """Get thumbnail background image as base64 data URL."""
    root = get_project_root()
    bg_path = root / "data" / "templates" / "background_thumbnail.png"

    if bg_path.exists():
        with open(bg_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{data}"
    else:
        return "linear-gradient(135deg, #06038D 0%, #5750FE 100%)"


def get_font_base64(font_path):
    """Get font as base64 data URL."""
    if font_path.exists():
        with open(font_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        suffix = font_path.suffix.lower()
        mime = "font/otf" if suffix == ".otf" else "font/woff2" if suffix == ".woff2" else "font/ttf"
        return f"data:{mime};base64,{data}"
    return None


def get_clash_display_fontface():
    """Generate @font-face declarations for Clash Display."""
    root = get_project_root()
    fonts_dir = root / "data" / "brand" / "fonts"

    font_faces = []
    weights = {
        "Extralight": 200,
        "Light": 300,
        "Regular": 400,
        "Medium": 500,
        "Semibold": 600,
        "Bold": 700,
    }

    for weight_name, weight_value in weights.items():
        font_path = fonts_dir / f"ClashDisplay-{weight_name}.otf"
        font_data = get_font_base64(font_path)
        if font_data:
            font_faces.append(f"""
    @font-face {{
      font-family: 'Clash Display';
      src: url('{font_data}') format('opentype');
      font-weight: {weight_value};
      font-style: normal;
    }}""")

    return "\n".join(font_faces)


def html_to_image(html_content: str, output_path: str, width: int = 1500, height: int = 1000):
    """Render HTML to image using Playwright."""

    # Replace placeholders
    html_content = html_content.replace("{{BACKGROUND_BASE64}}", get_background_base64())
    html_content = html_content.replace("{{BACKGROUND_THUMBNAIL_BASE64}}", get_background_thumbnail_base64())
    html_content = html_content.replace("{{FONT_CLASH_DISPLAY}}", get_clash_display_fontface())

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})

        # Set content
        page.set_content(html_content)

        # Wait for fonts and images to load
        page.wait_for_load_state("networkidle")

        # Take screenshot as PNG
        png_bytes = page.screenshot(type="png")

        browser.close()

    # Convert to WebP with size optimization
    img = Image.open(io.BytesIO(png_bytes))

    # Convert RGBA to RGB if needed
    if img.mode == "RGBA":
        rgb_img = Image.new("RGB", img.size, (255, 255, 255))
        rgb_img.paste(img, mask=img.split()[3])
        img = rgb_img

    # Save with quality optimization for <100KB
    out_path = Path(output_path)
    quality = 85
    while True:
        img.save(out_path, "WEBP", quality=quality, method=6)
        if out_path.stat().st_size < 100000 or quality <= 10:
            break
        quality -= 5

    print(f"Generated {out_path} ({out_path.stat().st_size} bytes, q={quality})")
    return str(out_path)


def main():
    parser = argparse.ArgumentParser(description="Convert HTML to WebP image")
    parser.add_argument("--html", help="HTML content as string")
    parser.add_argument("--file", help="HTML file path")
    parser.add_argument("--width", type=int, default=1500, help="Image width (default: 1500)")
    parser.add_argument("--height", type=int, default=1000, help="Image height (default: 1000)")
    parser.add_argument("output", help="Output file path (e.g., output.webp)")

    args = parser.parse_args()

    if args.html:
        html_content = args.html
    elif args.file:
        html_content = Path(args.file).read_text(encoding="utf-8")
    else:
        # Read from stdin
        html_content = sys.stdin.read()

    html_to_image(html_content, args.output, args.width, args.height)


if __name__ == "__main__":
    main()
