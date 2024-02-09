from pyrogram import Client, filters
from pyrogram.types import Message
from CHOCO.config import LOG_GROUP_ID
from CHOCO import app

async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(_, message: Message):
    if (await app.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "Uɴᴋɴᴏᴡɴ Uᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "Pʀɪᴠᴀᴛᴇ Cʜᴀᴛ"
        chat_id = message.chat.id
        new = f"**✫** <b><u>Nᴇᴡ Gʀᴏᴜᴘ</u></b> **:**\n\n**Cʜᴀᴛ Iᴅ :** {chat_id}\n**Cʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :** {username}\n**Cʜᴀᴛ ᴛɪᴛʟᴇ :** {title}\n\n**Aᴅᴅᴇᴅ Bʏ :** {added_by}"
        await new_message(LOG_GROUP_ID, new)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "Uɴᴋɴᴏᴡɴ Usᴇʀ"
        title = message.chat.title
        chat_id = message.chat.id
        left = f"**✫** <b><u>Lᴇғᴛ Gʀᴏᴜᴘ</u></b> **:**\n\n**Cʜᴀᴛ Iᴅ :** {chat_id}\n**Cʜᴀᴛ Tɪᴛʟᴇ :** {title}\n\n**Rᴇᴍᴏᴠᴇᴅ Bʏ :** {remove_by}"
        await new_message(LOG_GROUP_ID, left)
