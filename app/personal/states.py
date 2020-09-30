from aiogram.dispatcher.filters.state import State, StatesGroup


class ProcessAuthStates(StatesGroup):
    enter_secret_hash = State()
