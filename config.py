from os import getenv


API_ID = int(getenv("API_ID", "22581733"))
API_HASH = getenv("API_HASH", "1db7bdcf908100cc641c6a5276765c3d")
BOT_TOKEN = getenv("BOT_TOKEN", "7651480119:AAHI9shRDU52ZL7sc4WWYpfHfNAR2pEzB9g")
OWNER_ID = int(getenv("OWNER_ID", "6530997270"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6530997270").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002487777733"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002487777733"))


