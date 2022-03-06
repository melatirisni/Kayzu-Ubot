# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot

from userbot import (
    BOT_VER,
    LOGS,
    bot,
    call_py,
)
from userbot.modules import ALL_MODULES

sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"🔥ҡᴀʏᴢᴜ-ᴜвσт🔥 ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
