import discord
from discord.ext import commands

#Helper Libraries
from datetime import datetime
import feedparser

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

def setup(bot):
    bot.add_cog(Server(bot))
