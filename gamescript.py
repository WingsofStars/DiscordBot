from http import client
import discord
import random
from dotenv import load_dotenv 
import os

isInGame = False

load_dotenv()
token = os.environ.get("TOKEN")
client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'
    .format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith('$game'):
        choices = ["rock","paper","scissors"]
        computer = random.choice(choices)
        player = None

        isInGame = True

        await message.channel.send("rock, paper, or scissors?: ")
        if message.content.startswith('!rock'):
            player="rock"
            print("player is rock")
        if message.content.startswith('!paper'):
            player="paper"
            print("player is paper")
        if message.content.startswith('!scissors'):
            player="scissors"
            print("player is scissors")

        if player == computer:
                await message.channel.send("computer: ",computer)
                await message.channel.send("player: ",player)
                await message.channel.send("Tie!")

        elif player == "rock":
            if computer == "paper":
                await message.channel.send("computer: ", computer)
                await message.channel.send("player: ", player)
                await message.channel.send("You lose!")
            if computer == "scissors":
                await message.channel.send("computer: ", computer)
                await message.channel.send("player: ", player)
                await message.channel.send("You win!")

        elif player == "scissors":
            if computer == "rock":
                await message.channel.send("computer: ", computer)
                await message.channel.send("player: ", player)
                await message.channel.send("You lose!")
            if computer == "paper":
                await message.channel.send("computer: ", computer)
                await message.channel.send("player: ", player)
                await message.channel.send("You win!")

        elif player == "paper":
            if computer == "scissors":
                await message.channel.send("computer: ", computer)
                await message.channel.send("player: ", player)
                await message.channel.send("You lose!")
            if computer == "rock":
                await message.channel.send("computer: ", computer)
                await message.channel.send("player: ", player)
                await message.channel.send("You win!")


        # while True:
        #     choices = ["rock","paper","scissors"]
        #     computer = random.choice(choices)
        #     player = None

        #     while player not in choices:

        #         # player = input("rock, paper, or scissors?: ").lower()

        #     if player == computer:
        #         print("computer: ",computer)
        #         print("player: ",player)
        #         print("Tie!")

        #     elif player == "rock":
        #         if computer == "paper":
        #             print("computer: ", computer)
        #             print("player: ", player)
        #             print("You lose!")
        #         if computer == "scissors":
        #             print("computer: ", computer)
        #             print("player: ", player)
        #             print("You win!")

        #     elif player == "scissors":
        #         if computer == "rock":
        #             print("computer: ", computer)
        #             print("player: ", player)
        #             print("You lose!")
        #         if computer == "paper":
        #             print("computer: ", computer)
        #             print("player: ", player)
        #             print("You win!")

        #     elif player == "paper":
        #         if computer == "scissors":
        #             print("computer: ", computer)
        #             print("player: ", player)
        #             print("You lose!")
        #         if computer == "rock":
        #             print("computer: ", computer)
        #             print("player: ", player)
        #             print("You win!")

        #     play_again = input("Play again? (yes/no): ").lower()

        #     if play_again != "yes":
        #         break

client.run(token)