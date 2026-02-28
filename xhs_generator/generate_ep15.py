#!/usr/bin/env python3
"""
小猪佩奇外挂 · 小红书图文生成器 · ep15 Picnic  v2
FABE框架 + 方法论包装 + 个人故事引流版
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"

# ─── ep15 数据 ────────────────────────────────────────────────────────

VOCAB_PAIRS = [
    [
        {
            "emoji": "🐝",
            "word": "wasp",
            "phonetic": "/wɒsp/",
            "meaning": "黄蜂",
            "action": "伸出一根手指飞来飞去，嘴里「Bzzzz~」",
        },
        {
            "emoji": "💪",
            "word": "exercise",
            "phonetic": "/ˈeksəsaɪz/",
            "meaning": "锻炼",
            "action": "夸张地原地跑步，越来越慢，最后瘫倒",
        },
    ],
    [
        {
            "emoji": "😋",
            "word": "delicious",
            "phonetic": "/dɪˈlɪʃəs/",
            "meaning": "美味的",
            "action": "闭眼揉肚子，发出「Mmm~」的满足声",
        },
        {
            "emoji": "😴",
            "word": "sleepy",
            "phonetic": "/ˈsliːpi/",
            "meaning": "困的",
            "action": "慢慢闭眼，头歪向一侧",
        },
    ],
]

SENTENCES = [
    {
        "num": 1,
        "pattern": "So much for...",
        "meaning": "就这？说好的呢",
        "example": "So much for Daddy Pig and his exercise.",
        "life": "So much for your homework!<br>→ 说好要写作业呢！",
    },
    {
        "num": 2,
        "pattern": "What a fuss!",
        "meaning": "大惊小怪！",
        "example": "What a fuss! It's only a little wasp.",
        "life": "What a fuss! It's just a little rain.<br>→ 大惊小怪，就下点雨嘛。",
    },
    {
        "num": 3,
        "pattern": "It's only a little...",
        "meaning": "不就是一点小…嘛",
        "example": "It's only a little wasp.",
        "life": "It's only a little scratch.<br>→ 不就是个小划痕嘛。",
    },
    {
        "num": 4,
        "pattern": "I managed to...",
        "meaning": "我（终于）设法做到了…",
        "example": "I managed to hang on to my cake.",
        "life": "I managed to finish my homework!<br>→ 我终于把作业写完了！",
    },
]

GOALS = [
    {
        "level": "最低目标 ✅",
        "desc": "孩子能用 3 个词说出剧情",
        "example": "wasp · run · cake",
        "color": "#06D6A0",
    },
    {
        "level": "中等目标 🎯",
        "desc": "孩子能用 3 句话讲故事",
        "example": "哪怕中英混杂也算！",
        "color": "#FFB347",
    },
    {
        "level": "理想目标 🌟",
        "desc": "孩子主动用句型造新句",
        "example": "So much for... / It's only a...",
        "color": "#FF6B9D",
    },
]

STORY = [
    "Daddy Pig said he wanted to exercise.",
    "But he fell asleep at the picnic!",
    "A wasp chased him — he ran so fast.",
    "So much for exercising, Daddy Pig! 😂",
]
STORY_COLORS = ["#06D6A0", "#FFB347", "#FF6B9D", "#6C63FF"]

PHASES = [
    ("🔥", "IGNITE", "点火",  "3min",  "#FF6B35", "激发好奇，孩子主动要看"),
    ("📺", "WATCH",  "观看",  "6min",  "#118AB2", "带任务看，每秒都有目的"),
    ("💬", "REACT",  "反应",  "5min",  "#6C63FF", "外教式聊天，孩子自然开口"),
    ("🎮", "PLAY",   "玩起来","12min", "#06D6A0", "TPR+配音，身体记住忘不了"),
    ("🎤", "OUTPUT", "输出",  "3min",  "#FF6B9D", "3句话讲完整故事"),
    ("🔒", "LOCK",   "锁定",  "1min",  "#2D2D2D", "拼读规律+悬念，下次还想学"),
]

# ─── 公共工具 ──────────────────────────────────────────────────────────

FONT = "'PingFang SC', 'Noto Sans SC', 'Microsoft YaHei', Helvetica, sans-serif"


def wrap(body: str) -> str:
    return (
        f'<!DOCTYPE html><html><head><meta charset="UTF-8"><style>'
        f"* {{margin:0;padding:0;box-sizing:border-box;}}"
        f"body {{width:1080px;height:1080px;font-family:{FONT};overflow:hidden;}}"
        f"</style></head><body>{body}</body></html>"
    )


def brand(color: str = "rgba(255,255,255,0.65)") -> str:
    return (
        f'<div style="position:absolute;bottom:28px;left:50%;'
        f"transform:translateX(-50%);color:{color};"
        f'font-size:22px;letter-spacing:6px;white-space:nowrap;">'
        f"小猪佩奇外挂 · 第15集 Picnic</div>"
    )


# ─── Post A 卡片（粉色主题）────────────────────────────────────────────
# FABE: E（亲历故事）→ B（30分钟开口）→ A（省钱不费妈）→ F（6步法脚本）


def cover_a() -> str:
    """个人故事钩子：5季·2年·0句话"""
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;
  background:linear-gradient(145deg,#FF4E8A 0%,#FF7AA4 45%,#FFA0BC 75%,#FFD0DF 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding:68px;">
  <div style="position:absolute;width:380px;height:380px;border-radius:50%;
    background:rgba(255,255,255,0.07);top:-100px;right:-90px;"></div>
  <div style="position:absolute;width:260px;height:260px;border-radius:50%;
    background:rgba(255,255,255,0.07);bottom:40px;left:-60px;"></div>

  <div style="background:rgba(255,255,255,0.22);border-radius:50px;padding:12px 32px;margin-bottom:32px;">
    <span style="color:white;font-size:28px;letter-spacing:2px;">👨‍👩‍👧 创作者亲历故事</span>
  </div>

  <div style="background:rgba(0,0,0,0.15);border-radius:16px;padding:18px 44px;margin-bottom:32px;">
    <div style="color:white;font-size:48px;font-weight:800;letter-spacing:6px;text-align:center;">
      5季 · 2年 · 0句话
    </div>
  </div>

  <div style="text-align:center;margin-bottom:36px;">
    <div style="font-size:64px;font-weight:800;color:white;line-height:1.3;
      text-shadow:0 4px 20px rgba(0,0,0,0.15);">
      我家孩子看了<br>5季小猪佩奇<br>最后去看中文动画了
    </div>
  </div>

  <div style="background:rgba(255,255,255,0.18);border-radius:20px;padding:24px 48px;text-align:center;">
    <div style="color:white;font-size:30px;line-height:1.85;">
      缺的不是内容，是<strong>方法</strong><br>
      <span style="font-size:26px;opacity:0.85;">磨了N个版本，才打磨出这套 👇</span>
    </div>
  </div>

  {brand()}
</div>"""
    )


