# Basics/dev.py
import os
import time
from watchfiles import run_process

IGNORED_DIRS = ("__pycache__", "assets", ".git", ".venv")

def banner():
    os.system("clear")
    print(f"🔁 Reloaded at {time.strftime('%H:%M:%S')}")
    print("=" * 40)

def watch_filter(change, path):
    return not any(ignored in path for ignored in IGNORED_DIRS)

def start():
    banner()
    run_process(
        ".",
        target="uv run python main.py",
        watch_filter=watch_filter,
    )

if __name__ == "__main__":
    start()
