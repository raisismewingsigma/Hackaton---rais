import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Sudah login sebagai: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Halo,aku bot {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Menyimpan gambar ke ./{attachment.filename}")
            get_class(model_path="keras_model.h5", labels_path="label.txt", image_path=f"./{attachment.filename}")
    else:
        await ctx.send("Gambar tidak ada.")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTM2MTY4MDI4OTI2MDExNDAzMA.Gy-cmT.EagbZU-nzXIp3kBlQchBkRzq6C0dIoGrctI-U4")