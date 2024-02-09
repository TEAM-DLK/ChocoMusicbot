from pyrogram import filters
from pyrogram.types import Message

from CHOCO.config import BANNED_USERS
from CHOCO import app
from CHOCO.core.call import CHOCOh
from CHOCO.utils.database import is_muted, mute_on
from CHOCO.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["mute", "cmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if await is_muted(chat_id):
        return await message.reply_text("**🔇𝐌𝐮𝐬𝐢𝐜 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐌𝐮𝐭𝐞𝐝 🌷 ...**")
    await mute_on(chat_id)
    await CHOCOh.mute_stream(chat_id)
    await message.reply_text("**🔇𝐌𝐮𝐭𝐞𝐝 🌷 ...**\n\n⎿𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲 > {}")

