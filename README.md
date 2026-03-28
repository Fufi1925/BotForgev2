# BotForgev2 / BotForgev1 Scaffold

Dieses Repository enthält jetzt eine produktionsnahe **BotForgev1**-Struktur mit:

- modularem Discord-Bot (AutoShardedBot)
- Cogs für Moderation, Security, Musik, Tracking und Utilities
- Aktivierungssystem (Server-gebunden, Key nur 1x nutzbar)
- FastAPI Dashboard-App
- Render-Deployment (`render.yaml` mit Worker + Web Service)

## Projektstruktur

```text
BotForge/
├── core/
├── services/
├── api/
├── cogs/
├── utils/
├── main.py
├── config.py
├── database.py
├── dashboard_app.py
├── requirements.txt
└── render.yaml
```

## Start lokal

```bash
pip install -r BotForge/requirements.txt
cp BotForge/.env.example .env
python BotForge/main.py
```

Dashboard:

```bash
uvicorn BotForge.dashboard_app:app --reload
```

## Render

1. Repo bei Render verbinden
2. Blueprint Deploy mit `BotForge/render.yaml`
3. Secrets aus `.env.example` in Render Environment Variables setzen
