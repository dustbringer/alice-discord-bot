import random
from datetime import datetime

import discord
from discord.ext import commands

from data.pasta_list import pasta_list

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
    bot.add_cog(CopyPastaCog(bot))

class CopyPastaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.setup()

    def setup(self):
        """ Copypasta commands """
        @self.bot.listen()
        async def on_message(message):
            # Ignore my own messages
            if message.author == self.bot.user:
                return

            # Get Pasta
            msg = message.content.split(" ")

            # Print embedded if exists
            if msg[0].lower().startswith("pasta."):
                cmd = msg[0].split(".")[1]

                # Print pasta
                if cmd == "random":
                    print(f"{datetime.now().time()}; Reacted to random copypasta")
                    cmd = random.choice(list(pasta_list))

                if cmd in pasta_list.keys():
                    print(f"{datetime.now().time()}; Reacted to copypasta '{cmd}'")
                    pasta = pasta_list[cmd]
                    embd = discord.Embed(title=pasta["name"], description=pasta["content"])
                    await message.channel.send(embed=embd)
