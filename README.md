# Twitch_Bot
Open Source Twitch Bot for community driven events developed for Black Hammer
Brewing in San Francisco, CA. 

The bot works by connecting to a live twitch chat and responding to user input.
This allows the community to interact with the stream and the streamers to
interact with the community in a seemless way.

# Use
Use !set_mode 'voting' to enter the voting mode then use !init to start the game.
To end the game and have the bot respond requires using the !end function.

# Config File
All private information is stored in a file called config.py. This is a private file in a folder called configs. This stores OAuth and ClientID information.

Example configs/config.py
```python
TMI_TOKEN = "oauth:sometokenhere"
CLIENT_ID = "yourclientidhere"
BOT_NICK = "accountnamehere"
BOT_PREFIX = "!"
CHANNEL = ["channelnamehere"]
ALLOWED_MODS = ["allowed", "users", "to", "interact"]
ALLOWED_GAMES = ["none", "voting", "trivia"]
```
Author: Michael Parkinson 2020
