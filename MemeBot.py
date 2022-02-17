from email import message
import getpass
from re import template
from urllib import request
import pydoc
import urllib
import requests
import os
import discord

imageURL = 'https://api.imgflip.com/get_memes'
captionURL = 'https://api.imgflip.com/caption_image'
TOKEN= 'OTQzMjY1NzI5NjA2NzIxNjY3.Ygwiqg.fNwEgbYGgHA77Bl8BBL6uK9UO5w'
client = discord.Client()
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 \
    Safari/537.36'

def getMemes():
    re = requests.get(imageURL)
    data = re.json()
    return data['data']['memes']

def setTheMeme(templateId, username, password, text0, text1):
    data = {
        'template_id': templateId,
        'username': username,
        'password': password,
        'text0': text0,
        'text1': text1
        }
    re = requests.post(captionURL, data=data)
    return re.json()
    
def saveTheMeme():
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', userAgent)
    filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')


@client.event
async def On_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def SendUserMeme(message):
    if message.author == client.user:
        return
    if message.content.startswith('!meme'):
        templateId = 29562797
        passoword = 'Password123'
        username1 = 'jesus641'
        text0 = 'Hello'
        text1 = 'MothaFUCKKAAA'
        image = setTheMeme(templateId,username1,passoword,text0,text1)
        await message.channel.send(image)
    
    print("We have logged in as {0.user}".format(client))


client.run(TOKEN)