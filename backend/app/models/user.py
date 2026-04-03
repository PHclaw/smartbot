"""
用户模型
"""
from sqlalchemy import Column, String, DateTime, Integer, Boolean, JSON, Text
from datetime import datetime
import uuid

from ..core.database import Base


class User(Base):
    """用户表"""
    __tablename__ = "users"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, index=True)
    password_hash = Column(String(255))
    nickname = Column(String(50))
    avatar = Column(String(500))
    
    # 订阅
    subscription_tier = Column(String(20), default="free")
    subscription_expires_at = Column(DateTime)
    stripe_customer_id = Column(String(100))
    
    # 配额
    quota = Column(JSON, default=dict)
    
    # 统计
    total_conversations = Column(Integer, default=0)
    total_messages = Column(Integer, default=0)
    
    # 状态
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login_at = Column(DateTime)
