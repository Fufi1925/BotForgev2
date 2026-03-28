from fastapi import Depends, FastAPI

from api.auth import verify_dashboard_key
from api.routes.system import router as system_router


def create_dashboard_app() -> FastAPI:
    app = FastAPI(title="BotForge Dashboard")
    app.include_router(system_router, prefix="/api", dependencies=[Depends(verify_dashboard_key)])

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
