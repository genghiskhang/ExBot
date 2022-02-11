import discord
from discord.ext import commands
import userdata as ud

prefix = '--'
token = open('assets\\token.txt', 'r').readline().strip() # Create a token.txt file in assets folder and paste your token in there
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(' ____                        __              \n'+
          '/\  _`\                     /\ \             \n'+
          '\ \ \L\ \     __     __     \_\ \  __  __    \n'+
          ' \ \ ,  /   /\'__`\ /\'__`\   /\'_` \/\ \/\ \   \n'+
          '  \ \ \ \  /\  __//\ \L\.\_/\ \L\ \ \ \_\ \  \n'+
          '   \ \_\ \_\ \____\ \__/.\_\ \___,_\/`____ \ \n'+
          '    \/_/\/ /\/____/\/__/\/_/\/__,_ /`/___/> \\\n'+
          '                                       /\___/\n'+
          '                                       \/__/ \n')

# Registers a new user's information
@bot.event
async def on_member_join(member):
    ud.initPlayerData(str(member.id), {
        str(member.id):{
            'fullname':f'{member.name}#{member.discriminator}',
            'name':member.name,
            'discriminator':member.discriminator,
            'id':member.id,
            'points':0
        }
    })
    print(f"{member.name} has joined")
    
# Updates a player's information when they update their personal information
@bot.event
async def on_member_update(member):
    pass

# Removes a player's information when they leave
@bot.event
async def on_member_remove(member):
    ud.removePlayerData(member.id)
    print(f"{member.name} has left")
    
# Registers a new user's information
@bot.command()
async def register_info(ctx):
    ud.createDataJson()
    
# Retrieves the amount of points a player has
@bot.command()
async def get_points(ctx):
    points = ud.getData()['playerInfo'][str(ctx.author.id)]['points']
    await ctx.channel.send(f'{ctx.author.name} currently has {points} points')
    
# @bot.command()
# async def clear_data(ctx):
#     ud.clearAllPlayerData()

bot.run(token)