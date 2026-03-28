from pathlib import Path

from discord.ext import commands


async def load_all_cogs(bot: commands.Bot) -> None:
    cog_dir = Path(__file__).resolve().parents[1] / "cogs"
    for file in cog_dir.glob("*.py"):
        if file.name.startswith("_"):
            continue
        await bot.load_extension(f"cogs.{file.stem}")
