from typing import Union

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from app.misc import dp


# cancel any user state
@dp.message_handler(commands="cancel", state="*")
@dp.callback_query_handler(text="cancel", state="*")
async def cancel_command_handler(message: Union[CallbackQuery, Message], state: FSMContext):
    real_message = message if isinstance(message, Message) else message.message

    await real_message.answer("Отменяю...")
    await state.finish()
