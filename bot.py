import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print('Bot is Ready')


@client.command()
async def hello(ctx):
    await ctx.send("Hi")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0:3] == 'max':
        orig = message.content[31:36]
        min = message.content[18:23]
        max = message.content[6:11]
        uncertainty = ((float(max) - float(min)) / 2) / float(orig)
        await message.channel.send(f'{message.author} your uncertainty is {uncertainty}')


client.run("")
