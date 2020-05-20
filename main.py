r"""
Execute the Twitch Bot.

python3 main.py
"""
from configs.config import TMI_TOKEN, CLIENT_ID, BOT_NICK
from configs.config import BOT_PREFIX, CHANNEL, ALLOWED_MODS
from twitchio.ext import commands
from src.random import roll_int
from src.games import voting
from collections import Counter

class Bot(commands.Bot):

    def __init__(self):
        self._GAME_ON = False
        self._WINNERS = {}
        super().__init__(
            irc_token=TMI_TOKEN,
            client_id=CLIENT_ID,
            nick=BOT_NICK,
            prefix=BOT_PREFIX,
            initial_channels=CHANNEL,
            )

    async def event_ready(self):
        ws = bot._ws
        await ws.send_privmsg(CHANNEL[0], f"/me has landed!")

    async def event_message(self, ctx):
        if self._GAME_ON is True:
            self._WINNERS = voting(self._WINNERS, ctx.author.name, ctx.content)
            print(ctx.author.name, ctx.content, flush=True)
        await self.handle_commands(ctx)

    @commands.command(name='greet')
    async def greet(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='roll')
    async def roll(self, ctx):
        value = roll_int(ctx)
        if value is not None:
            await ctx.channel.send(f"{ctx.author.name} rolled a {value}")

    @commands.command(name='init')
    async def init(self, ctx):
        if ctx.author.name in ALLOWED_MODS:
            self._GAME_ON = True
            await ctx.channel.send(f"GAME ON: {self._GAME_ON}")

    @commands.command(name='end')
    async def end(self, ctx):
        if ctx.author.name in ALLOWED_MODS:
            value, count = Counter(self._WINNERS.values()).most_common(1)[0]
            await ctx.channel.send(f"BEST ANSWER: {value}")
            self._WINNERS = {}
            self._GAME_ON = False
            await ctx.channel.send(f"GAME ON: {self._GAME_ON}")


if __name__ == "__main__":
    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt as e:
        raise e
