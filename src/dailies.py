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
    async def gatheringNodes(self):
        with open('data.json') as json_data:
            data = json.load(json_data)
        await self.bot.say('```\nRich Gathering Nodes\n' + data['gathering_nodes'] + '```')


def setup(bot):
    bot.add_cog(Dailies(bot))
