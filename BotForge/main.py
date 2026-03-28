import asyncio
import logging
import os

from aiohttp import web

from core.bot import create_bot
from core.loader import load_all_cogs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("botforge")


async def _start_health_server() -> web.AppRunner | None:
    """Start a tiny health server for Render web services.

    Render web services must bind to $PORT. If PORT is set, we expose /health.
    """
    port = os.getenv("PORT")
    if not port:
        return None

    app = web.Application()

    async def health(_: web.Request) -> web.Response:
        return web.json_response({"status": "ok"})

    app.router.add_get("/health", health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=int(port))
    await site.start()
    logger.info("Health server listening on port %s", port)
    return runner


async def main() -> None:
    bot = create_bot()
    await load_all_cogs(bot)

    health_runner = await _start_health_server()
    logger.info("Starting BotForge worker with sharding support")

    try:
        await bot.start(bot.settings.discord_token)
    finally:
        if health_runner is not None:
            await health_runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
