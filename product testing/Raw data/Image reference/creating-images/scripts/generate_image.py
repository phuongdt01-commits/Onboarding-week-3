#!/usr/bin/env python3
"""Generate branded blog images for Chatty.

Usage:
    python generate_image.py --layout auto --title "Title" --items "Item 1" "Item 2" output.webp
    python generate_image.py --layout pills --title "Title" --items "Short" "Items" output.webp
    python generate_image.py --layout cards --title "Title" --items "Longer items" output.webp

Layouts supported:
    - auto: Auto-select best layout based on content length
    - pills: Horizontal pills (best for short text)
    - cards: Vertical cards (best for longer text)
    - badges: Circular badges with numbers
    - text_simple: Simple centered text
"""
import argparse
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Brand colors
COLORS = {
    "navy": "#06038D",
    "purple": "#5750FE",
    "yellow": "#FBC80B",
    "white": "#FFFFFF",
    "black": "#000000",
}

# Text fitting constants
MIN_FONT_SIZE = 36  # Minimum readable font size
MAX_FONT_SIZE = 150

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def get_font(fonts_dir, size=40, weight="semibold"):
    """Get font from brand fonts or fallback to system font."""
    font = None
    if fonts_dir.exists():
        candidates = [str(p) for p in fonts_dir.iterdir() if p.suffix.lower() in [".otf", ".ttf"]]
        # Filter by weight preference
        weight_map = {"semibold": 0, "medium": 1, "bold": 2, "regular": 3}
        def score(name):
            n = name.lower()
            for w, s in weight_map.items():
                if w in n:
                    return s
            return 10
        candidates.sort(key=score)
        if candidates:
            try:
                font = ImageFont.truetype(candidates[0], size=size)
            except:
                pass

    if font is None:
        for candidate in ["arial.ttf", "DejaVuSans.ttf", "Helvetica.ttf", "segoeui.ttf"]:
            try:
                font = ImageFont.truetype(candidate, size=size)
                break
            except:
                pass

    if font is None:
        font = ImageFont.load_default()

    return font

def draw_rounded_rectangle(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    diameter = radius * 2

    # Draw rectangles
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

    # Draw corners
    draw.ellipse([x1, y1, x1 + diameter, y1 + diameter], fill=fill)
    draw.ellipse([x2 - diameter, y1, x2, y1 + diameter], fill=fill)
    draw.ellipse([x1, y2 - diameter, x1 + diameter, y2], fill=fill)
    draw.ellipse([x2 - diameter, y2 - diameter, x2, y2], fill=fill)

def draw_circle(draw, center, radius, fill=None):
    """Draw a filled circle."""
    x, y = center
    draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=fill)

def draw_icon_internal(draw, center, size, color):
    """Draw circular arrows icon for internal benchmarking."""
    x, y = center
    r = size // 2
    # Draw a circular arc with arrow - simplified as rotating arrows symbol
    draw.arc([x - r, y - r, x + r, y + r], 0, 270, fill=color, width=3)
    # Arrow head
    draw.polygon([(x + r - 5, y - 8), (x + r + 5, y), (x + r - 5, y + 8)], fill=color)

def draw_icon_competitive(draw, center, size, color):
    """Draw two opposing arrows for competitive benchmarking."""
    x, y = center
    r = size // 2
    # Left arrow
    draw.line([(x - r, y), (x - 3, y)], fill=color, width=3)
    draw.polygon([(x - r, y), (x - r + 8, y - 6), (x - r + 8, y + 6)], fill=color)
    # Right arrow
    draw.line([(x + 3, y), (x + r, y)], fill=color, width=3)
    draw.polygon([(x + r, y), (x + r - 8, y - 6), (x + r - 8, y + 6)], fill=color)

