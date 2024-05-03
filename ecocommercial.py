import discord
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.message_content = True

id_admin = '995025921071386654'

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def menu(ctx):
    await ctx.send(f'Im a bot selling things helping ecology and protecting from global warming. There is a list of products, type the number of product that you need. Example: pbr- 1, type $one (to check list type $list). You can also play in this text game!($game)')
    
@bot.command()
async def list(ctx):
    await ctx.send(f'1. Photobioreactor; 2.Sun battery; 3.thermogigrometer; 4.air ionisator; 5.water quality tester;')

@bot.command()
async def one(ctx):
    user = bot.get_user(int(id_admin))
    await user.send(ctx.message.author)
    await ctx.send(f'Photobioreactor(PBR) is gadget that cleans water and air using microalgae. You can buy it, call on the number:+7 (978) 596 45-24/ PayPal BAZZALT ECOLOGY/ email: basilic0503@mail.ru')

@bot.command()
async def two(ctx):
    await ctx.send(f'Sun battery is battery that use sun energy. You can buy it, call on the number: +7 (978) 596 45-24/ PayPal BAZZALT ECOLOGY/ email: basilic0503@mail.ru')

@bot.command()
async def three(ctx):
    await ctx.send(f'Thermogigrometer measures temperature and wentess level. You can buy it, call on the number: +7 (978) 596 45-24/ PayPal BAZZALT ECOLOGY/ email: basilic0503@mail.ru')

@bot.command()
async def four(ctx):
    await ctx.send(f'air ionisator cleanes air. You can buy it, call on the number: +7 (978) 596 45-24/ PayPal BAZZALT ECOLOGY/ email: basilic0503@mail.ru')

@bot.command()
async def five(ctx):
    await ctx.send(f'Water quality tester tests water quality. You can buy it, call on the number: +7 (978) 596 45-24/ PayPal BAZZALT ECOLOGY/ email: basilic0503@mail.ru')

@bot.command()
async def gpt(v):
        openai.api_key = "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"
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Ты бот, который следит за экологией и переживаешь за окружающий мир, когда тебе задают вопрос, ты отвечаешь на него с уклоконом в экологию, вот такой вопрос - '{v}'"}
            ])
        
        return completion.choices[0].message.content

# @bot.command()
# async def game(ctx):
#     await ctx.send(f'game dont work already, its still developing')

bot.run("MTIyODY0ODY2MDk2MzgyMzY1OA.G08ofP.G5-qHDytEgwAZOS0W1O7rO64vV41-xy_XamV4M")
