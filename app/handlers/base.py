from typing import Union

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from app.misc import dp


# todo: add a deeplink for auth from vas3k.club to telegram via one button
# see https://github.com/aiogram/aiogram/blob/dev-2.x/examples/regexp_commands_filter_example.py
# for more information
@dp.message_handler(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Я пока с тобой не знаком, но это альфа, так что разрешаю пользоваться")


# cancel any user state
@dp.message_handler(commands="cancel", state="*")
@dp.callback_query_handler(text="cancel", state="*")
async def cancel_command_handler(message: Union[CallbackQuery, Message], state: FSMContext):
    real_message = message if isinstance(message, Message) else message.message

    await real_message.answer("Отменяю..")
    await state.finish()
