"""
Normalize case-study screenshots to the sizes work-calvary-road.html expects.

You capture roughly; this strips any browser/DevTools chrome, crops to the
precise dimensions, and writes the six files straight into img/work.
Top-anchored crop, so the top of the page is always kept (that is where the
story is).

USAGE
  1. Drop your captures in a folder. The filename just has to say which shot it
     is - any of these spellings work:
        page:     home | beliefs
        state:    before | old | legacy      /  after | new
        device:   mobile | phone             (absent = desktop)
     e.g. "calvary desktop old.png", "before-home-mobile.png", "home new.png"
  2. python normalize-shots.py <folder-with-captures>
  3. Review img/work, then commit.

Requires Pillow.
"""
import sys, os, glob
from PIL import Image

REPO = r"C:\Git_Repos\alexharper-website-repo\img\work"

# (out_name, (w, h), page_keys, state_keys, is_mobile)
TARGETS = [
    ("calvary-before-home.jpg",        (1280, 800), ("home", "desktop"), ("before", "old", "legacy"), False),
    ("calvary-after-home.jpg",         (1280, 800), ("home", "desktop"), ("after", "new"),            False),
    ("calvary-before-home-mobile.jpg", (390, 844),  ("home", "desktop"), ("before", "old", "legacy"), True),
    ("calvary-after-home-mobile.jpg",  (390, 844),  ("home", "desktop"), ("after", "new"),            True),
    ("calvary-before-beliefs.jpg",     (1280, 800), ("beliefs",),        ("before", "old", "legacy"), False),
    ("calvary-after-beliefs.jpg",      (1280, 800), ("beliefs",),        ("after", "new"),            False),
]

MOBILE_WORDS = ("mobile", "phone")


def norm(name):
    return os.path.basename(name).lower().replace("_", "-").replace(".", " ")


def matches(fname, page_keys, state_keys, is_mobile):
    n = norm(fname)
    if any(w in n for w in MOBILE_WORDS) != is_mobile:
        return False
    if not any(k in n for k in state_keys):
        return False
    # "beliefs" must be explicit, so a desktop home shot cannot claim the beliefs slot
    if "beliefs" in n:
        return "beliefs" in page_keys
    return "beliefs" not in page_keys


def trim_chrome(im, max_frac=0.45, bg_frac=0.80):
    """Strip a neutral, light surround (DevTools device-mode grey, window chrome).

    A pixel counts as chrome if it is light, near-neutral, and not pure white:
    that describes the greys Chrome paints around an emulated device, while a
    real page's own white (255) and all its content fail the test. A row or
    column is chrome when bg_frac of it is chrome pixels, which keeps one stray
    toolbar button, or a band of near-white DevTools panel, from anchoring an
    entire edge. A real page column runs about 0.10 on this measure, so 0.80
    leaves a wide margin. Never trims more than max_frac of a dimension, so a
    page with genuinely pale edges cannot be eaten.
    """
    px = im.load()
    W, H = im.size

    def is_bg(x, y):
        r, g, b = px[x, y]
        # >=200 rather than a tighter figure: Chrome draws a faint full-height
        # separator line (~221) down the edge of the emulated device, and a
        # stricter test lets that one line anchor the whole edge.
        return min(r, g, b) >= 200 and (max(r, g, b) - min(r, g, b)) <= 18 and max(r, g, b) <= 253

    def row_is_chrome(y):
        xs = range(0, W, 2)
        n = sum(1 for x in xs if is_bg(x, y))
        return n >= bg_frac * len(list(xs))

    def col_is_chrome(x):
        ys = range(0, H, 2)
        n = sum(1 for y in ys if is_bg(x, y))
        return n >= bg_frac * len(list(ys))

    top, bottom = 0, H - 1
    left, right = 0, W - 1
    ylim, xlim = int(H * max_frac), int(W * max_frac)
    while top < ylim and row_is_chrome(top):
        top += 1
    while bottom > H - 1 - ylim and row_is_chrome(bottom):
        bottom -= 1
    while left < xlim and col_is_chrome(left):
        left += 1
    while right > W - 1 - xlim and col_is_chrome(right):
        right -= 1

    if right - left < 40 or bottom - top < 40:
        return im, None
    box = (left, top, right + 1, bottom + 1)
    if box == (0, 0, W, H):
        return im, None
    out = im.crop(box)

    # Second pass, columns only. Device-mode grey often sits next to a near-white
    # DevTools panel, which the pure-white guard above deliberately protects, so
    # a wide band can survive pass one. Dropping that guard is safe sideways: a
    # correctly captured page fills the full width, so light neutral columns at
    # the left or right edge can only be emulator surround. It is NOT safe
    # vertically, where a page's own white would get eaten from the bottom up.
    px2 = out.load()
    W2, H2 = out.size

    def bg2(x, y):
        r, g, b = px2[x, y]
        return min(r, g, b) >= 200 and (max(r, g, b) - min(r, g, b)) <= 18

    def col_is_chrome2(x):
        ys = range(0, H2, 2)
        return sum(1 for y in ys if bg2(x, y)) >= bg_frac * len(list(ys))

    l2, r2 = 0, W2 - 1
    xlim2 = int(W2 * max_frac)
    while l2 < xlim2 and col_is_chrome2(l2):
        l2 += 1
    while r2 > W2 - 1 - xlim2 and col_is_chrome2(r2):
        r2 -= 1
    if (l2, r2) != (0, W2 - 1) and r2 - l2 >= 40:
        out = out.crop((l2, 0, r2 + 1, H2))
        box = (box[0] + l2, box[1], box[0] + r2 + 1, box[3])
    return out, box


def fit_top(im, tw, th):
    """Scale to cover the target, then crop from the top (centred horizontally)."""
    r = max(tw / im.width, th / im.height)
    im = im.resize((max(1, round(im.width * r)), max(1, round(im.height * r))), Image.LANCZOS)
    x = (im.width - tw) // 2
    return im.crop((x, 0, x + tw, th))


def main(src_dir):
    if not os.path.isdir(src_dir):
        sys.exit(f"Not a folder: {src_dir}")
    if not os.path.isdir(REPO):
        sys.exit(f"Repo image folder missing: {REPO}")

    files = [f for f in glob.glob(os.path.join(src_dir, "*"))
             if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
    if not files:
        sys.exit("No images found in that folder.")

    used, done = set(), 0
    for out_name, (tw, th), page_keys, state_keys, is_mobile in TARGETS:
        match = next((f for f in files if f not in used
                      and matches(f, page_keys, state_keys, is_mobile)), None)
        if not match:
            print(f"  ..  nothing matched {out_name}  (leaving the existing file alone)")
            continue
        used.add(match)
        im = Image.open(match).convert("RGB")
        raw = im.size
        im, box = trim_chrome(im)
        out = fit_top(im, tw, th)
        dest = os.path.join(REPO, out_name)
        out.save(dest, "JPEG", quality=82, optimize=True)
        kb = round(os.path.getsize(dest) / 1024)
        trim = f"chrome trimmed to {im.width}x{im.height}" if box else "no chrome found"
        print(f"  OK  {os.path.basename(match)} {raw[0]}x{raw[1]} ({trim})")
        print(f"      -> {out_name}  {tw}x{th}  {kb}KB")
        done += 1

    print(f"\n{done} of {len(TARGETS)} images written to {REPO}")
    leftover = [os.path.basename(f) for f in files if f not in used]
    if leftover:
        print("Unused captures (filename did not say which shot it is):", ", ".join(leftover))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
