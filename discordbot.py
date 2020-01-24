from discord.ext import commands
import os
import traceback
import discord
import sys
import random
from discord.ext import tasks
from googlesearch import search
import datetime

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == 'おみくじ':
        omikuji = ['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']
        await message.channel.send(random.choice(omikuji) + 'です')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('グーグル'):
        url = message.content[5:]
        if url == '':
            await message.channel.send('キーワードを入力してください 使い方：グーグル <キーワード>')
        else:
            await message.channel.send(url + ' の検索結果を表示します')
            count = 0
            for url in search(url, lang="jp", num=3):
                await message.channel.send(url)
                count += 1
                if count == 3:
                    await message.channel.send('検索結果の上位3件を表示しました')
                    break

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

client.run(token)

bot.run(token)
