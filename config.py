import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "inventory.db")

APP_NAME = "Enterprise inventory system"
VERSION = "1.0.0"
CURRENCY_SYMBOL = "$"