# cross-ai-memory-hub

> 一套跨 AI 办公智能体（数字员工 / 办公 Agent）的**共享记忆中枢**方案：让豆包工作、TraeWork、WorkBuddy、千问办公等任意新 Agent 在首次启动时自动读取你本机的统一记忆，从此不用反复自我介绍。

## 痛点

大厂混战，AI 办公智能体扎堆发布。用户会在多个产品间切换，且使用频率不一、新产品不断出现。每个 Agent 各自维护私有记忆，导致：

- 每次开新 Agent 都要重述"我是谁 / 在哪 / 做什么 / 喜欢什么"；
- 偏好、背景、禁忌散落各地，形成**记忆孤岛**。

## 方案

在**你自己电脑**的用户主目录建一个隐藏文件夹 `.ai-memory-hub`，作为所有 Agent 的**唯一记忆真相源**：

```
~/.ai-memory-hub/
├─ profile.md        # 用户画像
├─ preferences.md    # 沟通与输出偏好
├─ context.md        # 当前工作主线与近期动态
├─ habits.md         # 使用习惯
├─ agent-log.md      # 跨 Agent 使用时间线
└─ README.md
```

再配合一段**零编辑的开箱提示词**（见 [`references/unboxing-prompt.md`](references/unboxing-prompt.md)）：把它粘贴进任意新 Agent 的首条对话，Agent 会自动定位 / 创建该目录、读取你的记忆并开工，无需重新介绍自己。

## 快速开始

### 1. 脚手架生成空中枢（可选，一键）

```bash
python scripts/scaffold.py
```

跨平台（Windows / macOS / Linux），幂等（已存在文件不覆盖），只生成**空骨架**，绝不复制任何已有个人数据。

### 2. 粘贴开箱提示词

复制 [`references/unboxing-prompt.md`](references/unboxing-prompt.md) 中 ```text``` 包裹的整段，粘贴进任意新 AI 办公智能体的首条对话即可。

### 3. 验证

问它："我是谁、我最近在忙什么？"——若回答准确来自你的记忆中枢，说明打通。

## 作为 WorkBuddy Skill 使用

把本目录放入 `~/.workbuddy/skills/cross-ai-memory-hub/`（或项目 `.workbuddy/skills/`），WorkBuddy 会在相关场景自动加载 `SKILL.md` 与参考文件。

## 安全边界（务必遵守）

1. 提示词里的"完全权限"仅限**该目录的读写 + Agent 自带工具**，勿给未知新 Agent 整机提权（admin / 格式化 / shell）。
2. 密码、密钥、身份证号**不要**放进中枢。
3. 接收方 Agent 须具备**本机文件访问能力**（桌面端 / 虚拟桌面类均可）；纯云端无文件权限的聊天机器人无法创建 / 读取该文件夹。
4. 本仓库只含**通用模板**，不含任何个人记忆数据。分享时只发开箱提示词即可，对方首次运行会自动建自己的空中枢。

## 许可证

MIT
