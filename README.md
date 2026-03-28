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

### Render Port-Fehler beheben (`No open ports detected`)
Dieser Fehler entsteht, wenn der Bot als **Web Service** läuft, aber keinen Port öffnet.

Ab jetzt öffnet `BotForge/main.py` automatisch einen kleinen `/health` Server auf `$PORT` (wenn `PORT` gesetzt ist).

Empfehlung:
- Für den Discord-Bot: **Background Worker** verwenden.
- Falls du trotzdem Web Service nutzt: Start Command `python BotForge/main.py` oder `python main.py` und Render erkennt den offenen Port.

### Sehr wichtig: Richtiger Render Service-Typ
Für den Discord-Bot darfst du **nicht** "Web Service" nutzen, sonst kommt `No open ports detected`.

Nutze für den Bot:
- **Type:** `Background Worker`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python BotForge/main.py`

Nutze für das Dashboard:
- **Type:** `Web Service`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn dashboard_app:app --host 0.0.0.0 --port $PORT`

## Dashboard & Commands (Wichtig)

Wenn `https://deine-app.onrender.com/` vorher `Not Found` gezeigt hat:
- Das Dashboard hat jetzt eine echte Startseite auf `/`.
- API ist unter `/api/*` (mit API-Key), Health unter `/health`, Docs unter `/docs`.

Wenn der Bot online ist aber keine Slash-Commands sichtbar sind:
- `AUTO_SYNC_COMMANDS=true` setzen
- optional `DEV_GUILD_ID=<deine_guild_id>` setzen (schnelleres Command-Sync fürs Testen)
- Bot neu starten

Direkt verfügbare Commands:
- `/aktivieren`
- `/aktivierungsinfo`
- `/ping`
- `/botinfo`
- `/featureliste`

