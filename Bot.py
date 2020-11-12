import discord
from discord import Message, Member
from discord.ext import commands
import os
bot = commands.Bot(command_prefix='/')
ploxie_slova = ["бля", "сука", "гондон", "сучара", "нахер", "нахуй", "лох"]


@bot.event
async def on_ready():
    print("bot")


@bot.event
async def on_message(msg):
    for i in ploxie_slova:
        if i in msg.content:
            await Message.add_reaction(msg, emoji="🤬")
            await msg.channel.send("ОСУЖДАЮ ТАКИЕ СЛОВА!")
    if "ха" in msg.content:
        await Message.add_reaction(msg, emoji="😂")
        await msg.channel.send("хвхвхвх")
    await bot.process_commands(msg)


@bot.command()
async def rep(ctx, arg):
    await Message.delete(ctx.message)
    await ctx.send(arg)


@bot.command()
async def ban(ctx, member: discord.Member):
    await Message.delete(ctx.message)
    m_r = str(member.top_role)
    a_r = str(ctx.message.author.top_role)
    m_n = str(member)
    name = str(ctx.message.author)
    print(m_r)
    print(m_n)
    if m_r == "Bot Dmitry":
        await ctx.send(f"{name} за что!")
        await ctx.send("Нет уж!")
    elif m_r == "Bot_cross":
        await Message.add_reaction(ctx.message, "🖕")
        await ctx.send(f"{name} ни за что!")
        await ctx.send("Это мой друг!")
    elif m_n == "Дмитрий Чувилин#4366":
        await ctx.send(f"{name} мой создатель я не могу так с ним!")
    elif a_r == "admin" and m_r != "admin":
        await ctx.send(f"{name} зачем вы так с ним?")
        await Member.ban(member)
    else:
        await ctx.send(f"{name} вы не имеете право!")


@bot.command()
async def image(ctx, imag):
    if imag == "грусть":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/cry.jpg'))
    elif imag == "fuck":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/fuck.jpg'))
    elif imag == "да":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/yes.jpg'))
    elif imag == "ладно":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/ladno.jpeg'))
    elif imag == "niggaдяй":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/nigga.jpeg'))
    elif imag == "Аллахакбар":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/alax.jpeg'))
    elif imag == "бан":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/ban.jpeg'))
    elif imag == "бля":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/blya.jpeg'))
    elif imag == "конченый":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/kon.jpeg'))
    elif imag == "чего":
        await Message.delete(ctx.message)
        await ctx.send(file=discord.File('images/what.jpeg'))


@bot.command()
async def exit(ctx):
    await Message.delete(ctx.message)
    await Member.remove_roles(ctx.message.author, ctx.message.author.top_role)
    await Member.kick(ctx.message.author)



token = os.environ.get("BOT_TOKEN")