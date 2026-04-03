"""
SmartBot 主入口
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings
from .api import auth, bots, conversations, knowledge

app = FastAPI(
    title=settings.APP_NAME,
    description="SmartBot - AI 客服 SaaS",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/v1")
app.include_router(bots.router, prefix="/api/v1")
app.include_router(conversations.router, prefix="/api/v1")
app.include_router(knowledge.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "SmartBot API", "version": "1.0.0"}


@app.get("/health")
async def health():
    return {"status": "ok"}
