#Discord specific
import discord 
from discord.ext import commands

#Utils
import strings
import secret

#Specifies what extensions to load when the bot starts up from this directory
startup_extensions = ["easterEggs", "dailies", "timers"]

bot = commands.Bot(command_prefix='-', description=strings.helpDescription)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command(hidden=True)
async def load(extension_name : str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command(hidden=True)
async def unload(extension_name : str):
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(secret.client_secret)
