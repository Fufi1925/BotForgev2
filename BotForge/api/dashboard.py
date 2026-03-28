from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, Response

from api.auth import verify_dashboard_key
from api.routes.system import router as system_router


SITE_NAME = "BotForge"


def create_dashboard_app() -> FastAPI:
    app = FastAPI(title="BotForge Dashboard")
    app.include_router(system_router, prefix="/api", dependencies=[Depends(verify_dashboard_key)])

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request) -> str:
        base = str(request.base_url).rstrip("/")
        return f"""
<!doctype html>
<html lang='de'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width,initial-scale=1'>
  <title>{SITE_NAME} | Premium Discord Moderation Bot</title>
  <meta name='description' content='BotForge ist ein Premium Discord Bot für AutoModeration, AntiRaid, Logging, Musik und Dashboard-Steuerung.'>
  <meta name='robots' content='index,follow'>
  <link rel='canonical' href='{base}/'>
  <meta property='og:title' content='{SITE_NAME} | Premium Discord Moderation Bot'>
  <meta property='og:description' content='AutoMod, AntiRaid, Logging, Music, Dashboard.'>
  <meta property='og:type' content='website'>
  <meta property='og:url' content='{base}/'>
  <style>
    body {{font-family: Inter, Arial, sans-serif; background:#0b1020; color:#e7ebff; margin:0;}}
    .wrap {{max-width:980px; margin:48px auto; padding:0 20px;}}
    .card {{background:#131b33; border:1px solid #2a3766; border-radius:14px; padding:24px; margin-bottom:16px;}}
    .btn {{display:inline-block; background:#5865f2; color:white; text-decoration:none; padding:10px 14px; border-radius:10px; margin-right:10px;}}
    ul {{line-height:1.8;}}
  </style>
</head>
<body>
  <div class='wrap'>
    <div class='card'>
      <h1>🚀 {SITE_NAME} ist online</h1>
      <p>Premium Discord Bot für Moderation, AntiRaid, Musik, Logging und Dashboard.</p>
      <a class='btn' href='/health'>Health</a>
      <a class='btn' href='/docs'>API Docs</a>
      <a class='btn' href='/about'>About</a>
    </div>
    <div class='card'>
      <h2>Feature Highlights</h2>
      <ul>
        <li>KI-Spam-Schutz & Ghost-Ping-Detection</li>
        <li>Join-Gate, Raid-Schutz, Security Guards</li>
        <li>Music-System mit Lavalink-Support</li>
        <li>Live Dashboard + API</li>
      </ul>
    </div>
  </div>
</body>
</html>
        """

    @app.get("/about", response_class=HTMLResponse)
    async def about() -> str:
        return "<h1>About BotForge</h1><p>BotForge ist ein Discord Premium Bot mit Dashboard.</p>"

    @app.get("/robots.txt", response_class=PlainTextResponse)
    async def robots() -> str:
        return "User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n"

    @app.get("/sitemap.xml")
    async def sitemap(request: Request) -> Response:
        base = str(request.base_url).rstrip("/")
        xml = f"""<?xml version='1.0' encoding='UTF-8'?>
<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
  <url><loc>{base}/</loc></url>
  <url><loc>{base}/about</loc></url>
  <url><loc>{base}/health</loc></url>
</urlset>"""
        return Response(content=xml, media_type="application/xml")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app
