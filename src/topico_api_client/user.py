from topico_api_model.user import TopicoUser

from ..ext import Router

@Router.post("/v1/user/register", TopicoUser, 201)
def register(telegram_id: int):
    return NotImplemented

@Router.get("/v1/user/telegram/{id}", TopicoUser)
def get_user_by_telegram(id: int):
    """Return TopicoUser model by it telegram id"""
    return NotImplemented