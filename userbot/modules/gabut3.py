from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.tmo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


@register(outgoing=True, pattern='^.give(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


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

