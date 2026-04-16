from os import getenv
from dotenv import load_dotenv
load_dotenv()
class BotConfig:
    BOT_TOKEN = getenv("BOT_TOKEN")

class DatabaseConfig:
    DB_NAME = getenv("DB_NAME")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")
    DB_PORT = getenv("DB_PORT")

class ENV:
    bot = BotConfig()
    db = DatabaseConfig()
