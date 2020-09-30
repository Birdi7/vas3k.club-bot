from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message

from app.misc import dp
from app.models import User
from app.personal.states import ProcessAuthStates


# todo: add a deeplink for auth from vas3k.club to telegram via one button
# see https://github.com/aiogram/aiogram/blob/dev-2.x/examples/regexp_commands_filter_example.py
# for more information
@dp.message_handler(CommandStart())
async def start_command_handler(message: Message, user: User):
    if not user.is_club_user():
        await message.answer("Привет. Мы пока не знакомы. Привяжи меня на сайте или пришли мне секретный код 👇")
        await ProcessAuthStates.enter_secret_hash.set()
        raise SkipHandler


@dp.message_handler(state=ProcessAuthStates.enter_secret_hash)
async def enter_secret_hash_handler(message: Message, user: User, state: FSMContext):
    secret_hash = message.text
    if not user.process_auth(secret_hash):
        await message.answer("Неверный код!")

    await message.answer(f"Отлично! Приятно познакомиться, {user.slug}")
    await state.finish()
