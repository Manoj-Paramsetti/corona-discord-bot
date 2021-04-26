import discord, os, requests, json
from dotenv import load_dotenv

pages = ["Afghanistan, Albania, Algeria, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana, Brazil, Brunei, Bulgaria, Burkina Faso, Burma, Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Central African Republic, Chad, Chile, China, Colombia, Comoros, Congo (Brazzaville), Congo (Kinshasa), Costa Rica, Cote d'Ivoire, Croatia, Cuba, Cyprus, Czechia",
	"Denmark, Diamond Princess, Djibouti, Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Eswatini, Ethiopia, Fiji, Finland, France, Gabon, Gambia, Georgia, Germany, Ghana, Greece, Grenada, Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Holy See, Honduras, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya, Korea, South, Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon, Lesotho",
	"Liberia, Libya, Liechtenstein, Lithuania, Luxembourg, MS Zaandam, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Mauritania, Mauritius, Mexico, Micronesia, Moldova, Monaco, Mongolia, Montenegro, Morocco, Mozambique, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, North Macedonia, Norway, Oman, Pakistan, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Qatar, Romania, Russia, Rwanda, Saint Kitts and Nevis, Saint Lucia",
	"Saint Vincent and the Grenadines, Samoa, San Marino, Sao Tome and Principe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, South Sudan, Spain, Sri Lanka, Sudan, Suriname, Sweden, Switzerland, Syria, Taiwan*, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Trinidad and Tobago, Tunisia, Turkey, US, Uganda, Ukraine, United Arab Emirates, United Kingdom, Uruguay, Uzbekistan, Vanuatu, Venezuela, Vietnam, West Bank and Gaza, Yemen, Zambia, Zimbabwe"]

#importing dotenv file
load_dotenv()

client = discord.Client()

def getcases(country = "global"):
	url = "https://covid19.mathdro.id/api"
	if country != "global":
		url = 'https://covid19.mathdro.id/api'+'/countries/'+country
	response = requests.request("GET", url)
	data = json.loads(response.text)
	return data, country

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!corona help'))
    

@client.event
async def on_message(message):
	
	global page

	if message.author == client.user:
		print("message is delivered")
	
	#checks when someone says hello
	if message.content.startswith("!hello"):
		await message.channel.send("Hello! <@!"+str(message.author.id)+">"+"\nType `!help'` to learn how to use this bot ")
	
	#checks when someone says help
	if message.content.startswith("!help"):
		embed=discord.Embed(title="Help for Corona Bot", color=discord.Color.blue())
		embed.add_field(name="!corona help", value="Says hello and shows how to open help", inline=True)
		embed.add_field(name="!corona", value="To get global corona virus status", inline=True)
		embed.add_field(name="!corona countryname", value="To get corona virus status in particular country", inline=True)
		embed.add_field(name="!corona list", value="To get list", inline=True)
		embed.add_field(name="!corona list n", value="To get list n. Here n is page number(1-4)", inline=True)
		embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
		
		await message.channel.send(embed=embed)
	
	#checks when someone says corona
	if message.content.startswith("!corona"):

		if message.content == "!corona":
			data, place = getcases() 
			confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
			active = confirmed - (recovered + death)

			embed=discord.Embed(title= place.capitalize()+" Corona Cases Status", color=discord.Color.blue())
			embed.add_field(name="Active Cases", value=active, inline=True)
			embed.add_field(name="Recovered", value=recovered, inline=True)
			embed.add_field(name="Deaths", value=death, inline=True)
			embed.add_field(name="Confirmed Cases", value= confirmed, inline=True)
			embed.set_footer(text="Type '!corona help' to know, how to see the other pages")	
			
			await message.channel.send(embed = embed) 

		country = message.content.split() 
		if len(country) >= 2:

			#showing available places
			if country[1] == "list":
				
				#Showing list of places
				if len(country) > 2: 
					print(country)
					if country[2] == "1":
						embed=discord.Embed(title="List of countries available", color=discord.Color.blue())
						embed.add_field(name="page 1 of 4", value=pages[0], inline=False)
						embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
						
						await message.channel.send(embed=embed)
					if country[2] == "2":
						embed=discord.Embed(title="List of countries available", color=discord.Color.blue())
						embed.add_field(name="page 2 of 4", value=pages[1], inline=False)
						embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
						
						await message.channel.send(embed=embed)
					if country[2] == "3":
						embed=discord.Embed(title="List of countries available", color=discord.Color.blue())
						embed.add_field(name="page 3 of 4", value=pages[2], inline=False)
						embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
						
						await message.channel.send(embed=embed)
					if country[2] == "4":
						embed=discord.Embed(title="List of countries available", color=discord.Color.blue())
						embed.add_field(name="page 4 of 4", value=pages[3], inline=False)
						embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
						
						await message.channel.send(embed=embed)
			
				else:
					embed=discord.Embed(title="List of countries available", color=discord.Color.blue())
					embed.add_field(name="page 1 of 4", value=pages[0], inline=False)
					embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
					
					await message.channel.send(embed=embed)

			elif  country[1] == "help":
				embed=discord.Embed(title="Help for Corona Bot", color=discord.Color.blue())
				embed.add_field(name="!corona help", value="Says hello and shows how to open help", inline=True)
				embed.add_field(name="!corona", value="To get global corona virus status", inline=True)
				embed.add_field(name="!corona countryname", value="To get corona virus status in particular country", inline=True)
				embed.add_field(name="!corona list", value="To get list", inline=True)
				embed.add_field(name="!corona list n", value="To get list n. Here n is page number(1-4)", inline=True)
				embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
				
				await message.channel.send(embed=embed)
			
			else:
				Country = ""

				#taking the splited element into concatenated string
				for i in range(1,len(country)):
					Country += country[i] + " "

				#This will work once author gives correct value to !corona token then it will get the data successfully from requests
				try:
					data, place = getcases(Country) 
					confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
					active = confirmed - (recovered + death)
					embed=discord.Embed(title= place.capitalize()+"Corona Cases Status", color=discord.Color.blue())
					embed.add_field(name="Active Cases", value=active, inline=True)
					embed.add_field(name="Recovered", value=recovered, inline=True)
					embed.add_field(name="Deaths", value=death, inline=True)
					embed.add_field(name="Confirmed Cases", value= confirmed, inline=True)
					embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
					await message.channel.send(embed = embed) 
				
				#This will work once author gives incorrect value to !corona token
				except KeyError:
					await message.channel.send("Send the correct arguments. Check the list of places using `!corona list`")
					print("error")
#Running bot using token id importing from .env file
client.run(os.getenv('TOKEN'))
