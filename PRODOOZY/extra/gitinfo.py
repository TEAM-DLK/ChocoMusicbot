import aiohttp
from pyrogram import filters
from CHOCO import app


@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git TEAM-DLK")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**Gɪᴛʜᴜʙ Iɴғᴏ Oғ {name}**

**Usᴇʀɴᴀᴍᴇ :** `{username}`
**Bɪᴏ :** `{bio}`
**Lɪɴᴋ :** [Here]({url})
**Cᴏᴍᴩᴀɴʏ :** `{company}`
**Cʀᴇᴀᴛᴇᴅ Oɴ :** `{created_at}`
**ʀᴇᴩᴏsɪᴛᴏʀɪᴇs :** `{repositories}`
**Bʟᴏɢ :** `{blog}`
**Lᴏᴄᴀᴛɪᴏɴ :** `{location}`
**Fᴏʟʟᴏᴡᴇʀs :** `{followers}`
**Fᴏʟʟᴏᴡɪɴɢ :** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
