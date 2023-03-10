#
# Copyright (C) 2021-2022 by TeamAl3omda@Github, < https://github.com/Al3omdaa >.
#
# This file is part of < https://github.com/Al3omdaa/Music_AST > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Al3omdaa/Music_AST- فراغ لسه هكمله- >
#
# All rights reserved.

from Al3omdaMusic.core.bot import Al3omdaBot
from Al3omdaMusic.core.dir import dirr
from Al3omdaMusic.core.git import git
from Al3omdaMusic.core.userbot import Userbot
from Al3omdaMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
