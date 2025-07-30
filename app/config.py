# config.py
import os

APP_ENV = os.environ.get("APP_ENV", "development")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
PORT = int(os.environ.get("PORT", 8080))
