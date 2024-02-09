import asyncio

from pyrogram import filters

from CHOCO import config
from CHOCO.DLK import get_command
from CHOCO import app
from CHOCO.misc import SUDOERS
from CHOCO.utils.database.memorydatabase import get_video_limit
from CHOCO.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭 ... 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬..."
    )
    v_limit = await get_video_limit()
    MUSIC_BOT_NAME = config.MUSIC_BOT_NAME
    up_r = f"[𝐑𝐞𝐩𝐨]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "𝐘𝐞𝐬"
    else:
        ass = "𝐍𝐨"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "𝐘𝐞𝐬"
    else:
        pvt = "𝐍𝐨"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "𝐘𝐞𝐬"
    else:
        a_sug = "𝐍𝐨"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "𝐘𝐞𝐬"
    else:
        down = "𝐍𝐨"

    if not config.GITHUB_REPO:
        git = "𝐍𝐨"
    else:
        git = f"[ʀᴇᴩᴏ]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "𝐍𝐨"
    else:
        start = f"[ɪᴍᴀɢᴇ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "𝐍𝐨"
    else:
        s_c = f"[ᴄʜᴀɴɴᴇʟ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "𝐍𝐨"
    else:
        s_g = f"[sᴜᴩᴩᴏʀᴛ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "𝐍𝐨"
    else:
        token = "𝐘𝐞𝐬"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "𝐍𝐨"
    else:
        sotify = "𝐘𝐞𝐬"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐂𝐨𝐧𝐟𝐢𝐠 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 :**

**<u>𝐁𝐚𝐬𝐢𝐜 𝐕𝐚𝐫𝐢𝐚𝐛𝐞𝐬:</u>**
**𝐁𝐨𝐭 𝐍𝐚𝐦𝐞** : `{MUSIC_BOT_NAME}`
**𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 𝐋𝐢𝐦𝐢𝐭** : `{play_duration} ᴍɪɴᴜᴛᴇs`
**𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐦𝐢𝐭** :` {song} ᴍɪɴᴜᴛᴇs`
**𝐎𝐰𝐧𝐞𝐫 𝐈𝐝** : `{owner_id}`
    
**<u>𝐑𝐞𝐩𝐨 𝐕𝐚𝐫:</u>**
**𝐔𝐩 𝐑𝐞𝐩𝐨** : `{up_r}`
**𝐔𝐩 𝐁𝐫𝐚𝐧𝐜𝐡** : `{up_b}`
**𝐆𝐢𝐭 𝐑𝐞𝐩𝐨** :` {git}`
**𝐆𝐢𝐭 𝐓𝐨𝐤𝐞𝐧**:` {token}`


**<u>𝐁𝐨𝐭 𝐕𝐚𝐫:</u>**
**𝐀𝐮𝐭𝐨_𝐋𝐞𝐚𝐯𝐢𝐧𝐠_𝐀𝐬𝐬** : `{ass}`
**𝐀𝐬𝐬_𝐋𝐞𝐚𝐯𝐞_𝐓𝐢𝐦𝐞** : `{auto_leave} sᴇᴄᴏɴᴅs`
**𝐀𝐮𝐭𝐨_𝐒𝐮𝐠𝐠_𝐌𝐨𝐝𝐞** :` {a_sug}`
**𝐀𝐮𝐭𝐨_𝐒𝐮𝐠𝐠_𝐓𝐢𝐦𝐞** : `{auto_sug} sᴇᴄᴏɴᴅs`
**𝐀𝐮𝐭𝐨_𝐃𝐨𝐰𝐧_𝐂𝐥𝐞𝐚𝐫** : `{down}`
**𝐏𝐫𝐢𝐯𝐚𝐭𝐞_𝐁𝐨𝐭_𝐌𝐨𝐝𝐞** : `{pvt}`
**𝐘𝐓_𝐄𝐝𝐢𝐭_𝐒𝐥𝐞𝐞𝐩** : `{yt_sleep} sᴇᴄᴏɴᴅs`
**𝐓𝐞𝐥𝐞_𝐄𝐝𝐢𝐭_𝐒𝐥𝐞𝐞𝐩** :` {tg_sleep} sᴇᴄᴏɴᴅs`
**𝐂𝐥𝐞𝐚𝐧𝐌𝐨𝐝𝐞_𝐌𝐢𝐧𝐬** : `{cm} ᴍɪɴᴜᴛᴇs`
**𝐕𝐢𝐝𝐞𝐨_𝐒𝐭𝐫𝐞𝐚𝐦_𝐋𝐢𝐦𝐢𝐭** : `{v_limit} ᴄʜᴀᴛs`
**𝐒𝐞𝐫𝐯𝐞𝐫_𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭_𝐋𝐢𝐦𝐢𝐭** :` {playlist_limit}`
**𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭_𝐅𝐞𝐭𝐜𝐡_𝐋𝐢𝐦𝐢𝐭** :` {fetch_playlist}`

**<u>𝐒𝐩𝐨𝐭𝐢𝐟𝐲 𝐕𝐚𝐫:</u>**
**𝐒𝐩𝐨𝐭𝐢𝐟𝐲_𝐂𝐥𝐢𝐞𝐧𝐭_𝐈𝐝** :` {sotify}`
**𝐒𝐩𝐨𝐭𝐢𝐟𝐲_𝐂𝐥𝐢𝐞𝐧𝐭_𝐒𝐞𝐜𝐫𝐞𝐭𝐬** : `{sotify}`

**<u>𝐏𝐥𝐚𝐲 𝐒𝐢𝐳𝐞 𝐕𝐚𝐫𝐬:</u>**
**𝐓𝐠_𝐀𝐮𝐝_𝐅𝐢𝐥𝐞_𝐋𝐢𝐦𝐢𝐭** :` {tg_aud}`
**𝐓𝐠_𝐕𝐢𝐝𝐞𝐨_𝐅𝐢𝐥𝐞_𝐋𝐢𝐦𝐢𝐭** :` {tg_vid}`

**<u>𝐄𝐱𝐭𝐫𝐚 𝐕𝐚𝐫𝐬:</u>**
**𝐒𝐮𝐩𝐩𝐨𝐫𝐭_𝐂𝐡𝐚𝐧𝐧𝐞𝐥** : `{s_c}`
**𝐒𝐮𝐩𝐩𝐨𝐫𝐭_𝐆𝐫𝐨𝐮𝐩** : ` {s_g}`
**𝐒𝐭𝐚𝐫𝐭_𝐈𝐦𝐠_𝐔𝐫𝐥** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
