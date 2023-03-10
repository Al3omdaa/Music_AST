#
# Copyright (C) 2021-2022 by Al3omda@Github, < https://github.com/Al3omdaa >.
#
# This file is part of < https://github.com/Al3omdaa/Music_AST > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Al3omdaa/Music_AST- فراغ لسه هكمله- >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Al3omdaMusic import LOGGER, app, userbot
from Al3omdaMusic.core.call import Al3omda
from Al3omdaMusic.plugins import ALL_MODULES
from Al3omdaMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Al3omdaMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Al3omdaMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
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
        importlib.import_module("Al3omdaMusic.plugins" + all_module)
    LOGGER("Al3omdaMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Al3omda.start()
    try:
        await Al3omda.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Al3omdaMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Al3omda.decorators()
    LOGGER("Al3omdaMusic").info("Al3omda Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Al3omdaMusic").info("Stopping Al3omda Music Bot! GoodBye")
