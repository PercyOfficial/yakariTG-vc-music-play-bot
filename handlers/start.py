from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME
from config import START_IMG as banner


@Client.on_message(filters.command(["start", "start@yakarimusicplaybot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAELdDVg7lKBBpbSRagP51fi5ZxmacYEvwACeQQAAsxUSQl-KKP9zEUlkR4E")
    await message.reply_text(
        text="**Hello 😋  {}!**\n\nI ** 🎙Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Features 🤖**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("🧑‍🔧 HOW TO USE THIS BOT  ", url="https://t.me/supunma")
            ],[
            InlineKeyboardButton("👨‍💻 Bot support group ", url="https://t.me/slbotzone"),
            InlineKeyboardButton("🔔 Bot update Channel ", url="https://t.me/sl_bot_zone")
            ],[
            InlineKeyboardButton("🎙 Add To Your Group ➕ ", url="https://t.me/yakarimusicplaybot?startgroup=true")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@yakarimusicplaybot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**🎧  Yakari music play services - Made by - @slbotzone 📛  Telegram UserBot to Play Audio in Telegram Voice Chats 🎙 Stay safe 😷  & enjoy 🥳  Features✨
🔥 Thumbnail Support
🔥 Playlist Support
🔥 Current playback support
🔥 Showing track names when skipping
🔥 Zero downtime, Fully Stable
🔥 Deezer,YouTube & Saavan PlayBack Supported
🔥 Settings panel
🔥 Control with buttons
🔥 Userbot auto join
🔥 Thanks Message When Add The Bot Join On A Grou **",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text=" ⚡️  Developer ", url="https://t.me/MusicBotSupports")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@yakarimusicplaybot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**〽️ yakari music play service  : Help Menu**

__× ➕  First Add Me To Your Group 👮‍♀️..
× Promote Me As Admin In Your Group With All Permission 👮‍♀️ ..__

**🏷 Common Commands ♻️ .**

• /play - Song Name : __Plays Via Youtube__
• /dplay - Song Name : __Play Via Deezer__
• /splay - Song Name : __Play Via Jio Saavn__
• /playlist - __Show now playing list__
• /current - __Show now playing__

• /song - Song Name : __Get The Song From YouTube__
• /vid - Video Name : __Get The Video From YouTube__
• /deezer - song name : __download songs you want quickly via deezer__
• /saavn - song name : __download songs you want quickly via saavn__
• /search - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands 🔰 .**

• /skip : __Skips Music__
• /pause : __Pause Playing Music__
• /resume : __Resume Playing Music__
• /end : __Stops playing Music__
• /reload : __Reloads Admin List__
• /userbotjoin : __Assistant Joins The Group__
• /userbotleave  : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text=" 📦 How to Deploy your one 📦  ", url="https://github.com/youtubeslgeekshow/yakariTG-vc-music-play-bot")
              ]]
          )
      )
