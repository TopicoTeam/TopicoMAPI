from uuid import UUID

from topico_api_model.ticket import Ticket

from ..ext import Router


@Router.get("/v1/ticket/{id}", Ticket, 200)
def get_ticket(id: UUID) -> Ticket:
    return NotImplemented
