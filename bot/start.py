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
            f"๐ ๐๐๐๐๐ ๐๐ผ๐๐ผ ๐๐๐๐๐๐๐ผ๐๐๐๐ฟ๐๐\n๐ก๐๐๐ฎ๐ ๐๐ ๐๐ฃ ๐ข๐๐ข๐๐๐ฃ๐ฉ๐ช ๐ข๐๐ง๐๐ข๐๐๐ ๐๐ฃ ๐๐ง๐ช๐ฅ ๐ ๐๐ก๐๐๐ฃ ๐๐๐ฃ๐๐๐ฃ ๐๐๐ง๐ ๐ข๐๐ข๐ช๐ฉ๐๐ง๐ ๐๐ฃ ๐ซ๐๐๐๐ค ๐๐ ๐ค๐๐ง๐ค๐ก๐๐ฃ ๐จ๐ช๐๐ง๐ ๐จ๐๐จ๐ช๐๐ ๐ฎ๐๐ฃ๐ ๐ ๐๐ก๐๐๐ฃ ๐ข๐๐ฃ๐ฉ๐\n\nโ[๐๐๐๐พ๐ ๐ฟ๐๐๐๐๐](https://t.me/KGVideostream_bot?startgroup=true) ๐๐ฃ๐ฉ๐ช๐  ๐ข๐๐ฃ๐๐ข๐๐๐๐ ๐๐ฃ ๐จ๐๐ฎ๐ ๐ ๐๐๐ง๐ช๐ฅ."
            f"โก๐๐๐๐๐๐๐ฟ ๐ฝ๐ @rakasupport",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "โสแดแดก แดแด แดsแด", callback_data="cbguide")
                ], [
                    InlineKeyboardButton(
                        "๐ ๏ธsแดแดสแดแด แดแดแดแด", url=f"https://github.com/kalolonte1"),
                    InlineKeyboardButton(
                        "แดแดแด แดสแดแดแดส", url=f"https://t.me/knsgnwn")
                ], [
                    InlineKeyboardButton(
                        "แดแดสแด สแดแดษชแด", callback_data="cbinfo")
                ]]
            ))
    else:
        await m.reply_text("**โจ bot is online now โจ**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton(
                                       "โสแดแดก แดแด แดsแด", callback_data="cbguide")
                               ], [
                                   InlineKeyboardButton(
                                       "๐sแดแดสแดส สแดแดแดแดสแด", switch_inline_query='')
                               ], [
                                   InlineKeyboardButton(
                                       "แดแดสแด สแดแดษชแด", callback_data="cbinfo"),
                               ]]
                           )
                           )


@Client.on_message(command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""โ **bot is running**\n<b>๐  **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ษขสแดแดแด", url=f"https://t.me/fantasyvirtual"
                    ),
                    InlineKeyboardButton(
                        "แดสแดษดษดแดส", url=f"https://t.me/rakasupport"
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
        "๐ `PONG!!`\n"
        f"โก๏ธ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "๐ค bot status ๐ค\n\n"
        f"โข **uptime:** `{uptime}`\n"
        f"โข **start time:** `{START_TIME_ISO}`"
    )
