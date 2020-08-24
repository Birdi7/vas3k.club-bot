import logging
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import config

app_dir: Path = Path(__file__).parent.parent
locales_dir = app_dir / "locales"

logger = logging.getLogger("bot")

bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)

# todo: change to some persistent storage...probably
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def setup():
    logger.info("Configure handlers...")
    from app import middlewares

    middlewares.setup(dp)

    import app.handlers  # noqa
