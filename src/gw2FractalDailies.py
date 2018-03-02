#Discord specific
import discord 
from discord.ext import commands

#Helper Libraries
from urllib.request import urlopen
import json
from pprint import pprint
from operator import itemgetter

#Utils
import strings
import secret

bot = commands.Bot(command_prefix='-', description=strings.helpDescription)
tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
data = json.load(tomorrowsDailies)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

#Easter Eggs
@bot.command(hidden=True)
async def theEternal():
    await bot.say(strings.obi)

@bot.command(hidden=True)
async def michelle():
    await bot.say(strings.michelle)

#Main command
@bot.command(help=strings.tomorrowsFractalsDescription)
async def tomorrowsFractals():
    results = []
    formattedResults = None
    for fractalData in data['fractals']:  
        for ids in [fractalData['id']]:
            readTomorrowsFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
            tomorrowsFractalsData = json.load(readTomorrowsFractals)
            results.append(tomorrowsFractalsData[0]['name'])
    formattedResults = "\n".join(itemgetter(0,1,5,9,13,14)(results))
    await bot.say('```' + formattedResults + '```')

@bot.command(hidden=True)
async def PlatMichelleT4s():
    results = []
    formattedResults = None
    for fractalData in data['fractals']:  
        for ids in [fractalData['id']]:
            readTomorrowsFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
            tomorrowsFractalsData = json.load(readTomorrowsFractals)
            results.append(tomorrowsFractalsData[0]['name'])
    formattedResults = "\n".join(results)
    await bot.say(formattedResults)
    print (formattedResults[0,1,3,7,11,15])

displayName = urlopen("https://api.guildwars2.com/v2/achievements?ids=2327").read()
itemReward = urlopen("https://api.guildwars2.com/v2/items?ids=68126").read()

#print ("daily is: " + displayName)
#print ("reward is: " + itemReward)
bot.run(secret.client_secret)
