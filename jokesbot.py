import imp
import os
import discord
import requests
import json 


jokesToken = 'OTQxNTc2NTQ4NTI2NDg1NjI0.YgX9fg.KCcbMm5938evesD0aRQR9_kA_qg'
client = discord.Client()
def get_quote():
    headers = {'Accept': 'text/plain'}
    response = requests.get("https://icanhazdadjoke.com/", headers=headers)

# json_data = json.loads(response.text)
# quote = json_data[0]['q'] + " -" + json_data[0]['a']

    return(response.text)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    if message.content.lower().startswith('!hello'):
        await message.channel.send('Hello World!')

    if message.content.lower().startswith('!dadjoke'):
        quote = get_quote()
        await message.channel.send(quote) 

    if message.content.lower().startswith('!projoke'):
        response = requests.get('https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt')
        await message.channel.send(response.text)

    if message.content.lower().startswith('!punny'):
        response = requests.get('https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt')
        await message.channel.send(response.text)

    if message.content.lower().startswith('!spooky'):
        response = requests.get('https://v2.jokeapi.dev/joke/Spooky?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&format=txt')
        await message.channel.send(response.text)

client.run(jokesToken)