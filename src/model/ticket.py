from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from .user import TelegramUser


class TicketCategory(BaseModel):
    id: UUID
    name: str
    description: str
    limit: int

class TicketRequest(BaseModel):
    user: TelegramUser
    category: str | UUID = Field(description="Category name or UUID")
    is_closed: bool = Field(default=False)

class TicketMessage(BaseModel):
    """Ticket message model"""
    user_id: int = Field(description="Telegram user ID")
    message: str
    dt: datetime

class TicketAction(BaseModel):
    """Ticket action model. Example: Ticket closing"""
    user_id: int = Field(description="Telegram user ID")
    action: str

class Ticket(TicketRequest):
    topic_id: int
    dt: datetime
    messages: list[TicketMessage]
    actions: list[TicketAction]