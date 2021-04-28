import discord, os

from discord.ext import commands
import dotenv


from assets.getcorona import getcorona
from assets.embed import *

dotenv.load_dotenv()
client = commands.Bot(command_prefix="!", help_command=None)

#print when bot is live
@client.event
async def on_ready():
    print("Bot has logged in")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help'))
        
#load commands
client.load_extension('cogs.commands')
#initalizing the bot
client.run(os.getenv('TOKEN'))
