import discord
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
    if channel:
        await channel.send(f"Welcome, {member.mention}! Be sure to check out {rules_channel.mention}")

bot.run(os.getenv("MTQzMzY2OTUwOTcwMDY0ODk2MA.G4OpEP.bVX2G4-dTb4v-UXf5dqmuGga4KikAbgQWUdS50"))
