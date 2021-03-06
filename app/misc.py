import logging
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import settings

app_dir: Path = Path(__file__).parent.parent
locales_dir = app_dir / "locales"

logger = logging.getLogger("bot")

bot = Bot(settings.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)

# todo: change to some persistent storage...probably
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def setup():
    logger.info("Configure handlers...")
    from app.utils import filters, middlewares

    middlewares.setup(dp)
    filters.setup(dp)

    import app.handlers
    import app.personal.handlers  # noqa

    logger.info("Configuration finished")
