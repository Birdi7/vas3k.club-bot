import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils import markdown

from app.misc import dp
from app.personal.create_post.states import CreateNewPostStates
from app.utils.callback_data import create_post_callback
from app.utils.keyboards import inline_cancel_button

logger = logging.getLogger("bot")


@dp.message_handler(commands="create_post")
async def create_post_handler(message: Message, state: FSMContext):
    if len(message.text) <= 120:
        await message.answer("Маловато...")
        return

    async with state.proxy() as storage:
        storage["unfinished_new_post"] = dict()
        storage["unfinished_new_post"]["content"] = message.md_text

    await state.set_state(CreateNewPostStates.enter_title)
    await message.answer("Окей, жду заголовок!")


@dp.message_handler(state=CreateNewPostStates.enter_title)
async def create_post_enter_title_handler(message: Message, state: FSMContext):
    async with state.proxy() as storage:
        storage["unfinished_new_post"]["title"] = message.text

    await state.set_state(CreateNewPostStates.enter_post_type)

    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("📝 Как пост", callback_data=create_post_callback.new(type="regular_post")),
        InlineKeyboardButton("❔ Вопросом", callback_data=create_post_callback.new(type="question")),
    )
    keyboard.row(inline_cancel_button)

    await message.answer("Финальный вопрос: как постим?", reply_markup=keyboard)


@dp.callback_query_handler(create_post_callback.filter(), state=CreateNewPostStates.enter_post_type)
async def last_approval_before_creation_of_new_post(query: CallbackQuery, state: FSMContext, callback_data: dict):
    await query.answer()

    emoji = "🔥"

    async with state.proxy() as storage:
        storage["unfinished_new_post"]["type"] = callback_data["type"]

        text = (
            f"Итак, последняя проверка:\n\n"
            f'{emoji} {markdown.hbold(storage["unfinished_new_post"]["title"])}\n\n'
            f'{storage["unfinished_new_post"]["content"]}\n\n'
            f'{markdown.hbold("Будем постить?")} (после публикации его можно будет подредактировать на сайте)'
        )

    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("✅ Поехали?", callback_data="create_new_post"), inline_cancel_button)
    await state.set_state(CreateNewPostStates.enter_approval)
    await query.message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(text="create_new_post", state=CreateNewPostStates.enter_approval)
async def finish_new_post_create(query: CallbackQuery, state: FSMContext):
    await query.answer()

    # todo: send some request here to main server
    async with state.proxy() as storage:
        title, content, type = (
            storage["unfinished_new_post"]["title"],
            storage["unfinished_new_post"]["content"],
            storage["unfinished_new_post"]["type"],
        )

        logger.info(
            f"Okay, here we have all the data for the new post:\n\n"
            f"Title: {title}\n\nContent: {content}\n\nType: {type}\n\n"
        )
    await query.message.answer("Посмотри в консоль, там вся инфа")
    await state.finish()
