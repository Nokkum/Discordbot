import discord
import os
import asyncio
import logging
from discord.ext import commands
from database import Database
from config import DEFAULT_PREFIX

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=DEFAULT_PREFIX, intents=intents)
db = Database()

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
    logger.info(f"Connected to {len(bot.guilds)} guild(s)")
    
    try:
        await load_extensions()
        await sync_commands()
        logger.info("Bot is ready!")
        print(f"Logged in as {bot.user}")
    except Exception as e:
        logger.error(f"Error during startup: {e}")

async def load_extensions():
    try:
        import commands as bot_commands
        import events as bot_events
        
        await bot_commands.setup(bot, db)
        await bot_events.setup(bot, db)
        
        logger.info("Successfully loaded all extensions")
    except Exception as e:
        logger.error(f"Failed to load extensions: {e}")
        raise

async def sync_commands():
    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing required argument: {error.param}")
    else:
        logger.error(f"Unhandled error: {error}")
        await ctx.send(f"❌ An error occurred: {str(error)}")

@bot.event
async def on_app_command_error(interaction: discord.Interaction, error):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await interaction.response.send_message(
            "❌ You don't have permission to use this command.",
            ephemeral=True
        )
    else:
        logger.error(f"Unhandled app command error: {error}")
        if not interaction.response.is_done():
            await interaction.response.send_message(
                f"❌ An error occurred: {str(error)}",
                ephemeral=True
            )

async def main():
    async with bot:
        token = os.getenv("TOKEN")
        if not token:
            logger.error("No TOKEN found in environment variables!")
            return
        
        try:
            await bot.start(token)
        except discord.LoginFailure:
            logger.error("Invalid token provided!")
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot shutdown requested")
