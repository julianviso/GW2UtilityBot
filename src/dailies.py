import discord
from discord.ext import commands

#Helper Libraries
from urllib.request import urlopen
import json
from operator import itemgetter

#Utils
import strings

class Dailies():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help=strings.tomorrowsFractalsDescription)
    async def tomorrowsFractals(self):
        tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
        data = json.load(tomorrowsDailies)
        results = []
        formattedResults = None
        for fractalData in data['fractals']:  
            for ids in [fractalData['id']]:
                readTomorrowsFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                tomorrowsFractalsData = json.load(readTomorrowsFractals)
                results.append(tomorrowsFractalsData[0]['name'])
        formattedResults = "\n".join(itemgetter(0,1,5,9,13,14)(results))
        await self.bot.say('```' + formattedResults + '```')

    @commands.command(help=strings.dailyFractalsDescription)
    async def dailyFractals(self):
        todaysDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily")
        data = json.load(todaysDailies)
        results = []
        formattedResults = None
        for fractalData in data['fractals']:
            for ids in [fractalData['id']]:
                readDailyFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                todaysFractalsData = json.load(readDailyFractals)
                results.append(todaysFractalsData[0]['name'])
        formattedResults = "\n".join(itemgetter(0,1,5,9,13,14)(results))
        await self.bot.say('```' + formattedResults + '```')

    @commands.command()
    async def dailyPVE(self):
        todaysDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily")
        results = []
        data = json.load(todaysDailies)
        for pveData in data['pve']:
            for ids in [pveData['id']]:
                readDailyPVE = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                todaysDailyPVE = json.load(readDailyPVE)
                results.append(todaysDailyPVE[0]['name'])
        formattedResults = "\n".join(results)
        await self.bot.say('```' + formattedResults + '```')

    @commands.command()
    async def tomorrowsPVE(self):
        tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
        data = json.load(tomorrowsDailies)
        results = []
        for pveData in data['pve']:
            for ids in [pveData['id']]:
                readTomorrowsPVE = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                tomorrowsPVEData = json.load(readTomorrowsPVE)
                results.append(tomorrowsPVEData[0]['name'])
        formattedResults = "\n".join(results)
        await self.bot.say('```' + formattedResults + '```')

    @commands.command(help=strings.gatheringNodesDescription)
    async def gatheringNodes(self):
        output = []
        with open('data.json') as json_data:
            data = json.load(json_data)
        for gatheringNodes in data['gathering_nodes']:
            name = gatheringNodes['name']
            waypoints = gatheringNodes['waypoints']
            output.extend((name, waypoints))
        message = str(output[0]) + "\n\n" + str(output[1]) + "\n\n" + str(output[2]) + "\n\n" + str(output[3]) + "\n\n" + str(output[4]) + \
            "\n\n" + str(output[5]) + "\n\n" + str(output[6]) + "\n\n" + str(output[7])
        await self.bot.say('```\nRich Gathering Node Waypoints\n\n' + message + "```")
   
def setup(bot):
    bot.add_cog(Dailies(bot))
