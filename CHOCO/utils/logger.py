from CHOCO.config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from CHOCO import app
from CHOCO.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Pʀɪᴠᴀᴛᴇ Cʜᴀᴛ"
        logger_text = f""" ❲⛦❳─── ★ ⛨ ★ ───❲⛦❳     
**{MUSIC_BOT_NAME} 𝖯𝖫𝖠𝖸 𝖫𝖮𝖦𝖦𝖤𝖱**
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳
       ༺𝖢ʜᴀᴛ Iɴꜰᴏ༻
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳      
**𝖢ʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**𝖢ʜᴀᴛ 𝖫ɪɴᴋ:** {chatusername}
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳
       ༺𝖴ꜱᴇʀ Iɴꜰᴏ༻
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳ 
**𝖴ꜱᴇʀ:** {message.from_user.mention}

**𝖴ꜱᴇʀ Name:** @{message.from_user.username}
**Iᴅ:** `{message.from_user.id}`
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳
       ༺Pʟᴀʏ Iɴꜰᴏ༻
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳ 
**𝖲ᴇᴀʀᴄʜᴇᴅ 𝖥ʀᴏ:** {message.text}

**𝖲ᴛʀᴇᴀᴍ 𝖳ʏᴘᴇ:** {streamtype}
❲⛦❳─── ★ ⛨ ★ ───❲⛦❳"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
