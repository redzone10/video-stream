from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{bn} to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /vplay (reply to video) to start streaming.
6.) type /vstop to end the video streaming.

📝 **note: stream & stop command can only be executed by group admin only!**

⚡ __Maintained by KGPROJECT__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "ʙᴀᴄᴋ", callback_data="cbstart"),
                InlineKeyboardButton(
                    "ɴᴇxᴛ", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"👋 𝙃𝙀𝙇𝙇𝙊 𝙎𝘼𝙔𝘼 𝙆𝙂𝙎𝙏𝙍𝙀𝘼𝙈𝙑𝙄𝘿𝙀𝙊\n\n💡𝙎𝙖𝙮𝙖 𝙖𝙠𝙖𝙣 𝙢𝙚𝙢𝙗𝙖𝙣𝙩𝙪 𝙢𝙚𝙧𝙖𝙢𝙖𝙞𝙠𝙖𝙣 𝙜𝙧𝙪𝙥 𝙠𝙖𝙡𝙞𝙖𝙣 𝙙𝙚𝙣𝙜𝙖𝙣 𝙘𝙖𝙧𝙖 𝙢𝙚𝙢𝙪𝙩𝙖𝙧𝙠𝙖𝙣 𝙫𝙞𝙙𝙚𝙤 𝙙𝙞 𝙤𝙗𝙧𝙤𝙡𝙖𝙣 𝙨𝙪𝙖𝙧𝙖 𝙨𝙚𝙨𝙪𝙖𝙞 𝙮𝙖𝙣𝙜 𝙠𝙖𝙡𝙞𝙖𝙣 𝙢𝙞𝙣𝙩𝙖\n❓[𝙆𝙇𝙄𝘾𝙆 𝘿𝙄𝙎𝙄𝙉𝙄](https://t.me/KGVideostream_bot?startgroup=true) 𝙐𝙣𝙩𝙪𝙠 𝙢𝙚𝙣𝙖𝙢𝙗𝙖𝙝𝙠𝙖𝙣 𝙨𝙖𝙮𝙖 𝙠𝙚𝙜𝙧𝙪𝙥."
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


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""𝙹𝚊𝚗𝚐𝚊𝚗 𝙻𝚞𝚙𝚊 𝙹𝚘𝚒𝚗 𝚈𝚊𝚗𝚐 𝙳𝚒𝚋𝚊𝚠𝚊𝚑 𝚢𝚊!!""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton ("ᴋɢsᴜᴘᴘᴏʀᴛ", url=f"https://t.me/KGSupportgroup"),
                InlineKeyboardButton ("ᴋɢᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/rakasupport"),
            ],
            [
                InlineKeyboardButton ("ғᴀɴᴛᴀsʜ ᴠɪʀᴛᴜᴀʟ", url=f"https://t.me/fantasyvirtual"),
                InlineKeyboardButton ("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/knsgnwn"),
            ],
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cbstart"),
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 All Command List:

» /vplay (reply to video or yt/live url) - to stream video
» /vstop - stop the video streaming
» /song (song name) - download song from YT
» /vsong (video name) - download video from YT
» /lyric (song name) - lyric scrapper
» /vjoin - invite assistant join to your group
» /vleave - order assistant leave from your group

🎊 FUN CMD:

» /asupan - check it by yourself
» /chika - check it by yourself
» /wibu - check it by yourself
» /truth - check it by yourself
» /dare - check it by yourself

🔰 EXTRA CMD:

» /tts (reply to text) - text to speech
» /alive - check bot alive status
» /ping - check bot ping status
» /uptime - check bot uptime status
» /sysinfo - check bot system information

💡 SUDO ONLY:

» /rmd - remove all downloaded files
» /rmw - remove all downloaded raw files
» /leaveall - order assistant leave from all group

⚡ __Maintained by KGPROJECT__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
