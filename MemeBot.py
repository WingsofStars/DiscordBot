from distutils import command
from email import header, message
from fileinput import filename
import getpass
import math
from multiprocessing import connection
from re import template
import traceback
from turtle import title
from urllib import request, response
from numpy import imag
import requests
import discord
import random
import time
import pymysql.cursors
import urllib
import praw
from pytube import YouTube
import os
from discord.ext import commands
from discord.ext.commands import bot
import ffmpeg

imageURL = 'https://api.imgflip.com/get_memes'
captionURL = 'https://api.imgflip.com/caption_image'
TOKEN= 'OTQzMjY1NzI5NjA2NzIxNjY3.Ygwiqg.fNwEgbYGgHA77Bl8BBL6uK9UO5w'
client = discord.Client()
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'
bot = commands.Bot(command_prefix='!')

savedMemes = ['https://i.imgflip.com/65qhkz.jpg']

memeTerms = ['amogus', 'what are those!!!', 'Justin SUCKS']

taunts = ['Are you even cracked at Fortnite?', 'I actually like Joe Rogan', 'What? Evvvveeeerrrrrrr', 'Justin SUCKS']

vids = ["https://youtube.com/shorts/6JJb61rUSr0?feature=share", "https://youtube.com/shorts/IYfils4Vdqc?feature=share","https://youtube.com/shorts/HkGTdkjfKX0?feature=share","https://youtube.com/shorts/eSL7bxlVFKI?feature=share"]

beetleVids =["https://youtube.com/shorts/WrwizsruqFk?feature=share", "https://youtube.com/shorts/xun3qa09M5E?feature=share", "https://youtu.be/6F95B5Hpluc", "https://youtube.com/shorts/R00TdFwu1bA?feature=share", "https://youtube.com/shorts/eSL7bxlVFKI?feature=share", "https://youtube.com/shorts/yUpR6vhNfCE?feature=share" ]

redditMemes = []
videoIn = 0

connection = pymysql.connect(
    host='localhost', user='root', 
    password='test', database='discordbot',
    cursorclass=pymysql.cursors.DictCursor)

def DownloadResource(url, num):
    video = YouTube(url)
    #stream = video.streams.filter(file_extension='mp4')
    stream = video.streams.get_lowest_resolution()
    downloaded = stream.download()
    downloaded = os.rename(downloaded, f"Video{videoIn}.mp4")
    #compress_video(f"{downloaded}.mp4", 50 * 1000)
    num+= 1
    print("Completed Download")


def testConnection():
    testCommand= "SELECT Joke FROM jokedata"
    with connection.cursor() as cursor:
        cursor.execute(testCommand)
        result = cursor.fetchone()
        print("Inside the with statement")
        print(result)
    connection.commit()

def fetchFromReddit(num):
    reddit = praw.Reddit(client_id= "ObhD_U7a18iaZmuJOJUHiQ", client_secret="JjAdqGTayoWvcHj06qvEAaeJgsNOIQ", username="Psychological_Page89", password="Test1234", user_agent="pythonpraw")
    subReddits = ["memes", "funny", "wholesomememes","programmingmemes"]
    if num == 1:
        sub_reddit = reddit.subreddit(subReddits[0])
        top = sub_reddit.top(limit=5)
        for info in top:
            redditMemes.append(info)
        return redditMemes
    if num == 2:
        sub_reddit = reddit.subreddit(subReddits[1])
        top = sub_reddit.top(limit=5)
        for info in top:
            redditMemes.append(info)
        return redditMemes
    if num == 3:
        sub_reddit = reddit.subreddit(subReddits[2])
        top = sub_reddit.top(limit=5)
        for info in top:
            redditMemes.append(info)
        return redditMemes
    if num == 4:
        sub_reddit = reddit.subreddit(subReddits[3])
        top = sub_reddit.top(limit=5)
        for info in top:
            redditMemes.append(info)
        return redditMemes


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
    saveMemeToDB(image)
    return image

def saveMemeToDB(URL):
    insertCommand = "INSERT INTO `memedata` (`url`) VALUES (%s)"
    with connection.cursor() as cursor:
        cursor.execute(insertCommand,(URL))
        print("Executed insert with %s", URL)
    connection.commit()


#DownloadResource("https://www.youtube.com/watch?v=cdwal5Kw3Fc",videoIn)

def shuffleVid():
    data = random.choice(beetleVids)
    return data



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# @bot.command(pass_context=True)
# async def send(ctx):
#     await ctx.channel.send(r"C:\\Users\\jedominguez\\Documents\\GitHub\\DiscordBot\\Video0.zip", filename="Test", content="Testing")

@client.event
async def on_message(message):
    uno = ["uno reverse", "reverse", "Uno reverse"]
    bb = ["!beetlejuice", "!Beetlejuice", "beetlejuice", "BeetleJuice", "beetle juice", "Beetle juice"]
    
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
        await message.channel.send(f'Yeah {message.content}')
    
    if any(word in message.content for word in bb):
        data = random.choice(beetleVids)
        await message.channel.send(data)
    
    if message.content.startswith('r/memes'):
        data = fetchFromReddit(1)
        data = random.choice(data)
        EarthTitle = data.title
        EarthUrl = data.url
        EarthPorn = discord.Embed(title=EarthTitle)
        EarthPorn.set_image(url=EarthUrl)
        await message.channel.send(embed=EarthPorn)
    
    if message.content.startswith('r/funny'):
        data = fetchFromReddit(2)
        data = random.choice(data)
        FunnyTitle = data.title
        FunnyUrl = data.url
        Funny = discord.Embed(title=FunnyTitle)
        Funny.set_image(url=FunnyUrl)
        await message.channel.send(embed=Funny)
    
    if message.content.startswith('r/WholesomeMemes'):
        data = fetchFromReddit(3)
        data = random.choice(data)
        WHTitle = data.title
        WHUrl = data.url
        WH = discord.Embed(title=WHTitle)
        WH.set_image(url=WHUrl)
        await message.channel.send(embed=WH)


    if message.content.startswith('r/ProgrammingMemes'):
        data = fetchFromReddit(4)
        data = random.choice(data)
        PTitle = data.title
        PUrl = data.url
        P = discord.Embed(title=PTitle)
        P.set_image(url=PUrl)
        await message.channel.send(embed=P)
    
    if any(word in message.content for word in uno):
        await message.channel.send("https://tenor.com/view/reverse-card-uno-uno-cards-gif-13032597")



client.run(TOKEN)
