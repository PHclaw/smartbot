# SmartBot - AI 客服 SaaS

<div align="center">

**Free & Open Source AI Customer Service**

Deploy in 5 minutes. Powered by AI. No vendor lock-in.

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com)
[![GitHub stars](https://img.shields.io/github/stars/PHclaw/smartbot?style=social)](https://github.com/PHclaw/smartbot)

</div>

---

## ✨ Features

- 🤖 **AI-Powered Replies** - RAG knowledge base, understands intent like a human
- 💬 **Multi-Channel** - Web Widget / WhatsApp / WeChat / Xiaohongshu
- 🚀 **5-Min Deployment** - Drag-and-drop config, no engineers needed
- 🔓 **100% Free & Open Source** - No vendor lock-in, deploy anywhere
- 🔄 **Human Handoff** - Seamless transfer to human agents
- 📊 **Analytics** - Conversation analysis, intent tracking, satisfaction

## 🏗️ Tech Stack

### Backend
- FastAPI + SQLAlchemy (async)
- PostgreSQL + pgvector (vector search)
- Redis + Celery (task queue)
- OpenAI / Anthropic / DeepSeek (LLM)

### Frontend
- React 18 + TypeScript
- Tailwind CSS
- Vite

## 🚀 Quick Start

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit http://localhost:5174

## 📁 Project Structure

```
smartbot/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core config
│   │   └── models/       # Data models
│   └── requirements.txt
├── frontend/
│   └── src/
│       └── App.tsx       # Landing page
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

<div align="center">

**Star us on GitHub ⭐**

[![Star](https://img.shields.io/github/stars/PHclaw/smartbot?style=social)](https://github.com/PHclaw/smartbot)

</div>
