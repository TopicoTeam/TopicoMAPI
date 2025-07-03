from datetime import datetime
from logging import fatal
from uuid import UUID

from pydantic import BaseModel, Field


class UserRole(BaseModel):
    """Role model"""
    nickname: str
    description: str


class MinecraftUser(BaseModel):
    id: UUID
    nickname: str


class TelegramUser(BaseModel):
    id: int = Field(description="User telegram ID")


class TopicoUser(BaseModel):
    id: UUID = Field(description="Internal topico team user ID")
    minecraft: MinecraftUser | None = Field(description="User minecraft account data")
    telegram: TelegramUser
    role: UserRole
