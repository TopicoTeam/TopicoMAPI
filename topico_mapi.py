from uuid import UUID

from pydantic import BaseModel, Field


class UserRole(BaseModel):
    """Ролевая модель"""
    id: UUID
    name: str
    description: str

class User(BaseModel):
    """Модель пользователя"""
    topico_id: UUID = Field(description="Internal topico team user ID")
    minecraft_id: UUID
    telegram_id: int
    role_id: UUID = Field(description="UserRole id")