def pain_card() -> str:
    """为什么看了那么多还是说不出来"""
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:#FFF0F5;
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#FF4E8A,#FF85A2);height:160px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:white;font-size:38px;font-weight:700;">
      看了那么多，为什么还是说不出来？
    </span>
  </div>

  <div style="flex:1;padding:48px 60px;display:flex;flex-direction:column;gap:28px;justify-content:center;">

    <div style="display:flex;gap:24px;">
      <div style="flex:1;background:white;border-radius:20px;padding:28px 32px;
        border:3px solid #FFB3CC;">
        <div style="font-size:28px;font-weight:700;color:#CC4477;margin-bottom:16px;">
          ❌ 大多数家庭
        </div>
        <div style="font-size:26px;color:#555;line-height:2;">
          打开动画 → 孩子看<br>
          孩子笑 → 关掉<br>
          第二天 → 忘了<br>
          再看 → 再笑 → 再忘...<br>
          <strong style="color:#CC4477;">循环 = 零英语输出</strong>
        </div>
      </div>
      <div style="flex:1;background:white;border-radius:20px;padding:28px 32px;
        border:3px solid #06D6A0;">
        <div style="font-size:28px;font-weight:700;color:#05A080;margin-bottom:16px;">
          ✅ 加上6步方法
        </div>
        <div style="font-size:26px;color:#555;line-height:2;">
          🔥 IGNITE → 孩子想看<br>
          📺 WATCH → 带任务看<br>
          💬 REACT → 孩子开口<br>
          🎤 OUTPUT → 讲完整故事<br>
          <strong style="color:#05A080;">相同动画 = 英语输出</strong>
        </div>
      </div>
    </div>

    <div style="background:white;border-radius:16px;padding:28px 36px;
      border-left:7px solid #FF6B9D;">
      <div style="font-size:30px;color:#2D2D2D;font-weight:600;line-height:1.65;">
        💡 缺的不是内容——<br>
        <span style="color:#FF4E8A;">缺的是看完动画之后的6个步骤。</span>
      </div>
    </div>

    <div style="background:#FFF5D6;border-radius:16px;padding:20px 32px;text-align:center;">
      <div style="font-size:28px;color:#664400;line-height:1.6;">
        外教课300元/小时，贵的不是英语水平<br>
        <strong>贵的是那套让孩子开口的方法</strong>
      </div>
    </div>
  </div>
  {brand("rgba(200,100,130,0.5)")}
</div>"""
    )


def sentence_card(s: dict) -> str:
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:#FFF0F5;
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#FF4E8A,#FF85A2);height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:rgba(255,255,255,0.65);font-size:28px;margin-right:auto;">
      句型 {s['num']:02d} / 04
    </span>
    <span style="color:white;font-size:32px;font-weight:600;">地道英语 · 学完能用一辈子</span>
  </div>
  <div style="flex:1;padding:52px 60px;display:flex;flex-direction:column;
    justify-content:center;gap:36px;">
    <div style="background:linear-gradient(135deg,#FF4E8A,#FF85A2);border-radius:20px;
      padding:32px 44px;text-align:center;">
      <div style="font-size:64px;font-weight:800;color:white;font-style:italic;">
        {s['pattern']}
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:20px;">
      <div style="width:6px;height:64px;background:#FF6B9D;border-radius:3px;flex-shrink:0;"></div>
      <div>
        <div style="color:#AAA;font-size:24px;margin-bottom:6px;">中文意思</div>
        <div style="color:#2D2D2D;font-size:44px;font-weight:700;">{s['meaning']}</div>
      </div>
    </div>
    <div style="background:white;border-radius:16px;padding:28px 36px;
      border-left:7px solid #FF6B9D;">
      <div style="color:#FF6B9D;font-size:24px;font-weight:600;margin-bottom:10px;">
        📺 剧中例句
      </div>
      <div style="color:#2D2D2D;font-size:36px;font-style:italic;line-height:1.5;">
        "{s['example']}"
      </div>
    </div>
    <div style="background:#FFF5D6;border-radius:16px;padding:28px 36px;">
      <div style="color:#CC8800;font-size:24px;font-weight:600;margin-bottom:10px;">
        💬 生活中这样用
      </div>
      <div style="color:#664400;font-size:32px;line-height:1.6;">{s['life']}</div>
    </div>
  </div>
  {brand("rgba(200,100,130,0.5)")}
</div>"""
    )


