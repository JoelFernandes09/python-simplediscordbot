import random
import discord

TOKEN = ''  # Enter your Discord Server Token here

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'text':
        await message.channel.send('You just typed "text"')

    if message.content == 'secret':
        await message.author.send('I see you know the secret eh?')

client.run(TOKEN)
