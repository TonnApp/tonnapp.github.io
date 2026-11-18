# Генератор сайту Tonn: python build.py
# Тексти — у langs.py, адреса — SITE нижче. Перегенеровує всі сторінки й sitemap.xml.
import json, pathlib, re
from langs import L, NAMES
from soon import SOON, BADGE
from posts import POSTS, DISCLAIMER
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
.hr{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center}.hr .bl{font-weight:600;text-decoration:none}
.post{max-width:720px;margin:0 auto}.post h1{margin-top:10px}.post h2{font-size:24px;margin:34px 0 12px}.post ul{padding-left:22px}.post li{margin:6px 0}
.post figure{margin:22px 0}.post figure img{width:100%;height:auto;border-radius:14px;display:block}.post figcaption{color:var(--m);font-size:14px;margin-top:6px}
.post figure.phone img{max-width:240px;margin:0 auto;border:6px solid #1d2a20;border-radius:26px}.post figure.phone figcaption{text-align:center}
.meta{color:var(--m);font-size:15px}.crumb{font-size:15px;margin-top:6px}.disc{color:var(--m);font-size:14px;border-top:1px solid var(--line);margin-top:34px;padding-top:14px}
.pc{padding:0;overflow:hidden}.pc img{width:100%;height:auto;display:block}.pc .tx{padding:14px 16px 16px}.pc h3 a{text-decoration:none;color:inherit}.pc h3 a:hover{text-decoration:underline}
.topics{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 14px}.topics a{border:1px solid var(--line);background:var(--c);border-radius:999px;padding:4px 14px;text-decoration:none;font-size:15px;font-weight:600}.topics a:hover{border-color:var(--g)}
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


def switcher(lang, urlfn, langs=None):
    items = []
    for c in (langs or LANGS):
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
<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {name}</b>{hnav(lang, urlfn)}</header>
<main><section class="hero"><div><h1>{d['h1']}</h1><p>{d['lead']}</p>
<p><a class="btn" href="{play}" rel="noopener">{d['cta']}</a></p></div>
<img src="{SITE}/img/hero.jpg" width="760" height="760" alt="{name} yoga instructor character" fetchpriority="high" class="h"></section>
<h2>{d['shots_h']}</h2><div class="shots">{shots}</div>
<h2>{d['feat_h']}</h2><div class="grid">{feats}</div>
{yoga_link(lang)}<div class="band"><h2 style="margin-top:0">{d['lvl_h']}</h2><p>{d['lvl']}</p><p><a class="btn" href="{play}" rel="noopener">{d['cta']}</a></p></div>
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
        f'<header><b>Tonn</b>{hnav(lang, urlfn)}</header><main><section class="hero home"><div><h1>{d["home_h1"]}</h1><p style="font-size:19px">{d["home_lead"]}</p></div><img src="{SITE}/img/hero-duo.jpg" width="900" height="760" alt="Tonn fitness characters" fetchpriority="high" class="h duo"></section><div class="grid">{cards}</div></main><img class="side l" src="{SITE}/img/side-woman.webp" alt="" aria-hidden="true"><img class="side r" src="{SITE}/img/side-man.webp" alt="" aria-hidden="true"><footer><p>© TonnProSport</p></footer></div></body></html>'


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
<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {name}</b>{hnav(lang, urlfn)}</header>
<main><section class="hero"><div><h1>{name} — {tag}</h1><p>{lead}</p>
<p><span class="btn off" aria-disabled="true">{BADGE[lang]}</span></p></div>{pic}</section>
<div class="grid">{cards}</div>
{hub_link(lang, HUB_MAIN_BY_APP.get(slug, ""))}<div class="band"><h2 style="margin-top:0">{fill('band_h')}</h2><p>{fill('band_t')}</p><p><span class="btn off" aria-disabled="true">{BADGE[lang]}</span></p></div>
<h2>{d['faq_h']}</h2>{faqs}</main>
<footer><a href="{url_home(lang)}">{d['all']}</a><a href="{SITE}/{slug}/privacy-policy.html">{d['priv']}</a><a href="{SITE}/{slug}/terms-of-use.html">{d['terms']}</a><p>© TonnProSport · {fill('foot')}</p></footer>
</div></body></html>"""


BLOG_LANGS = ["en", "uk"]
BLOG_T = {
 "en": {"blog": "Blog", "title": "Tonn blog – yoga, stretching and breathing guides", "desc": "Practical guides on yoga for beginners, stretching, breathing and healthy habits from the Tonn apps team.", "h1": "Tonn blog",
        "lead": "Practical guides on yoga, stretching and breathing.", "min": "min read", "related": "More articles",
        "tryh": "Practise with the app", "get": "Get it on Google Play", "soon": "is in development", "tryy": "Meanwhile, try the poses in TonnYog", "pub": "Published"},
 "uk": {"blog": "Блог", "title": "Блог Tonn – йога, розтяжка та дихання: практичні поради", "desc": "Практичні поради про йогу для початківців, розтяжку, дихання та здорові звички від команди додатків Tonn.", "h1": "Блог Tonn",
        "lead": "Практичні поради про йогу, розтяжку й дихання.", "min": "хв читання", "related": "Інші статті",
        "tryh": "Практикуйте з додатком", "get": "Завантажити в Google Play", "soon": "у розробці", "tryy": "А поки що спробуйте пози в TonnYog", "pub": "Опубліковано"},
}
APP_NAMES = {"tonnyog": "TonnYog", "tonnstretch": "TonnStretch", "tonncalm": "TonnCalm", "tonnpower": "TonnPower", "tonnfit": "TonnFit",
             "tonnworkout": "TonnWorkout", "tonnaim": "TonnAIM", "tonnprosport": "TonnProSport"}

def url_blog(lang): return f"{SITE}/{pre(lang)}blog/"
def url_post(lang, slug): return f"{SITE}/{pre(lang)}blog/{slug}/"

def hnav(lang, urlfn, langs=None):
    bl = (f'<a class="bl" href="{url_yoga(lang)}">{HUB_T[lang]["nav"]}</a><a class="bl" href="{url_blog(lang)}">{BLOG_T[lang]["blog"]}</a>') if lang in BLOG_LANGS else ""
    return f'<div class="hr">{bl}{switcher(lang, urlfn, langs)}</div>'

def _hub(dir_, groups, apps, image, en, uk):
    return {"dir": dir_, "groups": groups, "apps": apps, "image": image, "T": {"en": en, "uk": uk}}

HUBS = {}

HUBS["yoga"] = _hub("yoga", [
    ["yoga-for-beginners-at-home", "morning-yoga-10-minute-routine", "bedtime-yoga-for-better-sleep",
     "yoga-for-back-pain-office-workers", "yoga-for-men-myths-and-benefits", "how-long-to-hold-yoga-poses"],
    ["improve-flexibility-in-30-days", "how-to-do-the-splits", "middle-splits-step-by-step", "stretching-after-workout"],
    ["breathing-techniques-for-calm", "guided-breathing-circle-explained", "reduce-stress-in-3-minutes-breathing",
     "breathing-exercises-before-sleep", "meditation-for-beginners-5-minutes"]], ["tonnyog"], "butterfly",
 {"nav": "Yoga", "title": "Yoga Guides: Routines, Poses, Stretching and Breathing | Tonn",
  "desc": "A hub of practical yoga guides: routines for beginners, morning and bedtime yoga, back care, flexibility, splits, breathing and meditation.",
  "h1": "Yoga guides",
  "intro": ["Yoga is a practice of movement, breathing and attention. It can be as gentle as a ten-minute evening stretch or as demanding as a long strength-based flow. This page collects our practical guides so you can find the right starting point and follow a clear path.",
            "Not sure where to begin? Start with the beginner plan, add a short morning or evening routine, and use the breathing guides to relax. Always move within a comfortable range and stop if something hurts."],
  "groups": ["Getting started and daily routines", "Flexibility, stretching and splits", "Breathing and meditation"],
  "app_h": "Practise yoga with an app",
  "app_p": "TonnYog is an offline yoga app for Android with 30-day programs, voice-guided practice, a pose guide with pictures and your own routine builder."},
 {"nav": "Йога", "title": "Йога: поради, пози, розтяжка й дихання | Tonn",
  "desc": "Збірка практичних порад про йогу: програми для початківців, ранкова й вечірня йога, догляд за спиною, гнучкість, шпагат, дихання та медитація.",
  "h1": "Йога: усі поради",
  "intro": ["Йога це практика руху, дихання й уваги. Вона може бути такою ж м’якою, як десятихвилинна вечірня розтяжка, чи такою ж вимогливою, як довга силова послідовність. На цій сторінці зібрані наші практичні поради, щоб ви могли знайти відповідну точку старту й іти зрозумілим шляхом.",
            "Не знаєте, з чого почати? Візьміть план для початківців, додайте коротку ранкову чи вечірню практику й користуйтеся порадами з дихання для розслаблення. Рухайтеся в комфортному діапазоні й зупиняйтеся, якщо щось болить."],
  "groups": ["Початок і щоденні практики", "Гнучкість, розтяжка й шпагат", "Дихання та медитація"],
  "app_h": "Практикуйте йогу з додатком",
  "app_p": "TonnYog це офлайн-додаток для йоги на Android: програми на 30 днів, заняття з голосовим супроводом, довідник поз із зображеннями й конструктор власних програм."})

HUBS["stretching"] = _hub("stretching", [
    ["improve-flexibility-in-30-days", "how-to-do-the-splits", "middle-splits-step-by-step"],
    ["stretching-after-workout", "warm-up-before-running-and-cool-down", "yoga-for-back-pain-office-workers"]], ["tonnstretch"], "splits",
 {"nav": "Stretching", "title": "Stretching and Flexibility Guides: Splits, Cool-Downs, Routines | Tonn",
  "desc": "Practical stretching guides: improving flexibility in 30 days, the splits, stretching after workouts, cool-downs and back care.",
  "h1": "Stretching and flexibility guides",
  "intro": ["Flexibility improves with regular, patient practice rather than extreme stretches. These guides show how to warm up, which stretches matter most and how often to practise, from a simple 30-day plan to the front and middle splits.",
            "Stretch to mild tension, never to pain, and breathe slowly. Warm muscles stretch further and with less risk, so do your stretching after a short warm-up or a workout."],
  "groups": ["Flexibility and splits", "Around your workouts and for your back"],
  "app_h": "Stretching with an app",
  "app_p": "TonnStretch is in development. It will offer offline stretching programs by body zone, 30-day courses including one for the splits, a timer and voice guidance."},
 {"nav": "Розтяжка", "title": "Розтяжка й гнучкість: шпагат, заминка, комплекси | Tonn",
  "desc": "Практичні поради з розтяжки: як підвищити гнучкість за 30 днів, шпагат, розтяжка після тренування, заминка й догляд за спиною.",
  "h1": "Розтяжка й гнучкість: усі поради",
  "intro": ["Гнучкість росте від регулярної терплячої практики, а не від екстремальних розтяжок. Ці поради показують, як розминатися, які вправи важливі найбільше й як часто тренуватися: від простого плану на 30 днів до поздовжнього й поперечного шпагату.",
            "Розтягуйтеся до легкого напруження, ніколи до болю, і дихайте повільно. Розігріті м’язи розтягуються далі й безпечніше, тому розтягуйтеся після короткої розминки чи тренування."],
  "groups": ["Гнучкість і шпагат", "Навколо тренувань і для спини"],
  "app_h": "Розтяжка з додатком",
  "app_p": "TonnStretch у розробці. У ньому будуть офлайн-програми розтяжки за зонами тіла, курси на 30 днів (зокрема до шпагату), таймер і голосовий супровід."})

HUBS["strength"] = _hub("strength", [
    ["workout-diary-why-and-how", "progressive-overload-explained", "one-rep-max-1rm-calculate", "how-long-rest-between-sets"]],
 ["tonnpower"], "p_deadlift",
 {"nav": "Strength", "title": "Strength Training Guides: Gym Diary, Progression, 1RM, Rest | Tonn",
  "desc": "Practical guides for gym training: keeping a workout diary, progressive overload, estimating your 1RM and resting between sets.",
  "h1": "Strength training guides",
  "intro": ["Steady strength comes from tracking what you do and asking a little more of your muscles over time. These guides cover the basics of gym training: how to keep a diary, how to progress without plateaus, how to estimate your one-rep max and how long to rest.",
            "Technique always comes before weight. If you are unsure about a lift, ask a qualified coach, and use a spotter or safety bars for heavy sets."],
  "groups": ["Gym basics and progress"],
  "app_h": "A gym diary in your pocket",
  "app_p": "TonnPower is in development. It is an offline gym diary that logs weight and reps for each set, fills in the previous weight, has a rest timer with a voice countdown and shows personal records."},
 {"nav": "Силові", "title": "Силові тренування: щоденник, прогресія, 1ПМ, відпочинок | Tonn",
  "desc": "Практичні поради для тренувань у залі: ведення щоденника, прогресивне навантаження, оцінка 1ПМ і відпочинок між підходами.",
  "h1": "Силові тренування: усі поради",
  "intro": ["Стабільна сила з’являється, коли ви фіксуєте, що робите, і поступово вимагаєте від м’язів трохи більше. Ці поради охоплюють основи тренувань у залі: як вести щоденник, як прогресувати без застою, як оцінити одноповторний максимум і скільки відпочивати.",
            "Техніка завжди важливіша за вагу. Якщо сумніваєтеся щодо вправи, запитайте кваліфікованого тренера, а для важких підходів користуйтеся страхувальником чи запобіжними опорами."],
  "groups": ["Основи залу й прогрес"],
  "app_h": "Щоденник залу в кишені",
  "app_p": "TonnPower у розробці. Це офлайн-щоденник залу: він фіксує вагу й повтори кожного підходу, підставляє попередню вагу, має таймер відпочинку з голосовим відліком і показує особисті рекорди."})

HUBS["home-workouts"] = _hub("home-workouts", [
    ["home-workout-no-equipment-30-days", "how-many-push-ups-and-squats-per-day"],
    ["plank-technique-and-progression", "build-a-daily-exercise-habit"]], ["tonnfit", "tonnaim"], "m_pushup",
 {"nav": "Home workouts", "title": "Home Workouts: Bodyweight Plans, Planks, Daily Habits | Tonn",
  "desc": "Practical guides to training at home without equipment: a 30-day plan, push-ups and squats, the plank and building a daily exercise habit.",
  "h1": "Home workout guides",
  "intro": ["You do not need a gym to get fitter. A few bodyweight exercises, done regularly, can build strength and endurance. These guides give you a 30-day plan, daily repetition targets, the plank and a way to turn exercise into a habit.",
            "Start small, keep good form and increase gradually. Rest days are part of the plan."],
  "groups": ["Start training at home", "Core and consistency"],
  "app_h": "Home workouts with an app",
  "app_p": "TonnFit and TonnAIM are in development. TonnFit covers workouts with your own weight and equipment with 30-day programs and a tracker; TonnAIM is built for daily exercises with a “+5” button, streaks and planks."},
 {"nav": "Вдома", "title": "Тренування вдома: програми з власною вагою, планка, щоденні звички | Tonn",
  "desc": "Практичні поради для тренувань удома без інвентаря: план на 30 днів, віджимання й присідання, планка й формування щоденної звички.",
  "h1": "Тренування вдома: усі поради",
  "intro": ["Щоб стати у формі, зал не потрібен. Кілька вправ із власною вагою, виконуваних регулярно, розвинуть силу й витривалість. Ці поради дають план на 30 днів, денні цілі за повторами, планку й спосіб перетворити тренування на звичку.",
            "Починайте з малого, стежте за технікою й збільшуйте навантаження поступово. Вихідні це частина плану."],
  "groups": ["Починаємо вдома", "Кор і регулярність"],
  "app_h": "Тренування вдома з додатком",
  "app_p": "TonnFit і TonnAIM у розробці. TonnFit охоплює тренування з власною вагою та інвентарем із програмами на 30 днів і трекером; TonnAIM створений для щоденних вправ із кнопкою «+5», серіями днів і планками."})

HUBS["outdoor"] = _hub("outdoor", [
    ["pull-up-bar-and-parallel-bars-for-beginners"],
    ["how-many-steps-per-day", "interval-running-for-beginners", "warm-up-before-running-and-cool-down"]], ["tonnworkout"], "m_pullup",
 {"nav": "Outdoor", "title": "Outdoor Workouts: Pull-Up Bar, Steps, Running for Beginners | Tonn",
  "desc": "Practical guides for outdoor training: pull-up bar and parallel bars, daily steps, interval running and warm-up for runs.",
  "h1": "Outdoor workout guides",
  "intro": ["Parks, courtyards and streets are a free gym. These guides help you start on the pull-up bar and parallel bars, choose a daily step goal, build up running with intervals and warm up properly.",
            "Check equipment before use, wear suitable shoes and increase the load gradually."],
  "groups": ["Bars and bodyweight", "Walking and running"],
  "app_h": "Outdoor workouts with an app",
  "app_p": "TonnWorkout is in development. It will include pull-up bar and parallel bar programs, running warm-ups, daily step and distance goals and a 14-day chart."},
 {"nav": "Вулиця", "title": "Тренування просто неба: турнік, кроки, біг для початківців | Tonn",
  "desc": "Практичні поради для тренувань на вулиці: турнік і бруси, денні кроки, інтервальний біг і розминка перед пробіжкою.",
  "h1": "Тренування просто неба: усі поради",
  "intro": ["Парки, двори й вулиці це безкоштовний зал. Ці поради допоможуть почати на турніку й брусах, обрати денну ціль кроків, поступово нарощувати біг інтервалами та правильно розминатися.",
            "Перевіряйте інвентар перед використанням, носіть відповідне взуття й збільшуйте навантаження поступово."],
  "groups": ["Турнік і власна вага", "Ходьба та біг"],
  "app_h": "Вуличні тренування з додатком",
  "app_p": "TonnWorkout у розробці. У ньому будуть програми для турніка й брусів, розминки перед бігом, денні цілі кроків і дистанції та графік за 14 днів."})

HUB_ORDER = ["yoga", "stretching", "strength", "home-workouts", "outdoor"]
HUB_T = {l: HUBS["yoga"]["T"][l] for l in ("en", "uk")}
HUB_OF = {}
for _k in HUB_ORDER:
    for _g in HUBS[_k]["groups"]:
        for _s in _g:
            HUB_OF.setdefault(_s, _k)
HUB_MAIN_BY_APP = {"tonnyog": "yoga", "tonnstretch": "stretching", "tonnpower": "strength", "tonnfit": "home-workouts",
                   "tonnaim": "home-workouts", "tonnworkout": "outdoor"}

def url_hub(lang, key): return f"{SITE}/{pre(lang)}{HUBS[key]['dir']}/"
def url_yoga(lang): return url_hub(lang, "yoga")

def hub_link(lang, key):
    if lang not in BLOG_LANGS or key not in HUBS:
        return ""
    return f'<p><a href="{url_hub(lang, key)}"><strong>{HUBS[key]["T"][lang]["h1"]} →</strong></a></p>'

def yoga_link(lang):
    return hub_link(lang, "yoga")

def topics_nav(lang):
    links = "".join(f'<a href="{url_hub(lang, k)}">{HUBS[k]["T"][lang]["nav"]}</a>' for k in HUB_ORDER)
    return f'<nav class="topics" aria-label="Topics">{links}</nav>'

def hub_page(lang, key):
    H = HUBS[key]; h = H["T"][lang]; bt = BLOG_T[lang]
    by = {p["slug"]: p for p in POSTS}
    urlfn = lambda c: url_hub(c, key)
    alts = [("en", urlfn("en")), ("uk", urlfn("uk")), ("x-default", urlfn("en"))]
    secs = ""; items = []
    for title, slugs in zip(h["groups"], H["groups"]):
        cards = ""
        for s in slugs:
            p = by[s]; items.append(url_post(lang, s))
            cards += (f'<div class="card pc"><a href="{url_post(lang, s)}"><img src="{SITE}/img/blog/{p["image"]}.jpg" width="900" height="507" loading="lazy" alt="{p[lang]["title"]}"></a>'
                      f'<div class="tx"><h3><a href="{url_post(lang, s)}">{p[lang]["title"]}</a></h3><p>{p[lang]["desc"]}</p></div></div>')
        secs += f'<h2>{title}</h2><div class="grid">{cards}</div>'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": h["h1"], "description": h["desc"], "inLanguage": lang, "url": urlfn(lang)},
        {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": u} for i, u in enumerate(items)]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Tonn", "item": url_home(lang)},
            {"@type": "ListItem", "position": 2, "name": h["h1"], "item": urlfn(lang)}]}]}
    ldx = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    intro = "".join(f"<p>{x}</p>" for x in h["intro"])
    if H["apps"] == ["tonnyog"]:
        cta = f'<a class="btn" href="{PLAY}" rel="noopener">{bt["get"]}</a> &nbsp; <a href="{url_app(lang, "tonnyog")}">TonnYog</a>'
    else:
        names = " · ".join(f'<a href="{url_app(lang, a)}"><strong>{APP_NAMES[a]}</strong></a>' for a in H["apps"])
        cta = f'<p>{names} — {bt["soon"]}.</p><p>{bt["tryy"]}:</p><a class="btn" href="{PLAY}" rel="noopener">{bt["get"]}</a>'
    return head(lang, h["title"], h["desc"], urlfn(lang), alts, ldx, f"{SITE}/img/blog/{H['image']}.jpg") + \
        f'<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {h["nav"]}</b>{hnav(lang, urlfn, BLOG_LANGS)}</header>' \
        f'<main>{topics_nav(lang)}<h1>{h["h1"]}</h1>{intro}{secs}' \
        f'<div class="band"><h2 style="margin-top:0">{h["app_h"]}</h2><p>{h["app_p"]}</p>{cta if H["apps"] != ["tonnyog"] else "<p>" + cta + "</p>"}</div>' \
        f'<p class="disc">{DISCLAIMER[lang]}</p></main>' \
        f'<footer><a href="{url_blog(lang)}">{bt["blog"]}</a><a href="{url_home(lang)}">{L[lang]["all"]}</a><p>© TonnProSport</p></footer></div></body></html>'


def reading_min(html):
    words = len(re.sub(r"<[^>]+>", " ", html).split())
    return max(1, round(words / 200))

def render_body(lang, html):
    def fig(m):
        f, alt = m.group(1), m.group(2)
        if f == "practice":
            return f'<figure class="phone"><img src="{SITE}/img/blog/practice-{lang}.jpg" width="320" height="693" loading="lazy" alt="{alt}"><figcaption>{alt}</figcaption></figure>'
        return f'<figure><img src="{SITE}/img/blog/{f}" width="900" height="507" loading="lazy" alt="{alt}"><figcaption>{alt}</figcaption></figure>'
    return re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", fig, html)

def blog_index(lang):
    bt = BLOG_T[lang]
    alts = [("en", url_blog("en")), ("uk", url_blog("uk")), ("x-default", url_blog("en"))]
    cards = "".join(
        f'<div class="card pc"><a href="{url_post(lang, p["slug"])}"><img src="{SITE}/img/blog/{p["image"]}.jpg" width="900" height="507" loading="lazy" alt="{p[lang]["title"]}"></a>'
        f'<div class="tx"><h3><a href="{url_post(lang, p["slug"])}">{p[lang]["title"]}</a></h3><p>{p[lang]["desc"]}</p>'
        f'<p class="meta">{reading_min(p[lang]["body"])} {bt["min"]}</p></div></div>' for p in POSTS)
    return head(lang, bt["title"], bt["desc"], url_blog(lang), alts) + \
        f'<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {bt["blog"]}</b>{hnav(lang, url_blog, BLOG_LANGS)}</header>' \
        f'<main><h1>{bt["h1"]}</h1><p>{bt["lead"]}</p>{topics_nav(lang)}<div class="grid">{cards}</div></main>' \
        f'<footer><a href="{url_home(lang)}">{L[lang]["all"]}</a><p>© TonnProSport</p></footer></div></body></html>'

def blog_post(lang, p):
    bt = BLOG_T[lang]; d = p[lang]
    urlfn = lambda c: url_post(c, p["slug"])
    alts = [("en", url_post("en", p["slug"])), ("uk", url_post("uk", p["slug"])), ("x-default", url_post("en", p["slug"]))]
    img = f"{SITE}/img/blog/{p['image']}.jpg"
    art = {"@context": "https://schema.org", "@type": "Article", "headline": d["title"], "description": d["desc"], "inLanguage": lang,
           "datePublished": p["date"], "dateModified": p["date"], "image": img, "mainEntityOfPage": urlfn(lang),
           "author": {"@type": "Organization", "name": "TonnProSport"},
           "publisher": {"@type": "Organization", "name": "TonnProSport", "logo": {"@type": "ImageObject", "url": f"{SITE}/img/icon-512.png"}}}
    ld = f'<script type="application/ld+json">{json.dumps(art, ensure_ascii=False)}</script>'
    app = p["app"]; name = APP_NAMES[app]
    if app == "tonnyog":
        cta = f'<h2>{bt["tryh"]}</h2><p><a class="btn" href="{PLAY}" rel="noopener">{bt["get"]}</a></p>'
    else:
        cta = (f'<h2>{bt["tryh"]}</h2><p><a href="{url_app(lang, app)}"><strong>{name}</strong></a> — {bt["soon"]}.</p>'
               f'<p>{bt["tryy"]}:</p><p><a class="btn" href="{PLAY}" rel="noopener">{bt["get"]}</a></p>')
    hk = HUB_OF.get(p["slug"])
    same = [q for q in POSTS if q["slug"] != p["slug"] and hk and HUB_OF.get(q["slug"]) == hk]
    rest = [q for q in POSTS if q["slug"] != p["slug"] and q not in same]
    ycrumb = f' · <a href="{url_hub(lang, hk)}">{HUBS[hk]["T"][lang]["h1"]}</a>' if hk else ""
    rel = "".join(f'<li><a href="{url_post(lang, q["slug"])}">{q[lang]["title"]}</a></li>' for q in (same + rest)[:5])
    return head(lang, d["title"], d["desc"], urlfn(lang), alts, ld, img) + \
        f'<header><b><a href="{url_home(lang)}" style="text-decoration:none">Tonn</a> / {bt["blog"]}</b>{hnav(lang, urlfn, BLOG_LANGS)}</header>' \
        f'<main><article class="post"><p class="crumb"><a href="{url_blog(lang)}">← {bt["blog"]}</a>{ycrumb}</p><h1>{d["title"]}</h1>' \
        f'<p class="meta">{bt["pub"]}: {p["date"]} · {reading_min(d["body"])} {bt["min"]}</p>' \
        f'<figure><img src="{img}" width="900" height="507" alt="{d["title"]}" fetchpriority="high"></figure>' \
        f'{render_body(lang, d["body"])}<div class="band">{cta}</div>' \
        f'<h2>{bt["related"]}</h2><ul>{rel}</ul><p class="disc">{DISCLAIMER[lang]}</p></article></main>' \
        f'<footer><a href="{url_blog(lang)}">{bt["blog"]}</a><a href="{url_home(lang)}">{L[lang]["all"]}</a><p>© TonnProSport</p></footer></div></body></html>'


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


for lang in BLOG_LANGS:
    for _k in HUB_ORDER:
        write(f"{pre(lang)}{HUBS[_k]['dir']}/index.html", hub_page(lang, _k))
    write(f"{pre(lang)}blog/index.html", blog_index(lang))
    for p in POSTS:
        write(f"{pre(lang)}blog/{p['slug']}/index.html", blog_post(lang, p))


def sm_blog(fn):
    x = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{fn(c)}"/>' for c in BLOG_LANGS) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{fn("en")}"/>'
    return "".join(f"<url><loc>{fn(c)}</loc>{x}</url>\n" for c in BLOG_LANGS)


def sm_entry(urlfn):
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{u}"/>' for c, u in alts_for(urlfn))
    return "".join(f"<url><loc>{urlfn(c)}</loc>{alts}</url>\n" for c in LANGS)

slugs = [s for s, _, _ in APPS] + [n.lower() for n, _ in SOON]
body = sm_entry(url_home) + "".join(sm_entry(lambda c, s=s: url_app(c, s)) for s in slugs)
body += "".join(sm_blog(lambda c, k=k: url_hub(c, k)) for k in HUB_ORDER) + sm_blog(url_blog) + "".join(sm_blog(lambda c, q=q: url_post(c, q["slug"])) for q in POSTS)
body += "".join(f"<url><loc>{SITE}/{s}/{f}</loc></url>\n" for s in slugs for f in ("privacy-policy.html", "terms-of-use.html"))
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
write(".nojekyll", "")
print("OK", len(LANGS) * (1 + len(slugs)) + len(BLOG_LANGS) * (1 + len(HUB_ORDER) + len(POSTS)), "pages")
