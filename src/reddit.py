import discord
from discord.ext import commands

#Helper Libraries
import feedparser
import praw

#Utils
import strings
import secret

reddit = praw.Reddit(user_agent=secret.reddit_user_agent,
    client_id=secret.reddit_id,
    client_secret=secret.reddit_secret,
    username=secret.reddit_username,
    password=secret.reddit_password)

class Reddit():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def aww(self, ctx):
        subreddit = reddit.subreddit('aww').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True)
    async def Kat(self, ctx):
        subreddit = reddit.subreddit('cat').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True, hidden=True)
    async def luce(self, ctx):
        subreddit = reddit.subreddit('corgibutts').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True)
    async def prequels(self, ctx):
        subreddit = reddit.subreddit('PrequelMemes').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True)
    async def quotes(self, ctx):
        subreddit = reddit.subreddit('quotes').random()
        await self.bot.say(subreddit.title)

    @commands.command(pass_context=True)
    async def funny(self, ctx):
        subreddit = reddit.subreddit('funny').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True)
    async def risky(self, ctx):
        subreddit = reddit.subreddit('random').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True, hidden=True)
    async def liquid(self, ctx):
        subreddit = reddit.subreddit('corgi').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True)
    async def dank(self, ctx):
        subreddit = reddit.subreddit('dankmemes').random()
        await self.bot.say(subreddit.url)

    @commands.command(pass_context=True)
    async def wholesome(self, ctx):
        subreddit = reddit.subreddit('wholesomememes').random()
        await self.bot.say(subreddit.url)

def setup(bot):
    bot.add_cog(Reddit(bot))
