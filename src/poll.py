import discord
from discord.ext import commands
from discord import NotFound

import strings

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="poll", pass_context=True)
    async def poll(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('```' + strings.noCommandFound + '```')

    @poll.command(name="setup", pass_context=True, help=strings.setupDescription)
    async def setup(self, ctx, question, *options: str):
        if len(options) <= 1:
            await self.bot.say('```' + strings.oneOption + '```')
            return
        if len(options) > 10:
            await self.bot.say('```' + strings.tooManyOptions + '```')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await react_message.edit(embed=embed)

    @poll.command(name="tally", pass_context=True, help=strings.tallyDescription)
    async def tally(self, ctx, id):
        poll_to_count = await discord.abc.Messageable.fetch_message(ctx, id)
        for i in poll_to_count.reactions:
            await ctx.send(str(i.count) + ' votes for: ' + i.emoji)
        


def setup(bot):
    bot.add_cog(Poll(bot))
