import discord
import os
from dotenv import load_dotenv
import requests
import json

#importing dotenv file
load_dotenv()

client = discord.Client()

countries = "Afghanistan\nAlbania\nAlgeria\nAndorra\nAngola\nAntigua and Barbuda\nArgentina\nArmenia\nAustralia\nAustria\nAzerbaijan\nBahamas\nBahrain\nBangladesh\nBarbados\nBelarus\nBelgium\nBelize\nBenin\nBhutan\nBolivia\nBosnia and Herzegovina\nBotswana\nBrazil\nBrunei\nBulgaria\nBurkina Faso\nBurma\nBurundi\nCabo Verde\nCambodia\nCameroon\nCanada\nCentral African Republic\nChad\nChile\nChina\nColombia\nComoros\nCongo (Brazzaville)\nCongo (Kinshasa)\nCosta Rica\nCote d'Ivoire\nCroatia\nCuba\nCyprus\nCzechia\nDenmark\nDiamond Princess\nDjibouti\nDominica\nDominican Republic\nEcuador\nEgypt\nEl Salvador\nEquatorial Guinea\nEritrea\nEstonia\nEswatini\nEthiopia\nFiji\nFinland\nFrance\nGabon\nGambia\nGeorgia\nGermany\nGhana\nGreece\nGrenada\nGuatemala\nGuinea\nGuinea-Bissau\nGuyana\nHaiti\nHoly See\nHonduras\nHungary\nIceland\nIndia\nIndonesia\nIran\nIraq\nIreland\nIsrael\nItaly\nJamaica\nJapan\nJordan\nKazakhstan\nKenya\nKorea, South\nKosovo\nKuwait\nKyrgyzstan\nLaos\nLatvia\nLebanon\nLesotho\nLiberia\nLibya\nLiechtenstein\nLithuania\nLuxembourg\nMS Zaandam\nMadagascar\nMalawi\nMalaysia\nMaldives\nMali\nMalta\nMarshall Islands\nMauritania\nMauritius\nMexico\nMicronesia\nMoldova\nMonaco\nMongolia\nMontenegro\nMorocco\nMozambique\nNamibia\nNepal\nNetherlands\nNew Zealand\nNicaragua\nNiger\nNigeria\nNorth Macedonia\nNorway\nOman\nPakistan\nPanama\nPapua New Guinea\nParaguay\nPeru\nPhilippines\nPoland\nPortugal\nQatar\nRomania\nRussia\nRwanda\nSaint Kitts and Nevis\nSaint Lucia\nSaint Vincent and the Grenadines\nSamoa\nSan Marino\nSao Tome and Principe\nSaudi Arabia\nSenegal\nSerbia\nSeychelles\nSierra Leone\nSingapore\nSlovakia\nSlovenia\nSolomon Islands\nSomalia\nSouth Africa\nSouth Sudan\nSpain\nSri Lanka\nSudan\nSuriname\nSweden\nSwitzerland\nSyria\nTaiwan*\nTajikistan\nTanzania\nThailand\nTimor-Leste\nTogo\nTrinidad and Tobago\nTunisia\nTurkey\nUS\nUganda\nUkraine\nUnited Arab Emirates\nUnited Kingdom\nUruguay\nUzbekistan\nVanuatu\nVenezuela\nVietnam\nWest Bank and Gaza\nYemen\nZambia\nZimbabwe\n"

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

@client.event
async def on_message(message):
	
	#checking whether bot message is recieved
	if message.author == client.user:
		print("message is delivered")
	
	#checks when someone says hello
	if message.content.startswith("!hello"):
		await message.channel.send("Hello! <@!"+str(message.author.id)+">"+"\nType `!help'` to learn how to use this bot ")
	
	#checks when someone says help
	if message.content.startswith("!help"):
		await message.channel.send('''use this following commands:\n`!corona countryname`: To get corona virus status in particular country''')
	
	#checks when someone says corona
	if message.content.startswith("!corona"):
		if message.content == "!corona":
			data, place = getcases() 
			confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
			active = confirmed - (recovered + death)
			await message.channel.send(' **'+place.upper()+' CORONA CASES STATS**\n**Active cases:** '+str(active)+'\n**Recovered:** '+str(recovered)+'\n**Death:** '+str(death)+'\n**Total Confirmed:** '+str(confirmed)+'')
		country = message.content.split() 
		if len(country) >= 2:
			#showing available places
			if country[1] == "list":
				#Showing list of places
				await message.channel.send("List of countries available:\n```yaml\n"+countries+"```")
			else:
				Country = ""
				#replacing space with %20 for web request 
				Country = Country.replace(" ", "%20")
				#taking the splited element into concatenated string
				for i in range(1,len(country)):
					Country += country[i] + " " 
				
				#This will work once author gives correct value to !corona token then it will get the data successfully from requests
				try:
					data, place = getcases(Country) 
					confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
					active = confirmed - (recovered + death)
					await message.channel.send(' **'+place.upper()+' CORONA CASES STATS**\n**Active cases:** '+str(active)+'\n**Recovered:** '+str(recovered)+'\n**Death:** '+str(death)+'\n**Total Confirmed:** '+str(confirmed)+'') 
				
				#This will work once author gives incorrect value to !corona token
				except KeyError:
					await message.channel.send("Send the correct arguments. Check the list of places using `!corona list`")
#Running bot using token id importing from .env file
client.run(os.getenv('TOKEN'))
