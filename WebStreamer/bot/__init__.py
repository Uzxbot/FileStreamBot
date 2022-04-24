
from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    session_name='File_to_Link',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
