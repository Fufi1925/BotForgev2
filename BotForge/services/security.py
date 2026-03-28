import re

TOKEN_PATTERN = re.compile(r"[A-Za-z\d_]{24}\.[A-Za-z\d_]{6}\.[A-Za-z\d_-]{27}")


def contains_possible_token(message: str) -> bool:
    return bool(TOKEN_PATTERN.search(message))
