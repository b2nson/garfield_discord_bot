import discord
from discord.ext import commands
import random

# Define your dictionary of quotes
quotes = {
    "quote1": "Life is short, eat the lasagna first.",
    "quote2": "I'm not lazy, I'm just on energy-saving mode.",
    "quote3": "Dieting is 'die' with a 't'."
    # Add more quotes as needed
}

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hi I'm Garfield.")

@client.command()
async def randomquote(ctx):
    # Select a random quote from the dictionary
    random_quote = random.choice(list(quotes.values()))
    await ctx.send(random_quote)

client.run('MTIyOTk4ODkzODE3ODEwNTM1NA.GSSGYt.FgUWgZnKSKyLPCqCl_JDlB0X6grIFvm5vmtXJk')
