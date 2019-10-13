import discord
from discord.ext import commands

from urllib.request import urlopen
import json
from operator import itemgetter

import strings

class EasterEggs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def PlatMichelleT4s(self):
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
        await self.bot.say('```' + strings.platQuote + '\n\n' + formattedResults + '```')

def setup(bot):
    bot.add_cog(EasterEggs(bot))
