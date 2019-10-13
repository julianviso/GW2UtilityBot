import discord
from discord.ext import commands

#Helper Libraries
from datetime import datetime
import feedparser
import json

#Utils
import strings

#IRI: changed 'Server' to 'timers'
class timers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="server", pass_context=True)
    async def server(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('```' + strings.noCommandFound + '```')

    @server.command(name="time", pass_context=True, help=strings.serverTimeDescription)
    async def serverTime(self, ctx):
        await self.bot.say('```Server time: ' + datetime.utcnow().strftime("%I:%M%p") + '```')

    @server.command(name="news", pass_context=True, help=strings.releaseNotesDescription)
    async def releaseNotes(self, ctx):
        newestPost = feedparser.parse('https://www.guildwars2.com/en/feed')
        await self.bot.say(newestPost.entries[0]['link'])

def setup(bot):
    bot.add_cog(Server(bot))
