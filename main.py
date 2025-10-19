import discord
from discord.ext import commands

import os

from functions import botcommands
from functions import messages
from functions import robloxupds
from functions import roles
from functions import tempchats


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am a robot")

bot.run("Token")