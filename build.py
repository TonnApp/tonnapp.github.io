# Генератор сайту Tonn: python build.py
# Тексти — у langs.py, адреса — SITE нижче. Перегенеровує всі сторінки й sitemap.xml.
import json, pathlib
from langs import L, NAMES
from soon import SOON, BADGE
from features import FEAT, APP_FEATS, TAGS, COMMON, ORDER
import os

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
:root{--g:#2f6b3a;--l:color-mix(in srgb,var(--g) 13%,#fff);--ink:#1d2a20;--m:#5a6a5e;--bg:#fbfdf8;--c:#fff;--line:#dfe6d2}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:linear-gradient(180deg,var(--l) 0,var(--bg) 560px) no-repeat,var(--bg)}
a{color:var(--g)}.w{max-width:960px;margin:0 auto;padding:0 16px}
header{display:flex;flex-wrap:wrap;gap:10px 16px;justify-content:space-between;align-items:center;padding:14px 0}header b{font-size:20px}
.langs{display:flex;flex-wrap:wrap;gap:6px}.langs a{display:block;line-height:0;padding:3px;border:2px solid transparent;border-radius:6px;opacity:.75}
.langs a:hover{opacity:1}.langs a.cur{border-color:var(--g);opacity:1}.langs img{width:26px;height:17px;border-radius:2px;box-shadow:0 0 0 1px rgba(0,0,0,.18)}
@media(max-width:420px){.langs{gap:2px}.langs a{padding:2px}}
.hero.home{text-align:center}.hero{display:grid;gap:28px;align-items:center;padding:24px 0 40px}@media(min-width:760px){.hero{grid-template-columns:1.1fr .9fr}}
h1{font-size:clamp(28px,5vw,42px);line-height:1.15;margin:0 0 14px}h2{font-size:26px;margin:44px 0 16px}
.hero img{width:100%;height:auto;border-radius:20px}.hero img.h{max-width:420px;justify-self:center;box-shadow:0 10px 30px rgba(29,42,32,.15)}
.btn{display:inline-block;background:var(--g);color:#fff;padding:14px 22px;border-radius:12px;font-weight:700;text-decoration:none}
.grid{display:grid;gap:14px}@media(min-width:640px){.grid{grid-template-columns:1fr 1fr}}
.card{background:var(--c);border:1px solid var(--line);border-radius:14px;padding:16px}.card h3{margin:0 0 6px;font-size:18px}.card p{margin:0;color:var(--m)}
.band{background:var(--l);border-radius:16px;padding:20px;margin-top:40px}
details{background:var(--c);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin-bottom:10px}summary{cursor:pointer;font-weight:600}
.shots{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:10px}.shots{padding:6px 4px 16px}.shots img{height:440px;width:auto;border-radius:26px;border:6px solid #1d2a20;box-shadow:0 8px 20px rgba(29,42,32,.22);background:#1d2a20;scroll-snap-align:start;flex:none}
.soon{border-style:dashed;opacity:.8}.badge{display:inline-block;margin-top:10px;padding:2px 10px;border-radius:999px;background:var(--l);color:var(--g);font-size:14px;font-weight:600}
.btn.off{background:var(--line);color:var(--m);cursor:default}.appicon{width:200px;height:200px;border-radius:50%;justify-self:center}.ph{display:flex;align-items:center;justify-content:center;background:#3a8f8f;color:#fff;font-size:40px;font-weight:700}
.app{display:flex;gap:16px;align-items:flex-start}.app .lg{flex:none;line-height:0}.app .lg img,.app .lg .ph{width:72px;height:72px;border-radius:50%;transition:transform .15s}.app .lg img{background:#f6f8f0;padding:3px;box-shadow:0 0 0 1px var(--line)}.app .lg:hover img,.app .lg:hover .ph{transform:scale(1.07)}.app h3 a{color:inherit;text-decoration:none}.app h3 a:hover{text-decoration:underline}.btn.sm{padding:8px 16px;font-size:15px;border-radius:10px}
.side{display:none;position:fixed;bottom:0;width:auto;pointer-events:none;z-index:0}.side.l{height:540px;left:calc(50% - 480px - 215px)}.side.r{height:590px;left:calc(50% + 480px + 40px)}
@media(min-width:1500px){.side{display:block}.duo{display:none}.hero.home{grid-template-columns:1fr}.hero.home h1,.hero.home p{max-width:640px;margin-left:auto;margin-right:auto}}
footer{margin:48px 0 32px;color:var(--m);font-size:15px}footer a{margin-right:14px}
"""


def head(lang, title, desc, canon, alts, extra="", image=None):
    image = image or f"{SITE}/img/hero.jpg"
    hl = "".join(f'<link rel="alternate" hreflang="{k}" href="{v}">' for k, v in alts)
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">{hl}
<meta property="og:type" content="website"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{SITE}/favicon.png"><link rel="apple-touch-icon" href="{SITE}/img/apple-touch-icon.png">
<meta name="theme-color" content="#2f6b3a"><meta name="color-scheme" content="light">
<meta name="google-site-verification" content="q_HQcKnOih3g3LKpe_9UcSt0CxUO9D2H3V_Xl3kqjgw" />
<style>{CSS}</style>{extra}</head><body><div class="w">"""


ACCENT = {"tonnyog": "#2f6b3a", "tonnaim": "#b04a8c", "tonnfit": "#d96a00", "tonnpower": "#566a8e", "tonnstretch": "#7c6fb0",
          "tonnworkout": "#00833a", "tonnprosport": "#3d3d3d", "tonncalm": "#3a8f8f"}

def accent(slug):
    return f"<style>:root{{--g:{ACCENT[slug]}}}</style>"


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
    h = head(lang, d["title"], d["desc"], canon, alts_for(urlfn), ld + accent(slug) + f'<meta name="keywords" content="{d["kw"]}">')
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
    def logo(slug, name):
        if (ROOT / "img" / "apps" / f"{slug}.png").exists():
            im = f'<img src="{SITE}/img/apps/{slug}.png" width="72" height="72" alt="{name}" loading="lazy">'
        else:
            im = f'<span class="ph" role="img" aria-label="{name}" style="font-size:18px">Calm</span>'
        return f'<a class="lg" href="{url_app(lang, slug)}" title="{name}">{im}</a>'
    def card(slug, name, text, extra, soon):
        return f'<div class="card app{" soon" if soon else ""}">{logo(slug, name)}<div><h3><a href="{url_app(lang, slug)}">{name}</a></h3><p>{text}</p>{extra}</div></div>'
    cards = "".join(card(s, n, d["card"], f'<p style="margin-top:10px"><a class="btn sm" href="{pl}" rel="noopener">Google Play</a></p>', False) for s, n, pl in APPS)
    cards += "".join(card(n.lower(), n, tx[lang], f'<span class="badge">{BADGE[lang]}</span>', True) for n, tx in SOON)
    return head(lang, d["home_title"], d["home_desc"], urlfn(lang), alts_for(urlfn), ld) + \
        f'<header><b>Tonn</b>{switcher(lang, urlfn)}</header><main><section class="hero home"><div><h1>{d["home_h1"]}</h1><p style="font-size:19px">{d["home_lead"]}</p></div><img src="{SITE}/img/hero-duo.jpg" width="900" height="760" alt="Tonn fitness characters" fetchpriority="high" class="h duo"></section><div class="grid">{cards}</div></main><img class="side l" src="{SITE}/img/side-woman.webp" alt="" aria-hidden="true"><img class="side r" src="{SITE}/img/side-man.webp" alt="" aria-hidden="true"><footer><p>© TonnProSport</p></footer></div></body></html>'


def soon_page(lang, name, texts):
    d = L[lang]
    i = ORDER.index(lang)
    slug = name.lower()
    urlfn = lambda c: url_app(c, slug)
    tag = TAGS[slug][i]
    lead = texts[lang]
    fill = lambda k: COMMON[k][i].replace("{n}", name)
    title = f"{name} – {tag}"
    desc = f"{lead} {fill('devnote')}"
    icon = f"{SITE}/img/apps/{slug}.png"
    has_icon = os.path.exists(ROOT / "img" / "apps" / f"{slug}.png")
    feats = []
    for k in APP_FEATS[slug]:
        feats.append(d["feats"][6] if k == "offline" else d["feats"][7] if k == "langs" else tuple(FEAT[k][i].split("|", 1)))
    cards = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in feats)
    faq = [(fill("q1"), fill("a1")), (fill("q2"), fill("a2")), (fill("q3"), fill("a3"))]
    ld = f'<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang, "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}, ensure_ascii=False)}</script>'
    h = head(lang, title, desc, urlfn(lang), alts_for(urlfn), ld + accent(slug), icon if has_icon else None)
    pic = f'<img src="{icon}" width="200" height="200" alt="{name}" class="appicon">' if has_icon else f'<div class="appicon ph" role="img" aria-label="{name}">Calm</div>'
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    return h + f"""
<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {name}</b>{switcher(lang, urlfn)}</header>
<main><section class="hero"><div><h1>{name} — {tag}</h1><p>{lead}</p>
<p><span class="btn off" aria-disabled="true">{BADGE[lang]}</span></p></div>{pic}</section>
<div class="grid">{cards}</div>
<div class="band"><h2 style="margin-top:0">{fill('band_h')}</h2><p>{fill('band_t')}</p><p><span class="btn off" aria-disabled="true">{BADGE[lang]}</span></p></div>
<h2>{d['faq_h']}</h2>{faqs}</main>
<footer><a href="{url_home(lang)}">{d['all']}</a><a href="{SITE}/{slug}/privacy-policy.html">{d['priv']}</a><a href="{SITE}/{slug}/terms-of-use.html">{d['terms']}</a><p>© TonnProSport · {fill('foot')}</p></footer>
</div></body></html>"""


def write(rel, text):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


write("404.html", head("en", "Tonn", "Page not found", SITE + "/", []).replace("<head>", '<head><meta name="robots" content="noindex">') + f'<h1>404</h1><p><a href="{SITE}/">Tonn</a></p></div></body></html>')
for lang in LANGS:
    write(f"{pre(lang)}index.html", home_page(lang))
    for slug, name, play in APPS:
        write(f"{pre(lang)}{slug}/index.html", app_page(lang, slug, name, play))
    for name, texts in SOON:
        write(f"{pre(lang)}{name.lower()}/index.html", soon_page(lang, name, texts))


def sm_entry(urlfn):
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{u}"/>' for c, u in alts_for(urlfn))
    return "".join(f"<url><loc>{urlfn(c)}</loc>{alts}</url>\n" for c in LANGS)

slugs = [s for s, _, _ in APPS] + [n.lower() for n, _ in SOON]
body = sm_entry(url_home) + "".join(sm_entry(lambda c, s=s: url_app(c, s)) for s in slugs)
body += "".join(f"<url><loc>{SITE}/{s}/{f}</loc></url>\n" for s in slugs for f in ("privacy-policy.html", "terms-of-use.html"))
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
write(".nojekyll", "")
print("OK", len(LANGS) * (1 + len(slugs)), "pages")
