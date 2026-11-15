# Генератор сайту Tonn: python build.py
# Тексти — у langs.py, адреса — SITE нижче. Перегенеровує всі сторінки й sitemap.xml.
import json, pathlib
from langs import L, NAMES

SITE = "https://tonnapp.github.io"
PLAY = "https://play.google.com/store/apps/details?id=com.TonnProSport.Tonn_Yog"
ROOT = pathlib.Path(__file__).parent
LANGS = list(NAMES)                      # en, uk, es, de, fr, pt, pl, tr, it
APPS = [("tonnyog", "TonnYog", PLAY)]    # сюди додаються інші додатки серії


def pre(lang):                           # англійська — у корені, решта — у /<мова>/
    return "" if lang == "en" else lang + "/"

def url_home(lang): return f"{SITE}/{pre(lang)}"
def url_app(lang, slug): return f"{SITE}/{pre(lang)}{slug}/"

CSS = """
:root{--g:#2f6b3a;--l:#E7EFD3;--ink:#1d2a20;--m:#5a6a5e;--bg:#fbfcf7;--c:#fff;--line:#dfe6d2}
@media(prefers-color-scheme:dark){:root{--g:#8fd19a;--l:#1f2a21;--ink:#eaf1e6;--m:#a3b3a6;--bg:#141a15;--c:#1a231c;--line:#2b382d}}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:var(--g)}.w{max-width:960px;margin:0 auto;padding:0 16px}
header{display:flex;flex-wrap:wrap;gap:10px 16px;justify-content:space-between;align-items:center;padding:14px 0}header b{font-size:20px}
.langs{display:flex;flex-wrap:wrap;gap:6px}.langs a{display:block;line-height:0;padding:3px;border:2px solid transparent;border-radius:6px;opacity:.75}
.langs a:hover{opacity:1}.langs a.cur{border-color:var(--g);opacity:1}.langs img{width:26px;height:17px;border-radius:2px;box-shadow:0 0 0 1px rgba(0,0,0,.18)}
@media(max-width:420px){.langs{gap:2px}.langs a{padding:2px}}
.hero{display:grid;gap:28px;align-items:center;padding:24px 0 40px}@media(min-width:760px){.hero{grid-template-columns:1.1fr .9fr}}
h1{font-size:clamp(28px,5vw,42px);line-height:1.15;margin:0 0 14px}h2{font-size:26px;margin:44px 0 16px}
.hero img{width:100%;height:auto;border-radius:20px}.hero img.h{max-width:420px;justify-self:center}
.btn{display:inline-block;background:var(--g);color:#fff;padding:14px 22px;border-radius:12px;font-weight:700;text-decoration:none}
@media(prefers-color-scheme:dark){.btn{color:#10200f}}
.grid{display:grid;gap:14px}@media(min-width:640px){.grid{grid-template-columns:1fr 1fr}}
.card{background:var(--c);border:1px solid var(--line);border-radius:14px;padding:16px}.card h3{margin:0 0 6px;font-size:18px}.card p{margin:0;color:var(--m)}
.band{background:var(--l);border-radius:16px;padding:20px;margin-top:40px}
details{background:var(--c);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-bottom:10px}summary{cursor:pointer;font-weight:600}
.shots{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:10px}.shots img{height:440px;width:auto;border-radius:14px;border:1px solid var(--line);scroll-snap-align:start;flex:none}
footer{margin:48px 0 32px;color:var(--m);font-size:15px}footer a{margin-right:14px}
"""


