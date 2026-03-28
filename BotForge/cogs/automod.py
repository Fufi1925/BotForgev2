from discord.ext import commands


class AutoMod(commands.Cog):
    """KI-Spam-Erkennung, Mention-Blocker, Emoji-Spam-Schutz (Scaffold)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutoMod(bot))
