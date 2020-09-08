import os
import sys
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

"""
Example:
- https://github.com/agubelu/discord-bot-template
"""

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
ext = [
    'cogs.basic',
    'cogs.copypasta',
    'cogs.santa',
    'cogs.sample_listener'
]

def set_cogs(bot):
    for e in ext:
        bot.load_extension(e)


def main():
    bot = commands.Bot(command_prefix="a.")
    set_cogs(bot)



    @bot.event
    async def on_ready():
        # Get guild with matching name
        # guild = discord.utils.get(bot.guilds, name=GUILD)

        for guild in bot.guilds:
            print(
                f'{bot.user.name} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})\n'
                f'Guild Size: {len(guild.members)}\n'
            )

        # Setting `Playing ` status
        playing = random.choice(["Kirito", "Eugeo", "Selka", "the Administrator"])
        print(f"Status updated to 'Playing with {playing}'")
        await bot.change_presence(activity=discord.Game(name=f"with {playing}"))

        # # Setting `Streaming ` status
        # await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

        # # Setting `Listening ` status
        # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

        # # Setting `Watching ` status
        # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

    @bot.event
    async def on_member_join(member):
        # # Send a private message, note that we need to wait for dm to be created with `await`
        # await member.create_dm()
        # await member.dm_channel.send(
        #     f'Hi {member.name}, welcome to my Discord server!'
        # )
        pass

    @bot.event
    async def on_message(message):
        # Ignore my own messages
        if message.author == bot.user:
            return

        # Process commands
        await bot.process_commands(message)

        # if message.content == '99!':
        #     response = "testing!!!!!!!!!!! 99!"
        #     await message.channel.send(response)

    @bot.event
    async def on_error(event, *args, **kwargs):
        await super().on_error(event, *args, **kwargs)
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
                f.write(f'Error: {sys.exc_info()}\n\n')
            else:
                raise

    @bot.event
    async def on_command_error(ctx, error):
        await ctx.send('error moment')


    @bot.command(name='kirito', help='<3')
    async def kirito(ctx):
        response = "i love kirito <3"
        await ctx.send(response)

    bot.run(TOKEN)

if __name__ == "__main__":
    main()
