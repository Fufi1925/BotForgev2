from __future__ import annotations

import aiosqlite


class Database:
    def __init__(self, database_url: str) -> None:
        if database_url.startswith("sqlite"):
            self.path = database_url.split("///")[-1]
        else:
            self.path = "botforge.db"
        self._conn: aiosqlite.Connection | None = None

    async def connect(self) -> None:
        self._conn = await aiosqlite.connect(self.path)
        await self._conn.execute("PRAGMA journal_mode=WAL;")

    async def bootstrap(self) -> None:
        assert self._conn
        await self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS activations (
                guild_id INTEGER PRIMARY KEY,
                activation_key TEXT UNIQUE NOT NULL,
                activated_at TEXT NOT NULL
            )
            """
        )
        await self._conn.execute(
            """
            CREATE TABLE IF NOT EXISTS activation_keys (
                key TEXT PRIMARY KEY,
                used_by_guild INTEGER
            )
            """
        )
        await self._conn.commit()

    async def create_activation_key(self, key: str) -> None:
        assert self._conn
        await self._conn.execute("INSERT OR IGNORE INTO activation_keys(key, used_by_guild) VALUES(?, NULL)", (key,))
        await self._conn.commit()

    async def activate_guild(self, guild_id: int, key: str) -> bool:
        assert self._conn
        cur = await self._conn.execute("SELECT used_by_guild FROM activation_keys WHERE key = ?", (key,))
        row = await cur.fetchone()
        if not row or row[0] is not None:
            return False
        await self._conn.execute("UPDATE activation_keys SET used_by_guild=? WHERE key=?", (guild_id, key))
        await self._conn.execute(
            "INSERT OR REPLACE INTO activations(guild_id, activation_key, activated_at) VALUES(?, ?, datetime('now'))",
            (guild_id, key),
        )
        await self._conn.commit()
        return True

    async def is_activated(self, guild_id: int) -> bool:
        assert self._conn
        cur = await self._conn.execute("SELECT 1 FROM activations WHERE guild_id = ?", (guild_id,))
        return await cur.fetchone() is not None

    async def close(self) -> None:
        if self._conn:
            await self._conn.close()
