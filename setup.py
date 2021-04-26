import discord, os, requests, json
from dotenv import load_dotenv

pages = ["Page 1 of 4\nAfghanistan, Albania, Algeria, Andorra, Angola, Antigua and Barbuda, Argentina, Armenia, Australia, Austria, Azerbaijan, Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bhutan, Bolivia, Bosnia and Herzegovina, Botswana, Brazil, Brunei, Bulgaria, Burkina Faso, Burma, Burundi, Cabo Verde, Cambodia, Cameroon, Canada, Central African Republic, Chad, Chile, China, Colombia, Comoros, Congo (Brazzaville), Congo (Kinshasa), Costa Rica, Cote d'Ivoire, Croatia, Cuba, Cyprus, Czechia",
	"Page 2 of 4\nDenmark, Diamond Princess, Djibouti, Dominica, Dominican Republic, Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Eswatini, Ethiopia, Fiji, Finland, France, Gabon, Gambia, Georgia, Germany, Ghana, Greece, Grenada, Guatemala, Guinea, Guinea-Bissau, Guyana, Haiti, Holy See, Honduras, Hungary, Iceland, India, Indonesia, Iran, Iraq, Ireland, Israel, Italy, Jamaica, Japan, Jordan, Kazakhstan, Kenya, Korea, South, Kosovo, Kuwait, Kyrgyzstan, Laos, Latvia, Lebanon, Lesotho",
	"Page 3 of 4\nLiberia, Libya, Liechtenstein, Lithuania, Luxembourg, MS Zaandam, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Marshall Islands, Mauritania, Mauritius, Mexico, Micronesia, Moldova, Monaco, Mongolia, Montenegro, Morocco, Mozambique, Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, North Macedonia, Norway, Oman, Pakistan, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Qatar, Romania, Russia, Rwanda, Saint Kitts and Nevis, Saint Lucia",
	"Page 4 of 4\nSaint Vincent and the Grenadines, Samoa, San Marino, Sao Tome and Principe, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, South Sudan, Spain, Sri Lanka, Sudan, Suriname, Sweden, Switzerland, Syria, Taiwan*, Tajikistan, Tanzania, Thailand, Timor-Leste, Togo, Trinidad and Tobago, Tunisia, Turkey, US, Uganda, Ukraine, United Arab Emirates, United Kingdom, Uruguay, Uzbekistan, Vanuatu, Venezuela, Vietnam, West Bank and Gaza, Yemen, Zambia, Zimbabwe"]

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
		await message.channel.send('''**use these following commands:**
`!hello` or `!corona help` - Says hello and shows how to open help
`!corona` - To get global corona virus status
`!corona countryname` - To get corona virus status in particular country
`!corona list` - To get list 1
`!corona list n` - To get list n. Here n is page number(1-4)''')
	
	#checks when someone says corona
	if message.content.startswith("!corona"):

		if message.content == "!corona":
			data, place = getcases() 
			confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
			active = confirmed - (recovered + death)
			await message.channel.send(' **'+place.upper()+' CORONA CASES STATUS**\n**Active cases:** '+str(active)+'\n**Recovered:** '+str(recovered)+'\n**Death:** '+str(death)+'\n**Total Confirmed:** '+str(confirmed)+'')

		country = message.content.split() 
		if len(country) >= 2:

			#showing available places
			if country[1] == "list":
				
				#Showing list of places
				if len(country) > 2: 
					print(country)
					if country[2] == "1":
						await message.channel.send("List of countries available:\n```yaml\n"+pages[0]+"```")
					if country[2] == "2":
						await message.channel.send("List of countries available:\n```yaml\n"+pages[1]+"```")
					if country[2] == "3":
						await message.channel.send("List of countries available:\n```yaml\n"+pages[2]+"```")
					if country[2] == "4":
						await message.channel.send("List of countries available:\n```yaml\n"+pages[3]+"```")
			
				else:
					await message.channel.send("List of countries available:\n```yaml\n"+pages[0]+"```Type `!corona help` to know, how to see the other pages")

			elif  country[1] == "help":
						await message.channel.send('''**use these following commands:**
`!hello` or `!corona help` - Says hello and shows how to open help
`!corona` - To get global corona virus status
`!corona countryname` - To get corona virus status in particular country
`!corona list` - To get list 1
`!corona list n` - To get list n. Here n is page number(1-4)''')
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
					await message.channel.send(' **'+place.upper()+' CORONA CASES STATUS**\n**Active cases:** '+str(active)+'\n**Recovered:** '+str(recovered)+'\n**Death:** '+str(death)+'\n**Total Confirmed:** '+str(confirmed)+'') 
				
				#This will work once author gives incorrect value to !corona token
				except KeyError:
					await message.channel.send("Send the correct arguments. Check the list of places using `!corona list`")
					print("error")
#Running bot using token id importing from .env file
client.run(os.getenv('TOKEN'))
