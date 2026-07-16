from pathlib import Path
from dotenv import load_dotenv
from getpass import getpass
import os


CONFIG_DIR = Path.home() / ".config" / "cliweather"
CONFIG_FILE = CONFIG_DIR / ".env"


def load_config():
    """
    Loads the user's configuration file if it exists.
    """
    if CONFIG_FILE.exists():
        load_dotenv(CONFIG_FILE)

def setup():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    openweather = getpass("OpenWeatherMap API Key: ").strip()
    groq = getpass("Groq API Key: ").strip()

    with open(CONFIG_FILE, "w") as file:
        file.write(f"API_KEY={openweather}\n")
        file.write(f"GROQ_API_KEY={groq}\n")

    print()
    print("Configuration saved.")
    print(f"Location: {CONFIG_FILE}")