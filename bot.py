import discord
from discord.ext import commands

TOKEN = "put ur token here"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"bot: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} working")
    except Exception as e:
        print(f"err: {e}")

@bot.tree.command(name="test", description="test")
async def dev(interaction: discord.Interaction):
    await interaction.response.send_message("working")

bot.run(TOKEN)
