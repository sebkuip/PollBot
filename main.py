import discord
from discord.ext import commands

import config

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="p!", case_insensitive=True,intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def poll(ctx, question, *options):
        if len(options) == 1 or len(options) > 10:
            await ctx.send("Please enter a valid number of arguments")
            return

        if len(options) == 0:
            answers = ["Yes", "No"]
        else:
            answers = [answer for answer in options]
        
        embed = discord.Embed(title=question, color=discord.Color.blurple())
        for i, answer in enumerate(answers):
            embed.add_field(name=f"**{i+1}**", value=answer, inline=False)

        message = await ctx.send(embed=embed)
        reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

        for i in range(len(answers)):
            await message.add_reaction(reactions[i])

bot.run(config.TOKEN)