def vocab_card(pair: list) -> str:
    items = ""
    for v in pair:
        items += (
            f'<div style="background:white;border-radius:20px;padding:36px 44px;'
            f'box-shadow:0 4px 20px rgba(255,107,157,0.1);">'
            f'<div style="display:flex;align-items:center;flex-wrap:wrap;gap:16px;margin-bottom:16px;">'
            f'<span style="font-size:52px;">{v["emoji"]}</span>'
            f'<span style="font-size:52px;font-weight:800;color:#2D2D2D;">{v["word"]}</span>'
            f'<span style="font-size:28px;color:#FF6B9D;">{v["phonetic"]}</span>'
            f'<div style="margin-left:auto;background:#FFE4EF;border-radius:10px;'
            f'padding:8px 20px;white-space:nowrap;">'
            f'<span style="font-size:32px;font-weight:700;color:#FF4E8A;">{v["meaning"]}</span>'
            f"</div></div>"
            f'<div style="border-top:2px dashed #FFB3CC;padding-top:16px;">'
            f'<span style="color:#FF6B9D;font-size:24px;font-weight:600;">🎭 动作记忆：</span>'
            f'<span style="color:#444;font-size:28px;">{v["action"]}</span>'
            f"</div></div>"
        )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:#FFF0F5;
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#FF4E8A,#FF85A2);height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:white;font-size:38px;font-weight:700;">🎴 本集词汇 · 身体记忆法</span>
  </div>
  <div style="flex:1;padding:56px 60px;display:flex;flex-direction:column;
    justify-content:center;gap:40px;">
    {items}
  </div>
  {brand("rgba(200,100,130,0.5)")}
</div>"""
    )


def cost_compare_card() -> str:
    """FABE算账对比卡"""
    cols = [
        ("#FFE4E4", "#CC3333", "外教一对一", "300元/小时", "1年 ≈ 12,000+元", "外教质量不稳定", "孩子坐不住", "✗"),
        ("#FFF3E0", "#CC6600", "线上开口课", "2,000元起/期", "N期循环收费", "盯屏幕伤眼睛", "效果全靠自觉", "✗"),
        ("#E8FFF4", "#05A080", "这套方案", "几毛/集打印费", "一次性，全集通用", "亲子互动有温度", "30分钟可验证", "✅"),
    ]
    cols_html = ""
    for bg, color, name, price, cost, note1, note2, mark in cols:
        cols_html += (
            f'<div style="flex:1;background:{bg};border-radius:20px;padding:28px 24px;'
            f'text-align:center;border:3px solid {color};">'
            f'<div style="font-size:28px;font-weight:800;color:{color};margin-bottom:12px;">{name}</div>'
            f'<div style="font-size:36px;font-weight:900;color:{color};margin-bottom:8px;">{price}</div>'
            f'<div style="font-size:22px;color:#666;margin-bottom:20px;line-height:1.5;">{cost}</div>'
            f'<div style="font-size:22px;color:#555;margin-bottom:8px;">{note1}</div>'
            f'<div style="font-size:22px;color:#555;margin-bottom:16px;">{note2}</div>'
            f'<div style="font-size:48px;">{mark}</div>'
            f"</div>"
        )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:#FFF0F5;
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#FF4E8A,#FF85A2);height:160px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:white;font-size:40px;font-weight:700;">💰 算一笔账，看完你就明白了</span>
  </div>
  <div style="flex:1;padding:44px 52px;display:flex;flex-direction:column;justify-content:center;gap:28px;">
    <div style="display:flex;gap:20px;">
      {cols_html}
    </div>
    <div style="background:white;border-radius:16px;padding:24px 36px;text-align:center;
      box-shadow:0 4px 16px rgba(255,107,157,0.12);">
      <div style="font-size:32px;font-weight:800;color:#FF4E8A;line-height:1.6;">
        高中英语水平就够 · 不需备课 · 不费妈
      </div>
      <div style="font-size:26px;color:#888;margin-top:8px;">
        每集约8张A4，打印费不到1块钱
      </div>
    </div>
  </div>
  {brand("rgba(200,100,130,0.5)")}
</div>"""
    )


