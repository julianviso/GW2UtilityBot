import discord
from discord.ext import commands

#Helper Libraries
from urllib.request import urlopen
import json
from operator import itemgetter
from datetime import datetime

#Utils
import strings
from decorators import count

class Dailies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="daily", pass_context=True)
    async def daily(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('```' + strings.noCommandFound + '```')


    @daily.command(name="tomorrowsFractals", pass_context=True, help=strings.tomorrowsFractalsDescription)
    async def tomorrowsFractals(self, ctx):
        tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
        data = json.load(tomorrowsDailies)
        results = []
        formattedResults = None
        for fractalData in data['fractals']:  
            for ids in [fractalData['id']]:
                readTomorrowsFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                tomorrowsFractalsData = json.load(readTomorrowsFractals)
                results.append(tomorrowsFractalsData[0]['name'])
        formattedResults = "\n".join(itemgetter(0,1,2,6,10,14)(results))
        await self.bot.say('```' + formattedResults + '```')

    @daily.command(name="fractals", pass_context=True, help=strings.dailyFractalsDescription)
    async def dailyFractals(self, ctx):
        todaysDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily")
        data = json.load(todaysDailies)
        results = []
        formattedResults = None
        for fractalData in data['fractals']:
            for ids in [fractalData['id']]:
                readDailyFractals = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                todaysFractalsData = json.load(readDailyFractals)
                results.append(todaysFractalsData[0]['name'])
        formattedResults = "\n".join(itemgetter(0,1,2,6,10,14)(results))
        await self.bot.say('```' + formattedResults + '```')

    @daily.command(name="pve", pass_context=True, help=strings.dailyPVEDescription)
    async def dailyPVE(self, ctx):
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

    @daily.command(name="tomorrowsPVE", pass_context=True, help=strings.tomorrowsPVEDescription)
    async def tomorrowsPVE(self, ctx):
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

    @daily.command(name="pvp", pass_context=True, help=strings.dailyPVPDescription)
    async def dailyPVP(self, ctx):
        todaysPVP = urlopen("https://api.guildwars2.com/v2/achievements/daily")
        data = json.load(todaysPVP)
        results = []
        for pvpData in data['pvp']:
            for ids in [pvpData['id']]:
                readDailyPVP = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                todaysDailyPVP = json.load(readDailyPVP)
                results.append(todaysDailyPVP[0]['name'])
        formattedResults = "\n".join(results)
        await self.bot.say('```' + formattedResults + '```')

    @daily.command(name="tomorrowsPVP", pass_context=True, help=strings.tomorrowsPVPDescription)
    async def tomorrowsPVP(self, ctx):
        tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
        data = json.load(tomorrowsDailies)
        results = []
        for pvpData in data['pvp']:
            for ids in [pvpData['id']]:
                readTomorrowsPVP = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                tomorrowsPVPData = json.load(readTomorrowsPVP)
                results.append(tomorrowsPVPData[0]['name'])
        formattedResults = "\n".join(results)
        await self.bot.say('```' + formattedResults + '```')

    @daily.command(name="wvw", pass_context=True, help=strings.dailyWVWDescription)
    async def dailyWVW(self, ctx):
        todaysWVW = urlopen("https://api.guildwars2.com/v2/achievements/daily")
        data = json.load(todaysWVW)
        results = []
        for wvwData in data['wvw']:
            for ids in [wvwData['id']]:
                readDailyWVW = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                todaysDailyWVW = json.load(readDailyWVW)
                results.append(todaysDailyWVW[0]['name'])
        formattedResults = "\n".join(results)
        await self.bot.say('```' + formattedResults + '```')

    @daily.command(name="tomorrowsWVW", pass_context=True)
    async def tomorrowsWVW(self, ctx, help=strings.tomorrowsWVWDescription):
        tomorrowsDailies = urlopen("https://api.guildwars2.com/v2/achievements/daily/tomorrow")
        data = json.load(tomorrowsDailies)
        results = []
        for wvwData in data['wvw']:
            for ids in [wvwData['id']]:
                readTomorrowsWVW = urlopen("https://api.guildwars2.com/v2/achievements?ids="+str(ids))
                tomorrowsWVWData = json.load(readTomorrowsWVW)
                results.append(tomorrowsWVWData[0]['name'])
        formattedResults = "\n".join(results)
        await self.bot.say('```' + formattedResults + '```')

    @daily.command(name="psna", pass_context=True, help=strings.psnaDescription)
    async def psna(self, ctx):
        #Monday is 0, Sunday is 6
        day = datetime.today().weekday()
        with open('data.json') as json_data:
            data = json.load(json_data)
        await self.bot.say('```\nDaily Pact Supply Network Agent \n' + data['pact_supply_network_agent'][day] + '```')


    @commands.command(help=strings.gatheringNodesDescription)
    async def gatheringNodes(self, ctx):
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
