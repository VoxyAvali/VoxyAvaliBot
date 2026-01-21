# VoxyAvaliBot
scuffed python-based twitch utility bot.


# Setup
1. download the newest version from releases and save it in a new folder.
2. run setup.exe and follow the instructions
3. go to your twitch chat and send "/mod voxyavalibot"
4. whenever you´re ready to stream, just run bot.exe. you should see a message from the bot in your chat.

note: the bot is set up to automatically shoutout raiders, but this functionality works based on the incoming raid response by streamelements. if streamelements isn´t set up with the default incoming raid response, then auto-shoutouts will not work.

note 2: the bot is set up to shut itself down upon receiving Sery_Bot´s raidout message. if Sery_Bot isn´t set up, you will have to shut down the bot manually after stream.

# How to add Commands
1. navigate to where you saved the bot
2. open commands.json with any text editor program
3. add your commands in the same format as the pre-made commands: "!command": "what the command does"
4. make sure to add a comma "," to the end of the second-to-last line, otherwise it will not work and error out.
5. save commands.json.
6. start the bot, or send 'reloadcommands' in the bot´s console window if it´s already running.

you can edit any commands at any time, even during stream. Just remember to reload the commands after changing anything.

# Console Commands
These commands can be used by the person using the bot, in the bot´s console window:
- say [message] - say something via the bot.
- reloadcommands - reload commands.json
- exit - disconnect and shut down the bot


# What is planned
- adding settings to enable/disable unique chatter logging and chat logging


# How the bot works (aka Technical Overview)
upon running setup.exe, 2 .json files are created, those being:
- settings.json, containing the channel name and the message the bot sends to chat upon startup.
- commands.json, containing all commands that the bot has special responses to. can be reloaded any time by sending "reloadcommands" in the bot window, wich calls the load_commands() function again.

when bot.exe is launched, it reads these files and connects to the channel set in settings.json. It then sends a message, also set in settings.json, to that same chat.
After that, the bot goes into listening mode, in which it logs all chat messages to its console. In case a message starts with a "!", it passes it along to the handle_command() function, which, as the name implies, handles the commands. It looks at the text after the "!" and responds with whatever is assigned to that command in commands.json.

The Auto-Shoutout and end-of-stream-autoshutdown work by listening for specific messages from specific users, in this case it´s the default incoming raid message by Streamelements for the shoutouts, and the default message that Sery_Bot sends when you raid out which tells users where the raid went for the auto-shutdown.

The bot doesn´t know, nor care, who is a moderator, who is a VIP, etc.. It doesn´t even know who the broadcaster is. In essence, all it does is listen to twitch chat and respond if needed. It only does what it is told via the .json files.
