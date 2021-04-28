from discord.ext import commands

from assets.getcorona import getcorona
from assets.embed import *

class commander(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="check")
    async def chack_corona(self, ctx, arg):
        if arg == 'corona':
            await ctx.channel.send(embed = EmbedSymtoms())
        elif arg == "cogs":
            await ctx.channel.send(f"<@!{str(ctx.message.author.id)}> roger that!")

    @commands.command(name="hello", aliases=["Hello","hi","Hi"])
    async def hello_command(self, ctx):
        msg = f"Hello <@!{str(ctx.message.author.id)}>, Type `!help` to see more information"
        await ctx.channel.send(msg)

    @commands.command(name="corona")
    async def corona_command(self, ctx): 
        await ctx.channel.send(embed = getcorona(ctx.message.content))

    @commands.command(name="list")
    async def list_pages(self, ctx, arg="1"):
        await ctx.channel.send(embed = EmbedList(arg))

    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.channel.send(embed = EmbedHelp())

    @commands.command(name="go")
    async def go_corona(self, ctx, arg):
        if arg == "corona":
            await ctx.channel.send(embed = EmbedSafety())


def setup(bot):
    bot.add_cog(commander(bot))