from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME
from config import START_IMG as banner


@Client.on_message(filters.command(["start", "start@yakarimusicplaybot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAELdDVg7lKBBpbSRagP51fi5ZxmacYEvwACeQQAAsxUSQl-KKP9zEUlkR4E")
    await message.reply_text(
        text="**Hello π  {}!**\n\nI ** πCan Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Features π€ π₯ Thumbnail Supportπ₯ Playlist Support π₯ Current playback support π₯ Showing track names when skipping  π₯ Zero downtime, Fully Stable π₯ Deezer,YouTube & Saavan PlayBack Supported π₯ Settings panel π₯ Control with buttons π₯ Userbot auto join   π₯ Thanks Message When Add The Bot Join On A Grou**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("π§βπ§ HOW TO USE THIS BOT  ", url="https://t.me/supunma")
            ],[
            InlineKeyboardButton("π¨βπ» Bot support group ", url="https://t.me/slbotzone"),
            InlineKeyboardButton("π Bot update Channel ", url="https://t.me/sl_bot_zone")
            ],[
            InlineKeyboardButton("π Add To Your Group β ", url="https://t.me/yakarimusicplaybot?startgroup=true")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@yakarimusicplaybot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**π§  Yakari music play services - Made by - @slbotzone π  Telegram UserBot to Play Audio in Telegram Voice Chats π Stay safe π·  & enjoy π₯³   **",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text=" β‘οΈ  Developer ", url="https://t.me/supunma")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@yakarimusicplaybot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**γ½οΈ yakari music play service  : Help Menu**

__Γ β  First Add Me To Your Group π?ββοΈ..
Γ Promote Me As Admin In Your Group With All Permission π?ββοΈ ..__

**π· Common Commands β»οΈ .**

β’ /play - Song Name : __Plays Via Youtube__
β’ /dplay - Song Name : __Play Via Deezer__
β’ /splay - Song Name : __Play Via Jio Saavn__
β’ /playlist - __Show now playing list__
β’ /current - __Show now playing__

β’ /song - Song Name : __Get The Song From YouTube__
β’ /vid - Video Name : __Get The Video From YouTube__
β’ /deezer - song name : __download songs you want quickly via deezer__
β’ /saavn - song name : __download songs you want quickly via saavn__
β’ /search - YouTube Title : __(Get YouTube Search Query)__

**π· Group Admin Commands π° .**

β’ /skip : __Skips Music__
β’ /pause : __Pause Playing Music__
β’ /resume : __Resume Playing Music__
β’ /end : __Stops playing Music__
β’ /reload : __Reloads Admin List__
β’ /userbotjoin : __Assistant Joins The Group__
β’ /userbotleave  : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text=" π¦ How to Deploy your one π¦  ", url="https://github.com/youtubeslgeekshow/yakariTG-vc-music-play-bot")
              ]]
          )
      )
