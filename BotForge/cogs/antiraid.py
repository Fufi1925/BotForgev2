from discord.ext import commands


class AntiRaid(commands.Cog):
    """Join-Rate-Limit, Account-Age-Gate, VPN-Check, Lockdown-Mode (Scaffold)."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AntiRaid(bot))
