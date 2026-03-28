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
pip install -r requirements.txt
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

### Render Build & Start Commands

**Worker (Discord Bot):**
- Build Command: `pip install -r requirements.txt`
- Start Command: `python main.py`

**Web Service (Dashboard):**
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn dashboard_app:app --host 0.0.0.0 --port $PORT`

### Wichtiger Hinweis (Render Fehlerbehebung)
Wenn in Render als Build Command nur `requirements.txt` eingetragen ist, schlägt der Build fehl ("command not found").
Nutze **immer** einen echten Befehl:

- Build Command: `pip install -r requirements.txt`
- Worker Start Command: `python main.py`
- Web Start Command: `uvicorn dashboard_app:app --host 0.0.0.0 --port $PORT`

- Falls du den Fehler `python: can\'t open file .../main.py` siehst, ist der Start Command falsch gesetzt.
  Nutze dann `python main.py` (oder alternativ `python BotForge/main.py`).

