from email import header, message
from fileinput import filename
import getpass
from multiprocessing import connection
from re import template
import traceback
from urllib import request, response
import requests
import discord
import random
import time
import pymysql.cursors
import urllib

imageURL = 'https://api.imgflip.com/get_memes'
captionURL = 'https://api.imgflip.com/caption_image'
TOKEN= 'OTQzMjY1NzI5NjA2NzIxNjY3.Ygwiqg.fNwEgbYGgHA77Bl8BBL6uK9UO5w'
client = discord.Client()
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'

savedMemes = ['https://i.imgflip.com/65qhkz.jpg']
memeTerms = ['amogus', 'what are those!!!', 'Justin SUCKS']
taunts = ['Are you even cracked at Fortnite?', 'I actually like Joe Rogan', 'What? Evvvveeeerrrrrrr', 'Justin SUCKS', 'Dick Rider in Chat']

connection = pymysql.connect(
    host='localhost', user='root', 
    password='test', database='discordbot',
    cursorclass=pymysql.cursors.DictCursor)

def testConnection():
    testCommand= "SELECT Joke FROM jokedata"
    with connection.cursor() as cursor:
        cursor.execute(testCommand)
        result = cursor.fetchone()
        print("Inside the with statement")
        print(result)
    connection.commit()



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

def saveMemeToDB(URL):
    insertCommand = "INSERT INTO `memedata` (`url`) VALUES (%s)"
    with connection.cursor() as cursor:
        cursor.execute(insertCommand,(URL))
        print("Executed insert with %s", URL)
    connection.commit()

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
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$SM'):
        for i in savedMemes:
            await message.channel.send(i)
            time.sleep(0.85)
    if message.content.startswith('$taunt'):
        random.shuffle(taunts)
        await message.channel.send(taunts[0])
    if any(word in message.content for word in memeTerms):
        await message.send(random.choice('Yeah' + memeTerms))


print(savedMemes)
print("--------------")

testConnection()

#client.run(TOKEN)