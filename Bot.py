import discord
from discord.ext import commands
#from Melads import *
client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready.")

@client.event
async def on_message(message):
    a=int(message)
    a=a*a
    message.channel.send(str(a))
    if message.author == client.user:
        return
    if message.content.startswith('Wake up professor'):
        await message.channel.send('THE PROFESSOR IS AWAKE')

client.run("DISCORD_API_KEY")
