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
    
@bot.command()
async def update_info(ctx):
    print(ud.initPlayerData({
        str(ctx.author.id):{
            "fullname":f"{ctx.author.name}#{ctx.author.discriminator}",
            "name":ctx.author.name,
            "discriminator":ctx.author.discriminator,
            "id":ctx.author.id
        }
    }))
    
# @bot.command()
# async def clear_data(ctx):
#     ud.clearAllPlayerData()

bot.run(token)