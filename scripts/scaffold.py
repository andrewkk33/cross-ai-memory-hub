#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cross-AI Memory Hub — scaffolder.

Creates an EMPTY `.ai-memory-hub` directory in the user's home directory with the
six standard skeleton files. NEVER copies any existing personal data. Idempotent:
existing files are left untouched.

Usage:
    python scaffold.py            # create under ~/<user>/.ai-memory-hub
    python scaffold.py --path X  # create under explicit absolute path X
"""

import argparse
import os
import sys

SKELETON = {
    "profile.md": (
        "# 用户画像 (Profile)\n\n"
        "> 首次由 AI 引导补全，或自行填写。\n\n"
        "- 称呼：\n"
        "- 所在城市：\n"
        "- 职业领域：\n"
        "- 身份特征 / 关键词：\n"
    ),
    "preferences.md": (
        "# 沟通与输出偏好 (Preferences)\n\n"
        "- 语言：\n"
        "- 回答风格（简洁 / 详尽 / 结构化）：\n"
        "- 输出形式偏好（表格 / 清单 / 长文）：\n"
        "- 禁忌（不要做的事）：\n"
    ),
    "context.md": (
        "# 当前工作主线与近期动态 (Context)\n\n"
        "- 主线一：\n"
        "- 主线二：\n"
        "- 近期重点：\n"
    ),
    "habits.md": (
        "# 使用习惯 (Habits)\n\n"
        "- 常用设备：\n"
        "- 在哪些 AI 办公智能体间切换：\n"
        "- 自动化 / 定时任务习惯：\n"
    ),
    "agent-log.md": (
        "# 跨 Agent 使用时间线 (Agent Log)\n\n"
        "> 每次使用任一 AI 后追加一行：`日期 | 用了哪个 Agent | 做了什么`\n\n"
    ),
    "README.md": (
        "# .ai-memory-hub — 跨 AI 共享记忆中枢\n\n"
        "本目录是你所有 AI 办公智能体的**唯一记忆真相源**。\n\n"
        "## 文件说明\n"
        "- `profile.md` 用户画像\n"
        "- `preferences.md` 沟通与输出偏好\n"
        "- `context.md` 当前工作主线与近期动态\n"
        "- `habits.md` 使用习惯\n"
        "- `agent-log.md` 跨 Agent 使用时间线\n\n"
        "## 使用方式\n"
        "把 `开箱提示词` 整段粘贴进任意新 AI 的首条对话，它会自动读 / 写本目录。\n\n"
        "## 安全须知\n"
        "- 仅放非密信息；密码 / 密钥 / 身份证号勿入。\n"
        "- 不要要求 AI 把本目录上传到不明外部服务。\n"
    ),
}


def resolve_hub_path(explicit: str | None) -> str:
    if explicit:
        return os.path.abspath(explicit)
    return os.path.join(os.path.expanduser("~"), ".ai-memory-hub")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold an empty cross-AI memory hub.")
    parser.add_argument("--path", help="Explicit absolute path for the hub (default: ~/ .ai-memory-hub)")
    args = parser.parse_args()

    hub = resolve_hub_path(args.path)
    created_dir = False
    if not os.path.isdir(hub):
        os.makedirs(hub, exist_ok=True)
        created_dir = True
        print(f"[ok] 已创建记忆中枢目录: {hub}")
    else:
        print(f"[info] 记忆中枢已存在: {hub}")

    for name, content in SKELETON.items():
        path = os.path.join(hub, name)
        if os.path.exists(path):
            print(f"[skip] 已存在，跳过: {name}")
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[ok] 已创建骨架文件: {name}")

    if created_dir:
        print("\n下一步：把开箱提示词粘贴进任意新 AI 的首条对话即可。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
