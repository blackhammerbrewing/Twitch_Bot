r"""
Execute the Twitch Bot.

python3 main.py
"""
from config import TMI_TOKEN, CLIENT_ID, BOT_NICK, BOT_PREFIX, CHANNEL
from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=TMI_TOKEN,
            client_id=CLIENT_ID,
            nick=BOT_NICK,
            prefix=BOT_PREFIX,
            initial_channels=CHANNEL
            )

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}', flush=True)
        ws = bot._ws
        await ws.send_privmsg(CHANNEL[0], f"/me has landed!")

    async def event_message(self, message):
        print(message.content, flush=True)
        await self.handle_commands(message)

    # Commands use a different decorator
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


if __name__ == "__main__":
    try:
        bot = Bot()
        bot.run()
    except KeyboardInterrupt as e:
        raise e
