import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import View, Button, Select, Modal, TextInput

from datetime import datetime
import os
import random
import json
import dotenv
import logging
import asyncio
import uuid

from scripts.functions import get_data

intents = discord.Intents.all()

dotenv.load_dotenv(".env")

current_date = datetime.now().strftime("%Y-%m-%d")
handler = logging.FileHandler(
    filename=f"logs/discord_{current_date}.log", encoding="utf-8", mode="w"
)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({round(bot.latency * 1000)})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=random.choice(get_data()["things"]),
            state="made with love and redbull",
        )
    )
    
bot.run(os.environ["TOKEN"] , log_handler=handler)