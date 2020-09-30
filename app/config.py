import logging

from envparse import env

# firstly, try to read .env flie
env.read_envfile()

TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN")
BOT_PUBLIC_PORT = env.int("BOT_PUBLIC_PORT", default=8080)

# NOTE: don't run with polling in production.

# DOMAIN = env.str("DOMAIN", default="vas3k.ru")
# WEBHOOK_BASE_PATH = env.str("WEBHOOK_BASE_PATH", default="/webhook")
# WEBHOOK_PATH = f"{WEBHOOK_BASE_PATH}/{TELEGRAM_TOKEN}"
# WEBHOOK_URL = f"https://{DOMAIN}{WEBHOOK_PATH}"

RUN_POLLING = True


CLUB_HOST = "localhost"

# Logging
logging.basicConfig(format="%(levelname)s %(asctime)s %(module)s %(message)s", level=logging.INFO)

logging.getLogger("aiogram.Middleware").setLevel(logging.DEBUG)
