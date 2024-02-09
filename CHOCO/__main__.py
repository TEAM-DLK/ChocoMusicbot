import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from CHOCO import config
from CHOCO import LOGGER, app, userbot
from CHOCO.core.call import CHOCOh
from CHOCO.misc import sudo
from PRODOOZY import ALL_MODULES
from CHOCO.utils.database import get_banned_users, get_gbanned
from CHOCO.config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PRODOOZY" + all_module)
    LOGGER("PRODOOZY").info("Successfully Imported Modules...")
    await userbot.start()
    await CHOCOh.start()
    await CHOCOh.decorators()
    LOGGER("CHOCO").info(
        "bot started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("CHOCO").info("Stopping Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
