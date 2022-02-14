# ReCode by @Kayzuuuuu
# FROM Kayzyu-Ubot <https://github.com/Kayzyu/Kayzu-Ubot>
# KONTOLLLLLLL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern=r"^\.pmt(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TERIMA KASIH PEMERINTAH PULANG DULU YA❤️❤️**")


@register(outgoing=True, pattern=r"^\.pmh(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASSALAMUALAIKUM PEMERINTAH HADIR UNTUK ANDA😘**")


@register(outgoing=True, pattern=r"^\.pmo(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PEMERINTAH TERLALU OP🔥MAU DI ADU KAH MANIEZZ🤭**")


@register(outgoing=True, pattern=r"^\.pma(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PEMERINTAH OP ABIEZZZZZZZ...🔥 ADA LAWAN KAH NYET? 😏**")


CMD_HELP.update(
    {
        "pmrth": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .pmt\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .pmh\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .pmo\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .pma\
        \n↳ : lihat sendiri\
        \n↳ **COBAIN AJA SENDIRI SEMUA!**.\
   "
    }
)
