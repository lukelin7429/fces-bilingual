#!/usr/bin/env python3
"""Generate FengChou News index + detail pages from a manifest.
Two forms (per Luke): (a) detailed article (text+photos), (b) photo gallery (brief + photos).
Re-run anytime: python3 build_news.py"""
import os, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Lato:wght@400;500;700&display=swap" rel="stylesheet">')

def topbar(prefix, active):
    def cls(n): return ' class="is-active"' if n==active else ''
    return f'''<div class="topbar">
  <div class="wrap topbar-inner">
    <div class="topbar-brand">
      <a href="{prefix}" style="display:flex;align-items:center;gap:12px;color:inherit;">
        <img src="{prefix}photos/logo.png" alt="FengChou Elementary School logo 豐洲國小校徽">
        <div class="topbar-name">FengChou Elementary<small>臺中市神岡區豐洲國民小學</small></div>
      </a>
    </div>
    <nav class="topbar-nav">
      <a href="{prefix}">Home</a>
      <a href="{prefix}principal/">Principal</a>
      <a href="{prefix}news/"{cls('news')}>News</a>
      <a href="{prefix}bilingual-campus/">Bilingual Campus</a>
      <a href="https://changhua-bilingual.org/festivals/" target="_blank" rel="noopener">Festivals</a>
    </nav>
  </div>
</div>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div>© 2026 臺中市神岡區豐洲國民小學 · FengChou Elementary School</div>
    <div class="partner">Bilingual page by <a href="https://www.mycultureconnect.org/" target="_blank" rel="noopener">My Culture Connect 人師教育協會</a> &middot; provided free of charge</div>
  </div>
</footer>'''

