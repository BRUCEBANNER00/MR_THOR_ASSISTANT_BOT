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
                text="πππ ππΌππ ππ πππ½ππΎπππ½π ππ πΎππΌππππ ππ πππ ππππ π½ππ π",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("β‘οΈπππΏπΌππ πΎππΌππππβ‘οΈ", url=f"t.me/{force_channel}")
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
    

        
print("β‘οΈPOWER FILLEDβ‘οΈ")

GODOFTHUNDER.run()
