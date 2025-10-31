# Discord Bot

## Overview
This is a Discord bot project built with discord.py. The bot welcomes new members to the server when they join.

**Current State:** Setup complete and ready to run. The bot requires a valid Discord bot token to connect to Discord.

**Last Updated:** October 31, 2025

## Recent Changes
- **October 31, 2025:** Initial project setup
  - Installed Python 3.11 and discord.py dependencies
  - Fixed code bug: Added proper `rules_channel` variable definition in `on_member_join` event
  - Added message content intent to prevent warnings
  - Created .gitignore for Python project
  - Configured workflow to run the bot
  - Set up deployment configuration

## Project Structure
```
.
├── bot.py              # Main bot file with Discord client and event handlers
├── requirements.txt    # Python dependencies
├── README.md          # Basic project readme
├── .gitignore         # Git ignore file for Python
└── replit.md          # This file - project documentation
```

## Features
- **Welcome Messages:** Automatically sends a welcome message in the #welcome channel when a new member joins
- **Rules Channel Reference:** If a #rules channel exists, the welcome message includes a mention to it

## Configuration

### Discord Bot Token
The bot requires a Discord bot token stored in the environment variable `TOKEN`. This token is managed through Replit Secrets.

**To get a Discord bot token:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section and create a bot
4. Copy the bot token
5. Add it to Replit Secrets as `TOKEN`

**Important:** Make sure to enable the following intents in the Discord Developer Portal:
- Server Members Intent (for `on_member_join` event)
- Message Content Intent (for bot commands)

### Bot Setup
1. Invite the bot to your server using the OAuth2 URL from the Discord Developer Portal
2. Make sure the bot has permissions to:
   - Read messages in channels
   - Send messages in the #welcome channel
3. Create a `#welcome` channel in your server (required)
4. Optionally create a `#rules` channel for the bot to reference

## Running the Bot

### Development
The bot runs automatically via the configured workflow. It will:
- Connect to Discord using the TOKEN environment variable
- Listen for new member join events
- Send welcome messages in the #welcome channel

### Deployment
The bot is configured to run continuously as a VM deployment, suitable for a Discord bot that needs to stay online 24/7.

## Dependencies
- **discord.py:** Python library for interacting with the Discord API
- **Python 3.11:** Runtime environment

## Architecture
The bot uses the discord.py commands framework with:
- **Intents:** Configured for default intents plus members and message content
- **Command Prefix:** `.` (dot) - ready for future commands
- **Event Handlers:**
  - `on_ready`: Logs when the bot successfully connects
  - `on_member_join`: Sends welcome messages to new members

## Troubleshooting

### Bot won't connect
- Check that the TOKEN environment variable is set correctly
- Verify the token is valid in the Discord Developer Portal
- Ensure you've regenerated the token if it was exposed

### Welcome messages not sending
- Verify a #welcome channel exists in your server
- Check that the bot has permission to send messages in that channel
- Ensure the Server Members Intent is enabled in the Discord Developer Portal

### Commands not working
- Make sure the Message Content Intent is enabled in the Discord Developer Portal
- Check that the bot has permission to read messages
