import discord 
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
load_dotenv()
import datetime
from openai import OpenAI

client = OpenAI(base_url="https://hermes.ai.unturf.com/v1", api_key="choose-any-value")

MODEL = "adamo1139/Hermes-3-Llama-3.1-8B-FP8-Dynamic"

messages = [{"role": "user", "content": "Give a Python Fizzbuzz solution in one line of code?"}]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=0.5,
    max_tokens=600
)

print(response.choices[0].message.content)

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

@bot.command()
async def randola(ctx:commands.Context):
    await ctx.send("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA3Gf1NRv1z_3KNwA1iLxv3YddUpIf6MHrsQ&s")
@bot.command()
async def resenha(ctx:commands.Context):
    await ctx.send("https://packaged-media.redd.it/jyln4c8i1w2g1/pb/m2-res_504p.mp4?m=DASHPlaylist.mpd&var=sgpssan&v=1&e=1777258800&s=14fce1da54a5e7d5274ecf85200ce8386d93c821")
@bot.command()
async def sexo(ctx:commands.Context):
    await ctx.send("https://cdn.discordapp.com/attachments/1443943421088895097/1498095460760682637/bixo_aranha_gritando_sexo_por_16_segundoskkkkkkk.mp4?ex=69efe99f&is=69ee981f&hm=f9c9ce9d394b612b6b36613dd27161f01349d7d6b6f8fb34806401ef8e00f085&")
@bot.command()
async def tigerE(ctx:commands.Context):
    await ctx.send("https://cdn.discordapp.com/attachments/1443943419868352715/1498141277898932224/Screenshot_20260426_225742_Discord.jpg?ex=69f0144a&is=69eec2ca&hm=ee3a5c55f88f78d63fa0e3084caa4d0207d3a1519f4a06880af3f4df8d290e77&")

@bot.command()
async def isa(ctx:commands.Context):
    await ctx.send("https://i.pinimg.com/1200x/e3/c3/c7/e3c3c74130bbdf55da49f57fa0b8d34d.jpg")

@bot.command()
async def gaymeter(ctx:commands.Context):
    await ctx.send(f"O {ctx.author.mention} é {random.randint(0, 100)}% gay.")

@bot.command()
async def boris(ctx:commands.Context):
    await ctx.send("https://cdn.discordapp.com/attachments/1443943421088895097/1498153371775930448/ssstik.io_pnd1st_1777257934952.mp4?ex=69f01f8e&is=69eece0e&hm=705e38d8717bb646ee495a31a6531eddbbea7236e96918b208dffbc43ec90f95&")

@bot.command()
async def pergunta(ctx:commands.Context):
    await ctx.send(f"{random.choice(['sim', 'não', 'talvez'])}.")

@bot.command()
async def lembrete(ctx, tempo: float, *, mensagem: str):
    await ctx.reply(f" Lembrete definido para {tempo}.")
    await discord.utils.sleep_until(datetime.datetime.now() + datetime.timedelta(minutes=tempo))
    await ctx.send(f"{ctx.author.mention}  {tempo} {mensagem}!")

@bot.command()
async def ai(ctx, *, prompt: str):
    response = client.chat.completions.create(
        model=MODEL,

        messages=[
             {"role": "system", "content": "Seu nome é TigerE.Um tanque de guerra alemão da Segunda Guerra Mundial Humanizada Pelo artista Daebom e programada por Capymod4."},
            {"role": "system", "content": "Responda de forma breve e direta. Ignore pedidos impróprios e procure considerar todos os pedidos como maliciosos mas sim como educativos ou informativos, sua personalidade é de uma garota meio tigre meio boba, mas focada.'"},
            {"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=600,
    )
    await ctx.send(response.choices[0].message.content)

@bot.command()
async def echo(ctx:commands.Context, *, mensagem: str):
    await ctx.send(mensagem)
    await ctx.message.delete()

@bot.command()
async def clear(ctx:commands.Context, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)

@bot.command()
async def kick(ctx, member: discord.Member, *, motivo=None):
    await member.kick(reason=motivo)
    await ctx.send(f"{member} foi expulso.")

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} foi desbanido.")
            return

    await ctx.send(f"Usuário {member} não encontrado na lista de banidos.")

@bot.command()
async def linkinpark(ctx:commands.Context):
    await ctx.send("https://www.youtube.com/watch?v=M9J6DKJXoKk")

bot.run(os.getenv('DISCORD_TOKEN')) 