def cta_card(post_type: str) -> str:
    items_map = {
        "hook": [
            "完整30分钟脚本，按步骤照着念",
            "4句地道英语 · 7个KET词汇 · 6个游戏",
            "每集约8张A4 · 打印费不到1块钱",
        ],
        "tutorial": [
            "Phase 1-6 完整脚本，高中英语即可",
            "孩子反应应对表 · 自然拼读规律卡",
            "每集约8张A4 · 打印即用",
        ],
        "result": [
            "我家孩子用过的，真实有效",
            "不需要英语好 · 不需要备课",
            "几毛打印费 = 30分钟专业外教课",
        ],
    }
    checks = "".join(
        f'<div style="color:white;font-size:30px;line-height:2;font-weight:500;">✓ {l}</div>'
        for l in items_map[post_type]
    )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;
  background:linear-gradient(145deg,#FF4E8A 0%,#FF7AA4 40%,#FFA0BC 75%,#FFD0DF 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding:80px;">
  <div style="position:absolute;width:320px;height:320px;border-radius:50%;
    background:rgba(255,255,255,0.07);top:-80px;left:-80px;"></div>
  <div style="position:absolute;width:240px;height:240px;border-radius:50%;
    background:rgba(255,255,255,0.07);bottom:60px;right:-40px;"></div>
  <div style="font-size:56px;margin-bottom:28px;">🛍️</div>
  <div style="font-size:64px;font-weight:800;color:white;text-align:center;
    line-height:1.3;margin-bottom:44px;text-shadow:0 4px 16px rgba(0,0,0,0.1);">
    想要完整版<br>打印材料？
  </div>
  <div style="background:rgba(255,255,255,0.18);border-radius:20px;padding:36px 52px;
    text-align:center;margin-bottom:44px;">
    {checks}
  </div>
  <div style="background:white;border-radius:16px;padding:22px 56px;
    box-shadow:0 8px 28px rgba(0,0,0,0.12);">
    <div style="color:#FF4E8A;font-size:38px;font-weight:800;letter-spacing:2px;">
      👆 主页购买链接
    </div>
  </div>
  {brand()}
</div>"""
    )


# ─── Post B 卡片（紫色主题）────────────────────────────────────────────
# FABE: F（6步法）→ A（外教同款流程）→ B（任何家长可用）→ E（脚本已写好）

PB = "#6C63FF"
PBG = "#F5F0FF"
PBL = "#EDE8FF"


def cover_b() -> str:
    """外教方法论：外教凭什么收300块"""
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;
  background:linear-gradient(145deg,#6C63FF 0%,#8A82FF 45%,#ADA6FF 75%,#D6D2FF 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding:72px;">
  <div style="position:absolute;width:360px;height:360px;border-radius:50%;
    background:rgba(255,255,255,0.07);top:-90px;right:-80px;"></div>
  <div style="background:rgba(255,255,255,0.2);border-radius:50px;padding:14px 36px;margin-bottom:44px;">
    <span style="color:white;font-size:30px;letter-spacing:2px;">🐷 小猪佩奇家长外挂 · 第15集</span>
  </div>
  <div style="text-align:center;margin-bottom:48px;">
    <div style="font-size:68px;font-weight:800;color:white;line-height:1.3;
      text-shadow:0 4px 20px rgba(0,0,0,0.12);">
      外教凭什么<br>收300块/小时？<br>就靠这6件事
    </div>
  </div>
  <div style="background:rgba(255,255,255,0.18);border-radius:20px;padding:28px 52px;text-align:center;">
    <div style="color:white;font-size:32px;line-height:1.85;">
      我把这6件事全写成了脚本<br>
      <span style="font-size:27px;opacity:0.85;">高中英语水平 · 照着念就行 · 不费妈</span>
    </div>
  </div>
  {brand()}
</div>"""
    )


def method_overview_card() -> str:
    """6步法全景图：核心差异化卡片"""
    rows_html = ""
    for i, (emoji, en, zh, time, color, desc) in enumerate(PHASES):
        rows_html += (
            f'<div style="display:flex;align-items:center;gap:20px;background:white;'
            f'border-radius:14px;padding:18px 28px;box-shadow:0 2px 10px rgba(108,99,255,0.07);">'
            f'<div style="width:44px;height:44px;background:{color};border-radius:50%;'
            f'display:flex;align-items:center;justify-content:center;'
            f'font-size:20px;font-weight:800;color:white;flex-shrink:0;">{i+1}</div>'
            f'<span style="font-size:32px;flex-shrink:0;">{emoji}</span>'
            f'<div style="flex:1;">'
            f'<div style="font-size:27px;font-weight:700;color:#2D2D2D;">'
            f'<span style="color:{color};">{en}</span> {zh}</div>'
            f'<div style="font-size:22px;color:#888;margin-top:2px;">{desc}</div>'
            f'</div>'
            f'<div style="background:{color};border-radius:20px;padding:4px 16px;'
            f'white-space:nowrap;flex-shrink:0;">'
            f'<span style="color:white;font-size:22px;font-weight:700;">{time}</span>'
            f'</div></div>'
        )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{PBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,{PB},#8A82FF);height:160px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <div>
      <div style="color:white;font-size:38px;font-weight:700;">6步家长外教法 · 30分钟完整课程</div>
      <div style="color:rgba(255,255,255,0.75);font-size:24px;margin-top:6px;">
        这就是外教上课的方式——每步都有完整脚本
      </div>
    </div>
  </div>
  <div style="flex:1;padding:36px 52px;display:flex;flex-direction:column;
    justify-content:center;gap:16px;">
    {rows_html}
    <div style="background:{PB};border-radius:14px;padding:16px 28px;text-align:center;margin-top:4px;">
      <div style="color:white;font-size:28px;font-weight:700;">
        高中英语水平即可 · 不需备课 · 不费妈
      </div>
    </div>
  </div>
  {brand("rgba(108,99,255,0.5)")}
</div>"""
    )


def step1_card() -> str:
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{PBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,{PB},#8A82FF);height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <div>
      <div style="color:rgba(255,255,255,0.65);font-size:24px;">Step 01 · IGNITE 点火</div>
      <div style="color:white;font-size:38px;font-weight:700;">让孩子主动要看——而不是被动坐着</div>
    </div>
  </div>
  <div style="flex:1;padding:48px 60px;display:flex;flex-direction:column;gap:28px;justify-content:center;">
    <div style="background:{PBL};border-radius:14px;padding:24px 32px;">
      <div style="color:{PB};font-size:24px;font-weight:600;margin-bottom:10px;">🧠 外教为什么先"点火"？</div>
      <div style="color:#333;font-size:28px;line-height:1.65;">
        孩子有「纠正大人」的本能。先故意说错，让孩子纠正——<br>
        大脑进入主动状态，上集词汇同时复盘，<strong>耗时20秒</strong>。
      </div>
    </div>
    <div style="background:white;border-radius:16px;padding:28px 36px;
      box-shadow:0 4px 16px rgba(108,99,255,0.1);">
      <div style="color:{PB};font-size:26px;font-weight:700;margin-bottom:14px;">👨 家长这样说（表情严肃）：</div>
      <div style="background:{PBG};border-radius:10px;padding:18px 24px;
        font-size:32px;color:#2D2D2D;font-style:italic;line-height:1.6;margin-bottom:14px;">
        「上次 Peppa 在泥坑跳，<br>
        Daddy Pig 说：'I am very
        <span style="color:#E53935;text-decoration:underline;">CLEAN</span>！'」
      </div>
      <div style="color:#999;font-size:24px;">（故意把 dirty 说成 clean，表情认真）</div>
    </div>
    <div style="background:white;border-radius:16px;padding:28px 36px;
      box-shadow:0 4px 16px rgba(108,99,255,0.1);">
      <div style="color:#06D6A0;font-size:26px;font-weight:700;margin-bottom:12px;">👧 孩子 99% 会喊：</div>
      <div style="font-size:40px;color:#2D2D2D;font-weight:700;margin-bottom:10px;">
        「不对！是 dirty！/ muddy！」
      </div>
      <div style="color:#06D6A0;font-size:28px;font-weight:500;">✓ 上集词汇复盘完成，耗时 20 秒！</div>
    </div>
  </div>
  {brand("rgba(108,99,255,0.5)")}
</div>"""
    )


