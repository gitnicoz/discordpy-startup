from discord.ext import commands
import os
import traceback
import discord
import sys
from discord.ext import tasks
import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@tasks.loop(seconds=5)
async def loop():
    text_channel = client.get_channel(id=645940109610450954)
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    if hour == 0:
        if minute == 0:
            await text_channel.send('0時になりました')
    if hour == 6:
        if minute == 0:
            await text_channel.send('6時になりました')
    if hour == 12:
        if minute == 0:
            await text_channel.send('正午になりました')
    if hour == 18:
        if minute == 0:
            await text_channel.send('18時になりました')
    if hour == 21:
        if minute == 0:
            await text_channel.send('21時になりました')

loop.start()

bot.run(token)
