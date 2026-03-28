from fastapi import Header, HTTPException

from config import Settings


def verify_dashboard_key(x_api_key: str = Header(default="")) -> None:
    settings = Settings.from_env()
    if x_api_key != settings.dashboard_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
