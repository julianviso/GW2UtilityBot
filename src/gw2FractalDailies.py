import discord 
from discord.ext import commands
from urllib.request import urlopen
import json
from pprint import pprint
import secret
from operator import itemgetter

bot = commands.Bot(command_prefix='-', description='testss')
tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
data = json.load(tomorrowsDailies)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def theEternal():
    await bot.say('sup Obi')

@bot.command()
async def info():
    await bot.say('Bot created by Valrok. If you have feedback or suggestions on new features contact me on discord Valrok.3742 or in game.')

@bot.command()
async def helpMe():
    await bot.say('```only current command: !tomorrowsFractals```')

@bot.command()
async def tomorrowsFractals():
    results = []
    formattedResults = None
    for fractalData in data['fractals']:  
        for ids in [fractalData['id']]:
            readTomorrowsFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
            tomorrowsFractalsData = json.load(readTomorrowsFractals)
            results.append(tomorrowsFractalsData[0]['name'])
    formattedResults = "\n".join(itemgetter(0,1,5,9,13,14)(results))
    await bot.say(formattedResults)

@bot.command()
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
