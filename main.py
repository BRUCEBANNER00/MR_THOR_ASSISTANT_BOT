from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
from pyrogram.errors import UserNotParticipant


force_channel = "Devil_Design"


API_ID = "19383278"
API_HASH = "6e6c8100d5564c59bfd82a7a86aadb95"
BOT_TOKEN = "5770979141:AAHItADdhe3w2_eH3WT9g5oZdi7qQ794r5k"


GODOFTHUNDER = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

PICS = [
 ""
]







@GODOFTHUNDER.on_message(filters.command("start"))
async def start_cmd(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="𝙔𝙊𝙐 𝙃𝘼𝙑𝙀 𝙏𝙊 𝙎𝙐𝘽𝙎𝘾𝙍𝙄𝘽𝙀 𝙈𝙔 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝙏𝙊 𝙐𝙎𝙀 𝙏𝙃𝙄𝙎 𝘽𝙊𝙏 😁",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("⚡️𝙐𝙋𝘿𝘼𝙏𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇⚡️", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=""
    )
    
@GODOFTHUNDER.on_message(filters.audio & filters.private)
def audio(client, message):
    message.reply(message.audio.file_id)
    
@GODOFTHUNDER.on_message(filters.command("song))
def song_cmd (client, message):
    bot.send_audio(message.chat.id, "")
    

        
print("⚡️POWER FILLED⚡️")

GODOFTHUNDER.run()
