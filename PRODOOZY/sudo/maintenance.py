from pyrogram import filters
from pyrogram.types import Message

from CHOCO.DLK import get_command, get_string
from CHOCO import app
from CHOCO.misc import SUDOERS
from CHOCO.utils.database import (get_lang, is_maintenance,
                                       maintenance_off,
                                       maintenance_on)
from CHOCO.utils.decorators.language import language

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        if await is_maintenance() is False:
            await message.reply_text(
                "🥀 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞 𝐌𝐨𝐝𝐞 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐄𝐧𝐚𝐛𝐞 💖"
            )
        else:
            await maintenance_on()
            await message.reply_text(_["maint_2"])
    elif state == "disable":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text(_["maint_3"])
        else:
            await message.reply_text(
                "🥀 𝐌𝐚𝐢𝐧𝐭𝐞𝐧𝐚𝐧𝐜𝐞 𝐌𝐨𝐝𝐞 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🚫"
            )
    else:
        await message.reply_text(usage)
