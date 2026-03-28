from discord import Interaction, app_commands
from discord.ext import commands

from utils.embeds import standard_embed


class Aktivierung(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="aktivieren", description="Aktiviert BotForge auf diesem Server")
    async def aktivieren(self, interaction: Interaction, key: str) -> None:
        if interaction.guild is None:
            return
        ok = await self.bot.db.activate_guild(interaction.guild.id, key)
        if ok:
            embed = standard_embed("✅ Aktiviert", "Alle Premium-Features wurden freigeschaltet.")
        else:
            embed = standard_embed("❌ Ungültig", "Aktivierungs-ID ist ungültig oder bereits verwendet.")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="aktivierungsinfo", description="Zeigt den Aktivierungsstatus")
    async def aktivierungsinfo(self, interaction: Interaction) -> None:
        if interaction.guild is None:
            return
        active = await self.bot.db.is_activated(interaction.guild.id)
        msg = "Server ist aktiviert." if active else "Server ist nicht aktiviert."
        await interaction.response.send_message(embed=standard_embed("Lizenzstatus", msg), ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Aktivierung(bot))
