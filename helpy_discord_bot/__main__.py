import discord
import os
from discord.ext import commands
from dotenv import load_dotenv


class HelpyHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)


load_dotenv("/app/.env")
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()

NL = "\n"

bot = commands.Bot(command_prefix="!", intents=intents)
bot.help_command = HelpyHelp()


@bot.event
async def on_ready():
    print("Logged on as", bot.user)
    print(f"Client {bot.user} is connected to servers:\n" + ",\n".join([guild.name for guild in bot.guilds]))


@bot.command(name="helpy-help", brief="Helpy's help", help="Helpy's help")
async def _help(ctx):
    message = f"**Helpy's commands:**{NL}"
    for command in bot.commands:
        message += f"**!{command.name}** - {command.brief}{NL}"
    await ctx.send(message)


@bot.command(name="helpy-poll", brief="Create a poll", help="Create a poll with a name and options")
async def _poll(ctx, name, *options):
    message = f"New poll{NL}**{name}**"
    for i in range(len(options)):
        message += f"{NL}{chr(127462 + i)} {options[i]}"
    poll = await ctx.send(message)
    for i in range(len(options)):
        await poll.add_reaction(chr(127462 + i))


@bot.command(name="helpy-hello", brief="Say Hello", help="Helpy politely greets you")
async def _hello(ctx):
    message = f"Hello {ctx.author.name}!"
    await ctx.send(message)


@bot.command(name="helpy-current-time", brief="Tell the current time", help="Helpy tells you the current time")
async def _current_time(ctx):
    import datetime
    now = datetime.datetime.now()
    message = f"The current time is {now.hour:02d}:{now.minute:02d}"
    await ctx.send(message)


def main():
    bot.run(TOKEN)
