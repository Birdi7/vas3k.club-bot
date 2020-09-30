from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateNewPostStates(StatesGroup):
    enter_title = State()
    enter_post_type = State()
    enter_approval = State()