# ---- Manifest ----
NEWS = [
 dict(slug="tugofwar-national", form="article", badge="Champions",
   date_en="Mar 29–30, 2025", date_zh="114-03-29 ~ 30",
   title_en="Double National Champions in Tug of War", title_zh="花蓮太平洋盃全國拔河賽 — 男・女生組雙料冠軍",
   lead_en="“One rope, soul and all.”",
   paras_en=[
     "FengChou’s tug-of-war team travelled all the way to Hualien for a three-day, two-night campaign at the 2025 Pacific Cup National Tug-of-War Championships — a tournament packed with strong teams from every county in Taiwan.",
     "Through round after round, both our boys’ team and our girls’ team fought their way into the semi-finals. From the first heats to the knockout rounds they advanced like an unstoppable tide — and although a few opponents pushed back hard, both teams stayed unbeaten and reached the finals as winners’ bracket champions.",
     "In the championship pulls, our young athletes battled to the last centimetre and took the title in <strong>both</strong> the boys’ and girls’ divisions — double national champions. With the parents’ support group cheering, and coaches and teammates lifting each other up, FengChou brought a national crown home to Taichung.",
   ],
   zh_paras=[
     "豐洲國小拔河隊一繩入魂，追求巔峰！遠赴花蓮三天兩日參加 114 年花蓮太平洋盃全國拔河錦標賽，各縣市報名隊伍實力堅強、競爭激烈。",
     "經過一連串分組比賽，本校男生組、女生組順利晉級複賽，由初賽到複賽一路勢如破竹；雖偶有驚險，男女生組皆以全勝之姿成為勝部冠軍，最終於冠亞軍賽奮戰到底，分別拿下國小男生組與女生組冠軍。",
     "在家長後援會鼎力支援、教練團與學生團隊相互打氣下，奪得耀眼佳績。大家相約，接下來的教育部全國拔河比賽，要繼續發光發熱，為台中留下全國冠軍！",
   ]),
 dict(slug="tugofwar-county", form="article", badge="Triple Champions",
   date_en="Apr 29, 2025", date_zh="114-04-29",
   title_en="Triple Champions at the Taichung Speaker’s Cup", title_zh="臺中市議長盃拔河錦標賽 — 三冠王",
   lead_en="Three divisions entered. Three gold medals home.",
   paras_en=[
     "At the 2025 Taichung Speaker’s Cup Tug-of-War Championships, FengChou’s teams swept the boards — winning the elementary boys’ Group A, the elementary girls’ Group A, <strong>and</strong> the elementary mixed Group A. Three divisions, three titles: triple champions of the city.",
     "Our heartfelt thanks go to Coach Tzu-yi and Director Da-feng, whose patient teaching and tireless training carried the team to such an outstanding result. Congratulations to every member of the tug-of-war team for shining so brightly!",
   ],
   zh_paras=[
     "狂賀！本校拔河隊榮獲 114 年臺中市議長盃拔河錦標賽國小男生甲組、國小女生甲組、國小混合甲組三冠王！",
     "感謝姿怡教練與大峯主任辛勤的教導與訓練，為本校奪得如此優秀的佳績，也恭喜拔河隊在此次比賽大放異彩！",
   ]),
 dict(slug="childrens-day", form="article",
   date_en="Apr 2, 2025", date_zh="114-04-02",
   title_en="A Joyful Children’s Day", title_zh="歡樂兒童節，一起同樂「趣」",
   lead_en="Laughter in every corner of the campus.",
   paras_en=[
     "To give the children an unforgettable, joy-filled Children’s Day, FengChou held a wonderful celebration on April 2nd. Teachers and students joined in with enthusiasm, and the whole campus filled with laughter.",
     "In the morning, the principal spoke at the awards ceremony, wishing every child a happy holiday and encouraging them to keep their childlike hearts and chase their dreams. The hall featured a model-student ceremony and a talent show — the school band performed, the dance club brought lively routines, and students from many grades took to the stage to warm applause.",
     "After the performances, the student affairs office ran a string of fun game booths and a mini market. On the basketball court, children took on challenges like “Golden Pitcher,” “Bullseye,” “Zigzag Run,” and the hopping games — running, leaping, and laughing their way through a happy Children’s Day, learning teamwork and sharing along the way.",
   ],
   zh_paras=[
     "為了讓孩子們度過一個難忘又充滿歡樂的兒童節，本校於 4 月 2 日舉辦了一場精彩的兒童節慶祝活動，全校師生熱情參與，校園充滿笑聲與歡樂的氣氛。",
     "活動當天早上，校長於表揚典禮中致詞，祝福所有小朋友節日快樂，並鼓勵大家保持童心、勇敢追夢。禮堂內安排了模範生表揚與兒童才藝表演——樂隊帶來精彩演奏、舞蹈社團帶來活潑表演，還有各年級學生帶來精采演出，贏得滿堂掌聲。",
     "表演結束後，學務處還準備了一連串闖關活動及小市集。籃球場上設有「金牌投手」「命中紅心」「蛇行大運」「滾滾樂」「跳跳樂」等遊戲，孩子們盡情奔跑、挑戰自我，在歡笑中學會合作與分享，度過一個快樂的兒童節。",
   ]),
 # ---- photo galleries (form b) ----
 dict(slug="food-farming", form="photo",
   date_en="Jan 9, 2025", date_zh="114-01-09",
   title_en="First-Grade Food &amp; Farming: Scallion Omelette", title_zh="一年級食農教育成果 — 蔥蛋",
   lead_en="Our youngest children grew their own scallions — then turned them into a hot, golden omelette. Learning you can taste.",
   lead_zh="一年級的孩子親手種蔥、親手採收，再親手煎成一盤金黃的蔥蛋。這是嚐得到味道的學習。"),
 dict(slug="storytelling", form="photo",
   date_en="Jan 10, 2025", date_zh="114-01-10",
   title_en="Big People Tell Stories", title_zh="圖書室「大人物說故事」",
   lead_en="In our tree-shaped library, Director Xiaoping became a storyteller — proof that a love of reading is something the whole school grows together.",
   lead_zh="在我們樹形的圖書室裡，曉萍主任化身說故事的人——閱讀的喜歡，是全校一起養大的。"),
 dict(slug="table-tennis", form="photo",
   date_en="School Programme", date_zh="校園課程",
   title_en="Table-Tennis Lessons", title_zh="桌球教學",
   lead_en="Bat, ball, and quick feet. Table tennis keeps FengChou children moving, focused, and smiling.",
   lead_zh="球拍、小白球，加上靈活的腳步。桌球讓豐洲的孩子動起來、專注起來，也笑了起來。"),
 dict(slug="childrens-carnival", form="photo",
   date_en="Apr 3, 2024", date_zh="113-04-03",
   title_en="Children’s Day Game Trail &amp; Flea Market", title_zh="兒童節闖關活動．跳蚤市場",
   lead_en="A campus turned playground — game booths to clear and a student-run flea market to explore.",
   lead_zh="整座校園變成遊戲場——一關一關的闖關遊戲，加上學生自己擺攤的跳蚤市場。"),
 dict(slug="mothers-day", form="photo",
   date_en="May 9, 2025", date_zh="114-05-09",
   title_en="Mother’s Day Evening", title_zh="母親節晚會",
   lead_en="An evening of songs and thank-yous, as FengChou families gathered to celebrate the mothers who hold everything together.",
   lead_zh="一個充滿歌聲與感謝的夜晚，豐洲的家庭齊聚一堂，謝謝把一切撐起來的媽媽們。"),
 dict(slug="graduation-dinner", form="photo",
   date_en="Jun 18, 2025", date_zh="114-06-18",
   title_en="The Graduation Banquet", title_zh="謝師宴",
   lead_en="One last table together before the sixth-graders move on — full of gratitude, photos, and a few happy tears.",
   lead_zh="六年級畢業前，最後一次圍在一起的餐桌——滿是感謝、合照，和幾滴開心的眼淚。"),
 dict(slug="new-student", form="photo",
   date_en="Mar 28, 2026", date_zh="115-03-28",
   title_en="New-Student Open Day &amp; Game Trail", title_zh="新生招生說明會暨闖關活動",
   lead_en="Future FengChou children and their families came to meet the school — with a welcome talk and a fun game trail around campus.",
   lead_zh="未來的豐洲孩子和家人一起來認識學校——有招生說明會，也有走遍校園的趣味闖關。"),
 dict(slug="fire-safety", form="photo",
   date_en="Safety Education", date_zh="安全教育",
   title_en="Fire Safety: Stop, Drop &amp; Roll", title_zh="消防安全宣導",
   lead_en="Children learned CPR and the “stop, drop and roll” rule for when clothes catch fire — important lessons FengChou even shares as a bilingual safety video.",
   lead_zh="孩子學會 CPR，也學會「身上著火，停、躺、滾」的保命口訣——這些重要的一課，豐洲甚至做成了雙語安全影片。"),
]

