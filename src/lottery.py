import discord
from discord.ext import commands

import random

import strings

class Lottery:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="lottery", pass_context=True)
    async def lottery(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('```' + strings.noCommandFound + '```')

    @lottery.command(name="start", pass_context=True)
    async def start(self, ctx):
        author = ctx.message.author
        await self.bot.create_role(author.server, name="Lottery")
        await self.bot.say('```Lottery role created for server```')

    @lottery.command(name="entry", pass_context=True)
    async def entry(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.server.roles, name="Lottery")
        await self.bot.add_roles(author, role)
        await self.bot.say('```' + str(author) + ' is now in Lottery```')

    @lottery.command(name="add", pass_context=True)
    async def add(self, ctx, *users: str):
        if len(users) < 1:
            await self.bot.say('```Need to enter at least one user you want to add to lottery```')
        server = self.bot.get_server(str(ctx.message.author.server.id))
        role = discord.utils.get(server.roles, name="Lottery")
        for user in users:
            print(user)
            await self.bot.add_roles(user, role)

    @lottery.command(name="contestants", pass_context=True)
    async def contestants(self, ctx):
        server = self.bot.get_server(str(ctx.message.author.server.id))
        contestants = []
        for member in server.members:
            for roles in member.roles:
                if (roles.name == "Lottery"):
                    contestants.append(str(member))
        await self.bot.say('```Contestants in lottery\n\n' + str(contestants) + '```')

    @lottery.command(name="run", pass_context=True)
    async def run(self, ctx):
        server = self.bot.get_server(str(ctx.message.author.server.id))
        contestants = []
        for member in server.members:
            for roles in member.roles:
                if (roles.name == "Lottery"):
                    contestants.append(str(member))
        await self.bot.say('```Lottery winner: ' + random.choice(contestants) + '```')

    @lottery.command(name="finish", pass_context=True)
    async def finish(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.server.roles, name="Lottery")
        await self.bot.delete_role(author.server, role)
        await self.bot.say('```Lottery finished, deleting lottery role for entire server```')

def setup(bot):
    bot.add_cog(Lottery(bot))
