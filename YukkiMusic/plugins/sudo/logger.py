#
# Copyright (C) 2021-2022 by TeamAl3omda@Github, < https://github.com/Al3omdaa >.
#
# This file is part of < https://github.com/Al3omdaa/Music_AST > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Al3omdaa/Music_AST- فراغ لسه هكمله- >
#
# All rights reserved.

from pyrogram import filters

import config
from strings import get_command
from Al3omdaMusic import app
from Al3omdaMusic.misc import SUDOERS
from Al3omdaMusic.utils.database import add_off, add_on
from Al3omdaMusic.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
