import os
import discord
import json
import requests
from dotenv import load_dotenv

from discord.ext.commands import bot
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.command(name='passport', help='Tells you the last game a pokemon is obtainable in and playable in')
async def pokemon(ctx, pokemon_name):
    with open('pokemon.json') as f:
        data = json.load(f)
    try:
        DexNumber = data[pokemon_name]['Pokedex Number']
        LastCatchable = data[pokemon_name]['Last Game Catchable In']
        LastPlayable = data[pokemon_name]['Last Game Playable in']
        url='https://pokeres.bastionbot.org/images/pokemon/{}.png'.format(DexNumber)
        e = discord.Embed()
        response = "{} was last catchable in {} and last useable in {}".format(pokemon_name,LastCatchable,LastPlayable)
    except:
        response = "You didn't enter a valid pokemon name"
    await ctx.send(response)
    e.set_image(url=url)
    await ctx.send(url)

bot.run(TOKEN)

client = discord.Client()

client.run(TOKEN)
