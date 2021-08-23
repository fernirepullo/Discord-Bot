import discord
import random
import aiohttp
import asyncio

from discord.ext import commands

pandaBot = commands.Bot(

    command_prefix="."
)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False


@pandaBot.event
async def on_ready():
    print('Logged in as')
    print(pandaBot.user.name)
    print(pandaBot.user.id)
    print('-----------')


@pandaBot.event
async def reply(self, message):
    if message.author.id == self.user.id:
        return

    elif message.content.startswith('hola') or message.content.startswith('Hola'):
        await message.reply('Buenas ', mention_author=True)

    elif message.content.startswith('buenas') or message.content.startswith('Buenas'):
        await message.reply('Que pasa ', mention_author=True)

    elif message.content.startswith('ey') or message.content.startswith('Ey'):
        await message.reply('Que dice su colega ', mention_author=True)


@pandaBot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))

    except Exception:
        await ctx.send('El formato tiene que ser XdY!')
        return

    resultado = ', '.join(str(random.randint(1, limit))
                          for r in range(rolls))
    await ctx.send(resultado)


@pandaBot.command()
async def yami(ctx):
    await ctx.send('Yami africana')


@pandaBot.command()
async def volkacio(ctx):
    await ctx.send('Volkacio is real')


@pandaBot.command()
async def lloreria(ctx, member1: discord.User, member2: discord.User):

    member1 = member1.name
    member2 = member2.name
    await ctx.send(f'{member1} ha mandado a {member2} a la llorería')


@pandaBot.command()
async def callate(ctx, member: discord.User):

    member = member.name
    await ctx.send(f'{member}, cállate ya hijoputa, que eres tontísimo')


@pandaBot.command()
async def joined(ctx, member: discord.User):
    await ctx.send(f'{member.name} se ha unido el {member.joined_at}'.format(member))

# TODO: Descargar datos a través de web scrapping y hacer el comando de recetas / reviews

#
# @pandaBot.command()
# async def obtenerReceta(ctx, message: str):
#     url = 'https://www.recetasgratis.net/busqueda?q='
#     async with aiohttp.ClientSession() as session:
#         raw_response = await session.get(url)
#         response = await raw_response.text()

pandaBot.run(
    "ODc5MzMxNzEzOTg4MzI5NTQz.YSOLeQ.LLctJ1eYey7QTpfvLg4H_92BmRk"
)
