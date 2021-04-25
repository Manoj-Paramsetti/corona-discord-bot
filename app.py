import discord
import os
from dotenv import load_dotenv

#importing dotenv file
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	#checking whether bot message is recieved
	if message.author == client.user:
		print("message is delivered")
	#checks when someone says hello
	if message.content.startswith("!hello"):
		await message.channel.send("Hello! <@!"+str(message.author.id)+">"+"\nType `!help'` to learn how to use this bot ")

#Running bot using token id importing from .env file
client.run(os.getenv('TOKEN'))
