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
                 "Yo ", "Sup ", "Hello ", "hello ", "sup "]
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

    if mess.content.startswith("/spam"):
        for i in range(100):
            pattern = '/spam(.*)'
            word = re.findall(pattern, mess.content)
            await mess.channel.send(word[0])
            time.sleep(0.75)
        await mess.channel.send("Made with Memesin mind")
    # if mess.content.startswith("/SpamBot -shutdown -4351"):
    #     await mess.channel.send("Shutting Down")
    #     client.close(token)

    if mess.content.startswith("/add to list"):
        pattern = '/add to list(.*)'
        await mess.channel.send("This might take a moment")
        message = re.findall(pattern, mess.content)
        connection = pyodbc.connect('Driver={SQL Server};'
            'Server=LAPTOP-NE5IT73K;'
            'Database=ReasonsWhy;'
            'Trusted_Connection=yes;')

        cursor = connection.cursor()
        cursor.execute("INSERT INTO reasons(Reason) VALUES('"+ message[0] +"')")
        await mess.channel.send("Reason has been added to the list")
        cursor.close()
        connection.close()

    if mess.content.startswith("/list why"):
        pattern = '/list why(.*)'
        print(mess)
        reasonnumber = re.findall(pattern, mess.content)
        # if len(reasonnumber) == 0:
        print("test")
        connection = pyodbc.connect('Driver={SQL Server};'
            'Server=LAPTOP-NE5IT73K;'
            'Database=ReasonsWhy;'
            'Trusted_Connection=yes;')

        cursor = connection.cursor()
        cursor.execute("Select Reason from reasons")
        for i in cursor:
            await mess.channel.send(i)
        cursor.close()
        connection.close()
        await mess.channel.send("That's why I'll always love Lonny")
client.run(token)

