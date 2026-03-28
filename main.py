"""Root entrypoint for Render services.

Allows `python main.py` to work even though the real bot entrypoint lives in
`BotForge/main.py`.
"""

from runpy import run_path
from pathlib import Path

if __name__ == "__main__":
    run_path(str(Path(__file__).parent / "BotForge" / "main.py"), run_name="__main__")
