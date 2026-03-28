from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    discord_token: str
    database_url: str
    lavalink_host: str
    lavalink_password: str
    spotify_client_id: str
    spotify_client_secret: str
    dashboard_secret: str
    dashboard_api_key: str
    embed_footer_icon: str

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            discord_token=os.getenv("DISCORD_TOKEN", ""),
            database_url=os.getenv("DATABASE_URL", "sqlite+aiosqlite:///botforge.db"),
            lavalink_host=os.getenv("LAVALINK_HOST", "localhost:2333"),
            lavalink_password=os.getenv("LAVALINK_PASSWORD", "youshallnotpass"),
            spotify_client_id=os.getenv("SPOTIFY_CLIENT_ID", ""),
            spotify_client_secret=os.getenv("SPOTIFY_CLIENT_SECRET", ""),
            dashboard_secret=os.getenv("DASHBOARD_SECRET", "change-me"),
            dashboard_api_key=os.getenv("DASHBOARD_API_KEY", "change-me"),
            embed_footer_icon=os.getenv(
                "EMBED_FOOTER_ICON",
                "https://cdn.discordapp.com/attachments/1484888992209047696/1487168273240952923/file_00000000f688720abc73d778f13d5c871.png",
            ),
        )
