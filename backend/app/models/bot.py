"""
Bot 模型
"""
from sqlalchemy import Column, String, DateTime, Integer, Boolean, JSON, Text
from datetime import datetime
import uuid

from ..core.database import Base


class Bot(Base):
    """Bot 表 - 一个 Bot 代表一个客服机器人"""
    __tablename__ = "bots"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), index=True)
    name = Column(String(100))
    description = Column(Text)
    
    # Bot 配置
    config = Column(JSON, default=dict)  # {welcome_message, ai_model, temperature, ...}
    system_prompt = Column(Text)  # AI 系统提示词
    
    # 渠道配置
    channels = Column(JSON, default=list)  # [{type: "web", widget_id: "xxx"}, ...]
    
    # 知识库
    knowledge_base_ids = Column(JSON, default=list)  # 关联的知识库 ID 列表
    
    # 统计
    total_conversations = Column(Integer, default=0)
    total_messages = Column(Integer, default=0)
    avg_satisfaction = Column(Integer, default=0)
    
    # 状态
    is_active = Column(Boolean, default=True)
    is_published = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Conversation(Base):
    """会话表"""
    __tablename__ = "conversations"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    bot_id = Column(String(36), index=True)
    visitor_id = Column(String(100))  # 访客标识
    
    # 消息
    messages = Column(JSON, default=list)
    
    # 状态
    status = Column(String(20), default="active")  # active / waiting / resolved / transferred
    resolved_by = Column(String(20))  # "ai" / "human"
    
    # 评分
    satisfaction = Column(Integer)  # 1-5
    
    # 上下文
    context = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime)


class Message(Base):
    """消息表"""
    __tablename__ = "messages"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String(36), index=True)
    bot_id = Column(String(36), index=True)
    
    role = Column(String(20))  # user / assistant / system
    content = Column(Text)
    
    # AI 分析
    intent = Column(String(100))  # 识别出的意图
    confidence = Column(Float)  # 置信度
    used_knowledge = Column(Boolean, default=False)  # 是否使用了知识库
    
    # 反馈
    feedback = Column(Integer)  # 1-5
    
    created_at = Column(DateTime, default=datetime.utcnow)


class KnowledgeBase(Base):
    """知识库"""
    __tablename__ = "knowledge_bases"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    bot_id = Column(String(36), index=True)
    name = Column(String(200))
    description = Column(Text)
    
    # 文档
    documents = Column(JSON, default=list)
    
    # 配置
    chunk_size = Column(Integer, default=500)
    chunk_overlap = Column(Integer, default=50)
    embedding_model = Column(String(100))
    
    # 统计
    total_chunks = Column(Integer, default=0)
    total_size = Column(Integer, default=0)
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class HumanTakeover(Base):
    """人工接管记录"""
    __tablename__ = "human_takeovers"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String(36), index=True)
    
    # 接管信息
    taken_by = Column(String(100))  # 客服人员 ID
    notes = Column(Text)
    
    # 时间
    taken_at = Column(DateTime, default=datetime.utcnow)
    returned_at = Column(DateTime)
