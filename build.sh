#!/usr/bin/env bash
set -euo pipefail

# ─── 配置 ─────────────────────────────────────────────────────────────────────
DOCKER_HUB_USER="${DOCKER_HUB_USER:-seonxp}"
IMAGE_NAME="peppa-waiban"
TAG="${TAG:-latest}"
FULL_IMAGE="${DOCKER_HUB_USER}/${IMAGE_NAME}:${TAG}"

echo "▶ 构建镜像: ${FULL_IMAGE}"
echo "────────────────────────────────────────"

# 支持 Apple Silicon / 多平台构建
PLATFORM="${PLATFORM:-linux/amd64}"

docker build \
  --platform "${PLATFORM}" \
  --tag "${FULL_IMAGE}" \
  --file Dockerfile \
  .

echo ""
echo "✅ 构建完成: ${FULL_IMAGE}"
echo ""
echo "本地运行示例："
echo "  docker run -d \\"
echo "    -p 8080:8080 \\"
echo "    -v \$(pwd)/data:/app/data \\"
echo "    -e OPENAI_API_KEY=sk-xxx \\"
echo "    --name peppa \\"
echo "    ${FULL_IMAGE}"
