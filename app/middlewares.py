import logging

from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware


def setup(dispatcher: Dispatcher):
    logging.basicConfig(level=logging.INFO)
    dispatcher.middleware.setup(LoggingMiddleware("bot"))
