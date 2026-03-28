"""Root ASGI app alias for Render.

Lets users run: `uvicorn dashboard_app:app --host 0.0.0.0 --port $PORT`
"""

from BotForge.dashboard_app import app

__all__ = ["app"]
