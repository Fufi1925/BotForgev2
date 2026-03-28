import discord
from discord import Interaction, app_commands
from discord.ext import commands

from utils.embeds import standard_embed


class UtilityPro(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Zeigt die Bot-Latenz")
    async def ping(self, interaction: Interaction) -> None:
        ms = round(self.bot.latency * 1000)
        await interaction.response.send_message(
            embed=standard_embed("🏓 Pong", f"Aktuelle Latenz: **{ms} ms**"),
            ephemeral=True,
        )

    @app_commands.command(name="botinfo", description="Zeigt Infos über BotForge")
    async def botinfo(self, interaction: Interaction) -> None:
        guild_count = len(self.bot.guilds)
        embed = standard_embed(
            "🤖 BotForge Info",
            f"Server: **{guild_count}**\nShard Count: **{self.bot.shard_count or 1}**",
        )
        embed.add_field(name="Version", value="BotForgev1", inline=True)
        embed.add_field(name="Framework", value=f"discord.py {discord.__version__}", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UtilityPro(bot))
