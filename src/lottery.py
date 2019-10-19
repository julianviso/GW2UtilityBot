import discord
from discord.ext import commands

import random

import strings

class Lottery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="lottery", pass_context=True)
    async def lottery(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('```' + strings.noCommandFound + '```')

    @lottery.command(name="start", pass_context=True)
    async def start(self, ctx):
        server = ctx.message.author.guild
        if discord.utils.get(server.roles, name="Lottery") == None:
            await server.create_role(name='Lottery')
            await ctx.send('```Lottery role created for server```')
        else:
            await ctx.send('```Lottery role already exists```')

    @lottery.command(name="entry", hidden=True, pass_context=True)
    async def entry(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name="Lottery")
        if discord.utils.get(author.roles, name="Lottery") == None:
            await author.add_roles(role)
            await ctx.send('```' + str(author) + ' is now in Lottery```')
        else:
            await ctx.send('```You already are a participant```')

    @lottery.command(name="add", pass_context=True)
    async def add(self, ctx, user: discord.Member):
        server = (ctx.message.author.guild)
        role = discord.utils.get(server.roles, name="Lottery")
        if discord.utils.get(user.roles, name="Lottery") == None:
            await user.add_roles(role)
            await ctx.send('```Adding ' + str(user) + ' to lottery```')
        else:
            await ctx.send('```' + str(user) + ' already has the role```')

    @lottery.command(name="contestants", pass_context=True)
    async def contestants(self, ctx):
        server = ctx.message.author.guild
        contestants = []
        for member in server.members:
            for roles in member.roles:
                if (roles.name == "Lottery"):
                    contestants.append(str(member))
        await ctx.send('```Contestants in lottery\n\n' + str(contestants) + '```')

    @lottery.command(name="run", pass_context=True)
    async def run(self, ctx):
        server = ctx.message.author.guild
        contestants = []
        for member in server.members:
            for roles in member.roles:
                if (roles.name == "Lottery"):
                    contestants.append(str(member))
        await ctx.send('```Lottery winner: ' + random.choice(contestants) + '```')

    @lottery.command(name="finish", pass_context=True)
    async def finish(self, ctx):
        server = ctx.message.author.guild
        role = discord.utils.get(server.roles, name="Lottery")
        await role.delete()
        await ctx.send('```Lottery finished, deleting lottery role for entire server```')

def setup(bot):
    bot.add_cog(Lottery(bot))
