import random
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
    bot.add_cog(SampleListenerCog(bot))

class SampleListenerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.setup()

    def setup(self):
        """ Kirito React """
        @self.bot.listen()
        async def on_message(message):
            # Ignore my own messages
            if message.author == self.bot.user:
                return

            if "kirito" in message.content.lower():
                print(f"Reacted to kirito at {datetime.now().time()}")
                emotes = ["💛"]
                vege = ["🥦", "🥬", "🍆", "🍌"]
                if "vege" in message.content.lower():
                    print(f"Reacted to (kirito) vege at {datetime.now().time()}")
                    emotes.extend([random.choice(vege)])

                for r in emotes:
                    await message.add_reaction(r)
