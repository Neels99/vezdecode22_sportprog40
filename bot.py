from dis import disco
import discord
import other
from discord.ext import commands

from pandas import DataFrame, date_range
from pandas import read_csv

import bot_logic

config = {
    'token': 'OTgyNTg0NjAxODYyMTExMjgz.Gl_4ow.v2cNi0ugFUthPWj6DC916CwzNt3bmLPxu7xeoU',
    'prefix': 'xd',
}

df = bot_logic.init()
bot = commands.Bot(command_prefix=config['prefix'])

@bot.event
async def on_voice_state_update(member, before, after):
    print("!!!")
    print(str(member) + ".")
    if not after.channel is None:
        # print(after.channel.name)
        bot_logic.user_connected(df, str(member), after.channel.name)


# @bot.event
# async def on_message(ctx):
#     if ctx.author != bot.user:
#         await ctx.reply('Не пиши мне чел, ты в муте')

bot.run(config['token'])