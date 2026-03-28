import discord

from config import Settings


def standard_embed(title: str, description: str) -> discord.Embed:
    settings = Settings.from_env()
    embed = discord.Embed(title=title, description=description, color=discord.Color.blurple())
    embed.set_footer(text="Powered by BotForge", icon_url=settings.embed_footer_icon)
    return embed
