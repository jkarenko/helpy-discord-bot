import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("/app/.env")
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
print(TOKEN)

NL = "\n"

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Logged on as", bot.user)

    print(f"Client {bot.user} is connected to servers:\n" + ",\n".join([guild.name for guild in bot.guilds]))


@bot.command("poll")
async def _poll(ctx, name, *options):
    message = f"New poll{NL}**{name}**"
    for i in range(len(options)):
        message += f"{NL}{chr(127462 + i)} {options[i]}"
    poll = await ctx.send(message)
    for i in range(len(options)):
        await poll.add_reaction(chr(127462 + i))


def main():
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
