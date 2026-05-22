#!/usr/bin/env python3
"""Generate 1200x630 OG (Open Graph) social-preview cards for each sport.

These render when someone shares an Academy page link in iMessage, Slack,
Facebook, X, LinkedIn, etc. Standard size is 1200x630 (Facebook/X spec).

Design:
- Source photo fills the canvas, cropped/scaled to cover
- Left half: dark gradient overlay so text is readable
- TZ horizontal logo at top-left
- Headline + tagline in Poppins
- Orange accent bar under the headline
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "images/logos/TZ_Horizontal_Lockup_White.png"
OUT_DIR = ROOT / "images/og"
OUT_DIR.mkdir(parents=True, exist_ok=True)

POPPINS_BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
POPPINS_MEDIUM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
POPPINS_REGULAR = "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf"

TZ_ORANGE = (245, 128, 48, 255)
WHITE = (255, 255, 255, 255)
DIM = (210, 210, 210, 255)

CARDS = [
    {
        "out": "basketball.jpg",
        "source": ROOT / "images/cohorts/junior-high.webp",
        "headline": "Train Like a Pro.",
        "headline_2": "Still Be a Kid.",
        "tagline": "TZ Academy — Basketball · Herriman, Utah",
    },
    {
        "out": "soccer.jpg",
        "source": ROOT / "images/coaches/Nik-College.webp",
        "headline": "Soccer Academy.",
        "headline_2": "Launching September.",
        "tagline": "Led by Nik Kizerian, former D1 player · Reserve your seat",
    },
    {
        "out": "volleyball.jpg",
        "source": ROOT / "images/coaches/Jessica.webp",
        "headline": "Volleyball Academy.",
        "headline_2": "Launching September.",
        "tagline": "Led by Jessica Finai, former D1 player · Reserve your seat",
    },
]


def fit_cover(img, size):
    """Resize img to cover size while preserving aspect, then center-crop."""
    target_w, target_h = size
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    target_ratio = target_w / target_h

    if src_ratio > target_ratio:
        # Source is wider — scale by height, crop horizontally
        new_h = target_h
        new_w = int(src_ratio * new_h)
    else:
        # Source is taller — scale by width, crop vertically
        new_w = target_w
        new_h = int(new_w / src_ratio)

    img = img.resize((new_w, new_h), Image.LANCZOS)
    # Center-crop
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def build_card(cfg):
    W, H = 1200, 630
    canvas = Image.new("RGB", (W, H), (15, 15, 15))

    # 1. Source photo, cover-fit
    src = Image.open(cfg["source"]).convert("RGB")
    src = fit_cover(src, (W, H))
    canvas.paste(src, (0, 0))

    # 2. Dark gradient overlay — opaque on left, semi-transparent on right
    #    Right side stays slightly dimmed so text remains readable even on
    #    bright photos. Fades from ~88% opacity left → ~38% opacity right.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_o = ImageDraw.Draw(overlay)
    for x in range(W):
        if x < 900:
            t = x / 900  # 0..1
            alpha = int(225 * (1 - t) + 95)  # 225 → 95 as t goes 0 → 1
        else:
            alpha = 95  # ~37% overlay across right side, keeps text legible
        draw_o.line([(x, 0), (x, H)], fill=(0, 0, 0, alpha))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")

    # 3. TZ logo top-left (scale to ~50px tall)
    logo = Image.open(LOGO).convert("RGBA")
    logo_h = 56
    logo_w = int(logo.width * (logo_h / logo.height))
    logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.paste(logo, (60, 56), logo)
    canvas = canvas_rgba

    draw = ImageDraw.Draw(canvas)

    # 4. Headline — two lines, big bold
    headline_font = ImageFont.truetype(POPPINS_BOLD, 64)
    line_1_y = 220
    line_spacing = 76
    draw.text((60, line_1_y), cfg["headline"], font=headline_font, fill=WHITE)
    draw.text((60, line_1_y + line_spacing), cfg["headline_2"], font=headline_font, fill=WHITE)

    # 5. Orange accent bar under headline
    bar_y = line_1_y + line_spacing * 2 + 24
    draw.rectangle([(60, bar_y), (60 + 80, bar_y + 4)], fill=TZ_ORANGE)

    # 6. Tagline
    tagline_font = ImageFont.truetype(POPPINS_MEDIUM, 24)
    draw.text((60, bar_y + 24), cfg["tagline"], font=tagline_font, fill=DIM)

    # Save as JPG (smaller files; OG previews don't need transparency)
    out_path = OUT_DIR / cfg["out"]
    canvas.convert("RGB").save(out_path, "JPEG", quality=88, optimize=True)
    size_kb = out_path.stat().st_size // 1024
    print(f"  ✓ {cfg['out']} ({W}x{H}, {size_kb} KB)")


def main():
    print(f"Generating OG cards in {OUT_DIR}...")
    for cfg in CARDS:
        build_card(cfg)
    print("Done.")


if __name__ == "__main__":
    main()
