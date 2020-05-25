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
    await client.change_presence(activity=discord.Game('Testing version'), status=discord.Status.online)
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

@client.command
async def commands(ctx):
        em = discord.Embed( 
            title='Commands',
            description='A simple list of commands',
            colour = discord.Colour.orange()
        )
        em.add_field(name='**Fun/Games**', value='-8ball\n-shoot', inline=True)
        em.add_field(name='**Anime Gifs**', value='-nezukogif\n-nezukorunningmeme\n-jojo\n-demonslayer', inline=True)
        em.add_field(name='**Misc.**', value='-menu\n-clear', inline=False)
        em.set_footer(text='Thanks for utilizing my bot ^-^')
        em.set_author(name='Jaden#6666',
        icon_url='https://cdn.discordapp.com/avatars/549347721442754582/a_dbe3c19d7298e972a497cdefff207300.gif?size=128')
        em.set_image(url='https://cdn.discordapp.com/avatars/641015595168432169/537a92cd882bb8e6bb05b35b827962b6.png?size=128')

        await message.channel.send('', embed=em)

client.run(str(os.environ.get('BOT_TOKEN')))

