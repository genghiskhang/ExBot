from discord.ext import commands
import json

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

# Checks if the discord user already has registered info inside the JSON
def checkExisting(userKey):
    with open('assets\\data.json', 'r') as file:
        if userKey in json.load(file):
            return True
    return False
            
# Initializes user data into the JSON
def initUser(ctx):
    pass
    
@bot.command()
async def update_info(ctx):
    print(ctx.author.name)

# bot.run(token)