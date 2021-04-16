import os
import aiohttp

import discord
import io
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")

@bot.command(name="hamster", help="Sends a random hamster image")
async def hamster_pic(context):
    await context.send("hamster incoming...")

    async with aiohttp.ClientSession() as session:
        async with session.get("https://source.unsplash.com/featured/?hamster") as resp:
            if resp.status != 200:
                return await context.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await context.send(file=discord.File(data, 'cool_image.png'))        

bot.run(TOKEN)