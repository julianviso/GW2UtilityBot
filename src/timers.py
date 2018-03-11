import discord
from discord.ext import commands

#Helper Libraries
from datetime import datetime
import feedparser
import json

#Utils
import strings

class Server():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help=strings.serverTimeDescription)
    async def serverTime(self):
        await self.bot.say('```Server time: ' + datetime.utcnow().strftime("%I:%M%p") + '```')

    @commands.command(help=strings.releaseNotesDescription)
    async def releaseNotes(self):
        newestPost = feedparser.parse('https://www.guildwars2.com/en/feed')
        await self.bot.say(newestPost.entries[0]['link'])

    @commands.command()
    async def psna(self):
        #Monday is 0, Sunday is 6
        day = datetime.today().weekday()
        with open('data.json') as json_data:
            data = json.load(json_data)
        await self.bot.say('```' + data['pact_supply_network_agent'][day] + '```')

def setup(bot):
    bot.add_cog(Server(bot))
