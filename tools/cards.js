// Renders one 1200x630 share card per page into src/cards/<slug>.png, and src/cards/book.png.
// Run locally when titles or card lines change:  node tools/cards.js FONTS_DIR
// FONTS_DIR holds the @fontsource fraunces and nunito-sans packages (npm i @fontsource/fraunces @fontsource/nunito-sans).
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..');
const fonts = process.argv[2];
const f = (pkg, file) => 'data:font/woff2;base64,' + fs.readFileSync(path.join(fonts, 'node_modules/@fontsource', pkg, 'files', file)).toString('base64');
const faces = `
@font-face{font-family:Fraunces;font-weight:800;src:url(${f('fraunces','fraunces-latin-800-normal.woff2')})}
@font-face{font-family:Fraunces;font-weight:400;font-style:italic;src:url(${f('fraunces','fraunces-latin-400-italic.woff2')})}
@font-face{font-family:Nunito;font-weight:800;src:url(${f('nunito-sans','nunito-sans-latin-800-normal.woff2')})}
@font-face{font-family:Nunito;font-weight:700;src:url(${f('nunito-sans','nunito-sans-latin-700-normal.woff2')})}`;
const pages = JSON.parse(execFileSync('python3', ['-c', 'import json,sys;sys.path.insert(0,"tools");import pages;print(json.dumps(pages.pages()))'], { cwd: root }));
pages.push({ slug: 'book', eyebrow: 'The book', heading: 'The Grove', card: 'The first network of organisations running on an operating system for organisations without a boss. Written in public, while it’s being built.' });
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
const html = p => `<!doctype html><html><head><meta charset="utf-8"><style>${faces}
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;background:#f4efe4;position:relative;overflow:hidden;font-family:Nunito}
.band{position:absolute;right:0;top:0;bottom:0;width:300px;background:#173328}
.leaf{position:absolute;right:62px;top:150px;width:176px;height:330px}
.box{position:absolute;left:84px;top:78px;width:760px;height:474px;display:flex;flex-direction:column}
.eye{font-weight:800;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:#3f6b53;display:flex;align-items:center;gap:14px}
.eye i{display:inline-block;width:46px;height:3px;background:#d98a2b}
h1{font-family:Fraunces;font-weight:800;color:#173328;letter-spacing:-.02em;line-height:1.04;margin-top:30px}
p{font-family:Fraunces;font-style:italic;font-weight:400;color:#5f5648;line-height:1.35;margin-top:26px}
.foot{margin-top:auto;font-weight:700;font-size:21px;color:#857b6a}
.foot b{color:#173328;font-weight:800}
</style></head><body>
<div class="band"></div>
<svg class="leaf" viewBox="0 0 22 26"><path d="M11 1C6 6 3 11 3 16a8 8 0 0 0 16 0c0-5-3-10-8-15Z" fill="#3f6b53"/><path d="M11 7v15" stroke="#f2c98a" stroke-width="1.2" fill="none"/></svg>
<div class="box"><div class="eye"><i></i>The Grove &middot; ${esc(p.eyebrow)}</div>
<h1 id="h">${esc(p.heading)}</h1><p id="p">${esc(p.card)}</p>
<div class="foot"><b>The Grove</b> &middot; the book, written in public</div></div>
</body></html>`;
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
  fs.mkdirSync(path.join(root, 'src/cards'), { recursive: true });
  for (const p of pages) {
    await pg.setContent(html(p));
    await pg.evaluate(() => document.fonts.ready);
    // fit: shrink the title, then the line beneath, until the box holds both
    await pg.evaluate(() => {
      const h = document.getElementById('h'), q = document.getElementById('p'), box = document.querySelector('.box');
      let hs = 78, ps = 32; h.style.fontSize = hs + 'px'; q.style.fontSize = ps + 'px';
      const fits = () => box.scrollHeight <= box.clientHeight && h.scrollWidth <= h.clientWidth;
      while (!fits() && hs > 50) { hs -= 2; h.style.fontSize = hs + 'px'; }
      while (!fits() && ps > 24) { ps -= 1; q.style.fontSize = ps + 'px'; }
    });
    await pg.screenshot({ path: path.join(root, 'src/cards', p.slug + '.png') });
  }
  await b.close();
  console.log('cards:', pages.length);
})();
