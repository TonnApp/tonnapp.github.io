# Статті блогу (EN і UK). Додати статтю = додати словник у POSTS і запустити build.py.
# У тексті: [[файл.jpg|підпис]] — картинка з img/blog/; [[practice|підпис]] — скриншот практики з додатка.
# app — додаток для блоку «Спробуйте». Дата — для Google (datePublished).

DISCLAIMER = {
 "en": "This article is for general information only and is not medical advice. If you are pregnant, injured or have a health condition, check with a doctor before you start. Stop any exercise that causes sharp pain, dizziness or numbness.",
 "uk": "Стаття має лише загальний інформаційний характер і не є медичною порадою. Якщо ви вагітні, маєте травму чи хронічне захворювання, перед заняттями порадьтеся з лікарем. Припиніть будь-яку вправу, що викликає різкий біль, запаморочення чи оніміння.",
}

POSTS = [
{
 "slug": "yoga-for-beginners-at-home", "date": "2026-11-15", "image": "warrior2", "app": "tonnyog",
 "en": {
  "title": "Yoga for Beginners at Home: A Simple 30-Day Plan",
  "desc": "Start yoga at home with a simple 30-day plan for beginners: how often to practise, which poses to learn first and how to avoid common mistakes.",
  "body": """
<p>You do not need a studio, special equipment or flexibility to start yoga. A quiet corner, a mat (or a firm rug) and 10–15 minutes are enough. This guide shows what to prepare, which poses to learn first and how to build a 30-day habit that you can actually keep.</p>
<h2>Before you start</h2>
<ul>
<li><strong>Space and time.</strong> Choose a spot where you can stretch your arms out to the sides. Practise on an empty stomach or two hours after a meal.</li>
<li><strong>Clothes.</strong> Anything that lets you move freely. Yoga is practised barefoot.</li>
<li><strong>Goal.</strong> Aim for three to four sessions a week at first. Short regular practice beats one long session a month.</li>
<li><strong>Breathing.</strong> Breathe through the nose, smoothly and without holding your breath. If you cannot breathe calmly in a pose, ease off.</li>
</ul>
<h2>Six poses to learn first</h2>
<p><strong>1. Downward-Facing Dog.</strong> Stretches the back of the legs and shoulders. Keep the knees slightly bent if the hamstrings are tight and push the floor away with your hands.</p>
[[dog.jpg|Downward-Facing Dog from the TonnYog pose guide]]
<p><strong>2. Cat-Cow.</strong> A gentle spine warm-up on hands and knees: round the back as you exhale, lift the chest as you inhale.</p>
[[catcow.jpg|Cat-Cow pose]]
<p><strong>3. Sphinx.</strong> A soft backbend that opens the chest and strengthens the lower back without strain.</p>
<p><strong>4. Warrior II.</strong> Builds strength in the legs and stamina. Bend the front knee over the ankle and keep the shoulders relaxed.</p>
<p><strong>5. Tree Pose.</strong> Trains balance. Rest the foot on the calf or inner thigh, never on the knee, and keep your eyes on one point.</p>
[[tree.jpg|Tree Pose for balance]]
<p><strong>6. Butterfly.</strong> A seated pose for the hips. Sit tall and let the knees drop naturally; do not push them down.</p>
<h2>The 30-day plan</h2>
<ul>
<li><strong>Days 1–7: foundations.</strong> 10–15 minutes. Learn the six poses above, hold each for 3–5 breaths and finish with a short rest lying on your back.</li>
<li><strong>Days 8–14: add the standing poses.</strong> 15 minutes. Repeat the sequence on both sides and add a minute of calm breathing at the end.</li>
<li><strong>Days 15–21: strength and balance.</strong> 15–20 minutes. Hold poses a little longer (5–8 breaths).</li>
<li><strong>Days 22–30: flow.</strong> 20 minutes. Link the poses into a smooth sequence and finish with five minutes of relaxation.</li>
</ul>
<p>Take one or two rest days a week. If you miss a day, simply continue from where you stopped; do not try to catch up.</p>
<h2>Common beginner mistakes</h2>
<ul>
<li>Forcing a pose to look like a photo. Depth is not the goal; comfortable breathing is.</li>
<li>Holding the breath or breathing in short gasps.</li>
<li>Skipping the warm-up and cool-down.</li>
<li>Practising through sharp pain. A stretch should feel like gentle tension, never like pain.</li>
<li>Comparing yourself with others. Everybody’s body is different.</li>
</ul>
<h2>Making it easier</h2>
<p>A ready-made program removes the hardest part, deciding what to do each day. The TonnYog app has a 30-day beginner course, voice-guided practice, a pose guide with pictures and works fully offline, so you can practise anywhere.</p>
""",
 },
 "uk": {
  "title": "Йога для початківців удома: простий план на 30 днів",
  "desc": "Почніть займатися йогою вдома за простим планом на 30 днів: як часто практикувати, які пози вивчити першими й чого уникати.",
  "body": """
<p>Щоб почати йогу, не потрібні студія, спеціальне обладнання чи гнучкість. Достатньо тихого кутка, килимка (або щільного килима) і 10–15 хвилин. У цій статті: що підготувати, які пози вивчити першими й як за 30 днів сформувати звичку, яку справді можна втримати.</p>
<h2>Перед початком</h2>
<ul>
<li><strong>Місце й час.</strong> Оберіть місце, де можна витягнути руки в сторони. Практикуйте натще або через дві години після їжі.</li>
<li><strong>Одяг.</strong> Будь-який, у якому зручно рухатися. Йогою займаються босоніж.</li>
<li><strong>Мета.</strong> Спочатку достатньо трьох-чотирьох занять на тиждень. Коротка регулярна практика краща за одне довге заняття на місяць.</li>
<li><strong>Дихання.</strong> Дихайте носом, плавно й без затримок. Якщо у вправі не вдається дихати спокійно, зменшіть амплітуду.</li>
</ul>
<h2>Шість поз, з яких варто почати</h2>
<p><strong>1. Собака мордою донизу.</strong> Розтягує задню поверхню ніг і плечі. Якщо м’язи ніг напружені, трохи зігніть коліна й відштовхуйтеся долонями від підлоги.</p>
[[dog.jpg|Собака мордою донизу з довідника поз TonnYog]]
<p><strong>2. Кішка-Корова.</strong> М’яка розминка хребта на руках і колінах: округлюйте спину на видиху, піднімайте груди на вдиху.</p>
[[catcow.jpg|Поза Кішки-Корови]]
<p><strong>3. Сфінкс.</strong> Легкий прогин, що розкриває груди й зміцнює поперек без перенапруги.</p>
<p><strong>4. Воїн II.</strong> Розвиває силу ніг і витривалість. Зігніть переднє коліно над щиколоткою, плечі тримайте розслабленими.</p>
<p><strong>5. Дерево.</strong> Тренує рівновагу. Притисніть стопу до гомілки чи внутрішньої частини стегна, але не до коліна, і дивіться в одну точку.</p>
[[tree.jpg|Поза Дерева для рівноваги]]
<p><strong>6. Метелик.</strong> Сидяча поза для стегон. Сидіть із прямою спиною й дозвольте колінам опускатися самим, не тисніть на них.</p>
<h2>План на 30 днів</h2>
<ul>
<li><strong>Дні 1–7: основи.</strong> 10–15 хвилин. Вивчіть шість поз, утримуйте кожну 3–5 вдихів-видихів і завершуйте коротким відпочинком лежачи на спині.</li>
<li><strong>Дні 8–14: додаємо стоячі пози.</strong> 15 хвилин. Повторюйте послідовність в обидва боки й додайте хвилину спокійного дихання наприкінці.</li>
<li><strong>Дні 15–21: сила й баланс.</strong> 15–20 хвилин. Утримуйте пози трохи довше (5–8 дихальних циклів).</li>
<li><strong>Дні 22–30: потік.</strong> 20 хвилин. З’єднуйте пози в плавну послідовність і закінчуйте п’ятьма хвилинами розслаблення.</li>
</ul>
<p>Робіть один-два вихідні на тиждень. Якщо пропустили день, просто продовжуйте з того місця, де зупинилися, не намагайтеся надолужувати.</p>
<h2>Типові помилки початківців</h2>
<ul>
<li>Намагатися «витиснути» позу, як на фото. Глибина не мета, мета комфортне дихання.</li>
<li>Затримувати дихання або дихати короткими ривками.</li>
<li>Пропускати розминку й завершальне розслаблення.</li>
<li>Терпіти різкий біль. Розтяжка має відчуватися як легке напруження, а не як біль.</li>
<li>Порівнювати себе з іншими. Тіло в кожного своє.</li>
</ul>
<h2>Як зробити простіше</h2>
<p>Готова програма знімає найскладніше: щодня вирішувати, що робити. У додатку TonnYog є 30-денний курс для початківців, заняття з голосовим супроводом, довідник поз із зображеннями, і він працює повністю офлайн, тож практикувати можна будь-де.</p>
""",
 },
},
{
 "slug": "how-to-do-the-splits", "date": "2026-11-15", "image": "splits", "app": "tonnstretch",
 "en": {
  "title": "How to Do the Splits: A Safe Step-by-Step Plan",
  "desc": "A safe plan to work towards the splits: warm-up, the best stretches, how long to hold them, how often to practise and the mistakes to avoid.",
  "body": """
<p>The splits look impressive, but they are not a gift for the lucky few. With a safe routine and patience most healthy people can move closer to them. Be realistic though: it takes weeks or months, and the timeline depends on your starting flexibility, age and consistency.</p>
<h2>Two kinds of splits</h2>
<p>The <strong>front splits</strong> (one leg forward, one back) need flexible hamstrings and hip flexors. The <strong>middle (straddle) splits</strong> (legs to the sides) need open inner thighs. Choose one and train it first; the stretches overlap a little.</p>
[[splits.jpg|The front splits as shown in the TonnYog pose catalogue]]
<h2>Warm up first</h2>
<p>Never stretch cold muscles. Spend 5–10 minutes on brisk walking in place, leg swings, gentle squats and lunges until you feel warm. A warm muscle stretches further and with less risk.</p>
<h2>The best stretches</h2>
<ul>
<li><strong>Low lunge.</strong> Opens the hip flexors of the back leg. Keep the hips square.</li>
<li><strong>Pyramid pose.</strong> A forward fold with straight front leg for the hamstrings.</li>
<li><strong>Half splits.</strong> Hips back over the back knee, front leg straight, folding gently forward.</li>
<li><strong>Butterfly.</strong> Opens the inner thighs, useful for the middle splits.</li>
</ul>
[[pyramid.jpg|Pyramid pose for the hamstrings]]
<h2>How to practise</h2>
<ul>
<li>Train three to four times a week; give the muscles a rest day between hard sessions.</li>
<li>Hold each stretch for 30–60 seconds, breathing slowly. On each exhale you can sink slightly deeper.</li>
<li>Never bounce. Bouncing triggers a protective reflex and increases the risk of a strain.</li>
<li>Use support: blocks, cushions or a folded blanket under the hands or hips. Support lets you relax, and relaxed muscles lengthen.</li>
<li>Do both sides, even if one is more flexible.</li>
</ul>
<h2>Common mistakes</h2>
<ul>
<li><strong>Forcing it.</strong> Pain means stop. Aim for strong but tolerable tension.</li>
<li><strong>Twisting the hips.</strong> In the front splits keep the hips square and the back toes pointing down or neatly turned, not rolled out.</li>
<li><strong>Neglecting the hip flexors.</strong> Many people stretch only the hamstrings and then wonder why progress stalls.</li>
<li><strong>Skipping rest.</strong> Flexibility improves during recovery. Overstretching irritates the muscles and slows progress.</li>
</ul>
<h2>A weekly template</h2>
<p>Day 1: lunge and pyramid. Day 2: rest or a walk. Day 3: half splits and butterfly. Day 4: rest. Day 5: all stretches, a little longer. Weekends: gentle mobility. Track the distance between your hips and the floor so you can see progress.</p>
<h2>Let an app plan it</h2>
<p>Our TonnStretch app, which is in development, will include a 30-day course aimed at the splits, with zone-based stretching programs, a timer and voice guidance. Meanwhile, you can practise many of the poses above in TonnYog.</p>
""",
 },
 "uk": {
  "title": "Як сісти на шпагат: безпечний покроковий план",
  "desc": "Безпечний план підготовки до шпагату: розминка, найкращі вправи, скільки утримувати розтяжку, як часто тренуватися й яких помилок уникати.",
  "body": """
<p>Шпагат виглядає вражаюче, але це не дар обраних. За безпечної методики й терпіння більшість здорових людей можуть до нього наблизитися. Проте будьте реалістами: це займає тижні або місяці, а терміни залежать від вихідної гнучкості, віку й регулярності.</p>
<h2>Два види шпагату</h2>
<p><strong>Поздовжній шпагат</strong> (одна нога вперед, друга назад) потребує гнучких м’язів задньої поверхні стегна й згиначів стегна. <strong>Поперечний шпагат</strong> (ноги в сторони) потребує відкритих внутрішніх поверхонь стегон. Оберіть один і тренуйте його першим: вправи частково збігаються.</p>
[[splits.jpg|Поздовжній шпагат із каталогу поз TonnYog]]
<h2>Спочатку розігрійтеся</h2>
<p>Ніколи не розтягуйте холодні м’язи. Витратьте 5–10 хвилин на швидку ходьбу на місці, махи ногами, легкі присідання й випади, поки не відчуєте тепло. Розігрітий м’яз розтягується далі й з меншим ризиком.</p>
<h2>Найкращі вправи</h2>
<ul>
<li><strong>Низький випад.</strong> Розкриває згиначі стегна задньої ноги. Тримайте таз рівно.</li>
<li><strong>Поза піраміди.</strong> Нахил уперед із прямою передньою ногою для м’язів задньої поверхні стегна.</li>
<li><strong>Півшпагат.</strong> Таз назад над заднім коліном, передня нога пряма, плавний нахил уперед.</li>
<li><strong>Метелик.</strong> Відкриває внутрішні поверхні стегон, корисний для поперечного шпагату.</li>
</ul>
[[pyramid.jpg|Поза піраміди для м’язів задньої поверхні стегна]]
<h2>Як тренуватися</h2>
<ul>
<li>Тренуйтеся три-чотири рази на тиждень, залишайте день відпочинку між інтенсивними заняттями.</li>
<li>Утримуйте кожну вправу 30–60 секунд, дихаючи повільно. На кожному видиху можна опускатися трохи глибше.</li>
<li>Не пружиньте. Пружинні рухи запускають захисний рефлекс і підвищують ризик розтягнення.</li>
<li>Використовуйте опори: блоки, подушки чи складений плед під руки або таз. Опора допомагає розслабитися, а розслаблені м’язи подовжуються.</li>
<li>Працюйте в обидва боки, навіть якщо один гнучкіший.</li>
</ul>
<h2>Типові помилки</h2>
<ul>
<li><strong>Насильство над тілом.</strong> Біль означає: зупиніться. Орієнтуйтеся на сильне, але терпиме напруження.</li>
<li><strong>Перекручений таз.</strong> У поздовжньому шпагаті тримайте таз рівно, а носок задньої ноги дивиться вниз, не відвалюється назовні.</li>
<li><strong>Забуті згиначі стегна.</strong> Багато хто розтягує лише задню поверхню стегна, а потім дивується, чому прогрес зупинився.</li>
<li><strong>Відсутність відпочинку.</strong> Гнучкість росте під час відновлення. Перерозтягнення подразнює м’язи й сповільнює прогрес.</li>
</ul>
<h2>Тижневий шаблон</h2>
<p>День 1: випад і піраміда. День 2: відпочинок або прогулянка. День 3: півшпагат і метелик. День 4: відпочинок. День 5: усі вправи, трохи довше. Вихідні: м’яка мобільність. Фіксуйте відстань між тазом і підлогою, щоб бачити прогрес.</p>
<h2>Нехай план складе додаток</h2>
<p>У нашому додатку TonnStretch, який зараз у розробці, буде 30-денний курс до шпагату, програми розтяжки за зонами тіла, таймер і голосовий супровід. Тим часом багато з наведених вище поз можна практикувати в TonnYog.</p>
""",
 },
},
{
 "slug": "breathing-techniques-for-calm", "date": "2026-11-15", "image": "twist", "app": "tonncalm",
 "en": {
  "title": "Breathing Techniques for Calm: 4 Simple Exercises",
  "desc": "Four easy breathing exercises to calm down in a few minutes: belly breathing, box breathing, longer exhale and 4-7-8, with tips for beginners.",
  "body": """
<p>Breathing is the one body function that works automatically but that we can also control. Slow, steady breathing signals to the nervous system that you are safe, which is why breathing exercises are used for relaxation, before sleep and during stressful moments. Here are four simple techniques you can try today.</p>
<h2>The basics</h2>
<ul>
<li>Sit comfortably with a straight back or lie down.</li>
<li>Breathe through the nose unless a technique says otherwise.</li>
<li>Never strain. The breath should feel easy and quiet.</li>
<li>Five minutes is enough. Regular short sessions work better than one long one.</li>
</ul>
[[butterfly.jpg|A comfortable seated position for breathing practice]]
<h2>1. Belly (diaphragmatic) breathing</h2>
<p>Place one hand on the chest and one on the belly. Inhale slowly through the nose so the belly rises more than the chest; exhale slowly and let the belly sink. Continue for three to five minutes. This is the foundation for all other techniques.</p>
<h2>2. Box breathing</h2>
<p>Inhale for 4 counts, hold for 4, exhale for 4, hold for 4, then repeat. The even rhythm focuses attention and is popular for staying calm under pressure. If four counts feel long, start with three.</p>
<h2>3. Longer exhale</h2>
<p>Inhale for 4 counts and exhale for 6 or 8. A longer exhale tends to be relaxing, so this technique is a good choice when you feel tense or have trouble falling asleep.</p>
<h2>4. The 4-7-8 breath</h2>
<p>Inhale quietly through the nose for 4 counts, hold for 7, and exhale slowly through the mouth for 8. Start with just four cycles. Breath holds can feel strong, so do not push.</p>
<h2>Tips for beginners</h2>
<ul>
<li>Practise at the same time every day, for example after waking or before bed.</li>
<li>If you feel dizzy or uncomfortable, return to normal breathing.</li>
<li>Keep the shoulders and jaw relaxed.</li>
<li>If counting distracts you, use a visual or audio guide.</li>
</ul>
[[practice|The TonnYog practice screen with a countdown and a guided breathing circle]]
<h2>Guided breathing in the apps</h2>
<p>TonnYog includes a guided breathing circle with an even rhythm (4 seconds in, 4 seconds out) that you can enable during practice. Our TonnCalm app, which is in development, is built entirely around breathing techniques and meditation, with sounds for inhale, hold and exhale and the option to create your own technique.</p>
""",
 },
 "uk": {
  "title": "Техніки дихання для спокою: 4 прості вправи",
  "desc": "Чотири прості дихальні вправи, що заспокоюють за кілька хвилин: черевне дихання, «квадрат», подовжений видих і 4-7-8, з порадами для початківців.",
  "body": """
<p>Дихання єдина функція тіла, яка працює автоматично, але якою ми можемо й керувати. Повільне рівне дихання сигналізує нервовій системі, що ви в безпеці, тому дихальні вправи використовують для розслаблення, перед сном і в напружені моменти. Ось чотири прості техніки, які можна спробувати вже сьогодні.</p>
<h2>Основи</h2>
<ul>
<li>Сядьте зручно з прямою спиною або ляжте.</li>
<li>Дихайте носом, якщо техніка не передбачає іншого.</li>
<li>Ніколи не напружуйтеся. Дихання має бути легким і тихим.</li>
<li>П’яти хвилин достатньо. Регулярні короткі заняття працюють краще за одне довге.</li>
</ul>
[[butterfly.jpg|Зручна сидяча поза для дихальної практики]]
<h2>1. Черевне (діафрагмальне) дихання</h2>
<p>Покладіть одну руку на груди, другу на живіт. Повільно вдихайте носом так, щоб живіт піднімався більше, ніж груди; повільно видихайте, дозволяючи животу опускатися. Продовжуйте три-п’ять хвилин. Це основа для всіх інших технік.</p>
<h2>2. Дихання «квадратом»</h2>
<p>Вдих на 4 рахунки, затримка на 4, видих на 4, затримка на 4, і так по колу. Рівний ритм концентрує увагу й популярний для збереження спокою в напруженій ситуації. Якщо чотири рахунки задовгі, почніть із трьох.</p>
<h2>3. Подовжений видих</h2>
<p>Вдих на 4 рахунки, видих на 6 або 8. Довший видих зазвичай розслабляє, тому техніка добре підходить, коли ви напружені або не можете заснути.</p>
<h2>4. Дихання 4-7-8</h2>
<p>Тихий вдих носом на 4 рахунки, затримка на 7, повільний видих через рот на 8. Почніть лише з чотирьох циклів. Затримки дихання можуть відчуватися сильно, тож не форсуйте.</p>
<h2>Поради початківцям</h2>
<ul>
<li>Практикуйте в один і той самий час, наприклад після пробудження чи перед сном.</li>
<li>Якщо виникло запаморочення чи дискомфорт, поверніться до звичайного дихання.</li>
<li>Тримайте плечі й щелепу розслабленими.</li>
<li>Якщо рахунок відволікає, скористайтеся візуальною чи звуковою підказкою.</li>
</ul>
[[practice|Екран практики TonnYog із відліком і керованим колом дихання]]
<h2>Кероване дихання в додатках</h2>
<p>У TonnYog є кероване коло дихання з рівним ритмом (4 секунди вдих, 4 секунди видих), яке можна ввімкнути під час заняття. Наш додаток TonnCalm, що зараз у розробці, повністю присвячений техніками дихання та медитаціям, зі звуками вдиху, затримки й видиху та можливістю створити власну техніку.</p>
""",
 },
},
{
 "slug": "how-long-to-hold-yoga-poses", "date": "2026-11-15", "image": "tree", "app": "tonnyog",
 "en": {
  "title": "How Long Should You Hold Each Yoga Pose?",
  "desc": "How long to hold yoga poses: simple guidelines for beginners by pose type, signs it is time to come out and how to increase the time safely.",
  "body": """
<p>One of the most common questions from beginners is how long to stay in each pose. There is no single magic number, but there are sensible guidelines. The best measure is your breath: if you can breathe calmly and smoothly, you can stay; if the breath becomes ragged, it is time to come out.</p>
<h2>Quick guide</h2>
<ul>
<li><strong>Beginners, most poses:</strong> 15–30 seconds, about 3–5 slow breaths.</li>
<li><strong>Standing poses</strong> (such as Warrior II): 30–60 seconds on each side.</li>
<li><strong>Balance poses</strong> (such as Tree): 15–30 seconds on each side. Balance is tiring, so shorter is fine.</li>
<li><strong>Seated and forward folds:</strong> 30–60 seconds, up to 1–2 minutes as you gain experience.</li>
<li><strong>Restorative poses:</strong> 3–5 minutes with full support.</li>
<li><strong>Final relaxation (Savasana):</strong> 5–10 minutes.</li>
<li><strong>Flowing sequences:</strong> usually one breath per movement.</li>
</ul>
[[tree.jpg|Tree Pose: a balance pose, 15–30 seconds on each side]]
<h2>Why time matters</h2>
<p>Short holds build awareness and body control. Longer holds allow muscles to relax and lengthen, and train patience and steady breathing. A good session has a mix: shorter active poses, longer passive stretches, and a final rest.</p>
<h2>Signs it is time to come out</h2>
<ul>
<li>Sharp, pinching or burning pain, especially in joints.</li>
<li>Numbness or tingling.</li>
<li>Dizziness or shortness of breath.</li>
<li>Shaking that gets worse and makes you lose control of the pose.</li>
</ul>
<p>Mild muscle tension or a gentle trembling in the legs is normal. Sharp pain is not.</p>
[[warrior2.jpg|Warrior II: 30–60 seconds on each side]]
<h2>How to hold longer safely</h2>
<ul>
<li>Add only 5 seconds at a time. Progress slowly over weeks, not days.</li>
<li>Count breaths instead of seconds if clock-watching makes you tense.</li>
<li>Use props, such as blocks or a wall, to make a pose sustainable.</li>
<li>Always hold both sides for the same time.</li>
<li>Come out of the pose as slowly as you entered it.</li>
</ul>
<h2>Set the time in the app</h2>
<p>In TonnYog each exercise has a recommended time, and you can shorten or lengthen it by 5 seconds to suit your level, with spoken instructions and a countdown that tell you when to change. It works offline, so you can practise anywhere.</p>
""",
 },
 "uk": {
  "title": "Скільки утримувати кожну позу в йозі?",
  "desc": "Скільки тримати пози йоги: прості орієнтири для початківців за типом пози, ознаки, що час виходити з пози, і як безпечно збільшувати час.",
  "body": """
<p>Одне з найпоширеніших запитань початківців: скільки перебувати в кожній позі. Єдиного чарівного числа немає, але є розумні орієнтири. Найкраща міра це дихання: якщо дихаєте спокійно й плавно, можна залишатися; якщо дихання збивається, час виходити.</p>
<h2>Короткий орієнтир</h2>
<ul>
<li><strong>Початківці, більшість поз:</strong> 15–30 секунд, приблизно 3–5 повільних вдихів і видихів.</li>
<li><strong>Стоячі пози</strong> (наприклад, Воїн II): 30–60 секунд на кожну сторону.</li>
<li><strong>Пози на рівновагу</strong> (наприклад, Дерево): 15–30 секунд на кожну сторону. Баланс втомлює, тому коротше теж добре.</li>
<li><strong>Сидячі пози й нахили:</strong> 30–60 секунд, із досвідом до 1–2 хвилин.</li>
<li><strong>Відновлювальні пози:</strong> 3–5 хвилин із повною опорою.</li>
<li><strong>Завершальне розслаблення (Шавасана):</strong> 5–10 хвилин.</li>
<li><strong>Динамічні послідовності:</strong> зазвичай один вдих або видих на рух.</li>
</ul>
[[tree.jpg|Поза Дерева: баланс, 15–30 секунд на кожну сторону]]
<h2>Чому важливий час</h2>
<p>Короткі утримання розвивають усвідомленість і контроль над тілом. Довші дозволяють м’язам розслабитися й подовжитися та тренують терпіння й рівне дихання. У хорошому занятті поєднуються коротші активні пози, довші пасивні розтяжки й завершальний відпочинок.</p>
<h2>Ознаки, що час виходити з пози</h2>
<ul>
<li>Гострий, колючий чи пекучий біль, особливо в суглобах.</li>
<li>Оніміння чи поколювання.</li>
<li>Запаморочення або задишка.</li>
<li>Тремтіння, що наростає і змушує втрачати контроль над позою.</li>
</ul>
<p>Легке м’язове напруження чи м’яке тремтіння в ногах це нормально. Гострий біль ні.</p>
[[warrior2.jpg|Воїн II: 30–60 секунд на кожну сторону]]
<h2>Як безпечно утримувати довше</h2>
<ul>
<li>Додавайте лише по 5 секунд. Прогресуйте повільно, тижнями, а не днями.</li>
<li>Рахуйте дихальні цикли замість секунд, якщо стеження за годинником напружує.</li>
<li>Використовуйте опори, як-от блоки чи стіну, щоб позу можна було втримати.</li>
<li>Завжди тримайте обидва боки однаково довго.</li>
<li>Виходьте з пози так само повільно, як входили.</li>
</ul>
<h2>Задайте час у додатку</h2>
<p>У TonnYog кожна вправа має рекомендований час, який можна скоротити чи подовжити на 5 секунд під ваш рівень, а голосові підказки й відлік повідомляють, коли змінювати позу. Додаток працює офлайн, тож практикувати можна будь-де.</p>
""",
 },
},
]
