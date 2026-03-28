import asyncio
import logging

from core.bot import create_bot
from core.loader import load_all_cogs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("botforge")


async def main() -> None:
    bot = create_bot()
    await load_all_cogs(bot)
    logger.info("Starting BotForge worker with sharding support")
    await bot.start(bot.settings.discord_token)


if __name__ == "__main__":
    asyncio.run(main())
