from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse

from api.auth import verify_dashboard_key
from api.routes.system import router as system_router


def create_dashboard_app() -> FastAPI:
    app = FastAPI(title="BotForge Dashboard")
    app.include_router(system_router, prefix="/api", dependencies=[Depends(verify_dashboard_key)])

    @app.get("/", response_class=HTMLResponse)
    async def home() -> str:
        return """
<!doctype html>
<html lang='de'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width,initial-scale=1'>
  <title>BotForge Dashboard</title>
  <style>
    body {font-family: Inter, Arial, sans-serif; background:#0b1020; color:#e7ebff; margin:0;}
    .wrap {max-width:960px; margin:48px auto; padding:0 20px;}
    .card {background:#131b33; border:1px solid #2a3766; border-radius:14px; padding:24px; margin-bottom:16px;}
    h1 {margin-top:0;}
    a.btn {display:inline-block; background:#5865f2; color:white; text-decoration:none; padding:10px 14px; border-radius:10px; margin-right:10px;}
    ul {line-height:1.8;}
    code {background:#111935; padding:2px 6px; border-radius:6px;}
  </style>
</head>
<body>
  <div class='wrap'>
    <div class='card'>
      <h1>🚀 BotForge Dashboard ist online</h1>
      <p>Willkommen! Dein Dashboard läuft korrekt auf Render.</p>
      <a class='btn' href='/health'>Health Check</a>
      <a class='btn' href='/docs'>API Docs</a>
    </div>
    <div class='card'>
      <h2>Discord Bot Commands</h2>
      <ul>
        <li><code>/aktivieren</code> – aktiviert den Server mit Key</li>
        <li><code>/aktivierungsinfo</code> – zeigt Aktivierungsstatus</li>
        <li><code>/ping</code> – Bot Latenz prüfen</li>
        <li><code>/botinfo</code> – Bot Infos anzeigen</li>
        <li><code>/featureliste</code> – zeigt verfügbare Module</li>
      </ul>
    </div>
  </div>
</body>
</html>
        """

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
