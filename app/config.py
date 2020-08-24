
from envparse import env

TELEGRAM_TOKEN = env.str("TELEGRAM_TOKEN")
BOT_PUBLIC_PORT = env.int("BOT_PUBLIC_PORT", default=8080)

# NOTE: don't run with polling in production. 
RUN_POLLING = True
DOMAIN = env.str("DOMAIN", default="vas3k.ru")
WEBHOOK_BASE_PATH = env.str("WEBHOOK_BASE_PATH", default="/webhook")
WEBHOOK_PATH = f"{WEBHOOK_BASE_PATH}/{TELEGRAM_TOKEN}"
WEBHOOK_URL = f"https://{DOMAIN}{WEBHOOK_PATH}"

print(WEBHOOK_URL)
