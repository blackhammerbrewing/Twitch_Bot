r"""
Execute the Twitch Bot.

python3 main.py
"""
from configs.config import TMI_TOKEN, CLIENT_ID, BOT_NICK
from configs.config import BOT_PREFIX, CHANNEL, ALLOWED_MODS, ALLOWED_GAMES
from twitchio.ext import commands
from src.random import roll_int
from src.games import voting
from collections import Counter


class Bot(commands.Bot):

    def __init__(self):
        self._GAME_ON = False
        self._GAME_TYPE = ALLOWED_GAMES[0]
        self._WINNERS = {}
        super().__init__(
            irc_token=TMI_TOKEN,
            client_id=CLIENT_ID,
            nick=BOT_NICK,
            prefix=BOT_PREFIX,
            initial_channels=CHANNEL,
            )

    async def event_ready(self):
        """
        Bot ready function. Sends a private message to the channel indicating
        the bot has succesfully landed in the chat.
        """
        ws = bot._ws
        await ws.send_privmsg(CHANNEL[0], f"/me has landed!")

    async def event_message(self, ctx):
        """
        Bot message function. Looks for a command in chat and handles the game
        on mode for user interaction. This is the entry point for community
        driven events.
        """
        if self._GAME_ON is True:
            if self._GAME_TYPE == ALLOWED_GAMES[1]:
                self._WINNERS = voting(
                    self._WINNERS,
                    ctx.author.name,
                    ctx.content
                    )
            else:
                pass
        await self.handle_commands(ctx)

    @commands.command(name='greet')
    async def greet(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='roll')
    async def roll(self, ctx):
        value = roll_int(ctx)
        if value is not None:
            await ctx.channel.send(f"{ctx.author.name} rolled a {value}")

    @commands.command(name='list_modes')
    async def list_modes(self, ctx):
        string = ""
        if ctx.author.name in ALLOWED_MODS:
            for game in ALLOWED_GAMES:
                game_len = len(game)
                string += game
                for i in range(9-game_len):
                    string += "-"
                string += " "
            await ctx.channel.send(str(string))

    @commands.command(name='set_mode')
    async def set_mode(self, ctx):
        if ctx.author.name in ALLOWED_MODS:
            content = ctx.content.split(' ')
            game_mode = content[1]
            if game_mode in ALLOWED_GAMES:
                await ctx.channel.send(f"GAME: {game_mode} is OK")
                self._GAME_TYPE = game_mode

    @commands.command(name='init')
    async def init(self, ctx):
        if ctx.author.name in ALLOWED_MODS:
            self._GAME_ON = True
            await ctx.channel.send(f"GAME ON: {self._GAME_ON}")

    @commands.command(name='end')
    async def end(self, ctx):
        if ctx.author.name in ALLOWED_MODS:
            if self._GAME_TYPE is ALLOWED_GAMES[1]:
                votes = self._WINNERS.values()
                value, count = Counter(votes).most_common(1)[0]
                await ctx.channel.send(f"ANSWER: {value} with {count} votes")
                self._WINNERS = {}
            self._GAME_ON = False
            await ctx.channel.send(f"GAME ON: {self._GAME_ON}")


if __name__ == "__main__":
    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt:
        pass
