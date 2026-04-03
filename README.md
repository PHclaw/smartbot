# SmartBot - AI 客服 SaaS

<div align="center">

**🚀 面向出海团队 + 中小企业的 AI 客服 SaaS**

5 分钟配置上线，按消息计费，不用不花钱。

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg)](https://react.dev)

</div>

---

## ✨ 特性

- 🤖 **AI 智能回复** - RAG 知识库检索，像人工一样准确理解问题
- 💬 **全渠道覆盖** - 网站 / WhatsApp / 微信 / 小红书 一键接入
- 🚀 **5 分钟上线** - 无需工程团队，拖拽配置即可
- 💰 **按需计费** - 不用不花钱，超出部分按量计费
- 🔄 **无缝转人工** - AI 无法解决时，一键转接人工
- 📊 **数据驱动** - 对话分析、意图统计、满意度追踪

## 💰 定价

| 套餐 | 价格 | 消息数 | Bot 数 |
|:-----|:-----|:-------|:-------|
| 免费 | ¥0/月 | 100 条 | 1 个 |
| 入门 | ¥99/月 | 3,000 条 | 3 个 |
| 专业 | ¥299/月 | 10,000 条 | 10 个 |
| 企业 | ¥799/月 | 50,000 条 | 无限 |

## 🏗️ 技术栈

### 后端
- FastAPI + SQLAlchemy (异步)
- PostgreSQL + pgvector (向量搜索)
- Redis + Celery (任务队列)
- OpenAI / Anthropic / DeepSeek (LLM)

### 前端
- React 18 + TypeScript
- Tailwind CSS
- Vite

## 🚀 快速开始

### 后端

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

### 前端

```bash
cd frontend
npm install
npm run dev
```

访问 http://localhost:5174

## 📁 项目结构

```
smartbot/
├── backend/
│   ├── app/
│   │   ├── api/          # API 路由
│   │   ├── core/         # 核心配置
│   │   └── models/       # 数据模型
│   └── requirements.txt
├── frontend/
│   └── src/
│       └── App.tsx       # 落地页
└── README.md
```

## 📄 License

MIT License
