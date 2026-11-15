# Генератор сайту TonnYog: python build.py
# Одне джерело текстів -> index.html (EN), uk/index.html, privacy.html, sitemap.xml.
# Змінити адресу сайту — рядок SITE нижче, потім запустити скрипт ще раз.
import json, pathlib

SITE = "https://tonnapp.github.io"
PLAY = "https://play.google.com/store/apps/details?id=com.TonnProSport.Tonn_Yog"
ROOT = pathlib.Path(__file__).parent

L = {
 "en": {
  "path": "tonnyog/", "lang": "en", "home": "Home",
  "title": "TonnYog – Offline Yoga App: 30-Day Programs, Pose Guide & Tracker",
  "desc": "TonnYog is a free offline yoga app for Android: 30-day programs, voice-guided practice, a yoga pose guide, your own routine builder and a progress tracker. 9 languages, no sign-up.",
  "h1": "TonnYog — yoga app that works offline",
  "lead": "Practice yoga at home or on the road. Ready-made 30-day programs, voice guidance, a library of poses and a progress tracker — no account and no internet required.",
  "cta": "Get it on Google Play",
  "shots_h": "TonnYog yoga app screenshots", "alts": ["TonnYog home screen with weekly progress and current workout","30-day yoga programs and quick workouts in TonnYog","Voice-guided yoga practice: Butterfly Pose with countdown","Yoga progress tracker with activity calendar","Routine builder: create your own yoga program","TonnYog settings: voice guidance, pauses and 9 languages"],
  "feat_h": "What you get in the TonnYog yoga app",
  "feats": [
   ("30-day yoga programs", "Step-by-step courses for beginners and experienced practitioners. Start a program and follow it day by day."),
   ("Voice-guided practice", "Spoken pose descriptions and a countdown, so you can keep your eyes off the screen and focus on your breath."),
   ("Yoga pose guide", "A catalog of asanas with pictures and clear instructions on how to enter, hold and leave each pose."),
   ("Build your own routine", "Pick poses, set the order and time for each one, and save your personal yoga program."),
   ("Progress tracker", "Workout history, statistics and a weight chart help you stay consistent."),
   ("Breathing practice", "A guided breathing circle sets an even rhythm: 4 seconds in, 4 seconds out."),
   ("Works offline", "All content is stored on your phone. Practice in airplane mode, outdoors or while travelling."),
   ("9 languages", "English, Ukrainian, Spanish, German, French, Portuguese, Polish, Turkish and Italian."),
  ],
  "lvl_h": "Free to start, unlock more when you need it",
  "lvl": "The Simple level is free and includes the main practices. Standard and Advanced add more tools such as the routine builder, time adjustment, sharing programs and history. Levels are one-time purchases in Google Play.",
  "faq_h": "Frequently asked questions",
  "faq": [
   ("Is TonnYog free?", "You can start for free with the Simple level. Extra levels (Standard and Advanced) are one-time in-app purchases."),
   ("Do I need internet to do yoga with TonnYog?", "No. The app works fully offline once it is installed."),
   ("Is TonnYog good for beginners?", "Yes. It has beginner-friendly 30-day programs, a trial practice that teaches the interface, and a pose guide with step-by-step instructions."),
   ("Which platforms are supported?", "TonnYog is available for Android on Google Play."),
   ("Can I create my own yoga routine?", "Yes. The routine builder lets you choose poses, their order and duration, then save the program and practise it any time."),
  ],
  "foot": "Yoga app for Android by TonnProSport",
  "priv": "Privacy Policy", "terms": "Terms of Use", "all": "All Tonn apps", "other": "Українською", "kw": "yoga app, offline yoga, yoga for beginners, 30-day yoga program, yoga poses, asana guide, yoga tracker, yoga at home",
 },
 "uk": {
  "path": "uk/tonnyog/", "lang": "uk", "home": "Головна",
  "title": "TonnYog – йога офлайн: програми на 30 днів, довідник асан і трекер",
  "desc": "TonnYog — безкоштовний додаток для йоги на Android: програми на 30 днів, озвучене заняття, довідник асан, конструктор власних програм і трекер прогресу. 9 мов, без реєстрації.",
  "h1": "TonnYog — йога, яка працює без інтернету",
  "lead": "Займайтеся йогою вдома чи в дорозі. Готові програми на 30 днів, голосовий супровід, довідник асан і трекер прогресу — без акаунта й без інтернету.",
  "cta": "Завантажити в Google Play",
  "shots_h": "Скриншоти додатка для йоги TonnYog", "alts": ["Головний екран TonnYog: прогрес тижня й поточне тренування","Програми йоги на 30 днів у TonnYog","Заняття йогою з озвученням: поза метелика та відлік","Трекер прогресу йоги з календарем активності","Конструктор програм: власна програма йоги","Налаштування TonnYog: озвучення, пауза та 9 мов"],
  "feat_h": "Що є в додатку для йоги TonnYog",
  "feats": [
   ("Програми йоги на 30 днів", "Покрокові курси для початківців і досвідчених. Запустіть програму й виконуйте її день за днем."),
   ("Озвучене заняття", "Голосовий опис поз і відлік часу — можна не дивитися в екран і зосередитися на диханні."),
   ("Довідник асан", "Каталог поз із зображеннями й зрозумілими інструкціями: як увійти в позу, утримувати її та вийти."),
   ("Конструктор власних програм", "Обирайте пози, задавайте порядок і час кожної та зберігайте свою програму."),
   ("Трекер прогресу", "Історія занять, статистика й графік ваги допомагають займатися регулярно."),
   ("Дихальна практика", "Коло дихання задає рівний ритм: 4 секунди вдих, 4 секунди видих."),
   ("Працює офлайн", "Увесь контент зберігається на телефоні. Практикуйте в режимі польоту, на природі чи в подорожі."),
   ("9 мов", "Українська, англійська, іспанська, німецька, французька, португальська, польська, турецька й італійська."),
  ],
  "lvl_h": "Починайте безкоштовно, відкривайте більше за потреби",
  "lvl": "Рівень «Простий» безкоштовний і містить основні практики. «Стандарт» і «Просунутий» додають інструменти: конструктор, підлаштування часу, обмін програмами та історію. Рівні — разові покупки в Google Play.",
  "faq_h": "Часті запитання",
  "faq": [
   ("TonnYog безкоштовний?", "Почати можна безкоштовно з рівня «Простий». Додаткові рівні («Стандарт» і «Просунутий») — разові покупки в додатку."),
   ("Чи потрібен інтернет для занять йогою в TonnYog?", "Ні. Після встановлення додаток працює повністю офлайн."),
   ("Чи підходить TonnYog для початківців?", "Так. Є програми на 30 днів для початківців, пробна практика, що навчає інтерфейсу, і довідник поз із покроковими інструкціями."),
   ("На яких платформах доступний додаток?", "TonnYog доступний для Android у Google Play."),
   ("Чи можна створити власну програму йоги?", "Так. Конструктор дозволяє обрати пози, їх порядок і тривалість, зберегти програму й виконувати її будь-коли."),
  ],
  "foot": "Додаток для йоги на Android від TonnProSport",
  "priv": "Політика конфіденційності", "terms": "Умови використання", "all": "Усі додатки Tonn", "other": "English", "kw": "йога вдома, йога для початківців, програма йоги на 30 днів, асани, довідник асан, йога офлайн, трекер йоги",
 },
}

