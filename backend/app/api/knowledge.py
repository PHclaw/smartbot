"""
知识库 API
"""
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import os
import uuid

from ..core.database import get_db
from ..core.config import settings
from ..models.user import User
from ..models.bot import Bot, KnowledgeBase
from .auth import get_current_user

router = APIRouter(prefix="/knowledge", tags=["知识库"])


class KnowledgeCreate(BaseModel):
    name: str
    description: str = ""
    bot_id: str
    chunk_size: int = 500
    chunk_overlap: int = 50


class KnowledgeResponse(BaseModel):
    id: str
    bot_id: str
    name: str
    description: str
    total_chunks: int
    total_size: int
    is_active: bool
    created_at: str


@router.get("", response_model=List[KnowledgeResponse])
async def list_knowledge_bases(
    bot_id: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """获取知识库列表"""
    query = select(KnowledgeBase)
    if bot_id:
        query = query.where(KnowledgeBase.bot_id == bot_id)
    
    result = await db.execute(query.order_by(KnowledgeBase.created_at.desc()))
    bases = result.scalars().all()
    
    return [
        KnowledgeResponse(
            id=kb.id,
            bot_id=kb.bot_id,
            name=kb.name,
            description=kb.description,
            total_chunks=kb.total_chunks,
            total_size=kb.total_size,
            is_active=kb.is_active,
            created_at=kb.created_at.isoformat(),
        )
        for kb in bases
    ]


@router.post("", response_model=KnowledgeResponse)
async def create_knowledge_base(
    data: KnowledgeCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """创建知识库"""
    # 验证 Bot 所有权
    result = await db.execute(
        select(Bot).where(Bot.id == data.bot_id, Bot.user_id == current_user.id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Bot 不存在")
    
    kb = KnowledgeBase(
        bot_id=data.bot_id,
        name=data.name,
        description=data.description,
        chunk_size=data.chunk_size,
        chunk_overlap=data.chunk_overlap,
    )
    db.add(kb)
    await db.commit()
    await db.refresh(kb)
    
    return KnowledgeResponse(
        id=kb.id,
        bot_id=kb.bot_id,
        name=kb.name,
        description=kb.description,
        total_chunks=kb.total_chunks,
        total_size=kb.total_size,
        is_active=kb.is_active,
        created_at=kb.created_at.isoformat(),
    )


@router.post("/{kb_id}/upload")
async def upload_document(
    kb_id: str,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """上传文档到知识库"""
    # 验证所有权
    result = await db.execute(
        select(KnowledgeBase).where(KnowledgeBase.id == kb_id)
    )
    kb = result.scalar_one_or_none()
    
    if not kb:
        raise HTTPException(status_code=404, detail="知识库不存在")
    
    # 验证 Bot 所有权
    result = await db.execute(
        select(Bot).where(Bot.id == kb.bot_id, Bot.user_id == current_user.id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=403, detail="无权限")
    
    # 保存文件
    filename = f"{uuid.uuid4()}_{file.filename}"
    upload_dir = os.path.join(settings.APP_URL, "uploads", kb_id)
    os.makedirs(upload_dir, exist_ok=True)
    
    filepath = os.path.join(upload_dir, filename)
    content = await file.read()
    
    with open(filepath, "wb") as f:
        f.write(content)
    
    # 更新知识库
    documents = kb.documents or []
    documents.append({
        "filename": filename,
        "original_name": file.filename,
        "size": len(content),
        "uploaded_at": datetime.utcnow().isoformat(),
    })
    
    kb.documents = documents
    kb.total_size = (kb.total_size or 0) + len(content)
    kb.total_chunks = (kb.total_chunks or 0) + len(content) // kb.chunk_size
    
    await db.commit()
    
    return {
        "filename": filename,
        "size": len(content),
        "chunks": len(content) // kb.chunk_size,
        "message": "上传成功"
    }


@router.post("/{kb_id}/search")
async def search_knowledge(
    kb_id: str,
    query: str,
    top_k: int = 5,
):
    """搜索知识库"""
    # 简化实现
    return {
        "query": query,
        "results": [
            {
                "content": "这是匹配到的知识内容...",
                "score": 0.95,
                "source": "document.pdf",
            }
        ]
    }


@router.delete("/{kb_id}")
async def delete_knowledge_base(
    kb_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """删除知识库"""
    result = await db.execute(
        select(KnowledgeBase).where(KnowledgeBase.id == kb_id)
    )
    kb = result.scalar_one_or_none()
    
    if not kb:
        raise HTTPException(status_code=404, detail="知识库不存在")
    
    # 验证所有权
    result = await db.execute(
        select(Bot).where(Bot.id == kb.bot_id, Bot.user_id == current_user.id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=403, detail="无权限")
    
    await db.delete(kb)
    await db.commit()
    
    return {"message": "删除成功"}
