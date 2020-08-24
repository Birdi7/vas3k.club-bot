from app import config
from app.misc import setup

if __name__ == '__main__':
    setup()
    if hasattr(config, "RUN_POLLING") and config.RUN_POLLING:
        from app.utils.executor import runner
        runner.start_polling()
