import discord, os, requests, json
from assets.countries import countries_page as pages
def EmbedCases(confirmed, recovered, death, active, place):
	embed=discord.Embed(title = "Corona Case Stats", description = place, color = discord.Color.blue())
	embed.add_field(name="Active Cases", value=active, inline=True)
	embed.add_field(name="Recovered", value=recovered, inline=True)
	embed.add_field(name="Deaths", value=death, inline=True)
	embed.add_field(name="Confirmed Cases", value= confirmed, inline=True)
	embed.set_footer(text="Stay safe! Stay home 🏠")
	return embed

def EmbedList(arg):
    if arg.isnumeric():
        if int(arg) >= 1 and int(arg) <=4 :
            embed=discord.Embed(title="List of countries available", color=discord.Color.blue())
            embed.add_field(name="Page "+str(arg)+" of 4", value=pages[int(arg)-1], inline=False)
            embed.set_footer(text="Type '!corona help' to know, how to see the other pages")
            return embed
        else:
            title = "Received incorrect page number"
            desc = "Send the correct argument. Page number should have from 1 to 4"
            embed = discord.Embed(title=title, description=desc, color=discord.Color.blue())
            return embed
    else:
        title = "Recieved incorrect page number"
        desc = "Send the correct argument. Page number should have from 1 to 4 and only numerals"
        embed = discord.Embed(title=title, description=desc, color=discord.Color.blue())
        return embed

def EmbedHelp():
	embed=discord.Embed(title="Help for Corona Bot", color=discord.Color.blue())
	embed.add_field(name="!hello", value="Says hello and shows how to open help", inline=True)
	embed.add_field(name="!help", value="Shows available commands", inline=True)
	embed.add_field(name="!corona", value="To get global corona virus status", inline=True)
	embed.add_field(name="!corona countryname", value="To get corona virus status in particular country", inline=True)
	embed.add_field(name="!list", value="Shows page 1 of list", inline=True)
	embed.add_field(name="!list n", value="To get list n page, Here n is page number(1-4)", inline=True)
	embed.add_field(name="!go corona", value="Show corona safety precautions", inline=True)
	embed.add_field(name="!check corona", value="Shows corona symptoms", inline=True)
	embed.set_footer(text="Stay safe! Stay home 🏠")
	return embed

def EmbedSafety():
	embed=discord.Embed(title="Safety Measure from COVID-19", url = "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public?gclid=Cj0KCQjwyZmEBhCpARIsALIzmnKox_C8aLmkESAJ6iIFPJW1MoQp2KF4BA_o30HuHXg5UsSylt4lk04aAp7_EALw_wcB", color=discord.Color.blue())
	embed.add_field(name ="To prevent the spread of COVID-19:", value="Clean your hands often. Use soap and water, or an alcohol-based hand rub.\nMaintain a safe distance from anyone who is coughing or sneezing.\nWear a mask when physical distancing is not possible.\nDon’t touch your eyes, nose or mouth.\nCover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\nStay home if you feel unwell.\nIf you have a fever, cough and difficulty breathing, seek medical attention.", inline=True)
	embed.add_field(name ="Masks", value="Masks can help prevent the spread of the virus from the person wearing the mask to others. Masks alone do not protect against COVID-19, and should be combined with physical distancing and hand hygiene. Follow the advice provided by your local health authority.", inline=True)
	embed.add_field(name = "Recommended", value= "\n\nCalling in advance allows your healthcare provider to quickly direct you to the right health facility. This protects you, and prevents the spread of viruses and other infections.", inline=False)
	embed.set_footer(text="Stay safe! Stay home 🏠")
	return embed

def EmbedSymtoms():
	embed=discord.Embed(title="Symptoms for Corona Bot", color=discord.Color.blue())
	embed.add_field(name="Most common symptoms", value="fever\ndry cough\ntiredness", inline=True)
	embed.add_field(name="Less common symptoms", value="aches and pains\nsore throat\ndiarrhoea\nconjunctivitis\nheadache\nloss of taste or smell\na rash on skin, or discolouration of fingers or toes", inline=True)
	embed.add_field(name="Serious symptoms", value="difficulty breathing or shortness of breath\nchest pain or pressure\nloss of speech or movement", inline=True)
	embed.set_footer(text="Stay safe! Stay home 🏠")
	return embed
