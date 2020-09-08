from datetime import datetime

import discord
from discord.ext import commands

"""
https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be

The gist:
- Each cog is a Python class that subclasses commands.Cog.
- Every command is marked with the commands.command() decorator.
- Every listener is marked with the commands.Cog.listener() decorator.
- Cogs are then registered with the Bot.add_cog() call.
- Cogs are subsequently removed with the Bot.remove_cog() call.
"""
def setup(bot):
    bot.add_cog(BasicCog(bot))

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command('bruh')
    async def bruh(self, ctx):
        print(f"{datetime.now().time()}; Reacted to 'a.bruh', sent 'Bruhhhh'")
        await ctx.send("Bruhhhh")
