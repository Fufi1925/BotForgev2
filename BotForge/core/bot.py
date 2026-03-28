import discord
from discord.ext import commands

from config import Settings
from services.database import Database


class BotForge(commands.AutoShardedBot):
    def __init__(self, settings: Settings):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.settings = settings
        self.db = Database(settings.database_url)

    async def setup_hook(self) -> None:
        await self.db.connect()
        await self.db.bootstrap()

    async def close(self) -> None:
        await self.db.close()
        await super().close()


def create_bot() -> BotForge:
    settings = Settings.from_env()
    return BotForge(settings)
