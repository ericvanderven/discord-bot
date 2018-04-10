#bot by Eric

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random

bot = commands.Bot(command_prefix=';')

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.content == "Kitten":
        imgList = os.listdir("kitten gifs/") 
        imgString = random.choice(imgList) 
        path = "kitten gifs/" + imgString 
        await bot.send_file(message.channel, path) 

    if message.content == "high":
        imgList = os.listdir("weed/") 
        imgString = random.choice(imgList) 
        path = "weed/" + imgString 
        await bot.send_file(message.channel, path) 

    if message.content == "Jack" or message.content == "bugs bunny":
        await bot.send_file(message.channel, "Jack.png")

    if message.content == "Swinging Owl":
        await bot.send_file(message.channel, "SwingingOwl.gif")

    if message.content == "anal":
         await bot.send_file(message.channel, "anal.gif")

    if message.content == "bystander":
         await bot.send_file(message.channel, "bystander.png")


@bot.command(pass_context=True)
async def HitlerSugga(ctx):
    await bot.upload("hitlah suggaaaa.png")

@bot.command(pass_context=True)
async def DrunkToppie(ctx):
    await bot.upload("drunk.gif")

@bot.command(pass_context=True)
async def ConfusedToppie(ctx):
    await bot.upload("confused.gif")
    
bot.run("NDMxMTMyNzEzMDc3MDQ3Mjk2.DaaTUA.j3NQRIIMsgSkzz1Sp2NwLnKj4I8")