def step3_card() -> str:
    rows_data = [
        ("孩子说 No / 摇头", "NO！Zero exercise！He just... Zzzzz！<br>So much for Daddy Pig！"),
        ("孩子说 Yes / 点头", "He exercised?! Wait — the WASP made him<br>run. Does that count?！"),
        ("孩子不说话", "家长先演：举拳头 → 立刻假装睡着<br>再问 'Did he? YES or NO?'"),
    ]
    rows_html = ""
    for label, response in rows_data:
        rows_html += (
            f'<div style="display:flex;border-radius:14px;overflow:hidden;'
            f'box-shadow:0 2px 10px rgba(108,99,255,0.07);">'
            f'<div style="background:{PBL};padding:20px 24px;width:252px;flex-shrink:0;'
            f'display:flex;align-items:center;">'
            f'<div style="color:{PB};font-size:25px;font-weight:600;line-height:1.4;">{label}</div>'
            f"</div>"
            f'<div style="background:white;padding:20px 28px;flex:1;display:flex;align-items:center;">'
            f'<div style="color:#333;font-size:25px;line-height:1.5;font-style:italic;">{response}</div>'
            f"</div></div>"
        )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{PBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,{PB},#8A82FF);height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <div>
      <div style="color:rgba(255,255,255,0.65);font-size:24px;">Step 03 · REACT 反应</div>
      <div style="color:white;font-size:38px;font-weight:700;">外教式聊天——任何反应都有接话</div>
    </div>
  </div>
  <div style="flex:1;padding:44px 60px;display:flex;flex-direction:column;gap:20px;justify-content:center;">
    <div style="color:{PB};font-size:28px;font-weight:600;margin-bottom:4px;">
      💬 问孩子："Did Daddy Pig actually exercise? Yes or no?"
    </div>
    {rows_html}
    <div style="background:{PBL};border-radius:14px;padding:20px 28px;text-align:center;">
      <div style="color:{PB};font-size:26px;font-weight:700;">
        💡 外教的秘密：不考试，不问"学会了吗"<br>让孩子觉得在聊天——他自然就开口了
      </div>
    </div>
  </div>
  {brand("rgba(108,99,255,0.5)")}
</div>"""
    )


# ─── Post C 卡片（绿色主题）────────────────────────────────────────────
# FABE: E（结果证明）→ B（转变）→ F（材料内容）→ A（省钱省力）

CG = "#06D6A0"
CBG = "#F0FFF8"
CGL = "#E0FFF4"


def cover_c() -> str:
    """转变故事：英语一般的妈妈 + 看了2年的孩子 → 30分钟开口"""
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;
  background:linear-gradient(145deg,#05C091 0%,#06D6A0 40%,#3DE3B5 72%,#7EEDCC 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding:72px;">
  <div style="position:absolute;width:320px;height:320px;border-radius:50%;
    background:rgba(255,255,255,0.07);top:-70px;right:-70px;"></div>
  <div style="background:rgba(255,255,255,0.2);border-radius:50px;padding:14px 36px;margin-bottom:40px;">
    <span style="color:white;font-size:30px;letter-spacing:2px;">🐷 小猪佩奇家长外挂 · 第15集</span>
  </div>
  <div style="text-align:center;margin-bottom:44px;">
    <div style="font-size:60px;font-weight:800;color:white;line-height:1.35;
      text-shadow:0 4px 20px rgba(0,0,0,0.1);">
      英语一般的妈妈<br>
      + 看了2年没开口的孩子<br>
      =<br>
      30分钟后说出完整英语故事
    </div>
  </div>
  <div style="background:rgba(255,255,255,0.2);border-radius:20px;padding:24px 52px;text-align:center;">
    <div style="color:white;font-size:32px;line-height:1.85;">
      真实记录 · 第15集《Picnic 野餐》<br>
      <span style="font-size:27px;opacity:0.85;">打印一张A4，才花几毛钱</span>
    </div>
  </div>
  {brand()}
</div>"""
    )


