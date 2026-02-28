#!/usr/bin/env bash
set -euo pipefail

# ─── 配置 ─────────────────────────────────────────────────────────────────────
DOCKER_HUB_USER="${DOCKER_HUB_USER:-your-dockerhub-username}"
IMAGE_NAME="peppa-waiban"
TAG="${TAG:-latest}"
FULL_IMAGE="${DOCKER_HUB_USER}/${IMAGE_NAME}:${TAG}"

# ─── 检查是否已登录 Docker Hub ────────────────────────────────────────────────
if ! docker info 2>/dev/null | grep -q "Username"; then
  echo "⚠️  未登录 Docker Hub，正在登录..."
  docker login
fi

# ─── 推送镜像 ─────────────────────────────────────────────────────────────────
echo "▶ 推送镜像: ${FULL_IMAGE}"
echo "────────────────────────────────────────"

docker push "${FULL_IMAGE}"

# 同时打 latest 标签并推送（如果当前 TAG 不是 latest）
if [ "${TAG}" != "latest" ]; then
  LATEST_IMAGE="${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
  echo ""
  echo "▶ 同步推送 latest 标签: ${LATEST_IMAGE}"
  docker tag "${FULL_IMAGE}" "${LATEST_IMAGE}"
  docker push "${LATEST_IMAGE}"
fi

echo ""
echo "✅ 推送完成！"
echo "   镜像地址: https://hub.docker.com/r/${DOCKER_HUB_USER}/${IMAGE_NAME}"
