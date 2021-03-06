from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{bn} to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /vplay (reply to video) to start streaming.
6.) type /vstop to end the video streaming.

๐ **note: stream & stop command can only be executed by group admin only!**

โก __Maintained by KGPROJECT__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "สแดแดแด", callback_data="cbstart"),
                InlineKeyboardButton(
                    "ษดแดxแด", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"๐ ๐๐๐๐๐ ๐๐ผ๐๐ผ ๐๐๐๐๐๐๐ผ๐๐๐๐ฟ๐๐\n\n๐ก๐๐๐ฎ๐ ๐๐ ๐๐ฃ ๐ข๐๐ข๐๐๐ฃ๐ฉ๐ช ๐ข๐๐ง๐๐ข๐๐๐ ๐๐ฃ ๐๐ง๐ช๐ฅ ๐ ๐๐ก๐๐๐ฃ ๐๐๐ฃ๐๐๐ฃ ๐๐๐ง๐ ๐ข๐๐ข๐ช๐ฉ๐๐ง๐ ๐๐ฃ ๐ซ๐๐๐๐ค ๐๐ ๐ค๐๐ง๐ค๐ก๐๐ฃ ๐จ๐ช๐๐ง๐ ๐จ๐๐จ๐ช๐๐ ๐ฎ๐๐ฃ๐ ๐ ๐๐ก๐๐๐ฃ ๐ข๐๐ฃ๐ฉ๐\nโ[๐๐๐๐พ๐ ๐ฟ๐๐๐๐๐](https://t.me/KGVideostream_bot?startgroup=true) ๐๐ฃ๐ฉ๐ช๐  ๐ข๐๐ฃ๐๐ข๐๐๐๐ ๐๐ฃ ๐จ๐๐ฎ๐ ๐ ๐๐๐ง๐ช๐ฅ."
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


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐น๐๐๐๐๐ ๐ป๐๐๐ ๐น๐๐๐ ๐๐๐๐ ๐ณ๐๐๐๐ ๐๐ ๐ข๐!!""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton ("แดษขsแดแดแดแดสแด", url=f"https://t.me/KGSupportgroup"),
                InlineKeyboardButton ("แดษขแดแดแดแดแดแด", url=f"https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton ("าแดษดแดแดsส แด ษชสแดแดแดส", url=f"https://t.me/fantasyvirtual"),
                InlineKeyboardButton ("แดแดแด แดสแดแดแดส", url=f"https://t.me/knsgnwn"),
            ],
            [
                InlineKeyboardButton("สแดแดแด", callback_data="cbstart"),
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ All Command List:

ยป /vplay (reply to video or yt/live url) - to stream video
ยป /vstop - stop the video streaming
ยป /song (song name) - download song from YT
ยป /vsong (video name) - download video from YT
ยป /lyric (song name) - lyric scrapper
ยป /vjoin - invite assistant join to your group
ยป /vleave - order assistant leave from your group

๐ FUN CMD:

ยป /asupan - check it by yourself
ยป /chika - check it by yourself
ยป /wibu - check it by yourself
ยป /truth - check it by yourself
ยป /dare - check it by yourself

๐ฐ EXTRA CMD:

ยป /tts (reply to text) - text to speech
ยป /alive - check bot alive status
ยป /ping - check bot ping status
ยป /uptime - check bot uptime status
ยป /sysinfo - check bot system information

๐ก SUDO ONLY:

ยป /rmd - remove all downloaded files
ยป /rmw - remove all downloaded raw files
ยป /leaveall - order assistant leave from all group

โก __Maintained by KGPROJECT__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "๐ก Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
