import discord, os

from discord.ext import commands
import dotenv

dotenv.load_dotenv()
client = commands.Bot(command_prefix="!", help_command=None)

@client.event
async def on_ready():
    print("Bot has logged in")
    
    channel = client.get_channel(836141686122872872)
    embed=discord.Embed(title = "Hey!", description = "```\nNew code is deployed on Heroku\n```", color = discord.Color.teal())
    await channel.send(embed=embed)
    exit()
    
# Initalizing the bot
client.run(os.getenv('TOKEN'))
