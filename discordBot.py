# necessary for accesing API Keys/Tokens
import os
# Discord Client, allows us to connect to discord server
# As well as run our bot
import discord
# 
import openai
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')


openai.api_key = os.getenv('OPENAI_API_KEY')

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

client.run(DISCORD_TOKEN)

