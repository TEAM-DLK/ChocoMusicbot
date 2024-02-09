import requests
from requests import get 
from CHOCO import app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto

@app.on_message(filters.command(["image", "img"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**Gɪᴠᴇ Iᴍᴀɢᴇ Nᴀᴍᴇ Fᴏʀ Sᴇᴀʀᴄʜ 🔍**")

     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

     media_group = []
     count = 0

     msg = await message.reply(f"Sᴄʀᴀᴘɪɴɢ Iᴍᴀɢᴇs Fʀᴏᴍ Pɪɴᴛᴇʀᴇᴛs...")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"•🄲🄷🄾🄲🄾• Sᴄʀᴀᴘᴇᴅ Iᴍᴀɢᴇs {count}")

     try:
        
        await app.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")
