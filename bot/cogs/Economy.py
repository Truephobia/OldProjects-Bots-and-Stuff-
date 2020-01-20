import asyncio
import discord
from discord.ext import commands
import json


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is ready.')

        with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\UserBalance.json", 'r') as f:
            self.userBalance = json.load(f)

            self.bot.loop.create_task(self.save_users())

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\UserBalance.json", 'w') as f:
                json.dump(self.userBalance, f, indent=4)

            await asyncio.sleep(15)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)

        if author_id not in self.userBalance:
            self.userBalance[author_id] = {}
            self.userBalance[author_id]['Balance'] = 1000

    @commands.command(brief=": Shows a users balance", description=": Do (balance @username) to look up another users balance")
    async def balance(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if member_id not in self.userBalance:
            await ctx.send("Member doesn't have a Balance")
        else:
            message = f'{member} is  Balance ' + str(self.userBalance[member_id]['Balance'])
            await ctx.send(message)


def setup(bot):
    bot.add_cog(Economy(bot))
