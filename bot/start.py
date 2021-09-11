from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import BOT_USERNAME
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, m: Message):
    if m.chat.type == "private":
        await m.reply_text(
            f"👋 𝙃𝙀𝙇𝙇𝙊 𝙎𝘼𝙔𝘼 𝙆𝙂𝙎𝙏𝙍𝙀𝘼𝙈𝙑𝙄𝘿𝙀𝙊\n💡𝙎𝙖𝙮𝙖 𝙖𝙠𝙖𝙣 𝙢𝙚𝙢𝙗𝙖𝙣𝙩𝙪 𝙢𝙚𝙧𝙖𝙢𝙖𝙞𝙠𝙖𝙣 𝙜𝙧𝙪𝙥 𝙠𝙖𝙡𝙞𝙖𝙣 𝙙𝙚𝙣𝙜𝙖𝙣 𝙘𝙖𝙧𝙖 𝙢𝙚𝙢𝙪𝙩𝙖𝙧𝙠𝙖𝙣 𝙫𝙞𝙙𝙚𝙤 𝙙𝙞 𝙤𝙗𝙧𝙤𝙡𝙖𝙣 𝙨𝙪𝙖𝙧𝙖 𝙨𝙚𝙨𝙪𝙖𝙞 𝙮𝙖𝙣𝙜 𝙠𝙖𝙡𝙞𝙖𝙣 𝙢𝙞𝙣𝙩𝙖\n\n❓[𝙆𝙇𝙄𝘾𝙆 𝘿𝙄𝙎𝙄𝙉𝙄](https://t.me/KGVideostream_bot?startgroup=true) 𝙐𝙣𝙩𝙪𝙠 𝙢𝙚𝙣𝙖𝙢𝙗𝙖𝙝𝙠𝙖𝙣 𝙨𝙖𝙮𝙖 𝙠𝙚𝙜𝙧𝙪𝙥."
            f"⚡𝙋𝙊𝙒𝙀𝙍𝙀𝘿 𝘽𝙔 @rakasupport",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "❔ʜᴏᴡ ᴛᴏ ᴜsᴇ", callback_data="cbguide")
                ], [
                    InlineKeyboardButton(
                        "🛠️sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://github.com/kalolonte1"),
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/knsgnwn")
                ], [
                    InlineKeyboardButton(
                        "ᴄᴏʙᴀ ʟᴏᴋɪᴛ", callback_data="cbinfo")
                ]]
            ))
    else:
        await m.reply_text("**✨ bot is online now ✨**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton(
                                       "❔ʜᴏᴡ ᴛᴏ ᴜsᴇ", callback_data="cbguide")
                               ], [
                                   InlineKeyboardButton(
                                       "🔎sᴇᴀʀᴄʜ ʏᴏᴜᴛᴜʙᴇ", switch_inline_query='')
                               ], [
                                   InlineKeyboardButton(
                                       "ᴄᴏʙᴀ ʟᴏᴋɪᴛ", callback_data="cbinfo"),
                               ]]
                           )
                           )


@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""✅ **bot is running**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘ", url=f"https://t.me/fantasyvirtual"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/rakasupport"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    sturt = time()
    m_reply = await m.reply_text("pinging...")
    delta_ping = time() - sturt
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 bot status 🤖\n\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
