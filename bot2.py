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
    await client.change_presence(game=Game(name='Testing Mode On', type = 3))
    print('Loading AlteriaALPHA V3.1.2, ... Loaded Successfully.')
 


@client.command(pass_context = True)
async def kick(ctx, member: discord.User):
    await client.kick(member)
    await client.delete_message(ctx.message)


@client.command(pass_context = True)
async def ban(ctx, member: discord.User):
    await client.ban(member)
    await client.delete_message(ctx.message)

     
client.run(str(os.environ.get('BOT_TOKEN')))
