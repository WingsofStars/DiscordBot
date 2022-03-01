from pickle import TRUE
from unittest import async_case
import discord
from discord.ext import commands
from config import *
import random


bot=commands.Bot(command_prefix=PREFIX,description='ROCK-PAPER-SCISSORS BOT')

@bot.event
async def on_ready():
    print("Game Bot has started")


@bot.command(pass_context=True)
async def start(ctx):
    await ctx.send("Rock,Paper, or Scissors?")
    await ctx.send("To enter choice use !shoot (Your Choice)")

@bot.command(pass_context=True)
async def shoot(ctx, uinput:str):
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = uinput.lower()

    if player == computer:
        # await ctx.send("computer: ",computer)
        # await ctx.send("player: ",player)
        await ctx.send("Tie!")
        await ctx.send("Computer: "+computer+"\nPlayer: "+player)

    elif player == "rock":
        if computer == "paper":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You lose!")
            await ctx.send("Computer: "+computer+"\nPlayer: "+player)
        if computer == "scissors":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You win!")
            await ctx.send("Computer: "+computer+"\nPlayer: "+player)

    elif player == "scissors":
        if computer == "rock":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You lose!")
            await ctx.send("Computer: "+computer+"\nPlayer: "+player)
        if computer == "paper":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You win!")
            await ctx.send("Computer: "+computer+"\nPlayer: "+player)

    elif player == "paper":
        if computer == "scissors":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You lose!")
            await ctx.send("Computer: "+computer+"\nPlayer: "+player)
        if computer == "rock":
            # await ctx.send("computer: ", computer)
            # await ctx.send("player: ", player)
            await ctx.send("You win!")
            await ctx.send("Computer: "+computer+"\nPlayer: "+player)



bot.run(TOKEN,bot=True,reconnect=True)