from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tmo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`𝙏𝙈𝙊 𝙈𝙪𝙡𝙪 𝙇𝙪`")
    sleep(2)
    await typew.edit("`𝙅𝙖𝙙𝙞𝙖𝙣 𝙅𝙪𝙜𝙖 𝙆𝙖𝙜𝙖𝙠`")
    sleep(1)
    await typew.edit("`𝙏𝙖𝙥𝙞 𝙆𝙖𝙡𝙤 𝙇𝙪 𝙅𝙖𝙙𝙞𝙖𝙣, 𝙐𝙟𝙪𝙣𝙜-𝙐𝙟𝙪𝙣𝙜𝙣𝙮𝙖 𝙅𝙪𝙜𝙖 𝙆𝙚𝙣𝙖 𝙂𝙝𝙤𝙨𝙩𝙞𝙣𝙜`")


@register(outgoing=True, pattern='^.give(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Syarat Ikut Gipeewey`")
    sleep(2)
    await typew.edit("`Gcast Minimal 10 Grup`")
    sleep(1)
    await typew.edit("`Naik Os, Dan Ss Bukti Gcast`")


@register(outgoing=True, pattern='^.uno(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


CMD_HELP.update({
    "gabut3": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `tmo`\
    \n↳ : Cobain Sendiri\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.give`\
    \n↳ : Cobain Sendiri`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.uno`\
    \n↳ : Cobain Sendiri."
})
