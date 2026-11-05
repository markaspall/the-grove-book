"""After mdbook build: put share tags (title, description, card image) into each built page."""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages
BASE = "https://markaspall.github.io/the-grove-book/"
OUT = os.path.join(pages.ROOT, "book")

def tags(title, desc, url, image):
    e = lambda s: html.escape(s, quote=True)
    return f"""
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="The Grove">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{image}">
"""

def inject(file, block):
    p = os.path.join(OUT, file)
    if not os.path.exists(p): return
    s = open(p, encoding="utf-8").read()
    s = s.replace('<meta name="description" content="', '<meta name="x-old-description" content="', 1)
    s = s.replace("</head>", block + "</head>", 1)
    open(p, "w", encoding="utf-8").write(s)

ps = pages.pages()
for p in ps:
    title = p["title"] if p["eyebrow"] == "A way in" else f"{p['title']} | The Grove, the book"
    inject(p["slug"] + ".html", tags(title, p["description"], BASE + p["slug"] + ".html", BASE + "cards/" + p["slug"] + ".png"))
first = ps[0]
inject("index.html", tags("The Grove, the book", first["description"], BASE, BASE + "cards/book.png"))
print("share tags:", len(ps) + 1)
