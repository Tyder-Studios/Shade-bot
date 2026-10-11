import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Sets the prefix to a comma ','
bot = commands.Bot(command_prefix=",", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} successfully!")

# Roleplay Commands
@bot.command(name="kiss")
async def kiss(ctx, target: discord.Member = None):
    if not target:
        await ctx.send(f"⚠️ **{ctx.author.display_name}**, please mention someone to kiss!")
        return
    await ctx.send(f"💖 **{ctx.author.display_name}** gave a sweet kiss to **{target.display_name}**!")

@bot.command(name="hug")
async def hug(ctx, target: discord.Member = None):
    if not target:
        await ctx.send(f"⚠️ **{ctx.author.display_name}**, please mention someone to hug!")
        return
    await ctx.send(f"🤗 **{ctx.author.display_name}** warmly hugged **{target.display_name}**!")

@bot.command(name="pat")
async def pat(ctx, target: discord.Member = None):
    if not target:
        await ctx.send(f"⚠️ **{ctx.author.display_name}**, please mention someone to pat!")
        return
    await ctx.send(f"✋ **{ctx.author.display_name}** gently patted **{target.display_name}**!")

@bot.command(name="slap")
async def slap(ctx, target: discord.Member = None):
    if not target:
        await ctx.send(f"⚠️ **{ctx.author.display_name}**, please mention someone to slap!")
        return
    await ctx.send(f"👋 **{ctx.author.display_name}** slapped **{target.display_name}**!")

@bot.command(name="poke")
async def poke(ctx, target: discord.Member = None):
    if not target:
        await ctx.send(f"⚠️ **{ctx.author.display_name}**, please mention someone to poke!")
        return
    await ctx.send(f"👉 **{ctx.author.display_name}** poked **{target.display_name}**!")

# This safely pulls your token from the host environment
bot.run(os.getenv("DISCORD_TOKEN"))
