from distutils import command
from email import header, message
from fileinput import filename
import getpass
import math
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

taunts = ['Are you even cracked at Fortnite?', 'I actually like Joe Rogan', 'What? Evvvveeeerrrrrrr', 'Justin SUCKS', 'Dick Rider in Chat']

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
    compress_video(f"{downloaded}.mp4", 50 * 1000)
    num+= 1
    print("Completed Download")


def compress_video(video_full_path, size_upper_bound, two_pass=True, filename_suffix='1'):
    """
    Compress video file to max-supported size.
    :param video_full_path: the video you want to compress.
    :param size_upper_bound: Max video size in KB.
    :param two_pass: Set to True to enable two-pass calculation.
    :param filename_suffix: Add a suffix for new video.
    :return: out_put_name or error
    """
    filename, extension = os.path.splitext(video_full_path)
    extension = '.mp4'
    output_file_name = filename + filename_suffix + extension

    total_bitrate_lower_bound = 11000
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000
    min_video_bitrate = 100000

    try:
        # Bitrate reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
        probe = ffmpeg.probe(video_full_path)
        # Video duration, in s.
        duration = float(probe['format']['duration'])
        # Audio bitrate, in bps.
        audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
        # Target total bitrate, in bps.
        target_total_bitrate = (size_upper_bound * 1024 * 8) / (1.073741824 * duration)
        if target_total_bitrate < total_bitrate_lower_bound:
            print('Bitrate is extremely low! Stop compress!')
            return False

        # Best min size, in kB.
        best_min_size = (min_audio_bitrate + min_video_bitrate) * (1.073741824 * duration) / (8 * 1024)
        if size_upper_bound < best_min_size:
            print('Quality not good! Recommended minimum size:', '{:,}'.format(int(best_min_size)), 'KB.')
            # return False

        # Target audio bitrate, in bps.
        audio_bitrate = audio_bitrate

        # target audio bitrate, in bps
        if 10 * audio_bitrate > target_total_bitrate:
            audio_bitrate = target_total_bitrate / 10
            if audio_bitrate < min_audio_bitrate < target_total_bitrate:
                audio_bitrate = min_audio_bitrate
            elif audio_bitrate > max_audio_bitrate:
                audio_bitrate = max_audio_bitrate

        # Target video bitrate, in bps.
        video_bitrate = target_total_bitrate - audio_bitrate
        if video_bitrate < 1000:
            print('Bitrate {} is extremely low! Stop compress.'.format(video_bitrate))
            return False

        i = ffmpeg.input(video_full_path)
        if two_pass:
            ffmpeg.output(i, '/dev/null' if os.path.exists('/dev/null') else 'NUL',
                          **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                        ).overwrite_output().run()
            ffmpeg.output(i, output_file_name,
                          **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                        ).overwrite_output().run()
        else:
            ffmpeg.output(i, output_file_name,
                          **{'c:v': 'libx264', 'b:v': video_bitrate, 'c:a': 'aac', 'b:a': audio_bitrate}
                        ).overwrite_output().run()

        if os.path.getsize(output_file_name) <= size_upper_bound * 1024:
            return output_file_name
        elif os.path.getsize(output_file_name) < os.path.getsize(video_full_path):  # Do it again
            return compress_video(output_file_name, size_upper_bound)
        else:
            return False
    except FileNotFoundError as e:
        print('You do not have ffmpeg installed!', e)
        print('You can install ffmpeg by reading https://github.com/kkroening/ffmpeg-python/issues/251')
        return False



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
    subReddits = ["EarthPorn", "funny", "wholesomememes"]
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


DownloadResource("https://www.youtube.com/watch?v=cdwal5Kw3Fc",videoIn)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@bot.command(pass_context=True)
async def send(ctx):
    await ctx.channel.send(r"C:\\Users\\jedominguez\\Documents\\GitHub\\DiscordBot\\Video0.zip", filename="Test", content="Testing")

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
        await message.channel.send(random.choice('Yeah' + memeTerms))
    
    if message.content.startswith('!hello'):
        embedVar = discord.Embed(title="YouTube video player", description="Frugal Aset", color=0x00ff00)
        embedVar.add_field(name="URL", value="https://www.youtube.com/embed/aYaSgEB0JA0", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)
    
    if message.content.startswith('r/EarthPorn'):
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


client.run(TOKEN)
