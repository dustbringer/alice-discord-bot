from datetime import datetime

import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(SantaCog(bot))

class SantaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
