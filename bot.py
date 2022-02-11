from discord.ext import commands
import userdata as ud

prefix = '--'
token = open('assets\\token.txt', 'r').readline().strip() # Create a token.txt file in assets folder and paste your token in there
bot = commands.Bot(command_prefix = prefix)

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
@bot.command()
async def register_info(ctx):
    ud.createDataJson()
    await ctx.channel.send(ud.initPlayerData(str(ctx.author.id), {
        str(ctx.author.id):{
            'fullname':f'{ctx.author.name}#{ctx.author.discriminator}',
            'name':ctx.author.name,
            'discriminator':ctx.author.discriminator,
            'id':ctx.author.id,
            'points':0
        }
    }))
    
# Retrieves the amount of points a player has
@bot.command()
async def get_points(ctx):
    points = ud.getData()['playerInfo'][str(ctx.author.id)]['points']
    await ctx.channel.send(f'{ctx.author.name} currently has {points} points')
    
# @bot.command()
# async def clear_data(ctx):
#     ud.clearAllPlayerData()

bot.run(token)