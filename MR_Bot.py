# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())


# on_ready() handles the event that the Client has made a connection to Discord and prepared its response data.
@client.event
async def on_ready():
    # outputs all server names connected to bot

    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    print(member.name)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == 'general':
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hey {username}, how are you doing?')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}, have a great day!')
        elif user_message.lower() == 'im good':
            await message.channel.send(f" that's good {username}, glad to hear that!")


# client.run_until_complete(asyncio.sleep(0))
client.run(TOKEN)
