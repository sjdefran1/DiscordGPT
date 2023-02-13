# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
OPENAI_TOKEN = os.getenv('OPENAI_API_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # brooklyn_99_quotes = [
    #     'I\'m the human form of the  emoji.',
    #     'Bingpot!',
    #     (
    #         'Cool. Cool cool cool cool cool cool cool, '
    #         'no doubt no doubt no doubt no doubt.'
    #     ),
    # ]

    # if message.content == '99!':
    #     response = random.choice(brooklyn_99_quotes)
    #     await message.channel.send(response)


    await message.channel.send(message.content)


client.run(DISCORD_TOKEN)

