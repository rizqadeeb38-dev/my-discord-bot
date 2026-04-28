import os
import discord
from discord.ext import commands

# 1. BOT SETUP
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 2. DATA (Triggers)
HUB_DATA = {
    "redz": {
        "name": "🔴 Redz Hub",
        "script": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/realredz/RedzV2/main/loader.lua"))()'
    },
}

@bot.event
async def on_ready():
    print(f'✅ SUCCESS: Bot is ONLINE as {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower()
    if "redz" in msg:
        data = HUB_DATA["redz"]
        embed = discord.Embed(title=data["name"], color=discord.Color.red())
        embed.add_field(name="Script:", value=f"```lua\n{data['script']}\n```", inline=False)
        await message.reply(embed=embed)

    await bot.process_commands(message)

# 3. RUN BOT (Uses the Secret from Koyeb)
bot.run(os.getenv('DISCORD_TOKEN'))
