# ─── Stage 1: 依赖安装 ────────────────────────────────────────────────────────
FROM python:3.11-slim AS builder

# 安装 uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# 先复制依赖文件，利用 Docker 层缓存
COPY pyproject.toml uv.lock ./

# 安装依赖到 /app/.venv
RUN uv sync --frozen --no-dev --no-install-project

# ─── Stage 2: 运行时镜像 ──────────────────────────────────────────────────────
FROM python:3.11-slim AS runtime

WORKDIR /app

# 从 builder 复制虚拟环境
COPY --from=builder /app/.venv /app/.venv

# 复制项目源码
COPY main.py flashcard.py library.py episodes_data.py ./
COPY templates/ ./templates/
COPY static/ ./static/

# 数据库目录（使用 volume 挂载持久化）
VOLUME ["/app/data"]

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DB_PATH=/app/data/peppa.db

EXPOSE 8080

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
