import os
import discord
import requests
import json 

client = discord.Client()
def get_quote():
    headers = {'Accept': 'text/plain'}
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)
    return(response.text)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    if message.content.startswith('!Hello'):
        await message.channel.send('Hello World!')

    if message.content.startswith('!Joke'):
        quote = get_quote()
        await message.channel.send(quote)

client.run(os.getenv('jokesToken'))