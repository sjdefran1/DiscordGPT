# necessary for accesing API Keys/Tokens
import os
# Discord Client, allows us to connect to discord server
# As well as run our bot
import discord
# GPT
import openai
# Allows us to use .env
from dotenv import load_dotenv

# load our enviroment vars from .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up permissions for our bot
intents = discord.Intents.default()
intents.message_content = True

# Connect Bot to discord
client = discord.Client(intents=intents)

# Basic example of handling events
# When a user join's the server our bot will print
# {User} has joined server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# Handles Messages
# Allows us to use /GPT command and query ChatGPT
# Then send the response from GPT back to the discord server
@client.event
async def on_message(message):
    # Stop our bot from recursively responding to itself
    if message.author == client.user:
        return
    
    # GPT COMMAND
    if message.content[0:4] == '/GPT':   
        #save message sent from discord as prompt
        prompt = message.content.split('/GPT ')[1]

        # query gpt 
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt= prompt,
            temperature=0.5,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        await message.channel.send(response['choices'][0]['text'])

# Run the Bot
client.run(DISCORD_TOKEN)

