from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
from pyrogram.errors import UserNotParticipant


force_channel = "EnemyTech"


API_ID = "19383278"
API_HASH = "6e6c8100d5564c59bfd82a7a86aadb95"
BOT_TOKEN = "5536306168:AAH95cAElfZoxHsSOVlnbT5JzpBoA8jCyNM"


GODOFTHUNDER = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

PICS = [
 "https://telegra.ph/file/31da701dcccf1a90122a3.jpg",
 "https://telegra.ph/file/970b40fc3c36220ee53c8.jpg",
 "https://telegra.ph/file/fb739e0d1f519e0a30bfb.jpg",
 "https://telegra.ph/file/838ca0f650d9f23b3bc48.jpg",
 "https://telegra.ph/file/186b73793471aafff4e7d.jpg",
 "https://telegra.ph/file/37561d2e997466fe41f1d.jpg",
 "https://telegra.ph/file/5659f55af8716acac32da.jpg",
 "https://telegra.ph/file/e6d533d061bef79869eff.jpg",
 "https://telegra.ph/file/6bbc174f7a10701ba8fb3.jpg",
 "https://telegra.ph/file/9d5ae53d5e37d2d1e4583.jpg",
 "https://telegra.ph/file/ac8b25fdcbbe418711e55.jpg",
 "https://telegra.ph/file/b22d46598fc71d7034ad0.jpg"
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
        caption="""
𝙃𝙀𝙇𝙇𝙊...!
                                
𝙄 𝘼𝙈 𝘼 𝙎𝙄𝙈𝙋𝙇𝙀 𝘼𝙐𝙏𝙊 𝙁𝙄𝙇𝙏𝙀𝙍 𝘽𝙊𝙏.
𝙔𝙊𝙐 𝘾𝘼𝙉 𝙂𝙀𝙏 𝙁𝙄𝙇𝙀𝙎 𝙑𝙄𝘼 𝙄𝙉𝙇𝙄𝙉𝙀 𝙈𝙊𝘿𝙀.𝙅𝙐𝙎𝙏 𝙏𝙔𝙋𝙀 𝘽𝙊𝙏 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 𝘼𝙉𝘿 𝙈𝙊𝙑𝙄𝙀 𝙉𝘼𝙈𝙀.
                                
𝙀𝙂 : 𝘽𝙊𝙏 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 𝘼𝙑𝙀𝙉𝙂𝙀𝙍𝙎 𝙀𝙉𝘿𝙂𝘼𝙈𝙀.

@EnemyTech""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("⚡️Search Here⚡️", switch_inline_query_current_chat='')
            ],[
            InlineKeyboardButton("⚡UPDATES", url="t.me/EnemyTech"),
            InlineKeyboardButton("⚡CREATOR", url="t.me/MR_THOR_01")
            ]]
            )
        )
          
        
        
    
@GODOFTHUNDER.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""
𝙃𝙀𝙇𝙇𝙊...!
                                
𝙄 𝘼𝙈 𝘼 𝙎𝙄𝙈𝙋𝙇𝙀 𝘼𝙐𝙏𝙊 𝙁𝙄𝙇𝙏𝙀𝙍 𝘽𝙊𝙏.
𝙔𝙊𝙐 𝘾𝘼𝙉 𝙂𝙀𝙏 𝙁𝙄𝙇𝙀𝙎 𝙑𝙄𝘼 𝙄𝙉𝙇𝙄𝙉𝙀 𝙈𝙊𝘿𝙀.𝙅𝙐𝙎𝙏 𝙏𝙔𝙋𝙀 𝘽𝙊𝙏 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 𝘼𝙉𝘿 𝙈𝙊𝙑𝙄𝙀 𝙉𝘼𝙈𝙀.
                                
𝙀𝙂 : 𝘽𝙊𝙏 𝙐𝙎𝙀𝙍𝙉𝘼𝙈𝙀 𝘼𝙑𝙀𝙉𝙂𝙀𝙍𝙎 𝙀𝙉𝘿𝙂𝘼𝙈𝙀.

@EnemyTech""")
                                 
        




    
@GODOFTHUNDER.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption="""𝘽𝙊𝙏 𝙉𝘼𝙈𝙀 : 𝘼𝙐𝙏𝙊 𝙁𝙄𝙇𝙏𝙀𝙍 𝘽𝙊𝙏

 𝙇𝘼𝙉𝙂𝙐𝘼𝙂𝙀 : 𝙋𝙔𝙏𝙃𝙊𝙉

 𝘾𝙍𝙀𝘼𝙏𝙊𝙍  : 𝙂𝙊𝘿 𝙊𝙁 𝙏𝙃𝙐𝙉𝘿𝙀𝙍

 𝙐𝙋𝘿𝘼𝙏𝙀𝙎  : @EnemyTech

 𝙎𝙊𝙐𝙍𝘾𝙀  : GITHUB
                    
@EnemyTech""")




print("⚡️POWER FILLED⚡️")


GODOFTHUNDER.run()
