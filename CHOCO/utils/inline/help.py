from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from CHOCO import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            # text=_["BACK_BUTTON"],
            text="Uᴘᴅᴀᴛᴇs​",
            url=f"https://t.me/DOOZY_OFF",
        ),
        InlineKeyboardButton(
            text="Cʀᴇᴀᴛᴏʀ",
            url=f"t.me/iiiIiiiAiiiMiii",
        ),
        InlineKeyboardButton(
            text="C​​ʟᴏsᴇ", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Aᴅᴍɪɴ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Aᴜᴛʜ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="Bʟᴀᴄᴋʟɪsᴛ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="​​Bʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="Gʙᴀɴ",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Exᴛʀᴀ​",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Pɪɴɢ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Pʟᴀʏ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="Pʟᴀʏʟɪsᴛ",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Vɪᴅᴇᴏᴄʜᴀᴛs",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="Sᴛᴀʀᴛ",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="Sᴜᴅᴏ",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    # text=_["BACK_BUTTON"],
                    text="B​​ᴀᴄᴋ",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="B​​ᴀᴄᴋ",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
