import discord
from discord.ext import commands


class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    @commands.command(brief=": gets your ping", description=": Sends a ping to the discord bot and returns back a pong with the amount of time it took")
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency * 1000)}ms.')

    @commands.command(brief=": how to use the bots respond feature", description=": This uses the $command to let the bot send various messages back to the user")
    async def respond(self, ctx):
        await ctx.send('Type $help to see how to talk to the bot')


def setup(bot):
    bot.add_cog(Other(bot))
