import time


class TTLCache:
    def __init__(self) -> None:
        self._store: dict[str, tuple[float, object]] = {}

    def set(self, key: str, value: object, ttl: int) -> None:
        self._store[key] = (time.time() + ttl, value)

    def get(self, key: str) -> object | None:
        item = self._store.get(key)
        if not item:
            return None
        expires, value = item
        if expires < time.time():
            del self._store[key]
            return None
        return value
