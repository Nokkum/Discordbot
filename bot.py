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
    channel = discord.utils.get(member.guild.text_channels, name="👋-》welcome")
    if channel:
        await channel.send(f"Welcome, {member.mention}! Be sure to check out {#1372767539863748698}")

bot.run("https://discord.com/oauth2/authorize?client_id=1433669509700648960&permissions=52224&integration_type=0&scope=bot+applications.commands")
