import discord
from discord.ext.commands import Bot
import asyncio
import time
import random
from discord import Game
import os
import json
from discord.ext import commands





client = discord.Client()
client = commands.Bot(command_prefix = '-')


#Startup

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Type -commands for commands!'), status=discord.Status.online)
    print('We have logged in as {0.user}'.format(client))


#Level System(Broken)


@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)


    with open('users.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1

async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int (experience ** (1/4))

    if lvl_start < lvl_end:
        await client.sendmessage(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end

    
#Commands

@client.event
async def on_message(message):
    if message.content.startswith('-commands'):
        em = discord.Embed( 
            title='Commands',
            description='A simple list of commands',
            colour = discord.Colour.orange()
        )
        em.add_field(name='**Fun/Games**', value='-8ball\n-shoot', inline=True)
        em.add_field(name='**Anime Gifs**', value='-nezukogif\n-nezukorunningmeme\n-jojo', inline=True)
        em.add_field(name='**Misc.**', value='-menu\n-clear', inline=False)
        em.set_footer(text='Thanks for utilizing my bot ^-^')
        em.set_author(name='Jaden#6666',
        icon_url='https://cdn.discordapp.com/avatars/549347721442754582/a_dbe3c19d7298e972a497cdefff207300.gif?size=128')
        em.set_image(url='https://cdn.discordapp.com/avatars/641015595168432169/537a92cd882bb8e6bb05b35b827962b6.png?size=128')

        await message.channel.send('', embed=em)

    if message.content.startswith('-nezukogif'):
        randomgif=['https://media.giphy.com/media/ghBwyDXSAEto8PztXc/giphy.gif', 'https://media1.tenor.com/images/08aea234985337f204997fdba0cfce38/tenor.gif?itemid=15688586', 'https://media1.giphy.com/media/dAu9Hz9xEDMPCw6Lwz/source.gif',]
        em = discord.Embed(
            title='Nezuko GIF executed.',
            colour = discord.Colour.purple()
        )
        em.set_image(url= (random.choice(randomgif)))
        await message.channel.send(embed=em)

    if message.content.startswith('-nezukorunningmeme'):
        em = discord.Embed(
            description='**Sonic the Hedgehog music starts playing**',
            colour = discord.Colour.purple()
            )
        em.set_image(url='https://media.giphy.com/media/UTSDPWVW4Llw1rPC9k/giphy.gif')
        await message.channel.send('', embed=em)

    if message.content.startswith('-menu'):
        em = discord.Embed(
            title='Menu',
            description='Menu to order food from :).',
            colour = discord.Colour.blue()
        )
        em.add_field(name='**McDonalds Food:**', value='Big Mac\nChicken McNuggets\nFrench Fries', inline=True)
        em.add_field(name='**Beverages:**', value='Sprite\nCoca-Cola\nPepsi\nRoot Beer', inline=True)
        em.add_field(name='**KFC Food:**', value='Chicken Bucket\nChicken Tenders', inline=True)
        em.set_footer(text='More will be coming soon...')
        await message.channel.send('', embed=em)

    if message.content.startswith('-big mac'):
        em = discord.Embed(
            title='Big Mac',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Big-Mac.jpg?$Product_Desktop$')
        await message.channel.send('', embed=em)

    if message.content.startswith('-chicken mcnuggets'):
        em = discord.Embed(
            title='Chicken McNuggets',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://upload.wikimedia.org/wikipedia/commons/d/d0/McDonalds-Chicken-McNuggets.jpg')
        await message.channel.send('', embed=em)

    if message.content.startswith('-french fries'):
        em = discord.Embed(
            title='French Fries',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Fries-Small-Medium.jpg?$Product_Desktop$')
        await message.channel.send('', embed=em)

    if message.content.startswith('-sprite'):
        em = discord.Embed(
            title='Sprite',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://images-na.ssl-images-amazon.com/images/I/71Y5MLLmknL._SL1500_.jpg')
        await message.channel.send('', embed=em)

    if message.content.startswith('-cocacola'):
        em = discord.Embed(
            title='Coca-Cola',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://images-na.ssl-images-amazon.com/images/I/71W%2BHikjmKL._SL1500_.jpg')
        await message.channel.send('', embed=em)

    if message.content.startswith('-pepsi'):
        em = discord.Embed(
            title='Pepsi',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://www.pepsi.com/en-us/uploads/images/social-share.jpg?mtime=20180110134930')
        await message.channel.send('', embed=em)

    if message.content.startswith('-rootbeer'):
        em = discord.Embed(
            title='Root Beer',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://upload.wikimedia.org/wikipedia/commons/7/7d/Root_beer_in_glass_mug.jpg')
        await message.channel.send('', embed=em)

    if message.content.startswith('-chickenbucket'):
        em = discord.Embed(
            title='Chicken Bucket',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://www.thepackagingcompany.us/knowledge-sharing/wp-content/uploads/2018/09/ip-kfcbucket-blog.jpg')
        await message.channel.send('', embed=em)

    if message.content.startswith('-chickentenders'):
        em = discord.Embed(
            title='Chicken Tenders',
            description='Your order has came through :)',
            colour = discord.Colour.red()
        )
        em.set_image(url='https://www.dinneratthezoo.com/wp-content/uploads/2015/04/chicken-fingers-4.jpg')
        await message.channel.send('', embed=em)

    if message.content.startswith('-test'):
        em = discord.Embed(
            title = 'commands',
            description = 'Testing',
            colour = discord.Colour.blue()
        )
        await message.channel.send('', embed=em)

    if message.content.startswith('-8ball'):
        randomlist = ['Maybe','Yes','No',]
        randomgif = ['https://media3.giphy.com/media/141iprzbEPjCiQ/giphy.gif', 'https://i.imgur.com/akdtE4H.gif', 'https://thumbs.gfycat.com/QuestionableMajesticBillygoat-small.gif',]
        em = discord.Embed(
            title="The magic 8 ball has spoken.",
            description=(random.choice(randomlist)),
            colour = discord.Colour.blurple()
        )
        em.set_image(url= (random.choice(randomgif)))
        await message.channel.send(embed=em)
    
    if message.content.startswith('-jojo'):
        randomlist = ['https://media.giphy.com/media/h7FZESJ1Ter5bGhUDG/giphy.gif',  'https://thumbs.gfycat.com/ForthrightBoldDaddylonglegs-max-1mb.gif', 'https://media.giphy.com/media/f9jxYYRVPHtKsCf9sy/giphy.gif']
        em = discord.Embed(
            title='Here is your Jojo gif.',
            description=':)',
            colour = discord.Colour.purple()
        )
        em.set_image(url= (random.choice(randomlist)))
        await message.channel.send(embed=em)

    if message.content.startswith('-clear'):
        amount=5
        await message.channel.purge(limit=amount)

    if message.content.startswith('-shoot'):
        em = discord.Embed(
            title='You have been shot!',
            description='You have a gun shot in your chest',
            colour = discord.Colour.green()
        )
        em.set_image(url='https://media.giphy.com/media/9umH7yTO8gLYY/giphy.gif')
        await message.channel.send('', embed=em)
client.run(str(os.environ.get('BOT_TOKEN')))

