import time
import json

user = "{user}"
def channelSetup():    
    print("note: all of this can be changed any time via the generated .json files.")
    channel = input("Please enter your Twitch channel name: ").strip()
    try:
        with open("settings.json", "r") as settingsfile:
            settings = json.load(settingsfile)
    except FileNotFoundError:
        settings = {
            "Channel": "placeholderChannelName",
            "BotOnlineMessage": "VoHiYo"
            }
    settings["Channel"] = channel
    with open("settings.json", "w") as settingsfile:
        json.dump(settings, settingsfile, indent=2)

def botGreetSetup():
    botGreetMessage = input("What should the bot say upon startup? Default is VoHiYo. : ")
    with open("settings.json", "r") as settingsfile:
        settings = json.load(settingsfile)
    settings["BotOnlineMessage"] = botGreetMessage
    with open("settings.json", "w") as settingsfile:
        json.dump(settings, settingsfile, indent=2)

def dcSetup():
    discord_link = input("Please enter your Discord invite link: ").strip()
    try:
        with open("commands.json", "r") as commandsfile:
            commands = json.load(commandsfile)
    except FileNotFoundError:
        commands = {
            "!hello": "Hello, {user}!",
            "!discord": "if you see this then something did not work.",
            "!lurk": "{user} is lurking.",
            "!unlurk": "{user} has returned from their lurking."
            }
    commands["!discord"] = f"@{user} Join the discord here: {discord_link}"
    with open("commands.json", "w") as commandsfile:
        json.dump(commands, commandsfile, indent=2)

if __name__ == "__main__":
    channelSetup()
    dcSetup()
    botGreetSetup()
    print(f"Setup complete!")
    print("now exiting...")
    time.sleep(2)
