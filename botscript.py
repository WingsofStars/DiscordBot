import time
import discord
import os
import re
from dotenv import load_dotenv  # pip install python-dotenv
import pyodbc
import pandas as pd


load_dotenv()
token = os.environ.get('TOKEN')
client = discord.Client()


spambotNameList = ["Botbot", "botbot",
                   "Bot Bot", "bot bot", "bot Bot", "Bot bot"]
hellolist = ["/Hello"]
GreetingsList = ["hi ", "Hi ", "HI ", "YO ", "yo ",
                 "Yo ", "Sup ", "Hello ", "hello ", "sup ", "hey ", "Hey ", "HEY "]
spamCommandList = ["/spam", "/Spam", "/SPAM"]

for names in spambotNameList:
    for greetings in GreetingsList:
        hellolist.append(greetings + names)


@client.event
async def on_ready():
    print("WE HAVE LOGGED IN AS {0.user}".format(client))




@client.event
async def on_message(mess):
    if mess.author == client.user:
        return

    if mess.content.startswith(tuple(hellolist)):
        print(mess)
        await mess.channel.send("Hello there {0.author.name} >.<".format(mess))

    if mess.content.lower().startswith("/spam"):
        for i in range(100):
            pattern = '/spam(.*)'
            word = re.findall(pattern, mess.content, re.IGNORECASE)
            await mess.channel.send(word[0])
            time.sleep(0.75)
        await mess.channel.send("Made with Memes in mind")
    # if mess.content.startswith("/SpamBot -shutdown -4351"):
    #     await mess.channel.send("Shutting Down")
    #     client.close(token)

client.run(token)

