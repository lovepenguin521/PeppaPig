"""
单词库 & 句型库模块
- 建表：item_mastery / item_tips
- mastery CRUD
- review queue（不熟悉优先）
- LLM tips 生成与缓存（LangChain + OpenAI）
"""

import os
import random
import sqlite3
from datetime import datetime
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

BASE = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE, "peppa.db")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "")

MASTERY_ORDER = {"unfamiliar": 0, "normal": 1, "familiar": 2, "unknown": -1}


# ── 数据库 ────────────────────────────────────────────────────────────────────

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_library_tables():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS item_mastery (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            type       TEXT    NOT NULL,
            ep_num     INTEGER NOT NULL,
            item_key   TEXT    NOT NULL,
            mastery    TEXT    NOT NULL DEFAULT 'unknown',
            updated_at TEXT    NOT NULL,
            UNIQUE(type, ep_num, item_key)
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS item_tips (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            type     TEXT    NOT NULL,
            ep_num   INTEGER NOT NULL,
            item_key TEXT    NOT NULL,
            template TEXT    NOT NULL DEFAULT '',
            tip1     TEXT    NOT NULL DEFAULT '',
            tip2     TEXT    NOT NULL DEFAULT '',
            tip3     TEXT    NOT NULL DEFAULT '',
            UNIQUE(type, ep_num, item_key)
        )
    """)
    # 迁移：为旧表补充 template 列
    try:
        conn.execute("ALTER TABLE item_tips ADD COLUMN template TEXT NOT NULL DEFAULT ''")
        conn.commit()
    except Exception:
        pass
    conn.commit()
    conn.close()
    logger.info("library tables ready")


# ── 数据读取 ──────────────────────────────────────────────────────────────────

def get_all_items(item_type: str) -> list[dict]:
    """
    从 EPISODES_LIST 中提取所有 vocab 或 patterns，合并 DB 中的 mastery 状态。
    item_type: 'vocab' | 'pattern'
    """
    from episodes_data import EPISODES_LIST

    conn = get_conn()
    mastery_rows = conn.execute(
        "SELECT ep_num, item_key, mastery FROM item_mastery WHERE type=?",
        (item_type,),
    ).fetchall()
    conn.close()

    mastery_map: dict[tuple, str] = {
        (r["ep_num"], r["item_key"]): r["mastery"] for r in mastery_rows
    }

    items = []
    for ep in EPISODES_LIST:
        ep_num = ep["num"]
        ep_title_en = ep.get("title_en", "")
        ep_title_zh = ep.get("title_zh", "")
        ep_color = ep.get("color", "pink")

        if item_type == "vocab":
            for v in ep.get("vocab", []):
                key = v["word"]
                items.append({
                    "type": "vocab",
                    "ep_num": ep_num,
                    "ep_title_en": ep_title_en,
                    "ep_title_zh": ep_title_zh,
                    "ep_color": ep_color,
                    "item_key": key,
                    "word": v["word"],
                    "phonetic": v.get("phonetic", ""),
                    "pos": v.get("pos", ""),
                    "zh": v.get("zh", ""),
                    "action": v.get("action", ""),
                    "mastery": mastery_map.get((ep_num, key), "unknown"),
                })
        else:  # pattern
            for p in ep.get("patterns", []):
                key = p["pattern"]
                items.append({
                    "type": "pattern",
                    "ep_num": ep_num,
                    "ep_title_en": ep_title_en,
                    "ep_title_zh": ep_title_zh,
                    "ep_color": ep_color,
                    "item_key": key,
                    "pattern": p["pattern"],
                    "zh": p.get("zh", ""),
                    "example": p.get("example", ""),
                    "mastery": mastery_map.get((ep_num, key), "unknown"),
                })

    return items


# ── Mastery CRUD ──────────────────────────────────────────────────────────────

def set_mastery(item_type: str, ep_num: int, item_key: str, mastery: str) -> dict:
    """设置某词/句型的熟悉度。mastery: 'familiar' | 'normal' | 'unfamiliar'"""
    if mastery not in ("familiar", "normal", "unfamiliar"):
        raise ValueError(f"Invalid mastery: {mastery}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_conn()
    conn.execute(
        """INSERT INTO item_mastery (type, ep_num, item_key, mastery, updated_at)
           VALUES (?, ?, ?, ?, ?)
           ON CONFLICT(type, ep_num, item_key) DO UPDATE SET mastery=excluded.mastery, updated_at=excluded.updated_at""",
        (item_type, ep_num, item_key, mastery, now),
    )
    conn.commit()
    conn.close()
    return {"type": item_type, "ep_num": ep_num, "item_key": item_key, "mastery": mastery}


def get_tips_bulk(item_type: str) -> dict:
    """返回所有已缓存的 tips，key = 'ep_num:item_key'"""
    conn = get_conn()
    rows = conn.execute(
        "SELECT ep_num, item_key, template, tip1, tip2, tip3 FROM item_tips WHERE type=?",
        (item_type,),
    ).fetchall()
    conn.close()
    return {
        f"{r['ep_num']}:{r['item_key']}": {
            "template": r["template"],
            "tip1": r["tip1"],
            "tip2": r["tip2"],
            "tip3": r["tip3"],
        }
        for r in rows
        if r["tip1"]  # 只返回已生成的
    }


def get_mastery_stats() -> dict:
    """返回单词库和句型库各熟悉度的统计。"""
    from episodes_data import EPISODES_LIST
    conn = get_conn()

    stats: dict[str, dict] = {"vocab": {}, "pattern": {}}
    for item_type in ("vocab", "pattern"):
        rows = conn.execute(
            "SELECT mastery, COUNT(*) as cnt FROM item_mastery WHERE type=? GROUP BY mastery",
            (item_type,),
        ).fetchall()
        counts = {r["mastery"]: r["cnt"] for r in rows}

        total = sum(
            len(ep.get("vocab" if item_type == "vocab" else "patterns", []))
            for ep in EPISODES_LIST
        )
        marked = sum(counts.values())
        counts["unknown"] = counts.get("unknown", total - marked)
        counts["total"] = total
        stats[item_type] = counts

    conn.close()
    return stats


# ── Review Queue ──────────────────────────────────────────────────────────────

def get_review_queue(item_type: str | None = None) -> list[dict]:
    """
    返回复习队列：不熟悉 → 一般 → 未标记 → 熟悉
    item_type: None=混合, 'vocab', 'pattern'
    """
    types = ["vocab", "pattern"] if item_type is None else [item_type]
    all_items: list[dict] = []
    for t in types:
        all_items.extend(get_all_items(t))

    # 按熟悉度分组
    groups: dict[str, list[dict]] = {
        "unfamiliar": [], "unknown": [], "normal": [], "familiar": []
    }
    for item in all_items:
        m = item.get("mastery", "unknown")
        groups.setdefault(m, []).append(item)

    # 每组内部随机打乱
    queue: list[dict] = []
    for key in ("unfamiliar", "unknown", "normal", "familiar"):
        group = groups.get(key, [])
        random.shuffle(group)
        queue.extend(group)

    return queue


# ── LLM Tips ─────────────────────────────────────────────────────────────────

def _build_prompt(item_type: str, item: dict, ep_info: dict) -> str:
    ep_num = item["ep_num"]
    ep_title = f"EP{ep_num} {ep_info.get('title_en','')}（{ep_info.get('title_zh','')}))"
    synopsis = ep_info.get("synopsis", "")

    if item_type == "vocab":
        target = f"单词：{item['word']} {item.get('phonetic','')}，词性：{item.get('pos','')}，中文：{item.get('zh','')}"
        context = f"剧中场景动作：{item.get('action','')}"
        what = "单词"
        template_instruction = ""
    else:
        raw_pattern = item.get("pattern", "")
        zh = item.get("zh", "")
        example = item.get("example", "")
        target = f"原句：{raw_pattern}（{zh}）"
        context = f"剧中台词示例：{example}"
        what = "句型"
        template_instruction = f"""
第一行必须输出提炼后的句型模板（用 __ 代替可替换的词），格式：
TEMPLATE: <模板>
例如原句 "George's favourite toy is Mr Dinosaur." 应提炼为 "My favourite __ is __."
"""

    return f"""你是专业的幼儿英语启蒙顾问。以下是小猪佩奇动画中的一个英语{what}。

集数：{ep_title}
剧情：{synopsis}
{target}
{context}
{template_instruction}
请给家长提供 3 个具体的日常生活场景，让家长能把这个{what}自然地说给孩子听。

要求：
- 场景真实、具体（吃饭/洗澡/玩耍/出门/睡前等）
- 每条格式："【场景名】家长说：'英文例句'"，并附上一句中文解释，控制在30字内
- 英文例句必须用上这个{what}的核心结构
- 直接输出内容，不要多余说明

严格按以下格式输出（每行一条，共{'4' if item_type=='pattern' else '3'}行）：
{'TEMPLATE: <句型模板>' + chr(10) if item_type=='pattern' else ''}TIP1: <第1条场景>
TIP2: <第2条场景>
TIP3: <第3条场景>"""


def get_or_generate_tips(item_type: str, ep_num: int, item_key: str, item: dict, ep_info: dict) -> dict:
    """
    优先从 DB 缓存读取 tips；缓存不存在或 template 为空则调 LLM 重新生成。
    返回 {"template": ..., "tip1": ..., "tip2": ..., "tip3": ...}
    """
    conn = get_conn()
    row = conn.execute(
        "SELECT template, tip1, tip2, tip3 FROM item_tips WHERE type=? AND ep_num=? AND item_key=?",
        (item_type, ep_num, item_key),
    ).fetchone()
    conn.close()

    # 句型必须有 template，单词只需有 tip1
    if row and row["tip1"]:
        if item_type == "vocab" or row["template"]:
            return {
                "template": row["template"] or "",
                "tip1": row["tip1"],
                "tip2": row["tip2"],
                "tip3": row["tip3"],
            }

    # 调 LLM 生成
    result = _generate_tips_llm(item_type, item, ep_info)

    # 写入缓存
    conn = get_conn()
    conn.execute(
        """INSERT INTO item_tips (type, ep_num, item_key, template, tip1, tip2, tip3)
           VALUES (?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(type, ep_num, item_key) DO UPDATE SET
             template=excluded.template, tip1=excluded.tip1,
             tip2=excluded.tip2, tip3=excluded.tip3""",
        (item_type, ep_num, item_key, result["template"], result["tip1"], result["tip2"], result["tip3"]),
    )
    conn.commit()
    conn.close()

    return result


def _parse_llm_output(raw: str, item_type: str) -> dict:
    """解析 LLM 输出，提取 template / tip1 / tip2 / tip3。"""
    result = {"template": "", "tip1": "", "tip2": "", "tip3": ""}
    for line in raw.splitlines():
        line = line.strip()
        if line.upper().startswith("TEMPLATE:"):
            result["template"] = line.split(":", 1)[1].strip()
        elif line.upper().startswith("TIP1:"):
            result["tip1"] = line.split(":", 1)[1].strip()
        elif line.upper().startswith("TIP2:"):
            result["tip2"] = line.split(":", 1)[1].strip()
        elif line.upper().startswith("TIP3:"):
            result["tip3"] = line.split(":", 1)[1].strip()

    # 容错：如果解析失败，按行切割
    if not result["tip1"]:
        lines = [l.strip() for l in raw.splitlines() if l.strip()]
        for i, key in enumerate(["tip1", "tip2", "tip3"]):
            if i < len(lines):
                result[key] = lines[i]

    return result


def _generate_tips_llm(item_type: str, item: dict, ep_info: dict) -> dict:
    """调用 LangChain + OpenAI 生成模板 + 3条生活场景。"""
    if not OPENAI_API_KEY:
        logger.warning("OPENAI_API_KEY 未配置，返回默认内容")
        return _fallback_tips(item_type, item)

    try:
        from langchain_openai import ChatOpenAI
        from langchain_core.messages import HumanMessage

        kwargs: dict = {"model": "gpt-4o-mini", "api_key": OPENAI_API_KEY, "temperature": 0.7}
        if OPENAI_BASE_URL:
            kwargs["base_url"] = OPENAI_BASE_URL

        llm = ChatOpenAI(**kwargs)
        prompt = _build_prompt(item_type, item, ep_info)
        response = llm.invoke([HumanMessage(content=prompt)])
        raw = response.content.strip()
        logger.info(f"LLM 生成完成: {item_type} '{item.get('word') or item.get('pattern','')}' EP{item['ep_num']}")
        return _parse_llm_output(raw, item_type)

    except Exception as e:
        logger.error(f"LLM 生成 tips 失败: {e}")
        return _fallback_tips(item_type, item)


def _fallback_tips(item_type: str, item: dict) -> dict:
    """无 API key 时的兜底默认内容（需配置 OPENAI_API_KEY 才能获得 AI 生成版）。"""
    if item_type == "vocab":
        w = item.get("word", "")
        zh = item.get("zh", "")
        return {
            "template": "",
            "tip1": f"【户外】孩子看到相关事物，指着说：'Look! {w}!'（这就是{zh}）",
            "tip2": f"【日常】活动中自然带入：'This is so {w}!'，让孩子跟着说",
            "tip3": f"【睡前】问孩子：'Do you remember {w}? 它是什么意思？'",
        }
    else:
        p = item.get("pattern", "")
        zh = item.get("zh", "")
        # 生成简单模板：把专有名词替换为 __
        import re
        template = re.sub(r"\b[A-Z][a-z]+\b", "__", p)
        template = re.sub(r"Mr \w+", "__", template)
        return {
            "template": template,
            "tip1": f"【日常】孩子遇到相关情境，家长用这句引导：'{p}'（{zh}）",
            "tip2": f"【游戏】用这个句型造句，换成孩子喜欢的词",
            "tip3": f"【睡前】复习：家长说前半句，让孩子补完后半句",
        }
