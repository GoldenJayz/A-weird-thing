import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Gold Update this code', type = 3))
    print('Loading AlteriaALPHA V3.1.2, ... Loaded Successfully.') 

@client.event
async def on_message(message):
    if message.content == '`bugcall':
        await client.send_message(message.channel,'DM has been sent to the owner of this bot.')
    if message.content == '`creator':
        await client.send_message(message.channel,'The creators name is Jay or his other name is Gold.')
    if message.content.startswith('*tag'):
        await client.send_message(message.channel,'Your it! <@%s>'  %(message.author.id))
    if message.content == '`summon':
        await client.send_message(message.channel,'You have summoned Gold https://cdn.discordapp.com/attachments/492081670988496899/499007269057331200/Pokemon_HeartGold_-_Intro.mp4')
    if message.content == '`meme':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/277196107279237120/484473935354920970/567ilop.mov')
    if message.content == '`mlg':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/460117183520047115/499031279250046976/NORMIES_LEAVE_REEE.mp4')
    if message.content == '`messagetopuppy':
        await client.send_message(message.channel,'Hello, I am jay (Gold). I will not be talking to you puppy. I will have to think about the fight we had yesterday. After that fight I might not wanna be your friend anymore. If I dont respond to you on discord, you will know why. If you want to say anything to me DM me.')
    if message.content == '`commands':
        await client.send_message(message.channel,'*mlg, *meme, *bugcall, *creator, *tag, *summon, *sadmusic, *pumpernickel, *deported')
    if message.content == '`puppy':
        em = discord.Embed(description='')
        em.set_image(url='https://www.google.com/search?biw=1678&bih=979&tbm=isch&sa=1&ei=QAC9W9rOF8-9ggeeyqbICA&q=crying+&oq=crying+&gs_l=img.3..0i67j0j0i67l2j0l4j0i67l2.1387.4433..4729...1.0..2.72.714.12......2....1..gws-wiz-img.....0..35i39.6d-h819jVfw#imgrc=AU3FbLE0u_TP4M:')
        await client.send_message(message.channel, embed=em)
    if message.content == '`sadmusic':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=eXDU9um19HM')
    if message.content == '`fortnitemusic':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=jAMik-1DGKY')
    if message.content == '`pumpernickel':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=ngFEQZwV3HA&t=1598s')
    if message.content == '`deported':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=P1-uCWIjZWM&index=20&list=PL_gap6ACbie81lL4scX1o73lY2tQP8DLD')
    if message.content == 'Hi':
        await client.send_message(message.channel,'Hi!')
    if message.content == 'hi':
        await client.send_message(message.channel,'Hi!')
    if message.content == 'yo':
        await client.send_message(message.channel,'Hi!')
    if message.content == 'fuck':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == 'shit':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == 'heck':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == 'penis':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == 'dick':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == 'pussy':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == 'nigger':
        await client.send_message(message.channel,'What up my home boi.')
    if message.content == 'baby shark':
        await client.send_message(message.channel,'FUCK NO')
    if message.content == 'gold':
        await client.send_message(message.channel,'Gold doesnt want to talk to you.')
    if message.content == '`invite':
        await client.send_message(message.channel,'https://discordapp.com/oauth2/authorize?&client_id=498889046370680863&scope=bot&permissions=8')
    if message.content == '`slap':
        em = discord.Embed(description='You got slapped sike')
        em.set_image(url='https://i.giphy.com/media/mEtSQlxqBtWWA/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('pussy') in message.content:
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.delete_message(message)
    if message.content == 'shit':
        await client.send_message(message.channel,'Do not swear on my christian Minecraft server')
    if message.content == '`marry':
        em = discord.Embed(description='You have been married!')
        em.set_image(url='https://media.giphy.com/media/1x3LVhXaUdISA/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if ('nigga') in message.content:
       await client.delete_message(message)
    if ('cock') in message.content:
       await client.delete_message(message)
    if ('cunt') in message.content:
       await client.delete_message(message)
    if message.content == '`kiss':
        em = discord.Embed(description='You kissed. EWWWWW')
        em.set_image(url='https://media.giphy.com/media/l2Je2M4Nfrit0L7sQ/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '`fart':
        em = discord.Embed(description='You farted, the whole channel smells like ur bacon from last night.')
        em.set_image(url='https://media.giphy.com/media/cTfuWJAEYFyz6/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '`server':
        await client.send_message(message.channel,'The invite link for the Alteria Server is https://discord.gg/SvHxr3y You get amazing health benefits Lul.')
    if message.content == '`poop':
        em = discord.Embed(description='You have successfully pooped!')
        em.set_image(url='https://media.giphy.com/media/3o7TKRBB3E7IdVNLm8/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '`dump':
        em = discord.Embed(description='You have clogged the toilet! Say *unclog to unclog the toilet')
        em.set_image(url='https://media.giphy.com/media/3og0IJtAkb80B96jF6/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '`unclog':
        em = discord.Embed(description='You unclogged the toilet!')
        em.set_image(url='https://media.giphy.com/media/5Zuiy7XPMH21O/giphy.gif')
        await client.send_message(message.channel, embed=em)
client.run(str(os.environ.get('BOT_TOKEN')))