CSS = """
:root{--g:#2f6b3a;--l:#E7EFD3;--ink:#1d2a20;--m:#5a6a5e;--bg:#fbfcf7;--c:#fff;--line:#dfe6d2}
@media(prefers-color-scheme:dark){:root{--g:#8fd19a;--l:#1f2a21;--ink:#eaf1e6;--m:#a3b3a6;--bg:#141a15;--c:#1a231c;--line:#2b382d}}
*{box-sizing:border-box}body{margin:0;font:17px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:var(--g)}.w{max-width:960px;margin:0 auto;padding:0 16px}
header{display:flex;justify-content:space-between;align-items:center;padding:14px 0}header b{font-size:20px}
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

def head(d, title, desc, canon, alts, extra=""):
    hl = "".join(f'<link rel="alternate" hreflang="{k}" href="{v}">' for k, v in alts)
    return f"""<!doctype html>
<html lang="{d['lang']}"><head><meta charset="utf-8">
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

def index(d):
    other = L["uk" if d["lang"] == "en" else "en"]
    canon = f"{SITE}/{d['path']}"
    alts = [("en", f"{SITE}/tonnyog/"), ("uk", f"{SITE}/uk/tonnyog/"), ("x-default", f"{SITE}/tonnyog/")]
    app = {"@context": "https://schema.org", "@type": "MobileApplication", "name": "TonnYog",
           "operatingSystem": "ANDROID", "applicationCategory": "HealthApplication",
           "description": d["desc"], "url": canon, "downloadUrl": PLAY, "image": f"{SITE}/img/icon-512.png",
           "inLanguage": ["en", "uk", "es", "de", "fr", "pt", "pl", "tr", "it"],
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
           "author": {"@type": "Organization", "name": "TonnProSport"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (app, faq))
    h = head(d, d["title"], d["desc"], canon, alts, ld + f'<meta name="keywords" content="{d["kw"]}">')
    feats = "".join(f'<div class="card"><h3>{t}</h3><p>{p}</p></div>' for t, p in d["feats"])
    pre = "en" if d["lang"] == "en" else "uk"
    shots = "".join(f'<img src="{SITE}/img/shots/{pre}-{i}.jpg" width="203" height="440" loading="lazy" alt="{a}">' for i, a in enumerate(d["alts"], 1))
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in d["faq"])
    other_href = f"{SITE}/uk/tonnyog/" if d["lang"] == "en" else f"{SITE}/tonnyog/"
    return h + f"""
<header><b><a href="{SITE}/{'' if d['lang']=='en' else 'uk/'}" style="text-decoration:none">Tonn</a> / TonnYog</b><a href="{other_href}" hreflang="{other['lang']}">{d['other']}</a></header>
<main><section class="hero"><div><h1>{d['h1']}</h1><p>{d['lead']}</p>
<p><a class="btn" href="{PLAY}" rel="noopener">{d['cta']}</a></p></div>
<img src="{SITE}/img/hero.jpg" width="760" height="760" alt="TonnYog yoga instructor character" fetchpriority="high" class="h"></section>
<h2>{d['shots_h']}</h2><div class="shots">{shots}</div>
<h2>{d['feat_h']}</h2><div class="grid">{feats}</div>
<div class="band"><h2 style="margin-top:0">{d['lvl_h']}</h2><p>{d['lvl']}</p><p><a class="btn" href="{PLAY}" rel="noopener">{d['cta']}</a></p></div>
<h2>{d['faq_h']}</h2>{faqs}</main>
<footer><a href="{SITE}/{'' if d['lang']=='en' else 'uk/'}">{d['all']}</a><a href="{SITE}/tonnyog/privacy-policy.html">{d['priv']}</a><a href="{SITE}/tonnyog/terms-of-use.html">{d['terms']}</a><a href="{PLAY}" rel="noopener">Google Play</a><p>© TonnProSport · {d['foot']}</p></footer>
</div></body></html>"""


