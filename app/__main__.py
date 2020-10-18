from app import settings
from app.misc import setup

if __name__ == "__main__":
    setup()
    if hasattr(settings, "RUN_POLLING") and settings.RUN_POLLING:
        from app.utils.executor import runner

        runner.start_polling()
