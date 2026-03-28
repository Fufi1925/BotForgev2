import logging

import discord
from discord.ext import commands

from config import Settings
from services.database import Database

logger = logging.getLogger("botforge")


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

        if not self.settings.auto_sync_commands:
            logger.info("Command sync disabled by AUTO_SYNC_COMMANDS=false")
            return

        if self.settings.dev_guild_id:
            guild = discord.Object(id=self.settings.dev_guild_id)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            logger.info("Synced %s command(s) to dev guild %s", len(synced), self.settings.dev_guild_id)
        else:
            synced = await self.tree.sync()
            logger.info("Synced %s global command(s)", len(synced))

    async def close(self) -> None:
        await self.db.close()
        await super().close()


def create_bot() -> BotForge:
    settings = Settings.from_env()
    return BotForge(settings)
