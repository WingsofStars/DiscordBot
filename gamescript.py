from pickle import TRUE
from unittest import async_case
import discord
from discord.ext import commands
from config import *
import random
import giphy_client
from giphy_client.rest import ApiException


bot=commands.Bot(command_prefix=PREFIX,description='ROCK-PAPER-SCISSORS BOT')

@bot.event
async def on_ready():
    print("Game Bot has started")


@bot.command(pass_context=True)
async def start(ctx):
    await ctx.send("Rock,Paper, or Scissors?")
    await ctx.send("To enter choice use !shoot (Your Choice)")

@bot.command(pass_context=True)
async def gif(ctx,*,q="Tie"):
    api_key='TUGOCGmdycOCIMR7h5sXX7IFBLPvOSd7'
    api_instance=giphy_client.DefaultApi()

    try:
        api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
        lst=list(api_response.data)
        giff=random.choice(lst)

        await ctx.channel.send(giff.embed_url)

    except ApiException as e:
        print("Exceptio when Giffing")

@bot.command(pass_context=True)
async def shoot(ctx, uinput:str):
    api_key='TUGOCGmdycOCIMR7h5sXX7IFBLPvOSd7'
    api_instance=giphy_client.DefaultApi()
    q=""

    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = uinput.lower()

    if player == computer:
        # await ctx.send("computer: ",computer)
        # await ctx.send("player: ",player)
        await ctx.send("Tie!\nComputer: "+computer+"\nPlayer: "+player)
        q="Tie"
        try:
            api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
            lst=list(api_response.data)
            giff=random.choice(lst)

            await ctx.channel.send(giff.embed_url)

        except ApiException as e:
            print("Exceptio when Giffing")

    elif player == "rock":
        if computer == "paper":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You lose!\nComputer: "+computer+"\nPlayer: "+player)
            q="Loser"
            try:
                api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
                lst=list(api_response.data)
                giff=random.choice(lst)

                await ctx.channel.send(giff.embed_url)

            except ApiException as e:
                print("Exceptio when Giffing")
        if computer == "scissors":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You win!\nComputer: "+computer+"\nPlayer: "+player)
            q="Winner"
            try:
                api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
                lst=list(api_response.data)
                giff=random.choice(lst)

                await ctx.channel.send(giff.embed_url)

            except ApiException as e:
                print("Exceptio when Giffing")

    elif player == "scissors":
        if computer == "rock":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You lose!\nComputer: "+computer+"\nPlayer: "+player)
            q="Loser"
            try:
                api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
                lst=list(api_response.data)
                giff=random.choice(lst)

                await ctx.channel.send(giff.embed_url)

            except ApiException as e:
                print("Exceptio when Giffing")
        if computer == "paper":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You win!\nComputer: "+computer+"\nPlayer: "+player)
            q="Winner"
            try:
                api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
                lst=list(api_response.data)
                giff=random.choice(lst)

                await ctx.channel.send(giff.embed_url)

            except ApiException as e:
                print("Exceptio when Giffing")

    elif player == "paper":
        if computer == "scissors":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You lose!\nComputer: "+computer+"\nPlayer: "+player)
            q="Loser"
            try:
                api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
                lst=list(api_response.data)
                giff=random.choice(lst)

                await ctx.channel.send(giff.embed_url)

            except ApiException as e:
                print("Exceptio when Giffing")
        if computer == "rock":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You win!\nComputer: "+computer+"\nPlayer: "+player)
            q="Winner"
            try:
                api_response=api_instance.gifs_search_get(api_key,q,limit=5,rating='r')
                lst=list(api_response.data)
                giff=random.choice(lst)

                await ctx.channel.send(giff.embed_url)

            except ApiException as e:
                print("Exceptio when Giffing")



bot.run(TOKEN,bot=True,reconnect=True)