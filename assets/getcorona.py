import discord, os, requests, json
from assets.embed import EmbedCases

def getcases(country = "global"):
	url = "https://covid19.mathdro.id/api"
	if country != "global":
		url = 'https://covid19.mathdro.id/api'+'/countries/'+country
	response = requests.request("GET", url)
	data = json.loads(response.text)
	return data, country

def getcorona(country):
    if len(country.split()) >= 2 :
        Country = ""
        country = country.split()

        #taking the splited element into concatenated string
        for i in range(1,len(country)):
            Country += country[i].capitalize() + " "
        print(Country)

        #This will work once author gives correct value to !corona token then it will get the data successfully from requests    
        try:
            data, place = getcases(Country) 
            confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
            active = confirmed - (recovered + death)
            embed = EmbedCases(confirmed, recovered, death,active, place)
            return embed
        except KeyError:
            print("unknown place is received")
            title = "unknown place is received"
            desc = "Send the correct arguments. Check the list of places using `!list`"
            embed = discord.Embed(title=title, description= desc, color=discord.Color.blue())
            return embed

    else:
        data, place = getcases() 
        confirmed, recovered, death = data["confirmed"]["value"], data["recovered"]["value"], data["deaths"]["value"]
        active = confirmed - (recovered + death)	
        embed = EmbedCases(confirmed, recovered, death,active, place.capitalize())
        return embed
