#from settings import settings
import discord
import random
from discord.ext import commands
import os
import requests
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)





@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('animals'))
    with open(f'animals/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        animals = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=animals)



bot.run("token")