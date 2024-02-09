from pyrogram import filters
from pyrogram.types import Message

from CHOCO.config import BANNED_USERS
from CHOCO.utils.teamdlkmusic.proX import command
from CHOCO import app
from CHOCO.core.call import CHOCOh
from CHOCO.utils.database import is_muted, mute_off
from CHOCO.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["unmute", "cunmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**Error, Wrong Usage Of Commands...**")
    if not await is_muted(chat_id):
        return await message.reply_text("**Already Playing...**")
    await mute_off(chat_id)
    await CHOCOh.unmute_stream(chat_id)
    await message.reply_text(
        "**Unmuted...**".format(message.from_user.mention)
    )

