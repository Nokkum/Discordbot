import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    rules_channel = discord.utils.get(member.guild.text_channels, name="rules")
    if channel:
        if rules_channel:
            await channel.send(f"Welcome, {member.mention}! Be sure to check out {rules_channel.mention}")
        else:
            await channel.send(f"Welcome, {member.mention}!")

bot.run(os.getenv("TOKEN"))
