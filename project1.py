import discord 
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

from sampah import sampah_organik, sampah_anorganik

@bot.event
async def on_ready():
    print(f'bot sudah login dengan nama {bot.user}')

@bot.command()
async def organik(ctx):
    await ctx.send("salah satu sampah organik adalah : ")
    await ctx.send(sampah_organik())

@bot.command()
async def anorganik(ctx):
    await ctx.send("salah satu sampah anorganik adalah : ")
    await ctx.send(sampah_anorganik())

bot.run("apa hayooo :)")

