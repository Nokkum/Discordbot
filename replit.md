# Discord Welcome Bot

## Overview
A feature-rich Discord bot built with discord.py that welcomes new members, tracks departures, and provides useful server commands. The bot includes customizable messages, embeds, slash commands, and persistent server-specific settings.

**Current State:** Fully functional with all features operational. Running version 2.0.

**Last Updated:** October 31, 2025

## Recent Changes
- **October 31, 2025 (v2.0):** Major feature update
  - ✨ Added beautiful embed-based welcome and goodbye messages
  - 💾 Implemented JSON-based database for persistent server settings
  - 🎨 Added customizable welcome/goodbye messages with variable support
  - 🔧 Implemented slash commands: /help, /ping, /serverinfo, /userinfo, /config
  - 🛡️ Added comprehensive error handling throughout the codebase
  - 📁 Restructured code into modular files (bot.py, commands.py, events.py, database.py, utils.py, config.py)
  - 👋 Added goodbye messages when members leave
  - ⚙️ Added admin configuration command to customize bot behavior per server

- **October 31, 2025 (v1.0):** Initial project setup
  - Installed Python 3.11 and discord.py dependencies
  - Fixed code bug: Added proper `rules_channel` variable definition
  - Added message content intent
  - Created .gitignore for Python project
  - Configured workflow and deployment

## Project Structure
```
.
├── bot.py                  # Main bot file and initialization
├── commands.py             # Slash commands (help, ping, serverinfo, etc.)
├── events.py               # Event handlers (welcome, goodbye)
├── database.py             # JSON-based database manager
├── utils.py                # Utility functions for formatting and embeds
├── config.py               # Configuration constants
├── requirements.txt        # Python dependencies
├── server_settings.json    # Per-server settings storage (auto-generated)
├── .gitignore             # Git ignore file
├── README.md              # Basic project readme
└── replit.md              # This file - comprehensive documentation
```

## Features

### 🎉 Welcome Messages
- **Beautiful Embeds:** Welcome messages are displayed in attractive Discord embeds
- **Customizable Text:** Admins can customize the welcome message with variables
- **User Thumbnail:** Shows the new member's avatar
- **Member Count:** Displays the current member number
- **Rules Reference:** Automatically links to the rules channel if it exists
- **Toggle:** Can be enabled/disabled per server

**Supported Variables:**
- `{mention}` - Mentions the new member
- `{username}` or `{user}` - Member's username
- `{server}` or `{server_name}` - Server name
- `{member_count}` - Current member count

### 👋 Goodbye Messages
- **Leave Notifications:** Announces when members leave the server
- **Customizable:** Admins can customize goodbye messages
- **User Thumbnail:** Shows the departing member's avatar
- **Toggle:** Can be enabled/disabled per server

### 🤖 Slash Commands

#### `/help`
Shows all available commands with descriptions.

#### `/ping`
Checks the bot's response time and displays both API and WebSocket latency.

#### `/serverinfo`
Displays comprehensive server information:
- Server owner
- Server ID
- Creation date
- Member count
- Role count
- Channel count
- Server icon

#### `/userinfo [user]`
Shows detailed user information (defaults to command user):
- Username and ID
- Nickname
- Account creation date
- Server join date
- Number of roles
- User avatar

#### `/config <setting> <value>` (Admin Only)
Configure bot settings for your server:
- `welcome_channel` - Channel name for welcome/goodbye messages
- `rules_channel` - Rules channel name to reference
- `welcome_message` - Custom welcome message template
- `goodbye_message` - Custom goodbye message template
- `welcome_enabled` - Enable/disable welcome messages (true/false)
- `goodbye_enabled` - Enable/disable goodbye messages (true/false)

**Example:**
```
/config setting:welcome_message value:Welcome {mention}! You're member #{member_count}!
/config setting:welcome_enabled value:true
```

### 💾 Persistent Storage
- **Server-Specific Settings:** Each server has its own configuration
- **JSON Database:** Lightweight, file-based storage
- **Default Values:** New servers get sensible defaults automatically
- **Thread-Safe:** Safe concurrent access to settings

### 🛡️ Error Handling
- Graceful handling of missing channels
- Permission error catching
- Command error messages
- Logging for debugging
- User-friendly error messages

## Configuration

### Discord Bot Token
The bot requires a Discord bot token stored in the environment variable `TOKEN`.

