import asyncio
import json
import random
from discord.ext import commands
import discord


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is ready.')

        with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\UserBalance.json", 'r') as g:
            self.userBalance = json.load(g)

        self.bot.loop.create_task(self.save_userbalance())

    async def save_userbalance(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\UserBalance.json", 'w') as g:
                json.dump(self.userBalance, g, indent=4)

            await asyncio.sleep(15)

    @commands.command()
    async def rpshelp(self, ctx):
        await ctx.send('Type rps (choice) to play Rock, Paper, Scissors against the bot win or lose $50 (Currency is currently broken so no actual winning or lossing money)')

    @commands.command()
    async def dicehelp(self, ctx):
        await ctx.send('Type dice # to throw a number of dice against the computer highest combined total wins $25 (Currency is currently broken so no actual winning or lossing money)')

    @commands.command()
    async def rps(self, ctx, message):
        await ctx.send('Rock, Paper, Scissors')
        computer = random.randint(0, 2)
        if computer == 0:
            computer = "rock"
        elif computer == 1:
            computer = "paper"
        elif computer == 2:
            computer = "scissors"
        player = message.lower()
        if player == computer:
            await ctx.send("Tie!")
        elif player == "rock":
            if computer == "paper":
                await ctx.send("Paper covers Rock.")
                await ctx.send("You lose!")
                # self.userBalance[author_id]['Balance'] -= 50
            else:
                await ctx.send("Scissors get crushed by Rock.")
                await ctx.send("You win !")
                # self.userBalance[author_id]['Balance'] += 50
        elif player == "paper":
            if computer == "scissors":
                await ctx.send("Scissors cut Paper.")
                await ctx.send("You lose!")
                # self.userBalance[author_id]['Balance'] -= 50
            else:
                await ctx.send("Rock gets covered by Paper.")
                await ctx.send("You win!")
                # self.userBalance[author_id]['Balance'] += 50
        elif player == "scissors":
            if computer == "rock":
                await ctx.send("Rock crushes Scissors.")
                await ctx.send("You lose!")
                # self.userBalance[author_id]['Balance'] -= 50
            else:
                await ctx.send("Paper gets cut by Scissors")
                await ctx.send("You win!")
                # self.userBalance[author_id]['Balance'] += 50
        else:
            await ctx.send("Check your spelling")

    @commands.command()
    async def dice(self, ctx, message):
        n = int(message)
        i = 0
        computer = []
        player = []
        playtotal = 0
        comptotal = 0
        await ctx.send("rolling " + str(n) + " dice")
        while i < n:
            comp = random.randint(1, 6)
            play = random.randint(1, 6)
            computer.append(comp)
            player.append(play)
            playtotal += play
            comptotal += comp
            i += 1
        if comptotal == playtotal:
            await ctx.send("You Rolled " + str(playtotal) + " Dice: ||" + str(player) + "|| Your Opponent Rolled  " + str(comptotal) + " Dice: ||" + str(computer) +"||")
            await ctx.send("Tie!")
        elif comptotal > playtotal:
            await ctx.send("You Rolled " + str(playtotal) + " Dice: ||" + str(player) + "|| Your Opponent Rolled  " + str(comptotal) + " Dice: ||" + str(computer) +"||")
            await ctx.send("You Lose!")
        elif comptotal < playtotal:
            await ctx.send("You Rolled " + str(playtotal) + " Dice: ||" + str(player) + "|| Your Opponent Rolled  " + str(comptotal) + " Dice: ||" + str(computer) +"||")
            await ctx.send("You Win!")
        else:
            await ctx.send("Make sure you have entered a valid number")



def setup(bot):
    bot.add_cog(Games(bot))
