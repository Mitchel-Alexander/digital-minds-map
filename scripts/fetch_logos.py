"""
fetch_logos.py
--------------
Systematically fetches logos for all corpus organisations.

Strategy (in order):
1. Clearbit Logo API  — best for commercial/nonprofit orgs
2. og:image meta tag  — scraped from org homepage; good for academic sites
3. Favicon fallback   — last resort; low resolution but better than nothing

Outputs:
  outputs/logos/{slug}.png   — downloaded logo
  outputs/logos/logo_report.csv  — per-org result log

Usage:
  python scripts/fetch_logos.py

Options:
  --status included     only fetch for included orgs (default: all non-excluded)
  --delay 1.0           seconds between requests (default: 1.0)
  --force               re-download even if logo already exists
"""

import argparse
import csv
import os
import re
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# ── Paths ────────────────────────────────────────────────────────────────────

BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS     = os.path.join(BASE_DIR, "data", "corpus.csv")
LOGOS_DIR  = os.path.join(BASE_DIR, "outputs", "logos")
REPORT     = os.path.join(LOGOS_DIR, "logo_report.csv")

os.makedirs(LOGOS_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(name: str) -> str:
    """Convert org name to a safe filename slug."""
    name = name.lower()
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s_]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name[:80]  # cap length


def extract_domain(url: str) -> str | None:
    """Extract bare domain from a URL."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        # strip www.
        domain = re.sub(r"^www\.", "", domain)
        return domain if domain else None
    except Exception:
        return None


def save_image(response: requests.Response, path: str) -> bool:
    """Save image bytes from response. Returns True if file looks valid."""
    content = response.content
    if len(content) < 100:  # suspiciously small — likely an error page
        return False
    with open(path, "wb") as f:
        f.write(content)
    return True


# ── Fetch strategies ──────────────────────────────────────────────────────────

def try_clearbit(domain: str, path: str) -> bool:
    """Try Clearbit Logo API."""
    url = f"https://logo.clearbit.com/{domain}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200 and "image" in r.headers.get("Content-Type", ""):
            return save_image(r, path)
    except Exception:
        pass
    return False


def try_og_image(homepage: str, path: str) -> bool:
    """Scrape og:image meta tag from homepage."""
    try:
        r = requests.get(homepage, headers=HEADERS, timeout=12)
        if r.status_code != 200:
            return False
        soup = BeautifulSoup(r.text, "html.parser")

        # Try og:image first, then twitter:image
        for prop in ("og:image", "twitter:image", "og:image:secure_url"):
            tag = soup.find("meta", property=prop) or soup.find("meta", attrs={"name": prop})
            if tag and tag.get("content"):
                img_url = tag["content"].strip()
                if not img_url.startswith("http"):
                    # relative URL — resolve against homepage
                    from urllib.parse import urljoin
                    img_url = urljoin(homepage, img_url)
                img_r = requests.get(img_url, headers=HEADERS, timeout=10)
                if img_r.status_code == 200 and "image" in img_r.headers.get("Content-Type", ""):
                    return save_image(img_r, path)
    except Exception:
        pass
    return False


def try_favicon(domain: str, path: str) -> bool:
    """Last resort: Google Favicon API (32px — low quality)."""
    url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            return save_image(r, path)
    except Exception:
        pass
    return False


# ── Main ──────────────────────────────────────────────────────────────────────

def fetch_logos(status_filter: str, delay: float, force: bool):
    results = []

    with open(CORPUS, newline="", encoding="utf-8") as f:
        orgs = list(csv.DictReader(f))

    # Filter by status
    if status_filter == "included":
        orgs = [o for o in orgs if o["status"] == "included"]
    else:
        orgs = [o for o in orgs if o["status"] != "excluded"]

    print(f"Fetching logos for {len(orgs)} organisations...\n")

    for i, org in enumerate(orgs, 1):
        name    = org["org_name"]
        url     = org.get("url", "").strip()
        slug    = slugify(name)
        domain  = extract_domain(url)
        outpath = os.path.join(LOGOS_DIR, f"{slug}.png")

        prefix = f"[{i:02}/{len(orgs)}] {name[:50]}"

        if os.path.exists(outpath) and not force:
            print(f"{prefix} — already exists, skipping")
            results.append({"org_name": name, "slug": slug, "domain": domain,
                            "method": "cached", "status": "ok", "path": outpath})
            continue

        if not domain:
            print(f"{prefix} — no URL, skipping")
            results.append({"org_name": name, "slug": slug, "domain": "",
                            "method": "none", "status": "no_url", "path": ""})
            continue

        method = "none"
        success = False

        # Strategy 1: Clearbit
        if try_clearbit(domain, outpath):
            method, success = "clearbit", True
        else:
            time.sleep(0.3)
            # Strategy 2: og:image
            if url and try_og_image(url, outpath):
                method, success = "og_image", True
            else:
                time.sleep(0.3)
                # Strategy 3: favicon
                if try_favicon(domain, outpath):
                    method, success = "favicon", True

        status_str = "ok" if success else "manual_needed"
        print(f"{prefix} — {method} — {'✓' if success else '✗ manual needed'}")

        results.append({
            "org_name": name,
            "slug":     slug,
            "domain":   domain,
            "method":   method,
            "status":   status_str,
            "path":     outpath if success else "",
        })

        time.sleep(delay)

    # Write report
    with open(REPORT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["org_name", "slug", "domain", "method", "status", "path"])
        writer.writeheader()
        writer.writerows(results)

    # Summary
    ok           = sum(1 for r in results if r["status"] in ("ok", "cached"))
    manual       = sum(1 for r in results if r["status"] == "manual_needed")
    no_url       = sum(1 for r in results if r["status"] == "no_url")
    by_method    = {}
    for r in results:
        by_method[r["method"]] = by_method.get(r["method"], 0) + 1

    print(f"\n── Summary ───────────────────────────────────")
    print(f"  Total processed : {len(results)}")
    print(f"  Found           : {ok}")
    print(f"  Manual needed   : {manual}")
    print(f"  No URL          : {no_url}")
    print(f"  By method       : {by_method}")
    print(f"\nReport saved to: {REPORT}")
    if manual:
        print(f"\nOrgs needing manual logos:")
        for r in results:
            if r["status"] == "manual_needed":
                print(f"  - {r['org_name']}  ({r['domain']})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch org logos for the digital minds field map.")
    parser.add_argument("--status", choices=["included", "all"], default="all",
                        help="Which orgs to fetch logos for (default: all non-excluded)")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Seconds between requests (default: 1.0)")
    parser.add_argument("--force", action="store_true",
                        help="Re-download even if logo already exists")
    args = parser.parse_args()

    fetch_logos(args.status, args.delay, args.force)
