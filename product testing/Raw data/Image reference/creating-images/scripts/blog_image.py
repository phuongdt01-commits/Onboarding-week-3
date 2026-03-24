#!/usr/bin/env python3
"""Utility to create blog-specific image folders and generate branded images.

Usage:
    python blog_image.py "Blog Title" "Image description"

This script slugifies the blog title, makes a directory under `images/` named
after the slug, then invokes `generate_image.py` to create a webp inside that
directory. It ensures consistent organisation for blog asset generation.

Example:
    python blog_image.py "The customer is always right" "A support-themed banner"

This will produce:
    images/the-customer-is-always-right/banner.webp

You can run the script as many times as needed for different descriptions or size
variants; each invocation will create or reuse the blog's folder.
"""
import sys
from pathlib import Path
import re

if len(sys.argv) < 3:
    print("Usage: python blog_image.py \"Blog Title\" \"Image description\"")
    sys.exit(1)

blog_title = sys.argv[1]
desc = sys.argv[2]

# simple slugify: lowercase, replace non-alphanum with hyphens, collapse
slug = re.sub(r"[^a-z0-9]+", "-", blog_title.lower()).strip("-")

output_dir = Path("images") / slug
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "banner.webp"

# call generate_image.py
from subprocess import run

gen_script = Path(__file__).parent / "generate_image.py"
if not gen_script.exists():
    raise FileNotFoundError("generate_image.py not found")

cmd = ["python3", str(gen_script), desc, str(output_file)]
print("Running:", " ".join(cmd))
res = run(cmd)
res.check_returncode()
print(f"Generated image at {output_file}")
