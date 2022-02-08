from discord.ext import commands
from pathlib import Path
import os

prefix = '--'
token = open('assets\\token.txt', 'r').readline().strip()
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_ready():
    print('Ready')
    print(token)
    
@bot.command()
async def queue(ctx):
    pass

@bot.command()
async def leave(ctx):
    pass