def gallery_imgs(slug, prefix):
    d = os.path.join(ROOT, "news-img", "gallery", slug)
    files = sorted(glob.glob(os.path.join(d, "*.jpg")))
    return [f"{prefix}news-img/gallery/{slug}/{os.path.basename(f)}" for f in files]

def detail_page(n):
    slug=n["slug"]; pre="../../"
    badge = f' <span class="ncard__badge">{n["badge"]}</span>' if n.get("badge") else ""
    imgs = gallery_imgs(slug, pre)
    gal = "\n".join(f'      <figure><img src="{u}" alt="{html.escape(n["title_en"])} photo" loading="lazy"></figure>' for u in imgs)
    if n["form"]=="article":
        body = f'<p class="lead">{n["lead_en"]}</p>\n'
        body += "\n".join(f'      <p>{p}</p>' for p in n["paras_en"])
        body += '\n      <div class="zh-body">\n'
        body += "\n".join(f'        <p>{p}</p>' for p in n["zh_paras"])
        body += '\n      </div>'
    else:
        body = f'<p class="lead">{n["lead_en"]}</p>\n'
        body += f'      <div class="zh-body"><p>{n["lead_zh"]}</p></div>'
    gallery_block = f'\n    <div class="gallery">\n{gal}\n    </div>\n' if imgs else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(n["title_en"])} · News — FengChou Elementary</title>
