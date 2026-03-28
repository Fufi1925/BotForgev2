from discord import Interaction, app_commands
from discord.ext import commands

from utils.embeds import standard_embed


class Konfiguration(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="featureliste", description="Zeigt die wichtigsten BotForge Features")
    async def featureliste(self, interaction: Interaction) -> None:
        text = (
            "🛡️ AutoMod & AntiRaid\n"
            "🎵 Music Ultra (Lavalink Ready)\n"
            "📊 Stats & Tracking\n"
            "📋 Logging & Admin Tools\n"
            "🌐 Web Dashboard"
        )
        await interaction.response.send_message(
            embed=standard_embed("BotForge Module", text),
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Konfiguration(bot))
