# Thanks Full To Team Ultroid
# Fiks By Kay @Kayzuuuuu


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl import types
from telethon.utils import get_display_name

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kay_cmd

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(kay):
    kay = await kyy.client(getchat(kay.chat_id))
    await kay.client(getvc(kay.full_chat.call))
    await kay.client(getvc(kay.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@kay_cmd(pattern="startvc$")
async def start_voice(kay):
    chat = await kay.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await kay.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await kay.edit("`Memulai Obrolan Suara`")
    except Exception as ex:
        await kay.edit(f"**ERROR:** `{ex}`")


@kay_cmd(pattern="stopvc$")
async def stop_voice(kay):
    chat = await kay.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await kay.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await kay.client(stopvc(await get_call(kay)))
        await kay.edit("`Mematikan Obrolan Suara`")
    except Exception as ex:
        await kay.edit(f"**ERROR:** `{ex}`")


@kay_cmd(pattern="vcinvite")
async def _(kay):
    await kay.edit("`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in kay.client.iter_participants(kay.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await kay.client(invitetovc(call=await get_call(kay), users=p))
            z += 6
        except BaseException:
            pass
    await kay.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Invite semua member yang berada di group."
    }
)
