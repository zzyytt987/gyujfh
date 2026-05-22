#!/bin/bash
# ECS 初始化脚本 - Alibaba Cloud Linux
# 运行方式: ssh root@<ECS_IP> 'bash -s' < setup-ecs.sh

set -e

echo "=== 安装 Docker ==="
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "=== 启动 Docker 并设置开机自启 ==="
systemctl start docker
systemctl enable docker

echo "=== 创建项目目录 ==="
mkdir -p /opt/enterprise-backend/data
chmod 755 /opt/enterprise-backend/data

echo "=== 检查安装结果 ==="
docker --version
docker compose version

echo "=== ECS 初始化完成 ==="
echo "请确认安全组已开放端口 8000"
