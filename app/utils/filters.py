from typing import NoReturn, Union

from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery, Message

from app.models import User


class ClubUserFilter(BoundFilter):
    key = "is_club_user"

    def __init__(self, is_club_user: bool):
        self.is_club_user = is_club_user

    async def check(self, obj: Union[Message, CallbackQuery]) -> bool:
        real_user = User.from_aiogram_user(obj.from_user)
        return real_user.is_club_user()


def setup(dispatcher: Dispatcher) -> NoReturn:
    dispatcher.filters_factory.bind(
        ClubUserFilter,
    )
