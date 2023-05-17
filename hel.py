import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
load_dotenv()

class HelpyClient(discord.Client):

    def __init__(self, **kwargs):
        super().__init__(**kwargs, intents=intents)

    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content:
            await message.channel.send("Hello, World!")


client = HelpyClient()
client.run(os.environ.get("DISCORD_TOKEN"))
