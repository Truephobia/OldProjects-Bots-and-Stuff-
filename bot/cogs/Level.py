from datetime import time

import discord
from discord.ext import commands
import json
import asyncio


class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is ready.')

        with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\Users.json", 'r') as f:
            self.users = json.load(f)

        self.bot.loop.create_task(self.save_users())

        with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\UserBalance.json", 'r') as g:
            self.userBalance = json.load(g)

            self.bot.loop.create_task(self.save_userbalance())

    async def save_users(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\Users.json", 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(15)

    async def save_userbalance(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"C:\Users\Admin\PycharmProjects\bot\cogs\UserBalance.json", 'w') as g:
                json.dump(self.userBalance, g, indent=4)

            await asyncio.sleep(15)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']
        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]['level'] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return

        author_id = str(message.author.id)
        if author_id not in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0

        self.users[author_id]['exp'] += 1

        if self.lvl_up(author_id):
            await message.channel.send(f"{message.author.mention} is now level {self.users[author_id]['level']}")

    @commands.command(brief=": shows users current level", description=": Do (level @username) to see a specific users level")
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if member_id not in self.users:
            await ctx.send("Member doesn't have a level")
        else:
            message = f'{member} is level ' + str(self.users[member_id]['level'])
            await ctx.send(message)


def setup(bot):
    bot.add_cog(Level(bot))