**To get a Discord bot token:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select existing one
3. Go to the "Bot" section
4. Copy the bot token
5. Add it to Replit Secrets as `TOKEN`

**Required Intents (in Developer Portal):**
- ✅ **Server Members Intent** (for member join/leave events)
- ✅ **Message Content Intent** (for commands)

### Bot Permissions
When inviting the bot, grant these permissions:
- ✅ Read Messages/View Channels
- ✅ Send Messages
- ✅ Embed Links
- ✅ Mention Everyone
- ✅ Use Slash Commands

### Server Setup
1. **Create channels:**
   - `#welcome` - For welcome and goodbye messages (required)
   - `#rules` - For rules reference (optional)

2. **Invite the bot:**
   - Use OAuth2 URL Generator in Discord Developer Portal
   - Select `bot` and `applications.commands` scopes
   - Grant required permissions
   - Invite to your server

3. **Configure settings:**
   - Use `/config` command to customize messages and behavior
   - Messages support variables like `{mention}`, `{username}`, `{server}`, `{member_count}`

## Running the Bot

### Development
The bot runs automatically via the configured workflow:
- Connects to Discord using the TOKEN environment variable
- Loads all commands and event handlers
- Syncs slash commands with Discord
- Listens for member join/leave events
- Responds to slash commands

### Deployment
Configured for continuous VM deployment, perfect for a Discord bot that needs 24/7 uptime.

## Default Settings

When a server first uses the bot, these defaults are applied:

```json
{
  "welcome_channel": "welcome",
  "rules_channel": "rules",
  "welcome_enabled": true,
  "goodbye_enabled": true,
  "welcome_message": "Welcome to {server}, {mention}! 🎉\n\nWe're glad to have you here. You're member #{member_count}!",
  "goodbye_message": "{username} has left the server. We'll miss you! 👋",
  "embed_color": 0x00ff00
}
```

## Dependencies
- **discord.py 2.6.4+** - Python library for Discord API
- **Python 3.11** - Runtime environment

## Architecture

### Code Organization
The bot uses a modular architecture:
- **bot.py** - Main entry point, bot initialization, error handlers
- **commands.py** - Cog containing all slash commands
- **events.py** - Cog containing event handlers (join/leave)
- **database.py** - Database class for settings management
- **utils.py** - Utility functions for message formatting and embeds
- **config.py** - Configuration constants

### Intents
- Default intents
- Members intent (for join/leave events)
- Message content intent (for future features)

### Command System
- Uses Discord's modern slash command system
- Commands are registered via app_commands
- Auto-syncs on startup

### Event Handlers
- `on_ready` - Initialization and command syncing
- `on_member_join` - Welcome message handling
- `on_member_remove` - Goodbye message handling
- `on_command_error` - Error handling for text commands
- `on_app_command_error` - Error handling for slash commands

## Troubleshooting

### Bot won't connect
- Verify TOKEN is set in Replit Secrets
- Check token is valid in Discord Developer Portal
- Ensure you haven't regenerated the token

### Welcome/Goodbye messages not sending
- Verify `#welcome` channel exists
- Check bot has "Send Messages" and "Embed Links" permissions in that channel
- Use `/config` to check if welcome/goodbye is enabled
- Check console logs for error messages

### Slash commands not appearing
- Ensure bot was invited with `applications.commands` scope
- Wait a few minutes after bot startup for Discord to update
- Try re-inviting the bot with proper scopes
- Check logs for command sync errors

### Commands not working
- Verify Message Content Intent is enabled in Developer Portal
- Ensure Server Members Intent is enabled
- Check bot has necessary permissions in the server
- Use `/help` to see available commands

### Settings not saving
- Check file permissions on server_settings.json
- Look for errors in console logs
- Ensure bot has write access to the directory

## Logs and Debugging
The bot uses Python's logging system:
- **INFO** - Normal operations (joins, leaves, command usage)
- **WARNING** - Missing channels or configuration issues
- **ERROR** - Permission errors, failed operations

Check workflow logs in Replit for detailed debugging information.

## Version History
- **v2.0** (Oct 31, 2025) - Major feature update with embeds, commands, and database
- **v1.0** (Oct 31, 2025) - Initial release with basic welcome functionality

## Future Enhancement Ideas
- Verification system with buttons
- Auto-role assignment
- PostgreSQL database support
- Moderation commands
- Detailed logging dashboard
- Reaction roles
- Custom embed colors per server
- Welcome message preview command
