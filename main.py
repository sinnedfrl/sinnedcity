import os
import os
import os
import os
import discord, os, alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(command_prefix='!', self_bot=True)


# name = for your status and url = for your twitch link
@client.event
async def on_connect():
    await client.change_presence(activity=discord.Streaming(
      name="quit",url="https://twitch.tv/sinnedfrl"))
        


alive.alive()
client.run(os.getenv("TOKEN"), bot=False)