HOME = {
 "en": ("Tonn apps – fitness, yoga and wellness apps for Android", "Tonn is a series of offline fitness and wellness apps for Android: yoga, workouts and more. Free to start, no sign-up.", "Tonn apps", "Offline fitness and wellness apps for Android. Free to start, no sign-up.", "Learn more", "Get it on Google Play", ""),
 "uk": ("Додатки Tonn – фітнес, йога та wellness для Android", "Tonn — серія офлайн-додатків для фітнесу й здоров'я на Android: йога, тренування та інше. Можна почати безкоштовно, без реєстрації.", "Додатки Tonn", "Офлайн-додатки для фітнесу й здоров'я на Android. Можна почати безкоштовно, без реєстрації.", "Детальніше", "Завантажити в Google Play", "uk/"),
}
APPS = [("tonnyog", "TonnYog", {"en": "Offline yoga app: 30-day programs, pose guide, own routines and tracker.", "uk": "Йога офлайн: програми на 30 днів, довідник асан, власні програми й трекер."}, PLAY)]

def home(lang):
    t, desc, h1, lead, more, gp, pre = HOME[lang]
    canon = f"{SITE}/{pre}"
    alts = [("en", f"{SITE}/"), ("uk", f"{SITE}/uk/"), ("x-default", f"{SITE}/")]
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "TonnProSport", "url": f"{SITE}/", "logo": f"{SITE}/img/icon-512.png"}
    ld = f'<script type="application/ld+json">{json.dumps(org)}</script>'
    d = {"lang": lang}
    cards = "".join(f'<div class="card"><h3>{n}</h3><p>{tx[lang]}</p><p style="margin-top:12px"><a href="{SITE}/{pre}{slug}/">{more}</a> · <a href="{pl}" rel="noopener">{gp}</a></p></div>' for slug, n, tx, pl in APPS)
    other = f"{SITE}/uk/" if lang == "en" else f"{SITE}/"
    return head(d, t, desc, canon, alts, ld) + f'<header><b>Tonn</b><a href="{other}">{"Українською" if lang=="en" else "English"}</a></header><main><h1>{h1}</h1><p>{lead}</p><div class="grid">{cards}</div></main><footer><p>© TonnProSport</p></footer></div></body></html>'

for sub in ("tonnyog", "uk/tonnyog"):
    (ROOT / sub).mkdir(parents=True, exist_ok=True)
(ROOT / "index.html").write_text(home("en"), encoding="utf-8")
(ROOT / "uk" / "index.html").write_text(home("uk"), encoding="utf-8")
(ROOT / "tonnyog" / "index.html").write_text(index(L["en"]), encoding="utf-8")
(ROOT / "uk" / "tonnyog" / "index.html").write_text(index(L["uk"]), encoding="utf-8")
(ROOT / "404.html").write_text(head(L["en"], "Tonn", "Page not found", SITE + "/", []).replace("<head>", '<head><meta name="robots" content="noindex">') + f'<h1>404</h1><p><a href="{SITE}/">Tonn</a></p></div></body></html>', encoding="utf-8")
urls = [f"{SITE}/", f"{SITE}/uk/", f"{SITE}/tonnyog/", f"{SITE}/uk/tonnyog/", f"{SITE}/tonnyog/privacy-policy.html", f"{SITE}/tonnyog/terms-of-use.html"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
(ROOT / ".nojekyll").write_text("", encoding="utf-8")
print("OK")
