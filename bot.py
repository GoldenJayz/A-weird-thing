import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game
import os


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Alteria V4.9.8', type = 3))
    print('Loading AlteriaALPHA V3.1.2, ... Loaded Successfully.') 

@client.event
async def on_message(message):
    if message.content == '-bugcall':
        await client.send_message(message.channel,'DM has been sent to the owner of this bot.')
    if message.content == '-creator':
        await client.send_message(message.channel,'The creators name is Jay or his other name is Gold.')
    if message.content.startswith('-tag'):
        await client.send_message(message.channel,'Your it! <@%s>'  %(message.author.id))
    if message.content == '-meme':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/277196107279237120/484473935354920970/567ilop.mov')
    if message.content == '-mlg':
        await client.send_message(message.channel,'https://cdn.discordapp.com/attachments/460117183520047115/499031279250046976/NORMIES_LEAVE_REEE.mp4')
    if message.content == '-commands':
        em = discord.Embed(description='`Here is a list of commands. Fart, deported, slap, gold, invite, kiss, missletoe, marry, fart, dump, poop` **More is coming soon**')
        await client.send_message(message.channel, embed=em)
    if message.content == '-sadmusic':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=eXDU9um19HM')
    if message.content == '-fortnitemusic':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=jAMik-1DGKY')
    if message.content == '-pumpernickel':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=ngFEQZwV3HA&t=1598s')
    if message.content == '-deported':
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
    if message.content == '-invite':
        await client.send_message(message.channel,'https://discordapp.com/oauth2/authorize?&client_id=498889046370680863&scope=bot&permissions=8')
    if message.content == '-slap':
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
    if message.content == '-marry':
        em = discord.Embed(description='You have been married!')
        em.set_image(url='https://media.giphy.com/media/1x3LVhXaUdISA/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if ('nigga') in message.content:
       await client.delete_message(message)
    if ('cock') in message.content:
       await client.delete_message(message)
    if ('cunt') in message.content:
       await client.delete_message(message)
    if message.content == '-kiss':
        em = discord.Embed(description='You kissed. EWWWWW')
        em.set_image(url='https://media.giphy.com/media/l2Je2M4Nfrit0L7sQ/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '-fart':
        em = discord.Embed(description='You farted, the whole channel smells like ur bacon from last night.')
        em.set_image(url='https://media.giphy.com/media/cTfuWJAEYFyz6/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '-server':
        await client.send_message(message.channel,'**Here is the Invite ://discord.gg/qk9uVwJ If you join this server, you can get access to AlteriaVIP for FREE!')
    if message.content == '`dump':
        em = discord.Embed(description='You have clogged the toilet! Say *unclog to unclog the toilet')
        em.set_image(url='https://media.giphy.com/media/3og0IJtAkb80B96jF6/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == '-unclog':
        em = discord.Embed(description='You unclogged the toilet!')
        em.set_image(url='https://media.giphy.com/media/5Zuiy7XPMH21O/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('-8ball'):
        randomlist = ['Maybe','Yes','No',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('-kill'):
        randomlist = ['The bullet bounced back and hit you','You hit the person',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '-menu':
        await client.send_message(message.channel,'You can order a, Big mac, A whooper, and a large soda (pls note that you dont have to use the prefix for these commands)')
    if message.content == 'Big mac':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'big mac':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'Big Mac':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'Whooper':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'whooper':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'Large Soda':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'Large soda':
        await client.send_message(message.channel,'*Gives*')
    if message.content == 'large soda':
        await client.send_message(message.channel,'*Gives*')
    if message.content == '-about':
        await client.send_message(message.channel,'A little about Gold. Well Gold is the owner of this bot. He is a die hard Pokemon fan (It may sound childish but its amazing). Gold also, likes Zelda and has completed all Zelda and Pokemon games. Gold has caught them all in Pokemon Omega Ruby. Golds favorite Pokemon game is Pokemon Heartgold (Thats how I got my username LMAO). Gold Originated from Roblox as the user "jayboss980". He was a stupid kid then. But soon later he quit and started getting intrested in coding and created his first bot "Jays Assistant". This bot was absolute CRAP. It could only do 4 commands and those 4 commands are in this bot. (BUT THERE HIDDEN so dont even try).')
    if message.content == '-Alteria':
        await client.send_message(message.channel,'Alteria originaly was named "AlteriaALPHA". And, since Gold was new to coding and didnt even host his bot 24/7. He used github. AND PASTED HIS BOTS TOKEN. So somebody stole my bots token and destroyed everyone of my friends Discord servers and mine. (This is a screenshot https://cdn.discordapp.com/attachments/516304668528214016/516370555260370945/image0.png) But after that. I still had a old file of Alteria and added insane protection to Alteria so nobody can touch it. That bots name was called AlteriaREWRITE.')
    if message.content == '-alteria':
        await client.send_message(message.channel,'Alteria originaly was named "AlteriaALPHA". And, since Gold was new to coding and didnt even host his bot 24/7. He used github. AND PASTED HIS BOTS TOKEN. So somebody stole my bots token and destroyed everyone of my friends Discord servers and mine. (This is a screenshot https://cdn.discordapp.com/attachments/516304668528214016/516370555260370945/image0.png) But after that. I still had a old file of Alteria and added insane protection to Alteria so nobody can touch it. That bots name was called AlteriaREWRITE.')
    if message.content.startswith('`missletoe'):
        randomlist = ['You Walked under a missletoe and got kissed','Nobody saw you walk under the missletoe',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('-poop'):
        randomlist = ['You have clogged the toilet. Type -unclog to unclog it','You have pooped!',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == ('-poop'):
        em = discord.Embed(description='')
        em.set_image(url='https://media.giphy.com/media/3o7TKRBB3E7IdVNLm8/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content == ('-stats'):
        await client.send_message(message.channel,'`This bot is running on Microsoft windows 64x bit. Shard: 1/1`')
    if message.content == ('-upload'):
        await client.send_message(message.channel,'**@everyone Hello, Gold just uploaded a Youtube Video about Alteria. Go check it out--->https://www.youtube.com/channel/UCR6r5mq-pD3201_CBY-YeLA?view_as=subscriber**')
client.run(str(os.environ.get('BOT_TOKEN')))

