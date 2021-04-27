from discord.ext import commands
import dotenv
import discord, os, requests, json

from assets.getcorona import getcorona
from assets.embed import *

dotenv.load_dotenv()
client = commands.Bot(command_prefix="!", help_command=None)

#prints when bot is live
@client.event
async def on_ready():
    print("Bot has logged in")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help'))
        
#commands
@client.command(name="hello", aliases=["Hello","hi","Hi"])
async def hello_command(ctx):
    msg = f"Hello <@!{str(ctx.message.author.id)}>, Type `!help` to see more information"
    await ctx.channel.send(msg)

@client.command(name="corona")
async def corona_command(ctx): 
    await ctx.channel.send(embed = getcorona(ctx.message.content))

@client.command(name="list")
async def list_pages(ctx, arg=1):
    await ctx.channel.send(embed = EmbedList(arg))

@client.command(name="help")
async def list_pages(ctx, arg=1):
    await ctx.channel.send(embed = EmbedHelp())

@client.command(name="go corona")
async def list_pages(ctx, arg=1):
    await ctx.channel.send(embed = EmbedSafety())

@client.command(name="check corona")
async def list_pages(ctx, arg=1):
    await ctx.channel.send(embed = EmbedSymtoms())

client.run(os.getenv('TOKEN'))
