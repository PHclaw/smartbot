"""
对话 API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uuid

from ..core.database import get_db
from ..core.config import settings
from ..models.user import User
from ..models.bot import Bot, Conversation, Message
from .auth import get_current_user

router = APIRouter(prefix="/conversations", tags=["对话"])


class ChatRequest(BaseModel):
    message: str
    visitor_id: str
    session_id: Optional[str] = None
    metadata: dict = {}


class ChatResponse(BaseModel):
    session_id: str
    message: str
    intent: str = None
    confidence: float = None
    used_knowledge: bool = False
    conversation_id: str


class ConversationResponse(BaseModel):
    id: str
    visitor_id: str
    status: str
    messages: list
    created_at: str


# 意图识别关键词
INTENT_KEYWORDS = {
    "pricing": ["价格", "多少钱", "报价", "费用", "pricing", "price", "cost", "how much"],
    "demo": ["演示", "demo", "试用", "体验", "try", "show me"],
    "complaint": ["投诉", "complaint", "不满", "差", "垃圾", "烂"],
    "refund": ["退款", "refund", "退钱", "取消订单"],
    "order": ["订单", "order", "快递", "物流", "发货"],
    "technical": ["bug", "故障", "不能用", "error", "broken"],
}


def detect_intent(message: str) -> tuple[str, float]:
    """简单意图识别"""
    message_lower = message.lower()
    
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in message_lower:
                return intent, 0.8
    
    return "general", 0.5


def build_system_prompt(bot: Bot) -> str:
    """构建系统提示词"""
    base = bot.system_prompt or "你是一个专业的客服助手。"
    
    # 添加配置
    config = bot.config or {}
    if config.get("greeting"):
        base = f"{config['greeting']}\n\n{base}"
    
    return base


@router.post("/{bot_id}/chat", response_model=ChatResponse)
async def chat(
    bot_id: str,
    data: ChatRequest,
    db: AsyncSession = Depends(get_db),
):
    """发送消息"""
    # 获取 Bot
    result = await db.execute(select(Bot).where(Bot.id == bot_id, Bot.is_published == True))
    bot = result.scalar_one_or_none()
    
    if not bot:
        raise HTTPException(status_code=404, detail="Bot 不存在或未发布")
    
    # 获取或创建会话
    conversation = None
    if data.session_id:
        result = await db.execute(
            select(Conversation).where(
                Conversation.id == data.session_id,
                Conversation.bot_id == bot_id,
            )
        )
        conversation = result.scalar_one_or_none()
    
    if not conversation:
        conversation = Conversation(
            bot_id=bot_id,
            visitor_id=data.visitor_id,
            status="active",
        )
        db.add(conversation)
        await db.commit()
        await db.refresh(conversation)
    
    # 保存用户消息
    user_msg = Message(
        conversation_id=conversation.id,
        bot_id=bot_id,
        role="user",
        content=data.message,
    )
    db.add(user_msg)
    
    # 意图识别
    intent, confidence = detect_intent(data.message)
    
    # 更新会话消息列表
    messages = conversation.messages or []
    messages.append({"role": "user", "content": data.message})
    
    # 构建 AI 回复
    system_prompt = build_system_prompt(bot)
    ai_messages = [{"role": "system", "content": system_prompt}] + messages
    
    # 调用 LLM（简化实现）
    response_text = "感谢您的消息！我们的客服团队将尽快回复您。"
    
    # 模拟 AI 回复
    if "价格" in data.message or "多少钱" in data.message:
        response_text = "我们的价格方案非常灵活，从免费版到企业版都有。入门版每月 99 元，专业版每月 299 元。请问您想了解哪个版本的详情呢？"
    elif "你好" in data.message or "hello" in data.message.lower():
        response_text = "您好！我是 SmartBot 智能客服，很高兴为您服务。请问有什么可以帮助您的？"
    
    # 保存 AI 回复
    ai_msg = Message(
        conversation_id=conversation.id,
        bot_id=bot_id,
        role="assistant",
        content=response_text,
        intent=intent,
        confidence=confidence,
    )
    db.add(ai_msg)
    
    # 更新会话
    messages.append({"role": "assistant", "content": response_text})
    conversation.messages = messages
    conversation.updated_at = datetime.utcnow()
    
    # 更新 Bot 统计
    bot.total_messages = (bot.total_messages or 0) + 2
    bot.total_conversations = (bot.total_conversations or 0) + 1
    
    await db.commit()
    
    return ChatResponse(
        session_id=conversation.id,
        message=response_text,
        intent=intent,
        confidence=confidence,
        used_knowledge=False,
        conversation_id=conversation.id,
    )


@router.get("/{bot_id}/conversations", response_model=List[ConversationResponse])
async def list_conversations(
    bot_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取会话列表（需要登录）"""
    # 验证 Bot 所有权
    result = await db.execute(
        select(Bot).where(Bot.id == bot_id, Bot.user_id == current_user.id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Bot 不存在")
    
    # 获取会话
    result = await db.execute(
        select(Conversation)
        .where(Conversation.bot_id == bot_id)
        .order_by(Conversation.updated_at.desc())
        .limit(50)
    )
    conversations = result.scalars().all()
    
    return [
        ConversationResponse(
            id=conv.id,
            visitor_id=conv.visitor_id,
            status=conv.status,
            messages=conv.messages or [],
            created_at=conv.created_at.isoformat(),
        )
        for conv in conversations
    ]


@router.post("/{bot_id}/conversations/{conv_id}/resolve")
async def resolve_conversation(
    bot_id: str,
    conv_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """标记会话已解决"""
    result = await db.execute(
        select(Conversation).where(
            Conversation.id == conv_id,
            Conversation.bot_id == bot_id,
        )
    )
    conversation = result.scalar_one_or_none()
    
    if not conversation:
        raise HTTPException(status_code=404, detail="会话不存在")
    
    conversation.status = "resolved"
    conversation.resolved_by = "ai"
    conversation.resolved_at = datetime.utcnow()
    await db.commit()
    
    return {"message": "已标记为已解决"}


@router.post("/{bot_id}/conversations/{conv_id}/transfer")
async def transfer_to_human(
    bot_id: str,
    conv_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """转人工"""
    result = await db.execute(
        select(Conversation).where(
            Conversation.id == conv_id,
            Conversation.bot_id == bot_id,
        )
    )
    conversation = result.scalar_one_or_none()
    
    if not conversation:
        raise HTTPException(status_code=404, detail="会话不存在")
    
    conversation.status = "waiting"
    await db.commit()
    
    return {"message": "已转人工，请等待客服接入"}
