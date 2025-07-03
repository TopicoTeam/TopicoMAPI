from ..model.ticket import TicketRequest, Ticket, TicketMessage


def get_tickets(ticket_request: TicketRequest) -> list[Ticket]:
    return NotImplemented

def create_ticket(ticket_request: TicketRequest) -> Ticket:
    return NotImplemented

def ticket_message(message: TicketMessage):
    return NotImplemented