<meta name="description" content="{html.escape(n["title_en"])} — {html.escape(n["title_zh"])}. FengChou Elementary news.">
{FONT}
<link rel="stylesheet" href="{pre}assets/css/main.css">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
</head>
<body>

{topbar(pre,'news')}

<section class="article">
  <div class="wrap article-inner">
    <a class="back" href="{pre}news/">← Back to News · 回最新消息</a>
    <div class="meta">{n["date_en"]} · {n["date_zh"]}{badge}</div>
    <h1>{n["title_en"]}<span class="zh">{n["title_zh"]}</span></h1>
    {body}
{gallery_block}  </div>
</section>

{FOOTER}
<script src="{pre}assets/js/site.js"></script>
</body>
</html>
'''

def card(n):
    pre=""
    cta = "Read story →" if n["form"]=="article" else "See photos →"
    badge = f' <span class="ncard__badge">{n["badge"]}</span>' if n.get("badge") else ""
    return f'''      <a class="ncard" href="{n['slug']}/">
        <div class="ncard__img"><img src="../news-img/{n['slug']}.jpg" alt="{html.escape(n['title_en'])}" loading="lazy"></div>
        <div class="ncard__b">
          <span class="ncard__date">{n['date_en']}{badge}</span>
          <div class="ncard__title">{n['title_en']}<small>{n['title_zh']}</small></div>
          <div class="ncard__cta">{cta} <span>→</span></div>
        </div>
      </a>'''

def index_page():
    pre="../"
    highlights=[n for n in NEWS if n["form"]=="article"]
    life=[n for n in NEWS if n["form"]=="photo"]
    hi = "\n".join(card(n) for n in highlights)
    li = "\n".join(card(n) for n in life)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>News · 最新消息 — FengChou Elementary</title>
<meta name="description" content="School stories and news from FengChou Elementary — national tug-of-war champions, Children's Day, food &amp; farming, storytelling and more. 豐洲國小校園故事與最新消息。">
{FONT}
<link rel="stylesheet" href="{pre}assets/css/main.css">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
</head>
<body>

{topbar(pre,'news')}

<header class="page-hero ph-news">
  <div class="wrap">
    <span class="eyebrow">News &amp; Stories · 最新消息</span>
    <h1>From the FengChou Campus<span class="zh">豐洲的校園故事</span></h1>
    <p class="tagline">Champions, celebrations, and everyday learning — told in English and Chinese.<span class="zh">冠軍、慶典，與每一天的學習——用英文和中文說給你聽。</span></p>
  </div>
</header>

<section class="news-section">
  <div class="wrap">
    <p class="news-intro">A bilingual selection of recent stories from our school. Tap a card to read more or see the photos.<span class="zh">校園近期故事的中英文精選。點一張卡片，看更多文字或照片。</span></p>

    <div class="group-head"><div class="icon">🏆</div><h3>Champions &amp; Highlights<small>榮耀與焦點</small></h3></div>
    <div class="news-grid">
{hi}
    </div>

    <div class="group-head"><div class="icon">📸</div><h3>Campus Life<small>校園生活 — 看照片</small></h3></div>
    <div class="news-grid">
{li}
    </div>
  </div>
</section>

{FOOTER}
<script src="{pre}assets/js/site.js"></script>
</body>
</html>
'''

# ---- write ----
os.makedirs(os.path.join(ROOT,"news"), exist_ok=True)
open(os.path.join(ROOT,"news","index.html"),"w").write(index_page())
for n in NEWS:
    d=os.path.join(ROOT,"news",n["slug"]); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w").write(detail_page(n))
print("Wrote news/index.html +", len(NEWS), "detail pages")
for n in NEWS:
    print(" ", n["slug"], n["form"], len(gallery_imgs(n["slug"],"")), "imgs")
