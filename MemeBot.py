from email import message
import getpass
from re import template
import traceback
from urllib import request
import requests
import discord
import random
import time

imageURL = 'https://api.imgflip.com/get_memes'
captionURL = 'https://api.imgflip.com/caption_image'
TOKEN= 'OTQzMjY1NzI5NjA2NzIxNjY3.Ygwiqg.fNwEgbYGgHA77Bl8BBL6uK9UO5w'
client = discord.Client()
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 \
    Safari/537.36'

savedMemes = ['https://i.imgflip.com/65qhkz.jpg']
memeTerms = ['amogus', 'what are those!!!', 'Justin SUCKS']
taunts = ['Are you even cracked a Fortnite?', 'I actually like Joe Rogan', 'What? Evvvveeeerrrrrrr', 'Justin SUCKS', 'Dick Rider in Chat']

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

def getRandomIds():
    tempIdArry = []
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'id':image['id']} for image in data]
    for i in images:
        tempIdArry.append(i['id'])
    
    tempIdArry.pop()
    random.shuffle(tempIdArry)
    tempIdArry.pop()
    return tempIdArry

def generateMeme(text00,text01):
    id = getRandomIds()
    templateId = id[0]
    passoword = 'Password123'
    username1 = 'jesus641'
    text0 = text00
    text1 = text01
    image = setTheMeme(templateId,username1,passoword,text0,text1)
    return image

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def SendUserMeme(message, txt1 , txt2):
    if message.author == client.user:
        return
    if message.content.startswith('$meme'):
        meme = generateMeme(txt1, txt2)
        memer = meme['data']['url']
        print(memer)
        savedMemes.append(memer)
        await message.channel.send(memer)

@client.event
async def showMeTheSaveMemes(message):
    if message.author == client.user:
        return
    if message.content.startswith('$SavedMemes'):
        for i in savedMemes:
            await message.channel.send(i)
            time.sleep(0.85)

@client.event
async def tauntUser(message):
    if message.author == client.user:
        return
    if message.content.startswith('$taunt'):
        random.shuffle(taunts)
        await message.channel.send(taunts[0])


@client.event
async def backMeUp(message):
    if message.author == client.user:
        return
    msg = message.content
    if any(word in msg for word in memeTerms):
        await message.send(random.choice(memeTerms))



print(savedMemes)
print("--------------")

client.run(TOKEN)