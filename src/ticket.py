from topico_api_model.ticket import Ticket
from topico_api_model.user import TelegramUser


def get_tickets(user: TelegramUser, is_closed: bool) -> list[Ticket]:
    return NotImplemented

def get_ticket(user: TelegramUser) -> Ticket:
    return NotImplemented

def create_ticket(user: TelegramUser, category: str) -> Ticket:
    return NotImplemented

def ticket_message(user: TelegramUser, message: str):
    return NotImplemented

def ticket_action(user: TelegramUser, action: str):
    return NotImplemented