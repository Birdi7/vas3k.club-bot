from typing import Optional

from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import CallbackQuery, Chat, Message, User

from app.models import User as mUser


class ContextMiddleware(BaseMiddleware):
    @staticmethod
    async def setup_chat(data: dict, user: User, chat: Optional[Chat] = None):
        # replace aiogram's User with enriched subclass
        data["user"] = mUser.from_aiogram_user(user)
        data["chat"] = chat

    async def on_pre_process_message(self, message: Message, data: dict):
        await self.setup_chat(data, message.from_user, message.chat)

    async def on_pre_process_callback_query(self, query: CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user, query.message.chat if query.message else None)


def setup(dispatcher: Dispatcher):
    dispatcher.middleware.setup(LoggingMiddleware("bot"))
    dispatcher.middleware.setup(ContextMiddleware())
