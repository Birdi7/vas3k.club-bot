from app import settings
from app.misc import setup


# FIXME: remove this shit once the debug is over
async def test_api_caller():
    from app.utils.blog_api import BlogApiCaller

    caller = BlogApiCaller()
    await caller.call("user", ["dev", "my-secret-hash"])


if __name__ == "__main__":
    setup()
    if hasattr(settings, "RUN_POLLING") and settings.RUN_POLLING:
        from app.utils.executor import runner

        runner.start_polling()

    # FIXME: remove this shit once the debug is over
    import asyncio

    asyncio.run(test_api_caller())
