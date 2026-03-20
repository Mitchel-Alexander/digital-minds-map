"""
Normalise all PNGs in outputs/logos/ to uniform 200x200 white-background canvases.
Originals are backed up to outputs/logos/originals/ before modification.
"""
import os, shutil
from PIL import Image

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_DIR = os.path.join(ROOT, 'outputs', 'logos')
ORIG_DIR = os.path.join(LOGO_DIR, 'originals')
WIDTH    = 400
HEIGHT   = 100
PADDING  = 12   # minimum whitespace on each side

os.makedirs(ORIG_DIR, exist_ok=True)

files = sorted(f for f in os.listdir(LOGO_DIR) if f.endswith('.png'))
print(f"Processing {len(files)} logos → {WIDTH}×{HEIGHT}px, {PADDING}px padding")

for fname in files:
    src = os.path.join(LOGO_DIR, fname)
    dst_orig = os.path.join(ORIG_DIR, fname)

    # Back up original if not already backed up
    if not os.path.exists(dst_orig):
        shutil.copy2(src, dst_orig)

    # Always re-read from original to avoid compounding normalisation
    img = Image.open(dst_orig).convert('RGBA')

    # Trim transparent/white border to get the actual logo bounds
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    # Scale to fit within padded area, preserving aspect ratio
    max_w = WIDTH  - 2 * PADDING
    max_h = HEIGHT - 2 * PADDING
    img.thumbnail((max_w, max_h), Image.LANCZOS)

    # Compose onto white canvas
    canvas = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 255))
    x = (WIDTH  - img.width)  // 2
    y = (HEIGHT - img.height) // 2
    canvas.paste(img, (x, y), mask=img)

    # Save as RGB PNG (white background, no transparency)
    canvas.convert('RGB').save(src, 'PNG', optimize=True)
    print(f"  {fname:60s} {img.width}×{img.height} → {WIDTH}×{HEIGHT}")

print(f"\nDone. Originals preserved in outputs/logos/originals/")
