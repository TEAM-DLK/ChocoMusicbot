from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from CHOCO import config
from CHOCO import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Cᴏᴍᴍᴀɴᴅs",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="ʏᴏᴜTᴜʙᴇ", url=f"https://www.youtube.com/c/DJDOOZY"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="ʏᴏᴜTᴜʙᴇ", url=f"https://www.youtube.com/c/DJDOOZY"
            )
        ],
        [
            InlineKeyboardButton(
                text="Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER
            )
        ]
     ]
    return buttons
