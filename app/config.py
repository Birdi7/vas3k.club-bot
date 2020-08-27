from envparse import env
from sqlalchemy import create_engine
import logging

# firstly, try to read .env flie
env.read_envfile()

TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN")
BOT_PUBLIC_PORT = env.int("BOT_PUBLIC_PORT", default=8080)

# NOTE: don't run with polling in production.

DOMAIN = env.str("DOMAIN", default="vas3k.ru")
WEBHOOK_BASE_PATH = env.str("WEBHOOK_BASE_PATH", default="/webhook")
WEBHOOK_PATH = f"{WEBHOOK_BASE_PATH}/{TELEGRAM_TOKEN}"
WEBHOOK_URL = f"https://{DOMAIN}{WEBHOOK_PATH}"

RUN_POLLING = True


# Database connection
DB_USER = env.str("DB_USER", "postgres")
DB_PASSWORD = env.str("DB_PASSWORD", "postgres")
DB_HOST = env.str("DB_HOST", "db")
DB_PORT = env.str("DB_PORT", 5432)
DB_NAME = env.str("DB_NAME", "vas3k.club-bot")

ENGINE = create_engine(
    "postgres+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
        user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, dbname=DB_NAME
    ),
    client_encoding='utf-8'
)


# Logging
logging.basicConfig()#todo
logging.getLogger('sqlalchemy.dialects.postgresql').setLevel(logging.INFO)
