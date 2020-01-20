import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import has_permissions
bot = commands.Bot(command_prefix='.')


@bot.command(brief=": Admin command used to load plug-ins")
@has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print('load successful')


@bot.command(brief=": Admin command used to unload plug-ins")
@has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print('unload successful')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_member_join(member):
    print('(member) has joined the server')


@bot.event
async def on_member_remove(member):
    print('(member) has left the server')


@bot.event
async def on_message(message):
    if message.content.startswith('$hello'):
        response = random.randint(1, 5)
        if response == 1:
            await message.channel.send('Hello {0.author.mention}'.format(message))
        if response == 2:
            await message.channel.send('Hey {0.author.mention}'.format(message))
        if response == 3:
            await message.channel.send('Good day Fine Sir'.format(message))
        if response == 4:
            await message.channel.send('nǐ hǎo {0.author.mention}'.format(message))
        if response == 5:
            await message.channel.send('zzzz.... OH Hello there {0.author.mention}'.format(message))

    if message.content.startswith('$goodbye'):
        response = random.randint(1, 5)
        if response == 1:
            await message.channel.send('Goodbye {0.author.mention}'.format(message))
        if response == 2:
            await message.channel.send('Farewell {0.author.mention}'.format(message))
        if response == 3:
            await message.channel.send('You will be missed {0.author.mention}'.format(message))
        if response == 4:
            await message.channel.send('Have a nice day {0.author.mention}'.format(message))
        if response == 5:
            await message.channel.send('zài jiàn {0.author.mention}'.format(message))

    if message.content.startswith('$joke'):
        response = random.randint(1, 5)
        if response == 1:
            await message.channel.send('Why was the bot always angry?')
            await message.channel.send('Because someone kept pushing his buttons!')
        if response == 2:
            await message.channel.send('What is a bots favourite type of music?')
            await message.channel.send('Heavy Metal!')
        if response == 3:
            await message.channel.send('You could say I\'m nuts for these bad robot jokes get it?')
        if response == 4:
            await message.channel.send('Want to hear a joke?')
            await message.channel.send('Judgement day meat bag!')
        if response == 5:
            await message.channel.send('What do robots like to eat as a snack?')
            await message.channel.send('Microchips!')

    if message.content.startswith('$help'):
        await message.channel.send(
            'You can talk to me by saying $hello, $goodbye, $joke, $catimage, $dogimage, $failimage')

    if message.content.startswith('$catimage'):
        Image = random.randint(1, 32)
        if Image == 1:
            await message.channel.send("You rolled a 1.")
            await message.channel.send("https://i.imgur.com/1Kw7E6N.gifv")
        if Image == 2:
            await message.channel.send("You rolled a 2.")
            await message.channel.send("https://imgur.com/gallery/Xn4dR1F")
        if Image == 3:
            await message.channel.send("You rolled a 3.")
            await message.channel.send("https://imgur.com/r/CatGifs/Mo797M1")
        if Image == 4:
            await message.channel.send("You rolled a 4.")
            await message.channel.send("https://imgur.com/r/CatGifs/QXWgw7L")
        if Image == 5:
            await message.channel.send("You rolled a 5.")
            await message.channel.send("https://imgur.com/r/CatGifs/SA6UWPP")
        if Image == 6:
            await message.channel.send("You rolled a 6.")
            await message.channel.send("https://imgur.com/r/CatGifs/OhxBuUb")
        if Image == 7:
            await message.channel.send("You rolled a 7.")
            await message.channel.send("https://imgur.com/r/CatGifs/HETUdhl")
        if Image == 8:
            await message.channel.send("You rolled a 8.")
            await message.channel.send("https://imgur.com/r/CatGifs/xm4NYVz")
        if Image == 9:
            await message.channel.send("You rolled a 9.")
            await message.channel.send("https://imgur.com/r/CatGifs/GIdNqLw")
        if Image == 10:
            await message.channel.send("You rolled a 10.")
            await message.channel.send("https://imgur.com/r/CatGifs/Q2NG1NY")
        if Image == 11:
            await message.channel.send("You rolled a 11.")
            await message.channel.send("https://imgur.com/r/CatGifs/dYiqPC2")
        if Image == 12:
            await message.channel.send("You rolled a 12.")
            await message.channel.send("https://imgur.com/r/CatGifs/Iw5uCzv")
        if Image == 13:
            await message.channel.send("You rolled a 13.")
            await message.channel.send("https://imgur.com/r/CatGifs/9MjjHel")
        if Image == 14:
            await message.channel.send("You rolled a 14.")
            await message.channel.send("https://imgur.com/r/CatGifs/nkm6P25")
        if Image == 15:
            await message.channel.send("You rolled a 15.")
            await message.channel.send("https://imgur.com/r/CatGifs/xdVfiBd")
        if Image == 16:
            await message.channel.send("You rolled a 16.")
            await message.channel.send("https://imgur.com/r/CatGifs/z1okFEK")
        if Image == 17:
            await message.channel.send("You rolled a 17.")
            await message.channel.send("https://imgur.com/r/CatGifs/UZOXjyc")
        if Image == 18:
            await message.channel.send("You rolled a 18.")
            await message.channel.send("https://imgur.com/r/CatGifs/4reAQ1i")
        if Image == 19:
            await message.channel.send("You rolled a 19.")
            await message.channel.send("https://imgur.com/r/CatGifs/JclliF7")
        if Image == 20:
            await message.channel.send("You rolled a 20.")
            await message.channel.send("https://imgur.com/r/CatGifs/FFHTjlj")
        if Image == 21:
            await message.channel.send("You rolled a 21.")
            await message.channel.send("https://imgur.com/r/CatGifs/NV3KJ")
        if Image == 22:
            await message.channel.send("You rolled a 22.")
            await message.channel.send("https://imgur.com/r/CatGifs/KkQlcr1")
        if Image == 23:
            await message.channel.send("You rolled a 23.")
            await message.channel.send("https://imgur.com/r/CatGifs/X1aECBK")
        if Image == 24:
            await message.channel.send("You rolled a 24.")
            await message.channel.send("https://imgur.com/r/CatGifs/eY7BR4k")
        if Image == 25:
            await message.channel.send("You rolled a 25.")
            await message.channel.send("https://imgur.com/r/CatGifs/5AxjWO1")
        if Image == 26:
            await message.channel.send("You rolled a 26.")
            await message.channel.send("https://imgur.com/gallery/J5wbAur")
        if Image == 27:
            await message.channel.send("You rolled a 27.")
            await message.channel.send("https://imgur.com/r/CatGifs/k5lDsIK")
        if Image == 28:
            await message.channel.send("You rolled a 28.")
            await message.channel.send("https://imgur.com/gallery/uyAs6lx")
        if Image == 29:
            await message.channel.send("You rolled a 29.")
            await message.channel.send("https://imgur.com/gallery/QrOhkRj")
        if Image == 30:
            await message.channel.send("You rolled a 30.")
            await message.channel.send("https://imgur.com/gallery/itAcRf5")
        if Image == 31:
            await message.channel.send("You rolled a 31.")
            await message.channel.send("https://imgur.com/gallery/WvPv2yL")
        if Image == 32:
            await message.channel.send("You rolled a 32.")
            await message.channel.send("https://imgur.com/gallery/SNcyZ0E")

    if message.content.startswith('$dogimage'):
        Image = random.randint(1, 25)
        if Image == 1:
            await message.channel.send("You rolled a 1.")
            await message.channel.send("https://imgur.com/r/dogs/oT4qU")
        if Image == 2:
            await message.channel.send("You rolled a 2.")
            await message.channel.send("https://imgur.com/r/dogs/DtMIw")
        if Image == 3:
            await message.channel.send("You rolled a 3.")
            await message.channel.send("https://imgur.com/r/dogs/4Iu7m")
        if Image == 4:
            await message.channel.send("You rolled a 4.")
            await message.channel.send("https://imgur.com/r/dogs/qG9gA")
        if Image == 5:
            await message.channel.send("You rolled a 5.")
            await message.channel.send("https://imgur.com/r/dogs/YV7yj")
        if Image == 6:
            await message.channel.send("You rolled a 6.")
            await message.channel.send("https://imgur.com/r/dogs/T0mTd")
        if Image == 7:
            await message.channel.send("You rolled a 7.")
            await message.channel.send("https://imgur.com/r/dogs/Mmu0n")
        if Image == 8:
            await message.channel.send("You rolled a 8.")
            await message.channel.send("https://imgur.com/r/dogs/ccZ6b")
        if Image == 9:
            await message.channel.send("You rolled a 9.")
            await message.channel.send("https://imgur.com/r/dogs/pzEUC")
        if Image == 10:
            await message.channel.send("You rolled a 10.")
            await message.channel.send("https://imgur.com/r/dogs/Lfjiw")
        if Image == 11:
            await message.channel.send("You rolled a 11.")
            await message.channel.send("https://imgur.com/r/dogs/JtxdI")
        if Image == 12:
            await message.channel.send("You rolled a 12.")
            await message.channel.send("https://imgur.com/r/dogs/Ifqur")
        if Image == 13:
            await message.channel.send("You rolled a 13.")
            await message.channel.send("https://imgur.com/r/dogs/RmeBu")
        if Image == 14:
            await message.channel.send("You rolled a 14.")
            await message.channel.send("https://imgur.com/r/dogs/72JF1")
        if Image == 15:
            await message.channel.send("You rolled a 15.")
            await message.channel.send("https://imgur.com/r/dogs/KICVj")
        if Image == 16:
            await message.channel.send("You rolled a 16.")
            await message.channel.send("https://imgur.com/r/dogs/YONj8")
        if Image == 17:
            await message.channel.send("You rolled a 17.")
            await message.channel.send("https://imgur.com/r/dogs/XRQOm")
        if Image == 18:
            await message.channel.send("You rolled a 18.")
            await message.channel.send("https://imgur.com/r/dogs/AaGEx")
        if Image == 19:
            await message.channel.send("You rolled a 19.")
            await message.channel.send("https://imgur.com/r/dogs/VyQKV")
        if Image == 20:
            await message.channel.send("You rolled a 20.")
            await message.channel.send("https://imgur.com/r/dogs/vN0SZ")
        if Image == 21:
            await message.channel.send("You rolled a 21.")
            await message.channel.send("https://imgur.com/r/dogs/pI20a")
        if Image == 22:
            await message.channel.send("You rolled a 22.")
            await message.channel.send("https://imgur.com/r/dogs/tVNCc")
        if Image == 23:
            await message.channel.send("You rolled a 23.")
            await message.channel.send("https://imgur.com/r/dogs/xov9tkl")
        if Image == 24:
            await message.channel.send("You rolled a 24.")
            await message.channel.send("https://imgur.com/r/dogs/pzEUC")
        if Image == 25:
            await message.channel.send("You rolled a 25.")
            await message.channel.send("https://imgur.com/r/dogs/s1woz")

    if message.content.startswith('$failimage'):
        Image = random.randint(1, 25)
        if Image == 1:
            await message.channel.send("You rolled a 1.")
            await message.channel.send("https://imgur.com/r/fail/diRWvrY")
        if Image == 2:
            await message.channel.send("You rolled a 2.")
            await message.channel.send("https://imgur.com/gallery/Z5tCjZQ")
        if Image == 3:
            await message.channel.send("You rolled a 3.")
            await message.channel.send("https://imgur.com/gallery/znPRA3Y")
        if Image == 4:
            await message.channel.send("You rolled a 4.")
            await message.channel.send("https://i.imgur.com/hH4bBg3.gif")
        if Image == 5:
            await message.channel.send("You rolled a 5.")
            await message.channel.send("https://i.imgur.com/J3I9Iu8.gif")
        if Image == 6:
            await message.channel.send("You rolled a 6.")
            await message.channel.send("https://i.imgur.com/JMNxUDA.mp4")
        if Image == 7:
            await message.channel.send("You rolled a 7.")
            await message.channel.send("https://i.imgur.com/Ic5DWHt.gif")
        if Image == 8:
            await message.channel.send("You rolled a 8.")
            await message.channel.send("https://i.imgur.com/Use5OLf.gif")
        if Image == 9:
            await message.channel.send("You rolled a 9.")
            await message.channel.send("https://i.imgur.com/gBMogvI.gif")
        if Image == 10:
            await message.channel.send("You rolled a 10.")
            await message.channel.send("https://i.imgur.com/6qFWthX.gif")
        if Image == 11:
            await message.channel.send("You rolled a 11.")
            await message.channel.send("https://i.imgur.com/uD9QuQy.gif")
        if Image == 12:
            await message.channel.send("You rolled a 12.")
            await message.channel.send("https://i.imgur.com/rveNd5J.gif")
        if Image == 13:
            await message.channel.send("You rolled a 13.")
            await message.channel.send("https://i.imgur.com/jI8SEwD.mp4")
        if Image == 14:
            await message.channel.send("You rolled a 14.")
            await message.channel.send("https://i.imgur.com/uYqnpEL.mp4")
        if Image == 15:
            await message.channel.send("You rolled a 15.")
            await message.channel.send("https://i.imgur.com/uWFbxw2.gif")
        if Image == 16:
            await message.channel.send("You rolled a 16.")
            await message.channel.send("https://i.imgur.com/GmMpuU4.gif")
        if Image == 17:
            await message.channel.send("You rolled a 17.")
            await message.channel.send("https://i.imgur.com/TmMtwUQ.mp4")
        if Image == 18:
            await message.channel.send("You rolled a 18.")
            await message.channel.send("https://i.imgur.com/qtDiU00.mp4")
        if Image == 19:
            await message.channel.send("You rolled a 19.")
            await message.channel.send("https://i.imgur.com/qK6Xv87.gif")
        if Image == 20:
            await message.channel.send("You rolled a 20.")
            await message.channel.send("https://i.imgur.com/2bh8dTV.mp4")
        if Image == 21:
            await message.channel.send("You rolled a 21.")
            await message.channel.send("https://i.imgur.com/5F5CoQC.gif")
        if Image == 22:
            await message.channel.send("You rolled a 22.")
            await message.channel.send("https://i.imgur.com/GP9CT8t.gif")
        if Image == 23:
            await message.channel.send("You rolled a 23.")
            await message.channel.send("https://i.imgur.com/P05eCip.mp4")
        if Image == 24:
            await message.channel.send("You rolled a 24.")
            await message.channel.send("https://i.imgur.com/E1ICTOo.gif")
        if Image == 25:
            await message.channel.send("You rolled a 25.")
            await message.channel.send("https://i.imgur.com/6wE0EiQ.gif")

    await bot.process_commands(message)

bot.run('NjI2MDk1MzYxMDg1NDA3MjUz.XYpG9A.LgP8gD4aNhk3QC5L4GQvrWwvIKc')


