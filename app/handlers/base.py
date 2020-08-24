from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app.misc import dp


# todo: add a deeplink for auth from vas3k.club to telegram via one button
# see https://github.com/aiogram/aiogram/blob/dev-2.x/examples/regexp_commands_filter_example.py
# for more information
@dp.message_handler(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Я пока с тобой не знаком, но это альфа, так что разрешаю пользоваться")
