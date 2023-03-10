#
# Copyright (C) 2021-2022 by TeamAl3omda@Github, < https://github.com/Al3omdaa >.
#
# This file is part of < https://github.com/Al3omdaa/Music_AST > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Al3omdaa/Music_AST- فراغ لسه هكمله- >
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from Al3omdaMusic import app
from Al3omdaMusic.core.call import Yukki
from Al3omdaMusic.utils import bot_sys_stats
from Al3omdaMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Yukki.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
