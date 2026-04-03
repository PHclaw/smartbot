"""
Bot 管理 API
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional, List
import uuid

from ..core.database import get_db
from ..models.user import User
from ..models.bot import Bot, Conversation, Message
from .auth import get_current_user

router = APIRouter(prefix="/bots", tags=["Bots"])


class BotCreate(BaseModel):
    name: str
    description: str = ""
    system_prompt: str = "你是一个专业的客服助手，友好、专业地回答用户问题。"
    config: dict = {}


class BotUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    system_prompt: Optional[str] = None
    config: Optional[dict] = None
    channels: Optional[list] = None
    knowledge_base_ids: Optional[list] = None
    is_active: Optional[bool] = None


class BotResponse(BaseModel):
    id: str
    name: str
    description: str
    system_prompt: str
    config: dict
    channels: list
    knowledge_base_ids: list
    total_conversations: int
    is_active: bool
    is_published: bool
    created_at: str


@router.get("", response_model=List[BotResponse])
async def list_bots(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取用户的所有 Bot"""
    result = await db.execute(
        select(Bot).where(Bot.user_id == current_user.id).order_by(Bot.created_at.desc())
    )
    bots = result.scalars().all()
    
    return [
        BotResponse(
            id=bot.id,
            name=bot.name,
            description=bot.description,
            system_prompt=bot.system_prompt,
            config=bot.config or {},
            channels=bot.channels or [],
            knowledge_base_ids=bot.knowledge_base_ids or [],
            total_conversations=bot.total_conversations,
            is_active=bot.is_active,
            is_published=bot.is_published,
            created_at=bot.created_at.isoformat(),
        )
        for bot in bots
    ]


@router.post("", response_model=BotResponse)
async def create_bot(
    data: BotCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """创建新 Bot"""
    # 检查配额
    result = await db.execute(
        select(Bot).where(Bot.user_id == current_user.id)
    )
    bots_count = len(result.scalars().all())
    max_bots = current_user.quota.get("bots", 1) if current_user.quota else 1
    
    if bots_count >= max_bots:
        raise HTTPException(status_code=403, detail=f"已达 Bot 数量上限（{max_bots}个），请升级套餐")
    
    bot = Bot(
        user_id=current_user.id,
        name=data.name,
        description=data.description,
        system_prompt=data.system_prompt,
        config=data.config,
        widget_key=str(uuid.uuid4()),
    )
    db.add(bot)
    await db.commit()
    await db.refresh(bot)
    
    return BotResponse(
        id=bot.id,
        name=bot.name,
        description=bot.description,
        system_prompt=bot.system_prompt,
        config=bot.config or {},
        channels=bot.channels or [],
        knowledge_base_ids=bot.knowledge_base_ids or [],
        total_conversations=bot.total_conversations,
        is_active=bot.is_active,
        is_published=bot.is_published,
        created_at=bot.created_at.isoformat(),
    )


@router.get("/{bot_id}", response_model=BotResponse)
async def get_bot(
    bot_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取 Bot 详情"""
    result = await db.execute(
        select(Bot).where(Bot.id == bot_id, Bot.user_id == current_user.id)
    )
    bot = result.scalar_one_or_none()
    
    if not bot:
        raise HTTPException(status_code=404, detail="Bot 不存在")
    
    return BotResponse(
        id=bot.id,
        name=bot.name,
        description=bot.description,
        system_prompt=bot.system_prompt,
        config=bot.config or {},
        channels=bot.channels or [],
        knowledge_base_ids=bot.knowledge_base_ids or [],
        total_conversations=bot.total_conversations,
        is_active=bot.is_active,
        is_published=bot.is_published,
        created_at=bot.created_at.isoformat(),
    )


@router.put("/{bot_id}", response_model=BotResponse)
async def update_bot(
    bot_id: str,
    data: BotUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """更新 Bot"""
    result = await db.execute(
        select(Bot).where(Bot.id == bot_id, Bot.user_id == current_user.id)
    )
    bot = result.scalar_one_or_none()
    
    if not bot:
        raise HTTPException(status_code=404, detail="Bot 不存在")
    
    # 更新字段
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(bot, field, value)
    
    await db.commit()
    await db.refresh(bot)
    
    return BotResponse(
        id=bot.id,
        name=bot.name,
        description=bot.description,
        system_prompt=bot.system_prompt,
        config=bot.config or {},
        channels=bot.channels or [],
        knowledge_base_ids=bot.knowledge_base_ids or [],
        total_conversations=bot.total_conversations,
        is_active=bot.is_active,
        is_published=bot.is_published,
        created_at=bot.created_at.isoformat(),
    )


@router.delete("/{bot_id}")
async def delete_bot(
    bot_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """删除 Bot"""
    result = await db.execute(
        select(Bot).where(Bot.id == bot_id, Bot.user_id == current_user.id)
    )
    bot = result.scalar_one_or_none()
    
    if not bot:
        raise HTTPException(status_code=404, detail="Bot 不存在")
    
    await db.delete(bot)
    await db.commit()
    
    return {"message": "删除成功"}


@router.post("/{bot_id}/publish")
async def publish_bot(
    bot_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """发布 Bot"""
    result = await db.execute(
        select(Bot).where(Bot.id == bot_id, Bot.user_id == current_user.id)
    )
    bot = result.scalar_one_or_none()
    
    if not bot:
        raise HTTPException(status_code=404, detail="Bot 不存在")
    
    bot.is_published = True
    await db.commit()
    
    return {"widget_key": bot.config.get("widget_key") or bot.id, "message": "发布成功"}
