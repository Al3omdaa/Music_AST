#
# Copyright (C) 2021-2022 by TeamAl3omda@Github, < https://github.com/Al3omdaa >.
#
# This file is part of < https://github.com/Al3omdaa/Music_AST > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Al3omdaa/Music_AST- فراغ لسه هكمله- >
#
# All rights reserved.

class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
