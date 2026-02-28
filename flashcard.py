"""
艾宾浩斯闪卡系统
- seed_cards(): 从 episodes_data 导入所有 ammo 卡片到 SQLite
- SM-2 算法:    根据用户反馈（pass/fail）更新复习间隔
- get_due_card(): 优先返回最旧的到期卡，无到期卡则返回新卡
- push_card():  通过 ntfy.sh 推送安卓通知（带可交互按钮）
- start_scheduler(): 每天定时触发推送
"""

import os
import sqlite3
import httpx
from datetime import date, datetime, timedelta
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

load_dotenv()

# ── 配置 ─────────────────────────────────────────────────────────────────────

NTFY_TOPIC = os.getenv("NTFY_TOPIC", "")
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "http://localhost:8080").rstrip("/")
PUSH_HOUR = int(os.getenv("PUSH_HOUR", "8"))
PUSH_MINUTE = int(os.getenv("PUSH_MINUTE", "0"))
NTFY_SERVER = os.getenv("NTFY_SERVER", "https://ntfy.sh")

BASE = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE, "peppa.db")


# ── 数据库 ────────────────────────────────────────────────────────────────────

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_flashcard_table():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            ep_num       INTEGER NOT NULL,
            sentence     TEXT    NOT NULL,
            zh           TEXT    NOT NULL,
            usage        TEXT    NOT NULL DEFAULT '',
            interval     INTEGER NOT NULL DEFAULT 1,
            easiness     REAL    NOT NULL DEFAULT 2.5,
            repetitions  INTEGER NOT NULL DEFAULT 0,
            next_review  TEXT    NOT NULL DEFAULT (date('now')),
            last_pushed  TEXT
        )
    """)
    conn.commit()
    conn.close()


def seed_cards():
    """从 episodes_data 提取所有 ammo 卡片写入数据库（幂等）。"""
    from episodes_data import EPISODES_LIST

    init_flashcard_table()
    conn = get_conn()

    inserted = 0
    for ep in EPISODES_LIST:
        ep_num = ep["num"]
        for item in ep.get("ammo", []):
            sentence = item.get("sentence", "").strip()
            zh = item.get("zh", "").strip()
            usage = item.get("usage", "").strip()
            if not sentence:
                continue
            existing = conn.execute(
                "SELECT id FROM flashcards WHERE ep_num=? AND sentence=?",
                (ep_num, sentence),
            ).fetchone()
            if existing:
                continue
            conn.execute(
                "INSERT INTO flashcards (ep_num, sentence, zh, usage) VALUES (?, ?, ?, ?)",
                (ep_num, sentence, zh, usage),
            )
            inserted += 1

    conn.commit()
    conn.close()
    logger.info(f"seed_cards: 新入库 {inserted} 张卡片")
    return inserted


# ── SM-2 算法 ─────────────────────────────────────────────────────────────────

def _sm2_next(interval: int, easiness: float, repetitions: int, result: str):
    """
    SM-2 算法核心。
    result: "pass" = 记住了（q=4），"fail" = 没记住（q=1）
    返回: (new_interval, new_easiness, new_repetitions, next_review_date_str)
    """
    q = 4 if result == "pass" else 1

    if q >= 3:
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = round(interval * easiness)
        new_repetitions = repetitions + 1
    else:
        new_interval = 1
        new_repetitions = 0

    new_easiness = easiness + 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)
    new_easiness = max(1.3, new_easiness)

    next_review = (date.today() + timedelta(days=new_interval)).isoformat()
    return new_interval, round(new_easiness, 4), new_repetitions, next_review


def update_sm2(card_id: int, result: str) -> dict:
    """更新卡片 SM-2 状态，返回更新后的卡片数据。"""
    conn = get_conn()
    row = conn.execute("SELECT * FROM flashcards WHERE id=?", (card_id,)).fetchone()
    if not row:
        conn.close()
        raise ValueError(f"Card {card_id} not found")

    new_interval, new_easiness, new_reps, next_review = _sm2_next(
        row["interval"], row["easiness"], row["repetitions"], result
    )

    conn.execute(
        """UPDATE flashcards
           SET interval=?, easiness=?, repetitions=?, next_review=?
           WHERE id=?""",
        (new_interval, new_easiness, new_reps, next_review, card_id),
    )
    conn.commit()

    updated = dict(conn.execute("SELECT * FROM flashcards WHERE id=?", (card_id,)).fetchone())
    conn.close()

    emoji = "✅" if result == "pass" else "🔄"
    logger.info(
        f"{emoji} 卡片#{card_id} [{result}] → 下次复习: {next_review}（{new_interval}天后）"
    )
    return updated


# ── 卡片选取 ──────────────────────────────────────────────────────────────────

def get_due_card() -> dict | None:
    """
    选取今日推送卡片：
    1. 优先取 next_review <= 今天 且 last_pushed != 今天 的最旧卡片
    2. 没有到期卡则取从未推送过（last_pushed IS NULL）的最新加入卡片
    """
    conn = get_conn()
    today = date.today().isoformat()

    # 已到期但今天未推送
    row = conn.execute(
        """SELECT * FROM flashcards
           WHERE next_review <= ? AND (last_pushed IS NULL OR last_pushed < ?)
           ORDER BY next_review ASC
           LIMIT 1""",
        (today, today),
    ).fetchone()

    # 全新卡片（从未推送）
    if not row:
        row = conn.execute(
            """SELECT * FROM flashcards
               WHERE last_pushed IS NULL
               ORDER BY id ASC
               LIMIT 1"""
        ).fetchone()

    conn.close()
    return dict(row) if row else None


def mark_pushed(card_id: int):
    """记录本次推送时间。"""
    conn = get_conn()
    now = datetime.now().isoformat(timespec="seconds")
    conn.execute("UPDATE flashcards SET last_pushed=? WHERE id=?", (now, card_id))
    conn.commit()
    conn.close()


# ── ntfy 推送 ─────────────────────────────────────────────────────────────────

def push_card(card: dict) -> bool:
    """
    通过 ntfy.sh 推送卡片通知到安卓，带「✅ 记住了」和「❌ 没记住」两个按钮。
    返回 True 表示推送成功。
    """
    if not NTFY_TOPIC:
        logger.warning("NTFY_TOPIC 未配置，跳过推送")
        return False

    card_id = card["id"]
    pass_url = f"{PUBLIC_BASE_URL}/api/flashcard/{card_id}/review?result=pass"
    fail_url = f"{PUBLIC_BASE_URL}/api/flashcard/{card_id}/review?result=fail"

    ep_num = card["ep_num"]
    sentence = card["sentence"]
    zh = card["zh"]
    usage = card.get("usage", "")

    body_lines = [f"🗣️ {sentence}", f"📖 {zh}"]
    if usage:
        body_lines.append(f"💡 {usage}")

    body = "\n".join(body_lines)

    try:
        resp = httpx.post(
            f"{NTFY_SERVER}/{NTFY_TOPIC}",
            content=body.encode("utf-8"),
            headers={
                "Title": f"🐷 EP{ep_num} 今日英语弹药",
                "Priority": "default",
                "Tags": "peppa,english",
                "Actions": (
                    f"http, ✅ 记住了, {pass_url}, clear=true; "
                    f"http, ❌ 没记住, {fail_url}, clear=true"
                ),
            },
            timeout=10,
        )
        resp.raise_for_status()
        mark_pushed(card_id)
        logger.info(f"推送成功: 卡片#{card_id} 「{sentence[:20]}...」")
        return True
    except Exception as e:
        logger.error(f"推送失败: {e}")
        return False


def push_today():
    """定时任务入口：取今日卡片并推送。"""
    card = get_due_card()
    if card:
        push_card(card)
    else:
        logger.info("今日无待推送卡片")


# ── 调度器 ────────────────────────────────────────────────────────────────────

_scheduler: BackgroundScheduler | None = None


def start_scheduler():
    """启动后台定时调度器，每天 PUSH_HOUR:PUSH_MINUTE 触发推送。"""
    global _scheduler
    if _scheduler and _scheduler.running:
        return

    _scheduler = BackgroundScheduler()
    _scheduler.add_job(
        push_today,
        trigger="cron",
        hour=PUSH_HOUR,
        minute=PUSH_MINUTE,
        id="daily_push",
        replace_existing=True,
    )
    _scheduler.start()
    logger.info(f"定时推送已启动，每天 {PUSH_HOUR:02d}:{PUSH_MINUTE:02d} 推送")


def stop_scheduler():
    global _scheduler
    if _scheduler and _scheduler.running:
        _scheduler.shutdown(wait=False)


# ── 统计查询 ──────────────────────────────────────────────────────────────────

def get_stats() -> dict:
    """返回闪卡库整体统计数据。"""
    conn = get_conn()
    today = date.today().isoformat()

    total = conn.execute("SELECT COUNT(*) FROM flashcards").fetchone()[0]
    due = conn.execute(
        "SELECT COUNT(*) FROM flashcards WHERE next_review <= ?", (today,)
    ).fetchone()[0]
    new = conn.execute(
        "SELECT COUNT(*) FROM flashcards WHERE last_pushed IS NULL"
    ).fetchone()[0]
    learned = conn.execute(
        "SELECT COUNT(*) FROM flashcards WHERE repetitions >= 3"
    ).fetchone()[0]
    conn.close()

    return {
        "total": total,
        "due_today": due,
        "never_pushed": new,
        "learned": learned,
    }
