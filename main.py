# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
from chatbot import Chatbot
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv(override=True)
chatbot = Chatbot()

intents = discord.Intents.all()
contexts = discord.AppCommandContext.all()
bot = commands.Bot(command_prefix='!', intents=intents, contexts=contexts)

@bot.command(name="icebreaker", description="Provides a random icebreaker")
@commands.cooldown(15, 60)
async def icebreaker(ctx):
    icebreaker = chatbot.icebreaker()
    await ctx.send(icebreaker)

@bot.command(name="trivia", description="Provides a random trivia question")
@commands.cooldown(15, 60)
async def trivia(ctx):
    trivia = chatbot.trivia()
    await ctx.send(trivia)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# print(os.getenv("BOT_TOKEN"))
bot.run(os.getenv("BOT_TOKEN"))
