from pyrogram import Client, enums
from pyrogram.types import Message

@Client.on_message()
def start(client: Client, message: Message):
    # username
    username = message.forward_from.username if message.forward_from else message.from_user.username
    # user or chat id
    user_id = message.forward_from.id if message.forward_from else message.from_user.id
    # language
    language_code = message.from_user.language_code

    is_bot = message.forward_from.is_bot if message.forward_from else message.from_user.is_bot
    is_verified = message.forward_from.is_verified if message.forward_from else message.from_user.is_verified
    is_fake = message.forward_from.is_fake if message.forward_from else message.from_user.is_fake

    if message.from_user.status == enums.UserStatus.RECENTLY:
        last_seen = 'recently'
    elif message.from_user.status == enums.UserStatus.ONLINE:
        last_seen = 'online'
    elif message.from_user.status == enums.UserStatus.OFFLINE:
        last_seen = 'offline'
    else:
        last_seen = 'unknown'

    message.reply_chat_action(enums.ChatAction.TYPING)
    message.reply_text(
        f"**username: ** @{username}\n"
        f"**user Id: ** `{user_id}`\n"
        f"**language: ** {language_code}\n"
        f"**Is Bot: ** {is_bot}\n"
        f"**Is Verified: ** {is_verified}\n"
        f"**Is Fake: ** {is_fake}\n"
        f"**last seen: ** {last_seen}\n",
        reply_to_message_id=message.id,
    )

