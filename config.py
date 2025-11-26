import os

API_ID = int(os.environ.get("API_ID", "25527780"))
API_HASH = os.environ.get("API_HASH", "1ed74b5498913cd53b47063f692abd38")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1002557949787")
IS_PRIVATE = os.environ.get("IS_PRIVATE", True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "8124792926"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'ainfilm')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "8124792926").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
