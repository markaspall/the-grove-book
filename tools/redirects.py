"""After mdbook build: keep old addresses working.

Chapters used to have numbers in their addresses (05-why-an-operating-system.html).
Every old address gets a small page that carries the same share card and moves the
reader to the chapter's address now, keeping any #section."""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages
BASE = "https://markaspall.github.io/the-grove-book/"
OUT = os.path.join(pages.ROOT, "book")

# every numbered address a chapter has had, in either numbering
OLD = """00-before-we-begin 01-a-society-of-sovereigns 02-the-legacy-were-living 03-nature-has-no-bosses
04-what-if-an-organisation-were-alive 05-why-an-operating-system 06-the-spark 06b-one-tuesday 07-purpose
08-the-branch 09-belonging-without-a-seat 10-making-decisions 11-trust 12-work-that-finds-its-way
13-vision-as-hypothesis 14-promises 15-money-and-value 16-into-the-legal-world 17-the-read
18-holding-the-whole 19-the-co-pilot 20-memory 21-birth-division-and-death 22-between-organisations
23-dna-the-network-and-open-source 24-rehearsing-the-future 25-back-to-society
19-a-sense-of-itself 20-the-co-pilot 21-memory 22-birth-division-and-death 23-between-organisations
24-dna-the-network-and-open-source 25-rehearsing-the-future 26-back-to-society""".split()

by_slug = {p["slug"]: p for p in pages.pages()}
e = lambda s: html.escape(s, quote=True)
made = 0
for old in OLD:
    slug = old.split("-", 1)[1]
    p = by_slug.get(slug)
    if not p: print("no page for", old); continue
    new = slug + ".html"
    title = p["title"] if p["eyebrow"] == "A way in" else f"{p['title']} | The Grove, the book"
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{e(title)}</title>
<link rel="canonical" href="{BASE}{new}">
<meta name="robots" content="noindex">
<meta name="description" content="{e(p['description'])}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="The Grove">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(p['description'])}">
<meta property="og:url" content="{BASE}{new}">
<meta property="og:image" content="{BASE}cards/{slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}cards/{slug}.png">
<meta http-equiv="refresh" content="0; url={new}">
<script>location.replace("{new}" + location.hash);</script>
</head><body><p>This chapter has moved to <a href="{new}">{e(p['title'])}</a>.</p></body></html>
"""
    open(os.path.join(OUT, old + ".html"), "w", encoding="utf-8").write(doc)
    made += 1
print("redirects:", made)
