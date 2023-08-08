import os
from pyrogram import Client
# ---------------------------------------------------------------------------------------------
plugins = dict(root="plugins")
# ---------------------------------------------------------------------------------------------
APP_ID = int(os.environ.get('APP_ID', 'YOUR_APP_ID'))
APP_HASH = os.environ.get('APP_HASH', 'YOUR_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')
# ---------------------------------------------------------------------------------------------
app = Client(name="user_info_bot", api_id=APP_ID, api_hash=APP_HASH,bot_token=BOT_TOKEN,plugins=plugins).run()

