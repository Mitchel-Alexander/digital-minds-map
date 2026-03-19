"""
Normalise all PNGs in outputs/logos/ to uniform 200x200 white-background canvases.
Originals are backed up to outputs/logos/originals/ before modification.
"""
import os, shutil
from PIL import Image

ROOT     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_DIR = os.path.join(ROOT, 'outputs', 'logos')
ORIG_DIR = os.path.join(LOGO_DIR, 'originals')
SIZE     = 200
PADDING  = 16   # minimum whitespace on each side

os.makedirs(ORIG_DIR, exist_ok=True)

files = sorted(f for f in os.listdir(LOGO_DIR) if f.endswith('.png'))
print(f"Processing {len(files)} logos → {SIZE}×{SIZE}px, {PADDING}px padding")

for fname in files:
    src = os.path.join(LOGO_DIR, fname)
    dst_orig = os.path.join(ORIG_DIR, fname)

    # Back up original if not already backed up
    if not os.path.exists(dst_orig):
        shutil.copy2(src, dst_orig)

    img = Image.open(src).convert('RGBA')

    # Trim transparent/white border to get the actual logo bounds
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    # Scale to fit within (SIZE - 2*PADDING) square, preserving aspect ratio
    max_dim = SIZE - 2 * PADDING
    img.thumbnail((max_dim, max_dim), Image.LANCZOS)

    # Compose onto white canvas
    canvas = Image.new('RGBA', (SIZE, SIZE), (255, 255, 255, 255))
    x = (SIZE - img.width)  // 2
    y = (SIZE - img.height) // 2
    canvas.paste(img, (x, y), mask=img)

    # Save as RGB PNG (white background, no transparency)
    canvas.convert('RGB').save(src, 'PNG', optimize=True)
    print(f"  {fname:60s} {img.width}×{img.height} → {SIZE}×{SIZE}")

print(f"\nDone. Originals preserved in outputs/logos/originals/")