def before_after_card() -> str:
    """Before/After对比：看了2年 vs 30分钟"""
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{CBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#05C091,{CG});height:160px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:white;font-size:40px;font-weight:700;">📊 同一个孩子，差别只在于方法</span>
  </div>
  <div style="flex:1;padding:48px 52px;display:flex;gap:28px;align-items:stretch;">

    <div style="flex:1;background:#F0F0F0;border-radius:24px;padding:36px 32px;
      display:flex;flex-direction:column;gap:20px;">
      <div style="font-size:32px;font-weight:800;color:#666;text-align:center;margin-bottom:8px;">
        ❌ BEFORE
      </div>
      <div style="background:white;border-radius:12px;padding:20px 24px;text-align:center;">
        <div style="font-size:48px;font-weight:900;color:#999;">2年</div>
        <div style="font-size:22px;color:#AAA;">5季 · 100集以上</div>
      </div>
      <div style="background:white;border-radius:12px;padding:20px 24px;">
        <div style="font-size:22px;color:#888;margin-bottom:8px;">孩子说了多少英语：</div>
        <div style="font-size:36px;color:#BBB;font-style:italic;text-align:center;">
          "......"
        </div>
        <div style="font-size:22px;color:#AAA;text-align:center;">（沉默）</div>
      </div>
      <div style="background:white;border-radius:12px;padding:20px 24px;text-align:center;">
        <div style="font-size:24px;color:#888;line-height:1.6;">
          看了个热闹和寂寞<br>最后去看中文动画了
        </div>
      </div>
    </div>

    <div style="flex:1;background:white;border-radius:24px;padding:36px 32px;
      display:flex;flex-direction:column;gap:20px;box-shadow:0 4px 24px rgba(6,214,160,0.15);">
      <div style="font-size:32px;font-weight:800;color:{CG};text-align:center;margin-bottom:8px;">
        ✅ AFTER
      </div>
      <div style="background:{CGL};border-radius:12px;padding:20px 24px;text-align:center;">
        <div style="font-size:48px;font-weight:900;color:{CG};">30分钟</div>
        <div style="font-size:22px;color:#05A080;">1集 · 1张A4打印</div>
      </div>
      <div style="background:{CGL};border-radius:12px;padding:20px 24px;">
        <div style="font-size:22px;color:#05A080;margin-bottom:8px;">孩子说出来的：</div>
        <div style="font-size:26px;color:#2D2D2D;font-style:italic;line-height:1.6;">
          "So much for<br>exercising, Daddy Pig!"
        </div>
      </div>
      <div style="background:{CGL};border-radius:12px;padding:20px 24px;text-align:center;">
        <div style="font-size:24px;color:#05A080;line-height:1.6;">
          主动说「下次还看英文的」<br>妈妈当时就哭了
        </div>
      </div>
    </div>

  </div>
  {brand("rgba(5,170,130,0.5)")}
</div>"""
    )


def story_card() -> str:
    items = "".join(
        f'<div style="display:flex;gap:20px;align-items:flex-start;">'
        f'<div style="width:44px;height:44px;background:{c};border-radius:50%;'
        f"display:flex;align-items:center;justify-content:center;"
        f'font-size:22px;font-weight:800;color:white;flex-shrink:0;margin-top:6px;">{i + 1}</div>'
        f'<div style="background:white;border-radius:14px;padding:20px 28px;flex:1;'
        f'box-shadow:0 2px 10px rgba(0,0,0,0.05);">'
        f'<div style="font-size:30px;color:#2D2D2D;font-style:italic;line-height:1.5;">"{s}"</div>'
        f"</div></div>"
        for i, (s, c) in enumerate(zip(STORY, STORY_COLORS))
    )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{CBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#05C091,{CG});height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <div>
      <div style="color:rgba(255,255,255,0.7);font-size:24px;">Step 05 · OUTPUT 输出</div>
      <div style="color:white;font-size:36px;font-weight:700;">孩子用4句话讲完整个故事</div>
    </div>
  </div>
  <div style="flex:1;padding:48px 60px;display:flex;flex-direction:column;gap:24px;justify-content:center;">
    <div style="color:#05C091;font-size:28px;font-weight:600;">
      🎤 孩子在 Phase 5 能说出来的故事版本：
    </div>
    {items}
    <div style="background:{CGL};border-radius:14px;padding:20px 28px;border:2px dashed {CG};">
      <div style="color:#05A080;font-size:26px;line-height:1.6;">
        💡 即使孩子说中英混杂版，也算成功！<br>
        家长用 Recast 接话，自然纠正就够了。
      </div>
    </div>
  </div>
  {brand("rgba(5,170,130,0.5)")}
</div>"""
    )


