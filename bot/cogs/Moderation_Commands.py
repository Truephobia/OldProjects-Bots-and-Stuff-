import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class Moderation_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready.')

    @commands.command(hidden=True)
    @has_permissions(administrator=True)
    async def shutdown(self, ctx):
        await ctx.send(":robot: DBot is shutting down! :robot: ")
        await self.bot.close()

    @commands.command(brief=": kicks a user", description=": Do (kick @username reason) to kick a user from the server ")
    @has_permissions(manage_roles=True, kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        if reason == '':
            await ctx.send("You forgot to give a reason.")
        else:
            await ctx.send(f'Kicked {member.mention}')

    @kick.error
    async def kick_error(self, error, ctx):
        if isinstance(error, CheckFailure):
            await ctx.send('You lack permission to kick members')

    @commands.command(brief=": bans a user", description=": Do (ban @username reason) to ban a user from the server")
    @has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(brief=": unbans a user", description=": Do (unban username#1222) to unban a user from the server")
    @has_permissions(manage_roles=True, ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

    @commands.command(brief=": removes posts from the chat", description=": Removes a defined number of posts from the chat (purge x) where x is the number you want removed")
    @has_permissions(manage_roles=True, manage_channels=True)
    async def purge(self, ctx, amount=0):
        if amount == 0:
            await ctx.send("You must purge more then 0 messages")
        elif amount > 0:
            await ctx.channel.purge(limit=amount)

    @commands.command(brief=": mute a user", description=": Do (mute @username) to mute a user ")
    @has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send('please pass in a valid user')
            return
        else:
            role = discord.utils.get(ctx.guild.roles, name='muted')
            await member.add_roles(role)
            await ctx.send(f'{str(member)} was muted!')

    @commands.command(brief=": unmute a user", description=": Do (unmute @username) to unmute a user ")
    @has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send('please pass in a valid user to unmute')
            return
        else:
            await member.remove_roles(discord.utils.get(ctx.guild.roles, name="muted"))
            await ctx.send(f'{member.mention}has been unmuted')


def setup(bot):
    bot.add_cog(Moderation_Commands(bot))
