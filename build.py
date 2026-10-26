#!/usr/bin/env python3
"""Build the RemBase Handbook: chapters/*.md -> *.html (static, no server).

Needs pandoc. Run:  python3 build.py
Each chapter starts with a small front block:
    ---
    title: ...
    subtitle: ...
    slug: file name without .html (index = start page)
    order: number
    ---
"""
import datetime, glob, html, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))


def read_chapter(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    meta = dict(line.split(':', 1) for line in m.group(1).splitlines() if ':' in line)
    meta = {k.strip(): v.strip().strip('"') for k, v in meta.items()}
    meta['order'] = int(meta['order'])
    meta['body_md'] = text[m.end():]
    return meta


def md_to_html(md):
    out = subprocess.run(['pandoc', '-f', 'markdown+fenced_divs+pipe_tables', '-t', 'html5'],
                         input=md, capture_output=True, text=True, check=True).stdout
    # tap an image to open it full size (pinch to zoom on a phone)
    out = re.sub(r'<img src="([^"]+)"([^>]*)>', r'<a class="zoom" href="\1"><img src="\1" loading="lazy"\2></a>', out)
    # tables scroll sideways on a phone
    out = out.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    return out


def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', ' ', s)).replace('\n', ' ')


def sections(slug, title, body):
    """Search index entries: one per h2 section."""
    parts = re.split(r'(<h2 id="[^"]*">.*?</h2>)', body)
    items, head, anchor = [], title, ''
    for p in parts:
        h = re.match(r'<h2 id="([^"]*)">(.*?)</h2>', p)
        if h:
            anchor, head = h.group(1), strip_tags(h.group(2)).strip()
            continue
        txt = re.sub(r'\s+', ' ', strip_tags(p)).strip()
        if txt:
            items.append({'page': slug + '.html', 'chapter': title, 'section': head,
                          'anchor': anchor, 'text': txt[:600]})
    return items


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – RemBase Handbook</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📦</text></svg>">
</head>
<body>
<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="index.html"><span class="dot"></span>RemBase Handbook</a>
    <a class="toc-link" href="index.html#chapters">All chapters</a>
  </div>
</header>
<div class="banner"><div class="wrap">Until December 1: real work in <b>Fishbowl</b>. RemBase is for practice with <b>TEST</b> items.</div></div>
<main class="wrap">
  <h1>{title}</h1>
  <p class="lede">{subtitle}</p>
  {extra}
  <article>
{body}
  </article>
  {cards}
  <nav class="pager">{prev}{next}</nav>
</main>
<footer class="wrap foot">RemBase Handbook · Remington Supply · updated {date} · Private data in pictures is blacked out.</footer>
<script src="assets/search-index.js"></script>
<script src="assets/search.js"></script>
</body>
</html>
"""

SEARCH = """<div class="search-wrap">
  <input id="q" class="search" type="search" placeholder="Search the handbook… (try: receive, bin, labels)" autocomplete="off">
  <div id="results" class="results" hidden></div>
</div>"""


def main():
    chapters = sorted((read_chapter(p) for p in glob.glob(os.path.join(HERE, 'chapters', '*.md'))), key=lambda c: c['order'])
    for c in chapters:
        c['body'] = md_to_html(c['body_md'])
    index_items = []
    for c in chapters:
        index_items += sections(c['slug'], c['title'], c['body'])
    os.makedirs(os.path.join(HERE, 'assets'), exist_ok=True)
    with open(os.path.join(HERE, 'assets', 'search-index.js'), 'w', encoding='utf-8') as f:
        f.write('window.RB_INDEX = ' + json.dumps(index_items, ensure_ascii=False) + ';\n')

    cards = '<section id="chapters"><h2>All chapters</h2><div class="cards">' + ''.join(
        f'<a class="card" href="{c["slug"]}.html"><span class="num">{c["order"]}</span>'
        f'<span class="ct">{html.escape(c["title"])}</span><span class="cs">{html.escape(c["subtitle"])}</span></a>'
        for c in chapters if c['slug'] != 'index') + '</div></section>'

    today = datetime.date.today().strftime('%B %-d, %Y')
    for i, c in enumerate(chapters):
        prev = chapters[i - 1] if i > 0 else None
        nxt = chapters[i + 1] if i + 1 < len(chapters) else None
        page = PAGE.format(
            title=html.escape(c['title']), subtitle=html.escape(c['subtitle']), body=c['body'], date=today,
            extra=SEARCH if c['slug'] == 'index' else '',
            cards=cards if c['slug'] == 'index' else '',
            prev=f'<a class="prev" href="{prev["slug"]}.html">← {html.escape(prev["title"])}</a>' if prev else '<span></span>',
            next=f'<a class="next" href="{nxt["slug"]}.html">{html.escape(nxt["title"])} →</a>' if nxt else '<span></span>')
        with open(os.path.join(HERE, c['slug'] + '.html'), 'w', encoding='utf-8') as f:
            f.write(page)
        print('built', c['slug'] + '.html')

    # every image a page uses must exist; every image in img/ should be used
    used = set()
    for c in chapters:
        used |= set(re.findall(r'src="(img/[^"]+)"', c['body']))
    missing = [u for u in used if not os.path.exists(os.path.join(HERE, u))]
    unused = [f'img/{f}' for f in os.listdir(os.path.join(HERE, 'img')) if f'img/{f}' not in used]
    print('images used:', len(used), '| missing:', missing or 'none', '| unused:', unused or 'none')
    if missing:
        raise SystemExit(1)

    # this repo is public: no system ids (base/table/field/record/page) may appear in any text file
    id_rx = re.compile(r'\b(?:app|tbl|fld|rec|viw|wfl|wfd|pag)[A-Za-z0-9]{14}\b')
    leaks = []
    for root, _, files in os.walk(HERE):
        if '.git' in root:
            continue
        for fn in files:
            if fn.endswith(('.html', '.md', '.js', '.css', '.py', '.json', '.txt')) and fn != 'review.html':
                with open(os.path.join(root, fn), encoding='utf-8', errors='ignore') as fh:
                    leaks += [f'{fn}: {m}' for m in id_rx.findall(fh.read())]
    if leaks:
        print('ID LEAK in public files:', leaks[:5])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
