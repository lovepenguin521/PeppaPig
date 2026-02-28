from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import os
from contextlib import asynccontextmanager

from episodes_data import EPISODES_LIST, EPISODES_BY_NUM
import flashcard as fc
import library as lib

BASE = os.path.dirname(__file__)
DB_PATH = os.environ.get("DB_PATH", os.path.join(BASE, "peppa.db"))
STATIC_DIR = os.path.join(BASE, "static")
TEMPLATES_DIR = os.path.join(BASE, "templates")

templates = Jinja2Templates(directory=TEMPLATES_DIR)


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            ep_num      INTEGER NOT NULL DEFAULT 15,
            phase_id    TEXT    NOT NULL,
            reaction    TEXT    NOT NULL DEFAULT '',
            score       INTEGER NOT NULL DEFAULT 0,
            created_at  TEXT    NOT NULL
        )
    """)
    # Migration: add ep_num if missing
    try:
        conn.execute("ALTER TABLE records ADD COLUMN ep_num INTEGER NOT NULL DEFAULT 15")
        conn.commit()
    except Exception:
        pass
    conn.commit()
    conn.close()


init_db()


@asynccontextmanager
async def lifespan(app: FastAPI):
    fc.seed_cards()
    fc.start_scheduler()
    lib.init_library_tables()
    yield
    fc.stop_scheduler()


app = FastAPI(title="小猪佩奇外挂攻略", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class RecordIn(BaseModel):
    ep_num: int
    phase_id: str
    reaction: str
    score: int


@app.post("/api/records")
def create_record(body: RecordIn):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO records (ep_num, phase_id, reaction, score, created_at) VALUES (?, ?, ?, ?, ?)",
        (body.ep_num, body.phase_id, body.reaction, body.score, now),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return {"id": row_id, "ep_num": body.ep_num, "phase_id": body.phase_id,
            "reaction": body.reaction, "score": body.score, "created_at": now}


@app.get("/api/records/{ep_num}/{phase_id}")
def get_records(ep_num: int, phase_id: str):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM records WHERE ep_num=? AND phase_id=? ORDER BY created_at DESC",
        (ep_num, phase_id),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.delete("/api/records/{record_id}")
def delete_record(record_id: int):
    conn = get_conn()
    conn.execute("DELETE FROM records WHERE id=?", (record_id,))
    conn.commit()
    conn.close()
    return {"ok": True}


@app.get("/api/episodes/stats")
def episodes_stats():
    conn = get_conn()
    rows = conn.execute(
        "SELECT ep_num, COUNT(*) as cnt FROM records GROUP BY ep_num"
    ).fetchall()
    conn.close()
    return {r["ep_num"]: r["cnt"] for r in rows}


# ─── Flashcard API ────────────────────────────────────────────────────────────

@app.get("/api/flashcard/stats")
def flashcard_stats():
    return fc.get_stats()


@app.get("/api/flashcard/due")
def flashcard_due():
    card = fc.get_due_card()
    if not card:
        raise HTTPException(404, detail="No card due today")
    return card


@app.get("/api/flashcard/{card_id}/review")
def flashcard_review(card_id: int, result: str):
    if result not in ("pass", "fail"):
        raise HTTPException(400, detail="result must be 'pass' or 'fail'")
    try:
        updated = fc.update_sm2(card_id, result)
    except ValueError as e:
        raise HTTPException(404, detail=str(e))
    emoji = "✅" if result == "pass" else "🔄"
    msg = "已记住，下次间隔拉长！" if result == "pass" else "没关系，明天再来！"
    return {"ok": True, "emoji": emoji, "message": msg, "card": updated}


@app.post("/api/flashcard/push_now")
def flashcard_push_now():
    """立即触发一次推送（测试用）。"""
    card = fc.get_due_card()
    if not card:
        return {"ok": False, "message": "No card due today"}
    success = fc.push_card(card)
    return {"ok": success, "card_id": card["id"], "sentence": card["sentence"]}


# ─── Library API ──────────────────────────────────────────────────────────────

class MasteryIn(BaseModel):
    type: str
    ep_num: int
    item_key: str
    mastery: str


@app.get("/api/library/items")
def library_items(type: str = "vocab", mastery: str = "all", ep: str = "all"):
    items = lib.get_all_items(type)
    if mastery != "all":
        items = [i for i in items if i["mastery"] == mastery]
    if ep != "all":
        try:
            ep_num = int(ep)
            items = [i for i in items if i["ep_num"] == ep_num]
        except ValueError:
            pass
    return items


@app.post("/api/library/mastery")
def library_set_mastery(body: MasteryIn):
    try:
        return lib.set_mastery(body.type, body.ep_num, body.item_key, body.mastery)
    except ValueError as e:
        raise HTTPException(400, detail=str(e))


@app.get("/api/library/review-queue")
def library_review_queue(type: str = "all"):
    item_type = None if type == "all" else type
    queue = lib.get_review_queue(item_type)
    return queue


@app.get("/api/library/tips")
def library_tips(type: str, ep_num: int, item_key: str):
    from episodes_data import EPISODES_BY_NUM
    ep_info = EPISODES_BY_NUM.get(ep_num, {})
    items = lib.get_all_items(type)
    item = next((i for i in items if i["ep_num"] == ep_num and i["item_key"] == item_key), None)
    if not item:
        raise HTTPException(404, detail="Item not found")
    tips = lib.get_or_generate_tips(type, ep_num, item_key, item, ep_info)
    return tips


@app.get("/api/library/stats")
def library_stats():
    return lib.get_mastery_stats()


@app.get("/api/library/tips-bulk")
def library_tips_bulk(type: str = "pattern"):
    """返回所有已缓存的 tips，key = ep_num:item_key"""
    return lib.get_tips_bulk(type)


# ─── Pages ────────────────────────────────────────────────────────────────────

@app.get("/")
def directory(request: Request):
    conn = get_conn()
    rows = conn.execute(
        "SELECT ep_num, COUNT(*) as cnt FROM records GROUP BY ep_num"
    ).fetchall()
    conn.close()
    stats = {r["ep_num"]: r["cnt"] for r in rows}
    return templates.TemplateResponse("index.html", {
        "request": request,
        "episodes": EPISODES_LIST,
        "stats": stats,
    })


@app.get("/library")
def library_page(request: Request):
    stats = lib.get_mastery_stats()
    ep_list = [{"num": ep["num"], "title_en": ep["title_en"], "title_zh": ep["title_zh"]} for ep in EPISODES_LIST]
    return templates.TemplateResponse("library.html", {
        "request": request,
        "stats": stats,
        "ep_list": ep_list,
    })


@app.get("/ep/{num}")
def episode_page(request: Request, num: int):
    ep = EPISODES_BY_NUM.get(num)
    if not ep:
        raise HTTPException(404, detail=f"Episode {num} not found")
    sorted_nums = sorted(EPISODES_BY_NUM.keys())
    idx = sorted_nums.index(num)
    prev_ep = EPISODES_BY_NUM.get(sorted_nums[idx - 1]) if idx > 0 else None
    next_ep = EPISODES_BY_NUM.get(sorted_nums[idx + 1]) if idx < len(sorted_nums) - 1 else None
    return templates.TemplateResponse("episode.html", {
        "request": request,
        "ep": ep,
        "prev_ep": prev_ep,
        "next_ep": next_ep,
    })


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