def head(lang, title, desc, canon, alts, extra=""):
    hl = "".join(f'<link rel="alternate" hreflang="{k}" href="{v}">' for k, v in alts)
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">{hl}
<meta property="og:type" content="website"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/img/hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{SITE}/favicon.png"><link rel="apple-touch-icon" href="{SITE}/img/apple-touch-icon.png">
<meta name="theme-color" content="#2f6b3a">
<style>{CSS}</style>{extra}</head><body><div class="w">"""


def switcher(lang, urlfn):
    items = []
    for c in LANGS:
        cur = ' class="cur" aria-current="true"' if c == lang else ""
        items.append(f'<a href="{urlfn(c)}" hreflang="{c}" lang="{c}" title="{NAMES[c]}"{cur}><img src="{SITE}/img/flags/{c}.svg" width="26" height="17" alt="{NAMES[c]}"></a>')
    return '<nav class="langs" aria-label="Language">' + "".join(items) + "</nav>"


def alts_for(urlfn):
    a = [(c, urlfn(c)) for c in LANGS]
    return a + [("x-default", urlfn("en"))]


def app_page(lang, slug, name, play):
    d = L[lang]
    urlfn = lambda c: url_app(c, slug)
    canon = urlfn(lang)
    app = {"@context": "https://schema.org", "@type": "MobileApplication", "name": name,
           "operatingSystem": "ANDROID", "applicationCategory": "HealthApplication",
           "description": d["desc"], "url": canon, "downloadUrl": play, "image": f"{SITE}/img/icon-512.png",
           "inLanguage": lang, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
           "author": {"@type": "Organization", "name": "TonnProSport"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (app, faq))
    h = head(lang, d["title"], d["desc"], canon, alts_for(urlfn), ld + f'<meta name="keywords" content="{d["kw"]}">')
    feats = "".join(f'<div class="card"><h3>{t}</h3><p>{p}</p></div>' for t, p in d["feats"])
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in d["faq"])
    shots = "".join(f'<img src="{SITE}/img/shots/{lang}-{i}.jpg" width="203" height="440" loading="lazy" alt="{a}">' for i, a in enumerate(d["alts"], 1))
    return h + f"""
<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {name}</b>{switcher(lang, urlfn)}</header>
<main><section class="hero"><div><h1>{d['h1']}</h1><p>{d['lead']}</p>
<p><a class="btn" href="{play}" rel="noopener">{d['cta']}</a></p></div>
<img src="{SITE}/img/hero.jpg" width="760" height="760" alt="{name} yoga instructor character" fetchpriority="high" class="h"></section>
<h2>{d['shots_h']}</h2><div class="shots">{shots}</div>
<h2>{d['feat_h']}</h2><div class="grid">{feats}</div>
<div class="band"><h2 style="margin-top:0">{d['lvl_h']}</h2><p>{d['lvl']}</p><p><a class="btn" href="{play}" rel="noopener">{d['cta']}</a></p></div>
<h2>{d['faq_h']}</h2>{faqs}</main>
<footer><a href="{url_home(lang)}">{d['all']}</a><a href="{SITE}/{slug}/privacy-policy.html">{d['priv']}</a><a href="{SITE}/{slug}/terms-of-use.html">{d['terms']}</a><a href="{play}" rel="noopener">Google Play</a><p>© TonnProSport · {d['foot']}</p></footer>
</div></body></html>"""


def home_page(lang):
    d = L[lang]
    urlfn = url_home
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "TonnProSport", "url": f"{SITE}/", "logo": f"{SITE}/img/icon-512.png"}
    ld = f'<script type="application/ld+json">{json.dumps(org)}</script>'
    cards = "".join(f'<div class="card"><h3>{n}</h3><p>{d["card"]}</p><p style="margin-top:12px"><a href="{url_app(lang, s)}">{d["more"]}</a> · <a href="{pl}" rel="noopener">Google Play</a></p></div>' for s, n, pl in APPS)
    return head(lang, d["home_title"], d["home_desc"], urlfn(lang), alts_for(urlfn), ld) + \
        f'<header><b>Tonn</b>{switcher(lang, urlfn)}</header><main><h1>{d["home_h1"]}</h1><p>{d["home_lead"]}</p><div class="grid">{cards}</div></main><footer><p>© TonnProSport</p></footer></div></body></html>'


def write(rel, text):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


write("404.html", head("en", "Tonn", "Page not found", SITE + "/", []).replace("<head>", '<head><meta name="robots" content="noindex">') + f'<h1>404</h1><p><a href="{SITE}/">Tonn</a></p></div></body></html>')
for lang in LANGS:
    write(f"{pre(lang)}index.html", home_page(lang))
    for slug, name, play in APPS:
        write(f"{pre(lang)}{slug}/index.html", app_page(lang, slug, name, play))


def sm_entry(urlfn):
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{u}"/>' for c, u in alts_for(urlfn))
    return "".join(f"<url><loc>{urlfn(c)}</loc>{alts}</url>\n" for c in LANGS)

body = sm_entry(url_home) + "".join(sm_entry(lambda c, s=s: url_app(c, s)) for s, _, _ in APPS)
body += "".join(f"<url><loc>{SITE}/{s}/{f}</loc></url>\n" for s, _, _ in APPS for f in ("privacy-policy.html", "terms-of-use.html"))
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
write(".nojekyll", "")
print("OK", len(LANGS) * (1 + len(APPS)), "pages")
