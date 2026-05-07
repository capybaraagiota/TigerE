import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

bot.remove_command('help')

@bot.command()
async def oi(ctx:commands.Context):
    usuario = ctx.author
    await ctx.send (f"Ola, {ctx.author.mention}!")

@bot.command()
async def help(ctx:commands.Context):
    await ctx.send(f"Olá! Esse é um simples teste de bot usando discord.py. Use .projeto para ver a mensagem do projeto.")

@bot.command()
async def mommy(ctx:commands.Context):
    await ctx.send("https://media1.tenor.com/m/ibe09IFph04AAAAC/cool.gif")

@bot.command()
async def tiger(ctx:commands.Context):
    url: str = ("https://www.flamesofwar.com/Portals/0/all_images/Briefings/NorthAfrica/Tunisian-Tigers-01.jpg")
    await ctx.send(url)

@bot.command()
async def erika(ctx:commands.Context):
    url: str = ("https://media.discordapp.net/attachments/1443943422246391919/1498066065153069146/IMG-20260421-WA0024.jpg?ex=69efce3e&is=69ee7cbe&hm=b293c846869edd0f7e959ab4f4239a51782dd18f6e1146ff6713db18d806aed7&=&format=webp&width=283&height=503")
    await ctx.send(url)

@bot.command()
async def maho(ctx:commands.Context):
    await ctx.send("https://media.discordapp.net/attachments/1443943422246391919/1498066065656250461/20260421_183600.jpg?ex=69efce3e&is=69ee7cbe&hm=6f71ab75860f2240ec531e4610bffe6faf2361ecefbae2bc576fb4f5f70ce0c9&=&format=webp&width=232&height=503")

@bot.command()
async def jenzimibra(ctx:commands.Context):
    await ctx.send("https://preview.redd.it/jenzimibra-v0-3c59soouwfgd1.jpeg?width=640&crop=smart&auto=webp&s=298b84ac3810276df106d24b11bbca786353ea84")

@bot.command()
async def ghost(ctx:commands.Context):
    await ctx.send("Vai tomar no cu, @mr.ghostzer0")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, motivo=None):
    await member.ban(reason=motivo)
    await ctx.send(f"{member} foi banido.")

bot.run(os.getenv('DISCORD_TOKEN')) 
