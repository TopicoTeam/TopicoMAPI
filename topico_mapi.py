from datetime import datetime
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

class Ticket(BaseModel):
    """Модель заявки"""
    id: UUID
    topic_id: int = Field(description="Telegram topic ID")
    user_id: int = Field(description="Telegram user ID")
    dt: datetime

class TicketMessage(BaseModel):
    """Модель сообщения в заявке"""
    ticket_id: UUID
    user_id: int = Field(description="Telegram user ID")
    message: str
    dt: datetime

class TicketAction(BaseModel):
    """Модель действия в заявке (Пример: Закрытие)"""
    ticket_id: UUID
    user_id: int = Field(description="Telegram user ID")
    action: str