def content_card() -> str:
    items = [
        ("📋", "知识要点卡", "词汇+句型，家长30秒速览"),
        ("🎭", "Phase 1-6 完整脚本", "每句话怎么说，写好了"),
        ("🗂️", "孩子反应应对表", "任何回答都有接话方式"),
        ("🔡", "自然拼读规律", "每集提取1个，积少成多"),
        ("🎯", "3档教学目标", "随时调整，不焦虑"),
    ]
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:20px;background:white;'
        f'border-radius:14px;padding:20px 28px;box-shadow:0 2px 10px rgba(6,166,128,0.07);">'
        f'<span style="font-size:40px;flex-shrink:0;">{it[0]}</span>'
        f"<div>"
        f'<div style="font-size:30px;font-weight:700;color:#2D2D2D;">{it[1]}</div>'
        f'<div style="font-size:24px;color:#888;margin-top:4px;">{it[2]}</div>'
        f"</div></div>"
        for it in items
    )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{CBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#05C091,{CG});height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:white;font-size:38px;font-weight:700;">📦 每集打印材料包含什么？</span>
  </div>
  <div style="flex:1;padding:44px 60px;display:flex;flex-direction:column;
    justify-content:center;gap:20px;">
    {rows}
    <div style="background:{CG};border-radius:14px;padding:18px 28px;text-align:center;margin-top:8px;">
      <div style="color:white;font-size:30px;font-weight:700;">
        约8张 A4 · 打印费不到1块 · 无需备课
      </div>
    </div>
  </div>
  {brand("rgba(5,170,130,0.5)")}
</div>"""
    )


def goals_card() -> str:
    goals_html = "".join(
        f'<div style="background:white;border-radius:16px;padding:28px 36px;'
        f'box-shadow:0 4px 16px rgba(0,0,0,0.05);border-left:7px solid {g["color"]};">'
        f'<div style="font-size:34px;font-weight:800;color:{g["color"]};margin-bottom:8px;">'
        f'{g["level"]}</div>'
        f'<div style="font-size:34px;font-weight:600;color:#2D2D2D;margin-bottom:6px;">'
        f'{g["desc"]}</div>'
        f'<div style="font-size:26px;color:#888;">示例：{g["example"]}</div>'
        f"</div>"
        for g in GOALS
    )
    return wrap(
        f"""<div style="width:1080px;height:1080px;position:relative;background:{CBG};
  display:flex;flex-direction:column;">
  <div style="background:linear-gradient(135deg,#05C091,{CG});height:172px;
    flex-shrink:0;display:flex;align-items:center;padding:0 60px;">
    <span style="color:white;font-size:36px;font-weight:700;">
      🎯 这节课3档目标，达到哪档都赢
    </span>
  </div>
  <div style="flex:1;padding:52px 60px;display:flex;flex-direction:column;
    justify-content:center;gap:36px;">
    {goals_html}
  </div>
  {brand("rgba(5,170,130,0.5)")}
</div>"""
    )


# ─── 小红书文案（FABE框架）────────────────────────────────────────────

POST_A_TEXT = """\
【标题】
我家娃看了5季小猪佩奇，最后去看中文动画了——那2年，我亏了他一个方法 🐷

【正文】
两年前，我满怀期望给孩子开了小猪佩奇英文版。

说实话，那真的是看了个热闹和寂寞。

看了5季，孩子一句英语也没说过。后来索性换成汪汪队了。

那段时间真的很挫败——花了时间，什么都没留下。

问题不在孩子。问题在我。
那2年，我根本不知道看完动画之后应该做什么。

后来我研究了职业外教的教学逻辑，反复测试，改了好几版，
才打磨出这套「6步家长外教法」。

第15集《Picnic 野餐》，我和孩子试了一遍。
30分钟后，他说出来了——

"A wasp chased Daddy Pig. So much for exercising!"

这4句话，以前他一句都说不出来：
① So much for... → 就这？说好的呢
② What a fuss! → 大惊小怪！
③ It's only a little... → 不就是一点小…嘛
④ I managed to... → 我终于做到了

完整脚本材料 → 主页购买链接 👆

【账怎么算】
外教课：300元/小时
这套方案：几毛打印费/集
高中英语水平就够 · 不需备课 · 不费妈

【Tags】
#小猪佩奇英语 #英语启蒙踩坑 #家庭英语启蒙 #亲子英语 #儿童英语 #英语口语 #双语启蒙 #小猪佩奇 #英语学习方法 #家长陪读
"""

POST_B_TEXT = """\
【标题】
外教凭什么收300块/小时？就靠这6件事——我全给你写成了脚本 🎓

【正文】
外教贵，不是因为他英语比你好多少。

贵在他知道如何让孩子开口。

我研究了职业外教的上课流程，发现他们每节课都做这6件事：

🔥 第1步 IGNITE 点火（3分钟）
不是直接开电视——先让孩子「主动想看」。
用一个故意说错的句子，激活大脑，同时复盘上集词汇。

📺 第2步 WATCH 观看（6分钟）
不是傻看——是带着「任务」看。
孩子有目标，注意力全程在线。

💬 第3步 REACT 反应（5分钟）
外教式聊天：不考试，不问"你学会了吗"。
孩子觉得是在聊天，自然就开口了。

🎮 第4步 PLAY 玩起来（12分钟）
TPR动作记忆 + 静音配音 + Find the Bugs游戏。
身体记住的东西，忘不了。

🎤 第5步 OUTPUT 输出（3分钟）
用3句话讲完整故事——训练的是表达力，不是背诵。

🔒 第6步 LOCK 锁定（1分钟）
自然拼读规律 + 下集悬念——孩子主动要继续学。

我把这6步的完整脚本都写好了。

高中英语水平就够。照着念就行。不需备课。

完整材料 → 主页链接 👆

【Tags】
#英语启蒙方法 #6步外教法 #家庭英语 #小猪佩奇英语 #儿童英语启蒙 #亲子英语 #家长陪读 #英语学习方法 #双语家庭 #英语启蒙
"""

POST_C_TEXT = """\
【标题】
英语一般的妈妈 + 看了2年没开口的孩子 → 30分钟后说出完整英语故事 🎉（真实记录）

【正文】
我家孩子看了整整2年小猪佩奇。

一句英语都没说过。

后来去看中文动画了。

那段时间我真的很挫败，总觉得是自己没给孩子创造好的语言环境。

后来我研究了职业外教的上课方式，打磨了好几版方法，
做出了这套「6步家长外教法」的完整打印材料。

上周我们试了第15集《Picnic 野餐》。
30分钟后，孩子说出来了——

1️⃣ "Daddy Pig said he wanted to exercise."
2️⃣ "But he fell asleep at the picnic!"
3️⃣ "A wasp chased him — he ran so fast."
4️⃣ "So much for exercising, Daddy Pig! 😂"

然后他说：「妈妈下次我们还看英文的」。

我当时眼眶红了。

我的英语水平，普通到不行。
我没有给孩子请外教，没有报任何课程。
我只是打印了一张A4纸，才花了几毛钱。

第15集打印材料开放购买 → 主页链接 👆

【Tags】
#小猪佩奇英语 #英语启蒙 #亲子英语 #家庭英语 #儿童英语 #英语学习 #小猪佩奇 #双语启蒙 #家长陪读 #英语口语
"""


# ─── 主程序 ───────────────────────────────────────────────────────────


async def main() -> None:
    for folder in ["ep15_post1_hook", "ep15_post2_tutorial", "ep15_post3_result"]:
        (OUTPUT_DIR / folder).mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        async def shot(html: str, path: Path) -> None:
            await page.set_viewport_size({"width": 1080, "height": 1080})
            await page.set_content(html, wait_until="domcontentloaded")
            await page.wait_for_timeout(300)
            await page.screenshot(
                path=str(path),
                clip={"x": 0, "y": 0, "width": 1080, "height": 1080},
            )
            print(f"  ✓ {path.name}")

        # ── Post 1: 痛点钩子帖（粉色）FABE ──────────────────────────
        # E(故事) → F(句型) → A(算账) → CTA
        d = OUTPUT_DIR / "ep15_post1_hook"
        print("\n📱 Post 1: 痛点钩子帖（粉色）")
        await shot(cover_a(),              d / "01_cover.png")
        await shot(pain_card(),            d / "02_pain_为什么看了说不出来.png")
        for i, s in enumerate(SENTENCES, start=3):
            await shot(sentence_card(s),   d / f"{i:02d}_sentence.png")
        await shot(vocab_card(VOCAB_PAIRS[0]), d / "07_vocab.png")
        await shot(cost_compare_card(),    d / "08_cost_算一笔账.png")
        await shot(cta_card("hook"),       d / "09_cta.png")
        (d / "小红书文案.txt").write_text(POST_A_TEXT, encoding="utf-8")
        print("  ✓ 小红书文案.txt")

        # ── Post 2: 方法论帖（紫色）FABE ────────────────────────────
        # F(6步法) → A(外教同款) → B(照着念)
        d = OUTPUT_DIR / "ep15_post2_tutorial"
        print("\n📱 Post 2: 方法论帖（紫色）")
        await shot(cover_b(),              d / "01_cover.png")
        await shot(method_overview_card(), d / "02_method_6步法总览.png")
        await shot(step1_card(),           d / "03_step1_IGNITE点火.png")
        await shot(step3_card(),           d / "04_step3_REACT外教聊天.png")
        await shot(story_card(),           d / "05_output_孩子讲故事.png")
        await shot(cta_card("tutorial"),   d / "06_cta.png")
        (d / "小红书文案.txt").write_text(POST_B_TEXT, encoding="utf-8")
        print("  ✓ 小红书文案.txt")

        # ── Post 3: 结果帖（绿色）FABE ──────────────────────────────
        # E(Before/After) → B(孩子开口) → F(材料内容)
        d = OUTPUT_DIR / "ep15_post3_result"
        print("\n📱 Post 3: 结果帖（绿色）")
        await shot(cover_c(),              d / "01_cover.png")
        await shot(before_after_card(),    d / "02_before_after_对比.png")
        await shot(story_card(),           d / "03_story_故事输出.png")
        await shot(content_card(),         d / "04_content_材料内容.png")
        await shot(cta_card("result"),     d / "05_cta.png")
        (d / "小红书文案.txt").write_text(POST_C_TEXT, encoding="utf-8")
        print("  ✓ 小红书文案.txt")

        await browser.close()

    print(f"\n✅ 全部生成完成！共 20 张图片 + 3 份文案")
    print(f"📁 输出目录：{OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
