import asyncio
import discord
from discord_slash import SlashCommand # Importing the newly installed library.
from discord.ext import commands
import random
from tablice import *
from config import *

#komentarz kurwa

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True) # Declares slash commands through the client.
guild_ids = [572823253798617109]
prefix = '/'

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Wpisz ' + prefix + 'pomoc'))
    print('Bot {0.user} działa jak natura chciała'.format(bot))


@slash.slash()
async def pomoc(ctx):
    await ctx.send(prefix + 'siema - no elo byczku skąd to zwątpienie \n'
                   + prefix + 'minecraftlava - minecraftlava \n'
                   + prefix + 'gra - zagrajmy w gre \n'
                   + prefix + 'roll - rolluj w bannerze standardowym genshina')


@slash.slash()
async def siema(ctx):
    await ctx.send('Cześć Przyjacielu ' + ctx.author.mention)
    await ctx.send(
        'https://cdn.discordapp.com/attachments/572823794343870464/849747028632010812/1498940958_1aa.gif')


@slash.slash()
async def roll(ctx):
    czyqi=random.randint(1, 1000)
    if czyqi<=6:
        await ctx.send('Gratulacje ' + ctx.author.mention
                   + ' wylosowałeś Qiqi ' + str(discord.utils.get(bot.emojis, name='megabeka')))
        await ctx.send(
        'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1a2212b9-af4a-4302-9499-08be7aaa7ff2/de8t8yw-ee0a8eec-00b6-4f09-afd1-89039e9643f5.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFhMjIxMmI5LWFmNGEtNDMwMi05NDk5LTA4YmU3YWFhN2ZmMlwvZGU4dDh5dy1lZTBhOGVlYy0wMGI2LTRmMDktYWZkMS04OTAzOWU5NjQzZjUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.v5QiSeP_kzLfU2qaOlR5smy8FHKvry-AsQJxHfGOI8E')
    else:
        los=random.randint(0, 14)
        await ctx.send('Gratulacje ' + ctx.author.mention
                       + ' wylosowałeś ' + Genshin_nazwa[los])
        await ctx.send(Genshin_link[los])


@slash.slash()
async def minecraftlava(ctx):
    await ctx.send(str(discord.utils.get(bot.emojis, name='minecraft_lava')))


@slash.slash()
async def gra(ctx):
    channel = ctx.channel
    await channel.send('Zagrajmy w gre. Podaj liczbe.')

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=lambda message: message.author == ctx.author)
        await channel.send(str(int(msg.content) + 1))
        await channel.send('przegrałeś')
    except asyncio.TimeoutError:
        await channel.send('Chcesz mi komputer ugotować?')
    except ValueError:
        await channel.send('Liczba debilu wiesz co to znaczy?')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(word in message.content for word in DST):
        await message.reply(random.choice(DST_Reakcja), mention_author=True)

    if any(word in message.content for word in CZTERY):
        await message.add_reaction((discord.utils.get(bot.emojis, name='Jhin4')))

    if any(word in message.content for word in PENTA):
        f = open("penta.txt", "r")
        licznik=int(f.read())
        licznik+=1
        f.close()
        await message.channel.send('Where penta?: ' + str(licznik))
        await message.channel.send('https://cdn.discordapp.com/attachments/572823794343870464/852594093895843880'
                                   '/penta.png')
        f = open("penta.txt", "w")
        f.write(str(licznik))
        f.close()

    await bot.process_commands(message)

bot.run(token)