def draw_icon_industry(draw, center, size, color):
    """Draw bar chart icon for industry benchmarking."""
    x, y = center
    bar_width = size // 5
    gap = 3
    # Three bars of different heights
    h1, h2, h3 = size // 2, size * 3 // 4, size // 2 + 5
    base_y = y + size // 3
    draw.rectangle([x - bar_width * 2, base_y - h1, x - bar_width - gap, base_y], fill=color)
    draw.rectangle([x - bar_width // 2, base_y - h2, x + bar_width // 2, base_y], fill=color)
    draw.rectangle([x + bar_width + gap, base_y - h3, x + bar_width * 2, base_y], fill=color)

def draw_icon_star(draw, center, size, color):
    """Draw a star icon for best-in-class benchmarking."""
    import math
    x, y = center
    r_outer = size // 2
    r_inner = size // 4
    points = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        r = r_outer if i % 2 == 0 else r_inner
        px = x + r * math.cos(angle)
        py = y - r * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=color)

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width, return list of lines."""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = f"{current} {w}".strip()
        if draw.textlength(test, font=font) <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines

def auto_scale_font(text, max_width, fonts_dir, draw, start_size=150, min_size=60, weight="medium"):
    """Auto-scale font size to fit text within max_width.

    Returns: (font, actual_text_width)
    """
    size = start_size
    while size >= min_size:
        font = get_font(fonts_dir, size=size, weight=weight)
        text_width = draw.textlength(text, font=font)
        if text_width <= max_width:
            return font, text_width
        size -= 5
    # Return minimum size font even if text still too long
    font = get_font(fonts_dir, size=min_size, weight=weight)
    return font, draw.textlength(text, font=font)

def should_wrap_text(text, max_width, fonts_dir, draw, min_size=60):
    """Check if text needs wrapping (can't fit even at min font size)."""
    font = get_font(fonts_dir, size=min_size, weight="medium")
    return draw.textlength(text, font=font) > max_width

def get_best_layout(items, title=""):
    """Auto-select best layout based on title keywords and content length."""
    if not items:
        return "text_simple"

    title_lower = title.lower()

    # Detect zigzag for process/how-to content
    zigzag_keywords = ["how to", "steps to", "process", "implement", "guide", "workflow"]
    if any(kw in title_lower for kw in zigzag_keywords) and len(items) >= 4:
        return "zigzag"

    # Detect pills for lists/types content
    pills_keywords = ["types of", "reasons", "ways to", "features", "benefits", "tips"]
    if any(kw in title_lower for kw in pills_keywords):
        return "pills"

    # Fallback to text length detection
    max_len = max(len(item) for item in items)
    avg_len = sum(len(item) for item in items) / len(items)

    if max_len <= 40 and avg_len <= 30:
        return "pills"  # Short text -> horizontal pills
    else:
        return "cards"  # Longer text -> vertical cards

def layout_pills(img, draw, title, items, fonts_dir):
    """Draw horizontal pills layout with auto-scaling text."""
    width, height = img.size

    # Colors
    yellow = hex_to_rgb(COLORS["yellow"])
    white = hex_to_rgb(COLORS["white"])
    black = hex_to_rgb(COLORS["black"])

    # Layout parameters
    content_width = int(width * 0.96)
    margin_left = (width - content_width) // 2

    # Scale pill height based on number of items
    num_items = len(items)
    if num_items <= 3:
        pill_height = 200
        spacing = 40
    elif num_items <= 4:
        pill_height = 170
        spacing = 35
    else:
        pill_height = 150
        spacing = 30

    pill_radius = pill_height // 2

    # Title font - auto-scale
    title_max_width = int(width * 0.90)
    title_font, _ = auto_scale_font(title, title_max_width, fonts_dir, draw, start_size=220, min_size=140, weight="bold")
    title_lines = wrap_text(title, title_font, title_max_width, draw)
    line_height = int(title_font.size * 1.1)
    title_total_height = len(title_lines) * line_height

    pills_total_height = num_items * pill_height + (num_items - 1) * spacing
    title_pill_gap = 50

    total_content_height = title_total_height + title_pill_gap + pills_total_height

    # CENTER content block vertically
    start_y = (height - total_content_height) // 2

    # Draw title lines (centered)
    title_y = start_y
    for line in title_lines:
        line_width = draw.textlength(line, font=title_font)
        line_x = (width - line_width) // 2
        draw.text((line_x, title_y), line, font=title_font, fill=white)
        title_y += line_height

    # Calculate text area width for items
    circle_radius = int(pill_height * 0.4)
    circle_x_offset = int(pill_height * 0.6)
    text_area_start_offset = circle_x_offset + circle_radius + 30
    text_area_end_padding = 40
    text_area_width = content_width - text_area_start_offset - text_area_end_padding

    # Start pills
    pill_x = margin_left
    pills_start_y = start_y + title_total_height + title_pill_gap

    # Draw each pill
    for i, item_text in enumerate(items):
        pill_y = pills_start_y + i * (pill_height + spacing)

        # Draw yellow pill
        draw_rounded_rectangle(
            draw,
            [pill_x, pill_y, pill_x + content_width, pill_y + pill_height],
            radius=pill_radius,
            fill=yellow
        )

        # Draw black circle with number
        circle_x = pill_x + circle_x_offset
        circle_y = pill_y + pill_height // 2
        draw_circle(draw, (circle_x, circle_y), circle_radius, fill=black)

        # Draw number in circle (white, centered)
        number_font_size = int(circle_radius * 1.0)
        number_font = get_font(fonts_dir, size=number_font_size, weight="bold")
        num_text = str(i + 1)
        num_bbox = draw.textbbox((0, 0), num_text, font=number_font)
        num_width = num_bbox[2] - num_bbox[0]
        num_height = num_bbox[3] - num_bbox[1]
        num_x = circle_x - num_width // 2
        num_y = circle_y - num_height // 2 - 5
        draw.text((num_x, num_y), num_text, font=number_font, fill=white)

        # AUTO-SCALE item text to fit in pill
        text_area_start = pill_x + text_area_start_offset
        item_font, text_w = auto_scale_font(item_text, text_area_width, fonts_dir, draw,
                                             start_size=int(pill_height * 0.5), min_size=MIN_FONT_SIZE)
        text_bbox = draw.textbbox((0, 0), item_text, font=item_font)
        text_h = text_bbox[3] - text_bbox[1]

        # Center text horizontally in text area
        text_x = text_area_start + (text_area_width - text_w) // 2
        text_y = pill_y + (pill_height - text_h) // 2 - 5
        draw.text((text_x, text_y), item_text, font=item_font, fill=black)


def layout_cards(img, draw, title, items, fonts_dir):
    """Draw vertical cards layout - better for longer text."""
    width, height = img.size

    # Colors
    yellow = hex_to_rgb(COLORS["yellow"])
    white = hex_to_rgb(COLORS["white"])
    black = hex_to_rgb(COLORS["black"])

    # Layout parameters
    content_width = int(width * 0.92)
    margin_left = (width - content_width) // 2
    num_items = len(items)

    # Scale card dimensions based on number of items
    if num_items <= 3:
        card_height = 160
        spacing = 20
    elif num_items <= 4:
        card_height = 140
        spacing = 15
    else:
        card_height = 120
        spacing = 12

    card_radius = 20

    # Title font
    title_max_width = int(width * 0.90)
    title_font, _ = auto_scale_font(title, title_max_width, fonts_dir, draw, start_size=180, min_size=120, weight="bold")
    title_lines = wrap_text(title, title_font, title_max_width, draw)
    line_height = int(title_font.size * 1.15)
    title_total_height = len(title_lines) * line_height

    cards_total_height = num_items * card_height + (num_items - 1) * spacing
    title_card_gap = 40

    total_content_height = title_total_height + title_card_gap + cards_total_height
    start_y = (height - total_content_height) // 2

    # Draw title lines (centered)
    title_y = start_y
    for line in title_lines:
        line_width = draw.textlength(line, font=title_font)
        line_x = (width - line_width) // 2
        draw.text((line_x, title_y), line, font=title_font, fill=white)
        title_y += line_height

    # Start cards
    card_x = margin_left
    cards_start_y = start_y + title_total_height + title_card_gap

    # Number badge dimensions
    badge_size = int(card_height * 0.5)
    text_padding = 30

    for i, item_text in enumerate(items):
        card_y = cards_start_y + i * (card_height + spacing)

        # Draw yellow card
        draw_rounded_rectangle(
            draw,
            [card_x, card_y, card_x + content_width, card_y + card_height],
            radius=card_radius,
            fill=yellow
        )

        # Draw number badge (left side)
        badge_x = card_x + badge_size // 2 + 20
        badge_y = card_y + card_height // 2
        draw_circle(draw, (badge_x, badge_y), badge_size // 2, fill=black)

        # Number text
        num_font_size = int(badge_size * 0.6)
        num_font = get_font(fonts_dir, size=num_font_size, weight="bold")
        num_text = str(i + 1)
        num_bbox = draw.textbbox((0, 0), num_text, font=num_font)
        num_w = num_bbox[2] - num_bbox[0]
        num_h = num_bbox[3] - num_bbox[1]
        draw.text((badge_x - num_w // 2, badge_y - num_h // 2 - 3), num_text, font=num_font, fill=white)

        # Text area
        text_area_start = card_x + badge_size + 40
        text_area_width = content_width - badge_size - 60 - text_padding

        # Auto-scale text
        item_font, text_w = auto_scale_font(item_text, text_area_width, fonts_dir, draw,
                                             start_size=int(card_height * 0.45), min_size=MIN_FONT_SIZE)

        # Check if we need to wrap
        if text_w > text_area_width:
            # Wrap text into 2 lines
            lines = wrap_text(item_text, item_font, text_area_width, draw)
            total_text_height = len(lines) * (item_font.size + 5)
            text_y = card_y + (card_height - total_text_height) // 2
            for line in lines:
                draw.text((text_area_start, text_y), line, font=item_font, fill=black)
                text_y += item_font.size + 5
        else:
            # Single line, centered vertically
            text_bbox = draw.textbbox((0, 0), item_text, font=item_font)
            text_h = text_bbox[3] - text_bbox[1]
            text_y = card_y + (card_height - text_h) // 2 - 3
            draw.text((text_area_start, text_y), item_text, font=item_font, fill=black)


def layout_zigzag(img, draw, title, items, fonts_dir):
    """Draw zigzag flow diagram - steps connected in alternating pattern.

    Proportions match the pills sample: tall boxes, good vertical centering.
    """
    width, height = img.size

    # Colors
    yellow = hex_to_rgb(COLORS["yellow"])
    white = hex_to_rgb(COLORS["white"])
    black = hex_to_rgb(COLORS["black"])

    # Layout parameters
    num_items = len(items)
    content_width = int(width * 0.96)  # 96% of canvas width (like pills sample)
    margin_x = (width - content_width) // 2

    rows = (num_items + 1) // 2

    # Title first - to calculate remaining space
    title_max_width = int(width * 0.90)
    title_font, _ = auto_scale_font(title, title_max_width, fonts_dir, draw, start_size=220, min_size=150, weight="bold")
    title_lines = wrap_text(title, title_font, title_max_width, draw)
    line_height = int(title_font.size * 1.1)
    title_total_height = len(title_lines) * line_height

    # Calculate available height for boxes - fill more space
    title_gap = 40
    top_margin = 60
    bottom_margin = 50
    available_height = height - top_margin - title_total_height - title_gap - bottom_margin

    # Box dimensions - maximize space usage
    row_spacing = 35  # Larger gap between rows
    total_spacing = (rows - 1) * row_spacing
    box_height = (available_height - total_spacing) // rows
    box_height = max(140, min(200, box_height))  # Adjusted for more spacing

    # Box width: ~47% of content width each (maximize)
    box_width = int(content_width * 0.47)
    gap_between = content_width - (box_width * 2)

    box_radius = box_height // 2  # Full rounded ends like pills

    # Recalculate total height
    total_boxes_height = rows * box_height + (rows - 1) * row_spacing
    total_content_height = title_total_height + title_gap + total_boxes_height

    # Center content block vertically
    start_y = (height - total_content_height) // 2

    # Draw title lines (centered)
    title_y = start_y
    for line in title_lines:
        line_width = draw.textlength(line, font=title_font)
        line_x = (width - line_width) // 2
        draw.text((line_x, title_y), line, font=title_font, fill=white)
        title_y += line_height

    # Start boxes
    boxes_start_y = start_y + title_total_height + title_gap

    # Zigzag positions: left and right columns
    left_x = margin_x
    right_x = margin_x + box_width + gap_between

    for i, item_text in enumerate(items):
        row = i // 2
        is_left = (i % 2 == 0)  # Even index = left, Odd = right

        box_x = left_x if is_left else right_x
        box_y = boxes_start_y + row * (box_height + row_spacing)

        # Draw yellow box
        draw_rounded_rectangle(
            draw,
            [box_x, box_y, box_x + box_width, box_y + box_height],
            radius=box_radius,
            fill=yellow
        )

        # Draw number circle - positioned at left edge of box (like sample)
        circle_radius = int(box_height * 0.35)
        circle_x = box_x + circle_radius + 20
        circle_y = box_y + box_height // 2
        draw_circle(draw, (circle_x, circle_y), circle_radius, fill=black)

        # Number text
        num_font = get_font(fonts_dir, size=int(circle_radius * 1.1), weight="bold")
        num_text = str(i + 1)
        num_bbox = draw.textbbox((0, 0), num_text, font=num_font)
        num_w = num_bbox[2] - num_bbox[0]
        num_h = num_bbox[3] - num_bbox[1]
        draw.text((circle_x - num_w // 2, circle_y - num_h // 2 - 3), num_text, font=num_font, fill=white)

        # Text area - maximize space for text
        text_area_start = box_x + circle_radius * 2 + 45
        text_area_width = box_width - circle_radius * 2 - 60

        # Auto-scale text - larger size for bigger boxes
        item_font, text_w = auto_scale_font(item_text, text_area_width, fonts_dir, draw,
                                             start_size=int(box_height * 0.45), min_size=36)

        if text_w > text_area_width:
            # Wrap text
            lines = wrap_text(item_text, item_font, text_area_width, draw)
            line_spacing = 4
            total_text_height = len(lines) * item_font.size + (len(lines) - 1) * line_spacing
            text_y = box_y + (box_height - total_text_height) // 2
            for line in lines:
                draw.text((text_area_start, text_y), line, font=item_font, fill=black)
                text_y += item_font.size + line_spacing
        else:
            text_bbox = draw.textbbox((0, 0), item_text, font=item_font)
            text_h = text_bbox[3] - text_bbox[1]
            text_y = box_y + (box_height - text_h) // 2 - 2
            draw.text((text_area_start, text_y), item_text, font=item_font, fill=black)

        # Draw connector arrow to next item
        if i < num_items - 1:
            arrow_color = yellow
            arrow_width = 5
            arrow_head_size = 14

            if is_left and i + 1 < num_items:
                # Arrow from left to right (same row)
                arrow_start = (box_x + box_width + 15, box_y + box_height // 2)
                arrow_end = (right_x - 15, box_y + box_height // 2)
                draw.line([arrow_start, arrow_end], fill=arrow_color, width=arrow_width)
                # Arrow head
                draw.polygon([
                    (arrow_end[0], arrow_end[1]),
                    (arrow_end[0] - arrow_head_size, arrow_end[1] - arrow_head_size // 2),
                    (arrow_end[0] - arrow_head_size, arrow_end[1] + arrow_head_size // 2)
                ], fill=arrow_color)
            elif not is_left and i + 1 < num_items:
                # Arrow from right down to next row left
                next_row_y = boxes_start_y + (row + 1) * (box_height + row_spacing)
                mid_y = box_y + box_height + (row_spacing // 2)

                # Down from right box
                draw.line([(box_x + box_width // 2, box_y + box_height),
                           (box_x + box_width // 2, mid_y)], fill=arrow_color, width=arrow_width)
                # Horizontal to left
                draw.line([(box_x + box_width // 2, mid_y),
                           (left_x + box_width // 2, mid_y)], fill=arrow_color, width=arrow_width)
                # Down to left box
                draw.line([(left_x + box_width // 2, mid_y),
                           (left_x + box_width // 2, next_row_y)], fill=arrow_color, width=arrow_width)
                # Arrow head
                draw.polygon([
                    (left_x + box_width // 2, next_row_y),
                    (left_x + box_width // 2 - arrow_head_size // 2, next_row_y - arrow_head_size),
                    (left_x + box_width // 2 + arrow_head_size // 2, next_row_y - arrow_head_size)
                ], fill=arrow_color)


def draw_grid_icon(draw, icon_type, center, size, color):
    """Draw themed icons for grid cards."""
    import math
    x, y = center
    r = size // 2

    if icon_type == 0:  # Target/bullseye - for clarity/strategy
        # Outer circle
        draw.ellipse([x - r, y - r, x + r, y + r], outline=color, width=4)
        # Middle circle
        draw.ellipse([x - r*0.6, y - r*0.6, x + r*0.6, y + r*0.6], outline=color, width=3)
        # Center dot
        draw.ellipse([x - r*0.2, y - r*0.2, x + r*0.2, y + r*0.2], fill=color)

    elif icon_type == 1:  # Bar chart - for performance/gaps
        bar_w = size // 5
        gap = 4
        heights = [0.5, 0.8, 0.6]
        base_y = y + r * 0.7
        for i, h in enumerate(heights):
            bx = x - bar_w * 1.5 - gap + i * (bar_w + gap)
            by = base_y - size * h
            draw.rectangle([bx, by, bx + bar_w, base_y], fill=color)

    elif icon_type == 2:  # Gear/cog - for optimization/resources
        # Outer gear teeth
        teeth = 8
        for i in range(teeth):
            angle = i * 2 * math.pi / teeth
            tx = x + r * 0.9 * math.cos(angle)
            ty = y + r * 0.9 * math.sin(angle)
            draw.ellipse([tx - 6, ty - 6, tx + 6, ty + 6], fill=color)
        # Inner circle
        draw.ellipse([x - r*0.5, y - r*0.5, x + r*0.5, y + r*0.5], fill=color)
        # Center hole (use yellow background color)
        draw.ellipse([x - r*0.2, y - r*0.2, x + r*0.2, y + r*0.2], fill=(251, 200, 11))

    elif icon_type == 3:  # Arrow up/growth - for improvement
        # Arrow shaft
        shaft_w = size // 5
        draw.rectangle([x - shaft_w//2, y - r*0.3, x + shaft_w//2, y + r*0.7], fill=color)
        # Arrow head
        points = [
            (x, y - r*0.8),  # Top point
            (x - r*0.5, y - r*0.2),  # Bottom left
            (x + r*0.5, y - r*0.2),  # Bottom right
        ]
        draw.polygon(points, fill=color)


def layout_grid(img, draw, title, items, fonts_dir):
    """Draw 2x2 grid layout with large cards, icons - best for 4 items with longer text.

    Each card has:
    - Icon at top-right corner
    - Large number badge at top-left
    - Bold title (first part before colon)
    - Description text below
    """
    width, height = img.size

    # Colors
    yellow = hex_to_rgb(COLORS["yellow"])
    white = hex_to_rgb(COLORS["white"])
    black = hex_to_rgb(COLORS["black"])

    # Layout parameters per SKILL.md specs
    # Content width: 96% of canvas
    content_width = int(width * 0.96)  # 1440px

    # Title - 150-220px font per spec, avoid logo area (top-right)
    title_max_width = int(width * 0.70)  # Reduced to avoid logo
    title_font, _ = auto_scale_font(title, title_max_width, fonts_dir, draw, start_size=180, min_size=150, weight="bold")
    title_lines = wrap_text(title, title_font, title_max_width, draw)
    line_height = int(title_font.size * 1.1)
    title_total_height = len(title_lines) * line_height

    # Grid dimensions - 2x2
    cols = 2
    rows = 2

    # MAXIMIZED: Fill as much vertical space as possible
    gap = 20
    card_width = int(width * 0.46)  # 690px = 46% width each

    # Center the grid with proper margins
    grid_total_width = 2 * card_width + gap
    margin_x = (width - grid_total_width) // 2  # ~60px margin

    # Tight margins to maximize content
    top_margin = 160  # Below logo - increased to avoid overlap
    bottom_margin = 40
    title_gap = 25

    # Calculate available space for grid
    available_for_grid = height - top_margin - bottom_margin - title_total_height - title_gap
    card_height = (available_for_grid - gap) // rows
    card_height = max(card_height, 280)  # No upper limit - fill the space

    # Total content
    grid_height = rows * card_height + (rows - 1) * gap
    total_content_height = title_total_height + title_gap + grid_height

    # Start position - tight to top
    start_y = top_margin

    # Draw title
    title_y = start_y
    for line in title_lines:
        line_width = draw.textlength(line, font=title_font)
        line_x = (width - line_width) // 2
        draw.text((line_x, title_y), line, font=title_font, fill=white)
        title_y += line_height

    # Draw grid cards
    grid_start_y = start_y + title_total_height + title_gap

    for i, item_text in enumerate(items[:4]):
        row = i // cols
        col = i % cols

        card_x = margin_x + col * (card_width + gap)
        card_y = grid_start_y + row * (card_height + gap)

        # Draw card background
        card_radius = 28
        draw_rounded_rectangle(
            draw,
            [card_x, card_y, card_x + card_width, card_y + card_height],
            radius=card_radius,
            fill=yellow
        )

        # Icon - centered vertically in card, at right side
        icon_size = 140
        icon_x = card_x + card_width - 90
        icon_y = card_y + card_height // 2  # Center vertically
        draw_grid_icon(draw, i % 4, (icon_x, icon_y), icon_size, black)

        # Number badge - centered vertically in card, with proper padding from edge
        badge_size = 75
        badge_x = card_x + 40  # More padding from card edge
        badge_center_y = card_y + card_height // 2  # Center vertically
        draw_circle(draw, (badge_x + badge_size // 2, badge_center_y), badge_size // 2, fill=black)

        # Number text - LARGE
        num_font = get_font(fonts_dir, size=48, weight="bold")
        num_text = str(i + 1)
        num_bbox = draw.textbbox((0, 0), num_text, font=num_font)
        num_w = num_bbox[2] - num_bbox[0]
        num_h = num_bbox[3] - num_bbox[1]
        draw.text((badge_x + badge_size // 2 - num_w // 2,
                   badge_center_y - num_h // 2 - 2), num_text, font=num_font, fill=white)

        # Parse item: "Title: Description" or just text
        if ":" in item_text:
            item_title, item_desc = item_text.split(":", 1)
            item_title = item_title.strip()
            item_desc = item_desc.strip()
        else:
            item_title = item_text
            item_desc = ""

        # Text area - next to badge, leave space for icon
        text_x = badge_x + badge_size + 20
        text_width = card_width - text_x + card_x - icon_size - 25

        # Item title (bold) - LARGE title text
        title_item_font, _ = auto_scale_font(item_title, text_width, fonts_dir, draw,
                                               start_size=75, min_size=50, weight="bold")

        # Calculate total text height for vertical centering
        title_height = title_item_font.size
        desc_font = get_font(fonts_dir, size=48, weight="medium")
        desc_text_width = card_width - 60

        if item_desc:
            desc_lines = wrap_text(item_desc, desc_font, desc_text_width, draw)
            desc_height = len(desc_lines) * (desc_font.size + 8)
            total_text_height = title_height + 15 + desc_height
        else:
            total_text_height = title_height
            desc_lines = []

        # Center text block vertically in card
        text_start_y = card_y + (card_height - total_text_height) // 2

        # Draw title
        draw.text((text_x, text_start_y), item_title, font=title_item_font, fill=black)

        # Description (if exists)
        if desc_lines:
            desc_y = text_start_y + title_height + 15
            for line in desc_lines[:3]:
                draw.text((card_x + 30, desc_y), line, font=desc_font, fill=black)
                desc_y += desc_font.size + 8


# Keep old name for backwards compatibility
def layout_numbered_list(img, draw, title, items, fonts_dir, icons=None):
    """Alias for layout_pills (backwards compatibility)."""
    layout_pills(img, draw, title, items, fonts_dir)

def layout_text_simple(img, draw, title, fonts_dir):
    """Draw simple centered text (legacy layout)."""
    width, height = img.size
    font = get_font(fonts_dir, size=40)
    white = hex_to_rgb(COLORS["white"])

    # Wrap text
    max_width = width - 40
    lines = []
    words = title.split()
    current = ""
    for w in words:
        test = f"{current} {w}".strip()
        if draw.textlength(test, font=font) <= max_width:
            current = test
        else:
            lines.append(current)
            current = w
    if current:
        lines.append(current)

    # Draw centered
    y = height // 2 - (len(lines) * 50) // 2
    for line in lines:
        line_width = draw.textlength(line, font=font)
        x = (width - line_width) // 2
        draw.text((x, y), line, font=font, fill=white)
        y += 50

def main():
    parser = argparse.ArgumentParser(description="Generate branded Chatty blog images")
    parser.add_argument("--layout", choices=["auto", "pills", "cards", "zigzag", "grid", "numbered_list", "text_simple"],
                        default="auto", help="Layout type (auto will select based on content length)")
    parser.add_argument("--title", required=True, help="Title text")
    parser.add_argument("--items", nargs="*", help="List items")
    parser.add_argument("output", help="Output file path (e.g., output.webp)")

    args = parser.parse_args()

    # Paths - go up 4 levels: scripts -> creating-images -> skills -> .claude -> project root
    root = Path(__file__).resolve().parents[4]
    bg_path = root / "data" / "templates" / "background.png"
    fonts_dir = root / "data" / "brand" / "fonts"
    out_path = Path(args.output)

    # Load background
    if bg_path.exists():
        img = Image.open(bg_path).convert("RGBA")
    else:
        # Create default gradient background
        img = Image.new("RGBA", (1500, 1000), hex_to_rgb(COLORS["navy"]))

    draw = ImageDraw.Draw(img)

    # Determine layout
    layout = args.layout
    if layout == "auto" and args.items:
        layout = get_best_layout(args.items, args.title)
        print(f"Auto-selected layout: {layout}")

    # Apply layout
    if layout in ["pills", "numbered_list"]:
        if not args.items:
            print("Error: --items required for pills layout")
            sys.exit(1)
        layout_pills(img, draw, args.title, args.items, fonts_dir)
    elif layout == "cards":
        if not args.items:
            print("Error: --items required for cards layout")
            sys.exit(1)
        layout_cards(img, draw, args.title, args.items, fonts_dir)
    elif layout == "zigzag":
        if not args.items:
            print("Error: --items required for zigzag layout")
            sys.exit(1)
        layout_zigzag(img, draw, args.title, args.items, fonts_dir)
    elif layout == "grid":
        if not args.items:
            print("Error: --items required for grid layout")
            sys.exit(1)
        layout_grid(img, draw, args.title, args.items, fonts_dir)
    else:
        layout_text_simple(img, draw, args.title, fonts_dir)

    # Save with quality optimization for <100KB
    # Convert to RGB if RGBA (removes alpha channel, reduces size)
    if img.mode == "RGBA":
        rgb_img = Image.new("RGB", img.size, (255, 255, 255))
        rgb_img.paste(img, mask=img.split()[3])
        img = rgb_img

    quality = 80
    while True:
        # Use method=6 for better compression (slower but smaller)
        img.save(out_path, "WEBP", quality=quality, method=6)
        if out_path.stat().st_size < 100000 or quality <= 5:  # < 100KB (100000 bytes)
            break
        quality -= 5

    print(f"Generated {out_path} ({out_path.stat().st_size} bytes, q={quality})")

if __name__ == "__main__":
    main()
