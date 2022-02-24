# ReCode by @Kayzuuuuu
# FROM Kayzyu-Ubot <https://github.com/Kayzyu/Kayzu-Ubot>
# KONTOLLLLLLL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern=r"^\.50(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOII DAH TEMBUS 50**")


@register(outgoing=True, pattern=r"^\.trn(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TURUNKAN GIVEE EWEYY!!!**")


@register(outgoing=True, pattern=r"^\.gks(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOI GIKES ANJ!!!**")


@register(outgoing=True, pattern=r"^\.stp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**❌STOP❌**")


CMD_HELP.update(
    {
        "giveaway": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .50\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .trn\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .gks\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .stp\
        \n↳ : lihat sendiri\
        \n↳ **COBAIN AJA SENDIRI SEMUA!**.\
   "
    }
)
