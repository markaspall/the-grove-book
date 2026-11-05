"""Shared: read SUMMARY.md and each page's card line, description and title."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
TAGLINE = "The first network of organisations running on an operating system for organisations without a boss."

def pages():
    out, part = [], ""
    for line in open(os.path.join(SRC, "SUMMARY.md"), encoding="utf-8"):
        m = re.match(r"^# (?!Summary\b)(.+)$", line.strip())
        if m: part = m.group(1); continue
        if line.strip() == "---": part = "Appendix"; continue
        m = re.match(r"^\s*-?\s*\[(.+?)\]\((.+?)\.md\)", line)
        if not m: continue
        title, slug = m.group(1), m.group(2)
        text = open(os.path.join(SRC, slug + ".md"), encoding="utf-8").read()
        card = re.search(r"<!-- card: (.+?) -->", text)
        desc = re.search(r"<!-- description: (.+?) -->", text)
        num = re.match(r"^(\d+)\. (.+)$", title)
        if num:
            eyebrow, heading = "Chapter " + num.group(1), num.group(2)
        elif slug.startswith("ways-in"):
            eyebrow, heading = "A way in", title
        elif title.startswith("Interlude. "):
            eyebrow, heading = "Interlude", title[len("Interlude. "):]
        elif part == "Appendix":
            eyebrow, heading = "Appendix", title
        else:
            eyebrow, heading = "The book", title
        out.append(dict(slug=slug, title=title, eyebrow=eyebrow, heading=heading,
                        card=card.group(1) if card else TAGLINE,
                        description=desc.group(1) if desc else auto_description(text)))
    return out

def auto_description(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    parts = [p.strip() for p in re.split(r"\n\s*\n", text)]
    rules, got = 0, ""
    for p in parts:
        if p == "---": rules += 1; continue
        if rules >= 2 and p and not p.startswith(("#", "-", ">", "*", "|", "<")):
            p = re.sub(r"\[\^\d+\]|[*_`]", "", p)
            p = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", p)
            got = (got + " " + p).strip()
            if len(got) >= 140: break
        elif got: break
    if not got: return TAGLINE
    return got if len(got) <= 240 else got[:237].rsplit(" ", 1)[0] + "…"
