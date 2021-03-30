import config
import discord
import gifs
import random
import aiohttp
import json
from discord.ext import commands

from outsources import functions


class social(commands.Cog, name="Social"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Slap someone", enabled=False)
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason="Being bad"):
        if str(ctx.message.author.id) in str(members):
            await ctx.send("You can't slap yourself, derp!")
            return
        await functions.interactions(ctx, members, reason, "slap", "bad!", "slapped")

    @commands.command(brief="Snuggle someone")
    async def snuggle(self, ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
        await functions.interactions(ctx, members, reason, "snuggle", "how cute", "snuggled")

    #@commands.command(brief="Hug someone")
    #async def hug(self, ctx, members: commands.Greedy[discord.Member], *, reason="being lovely"):
    #    await functions.interactions(ctx, members, reason, "hug", "how lovely", "hugged")

    @commands.command(brief="Bonk someone", enabled=False)
    async def bonk(self, ctx, members: commands.Greedy[discord.Member], *, reason="bad!"):
        await functions.interactions(ctx, members, reason, "bonk", "how mean", "bonked")

    @commands.command(brief="Boop someone")
    async def boop(self, ctx, members: commands.Greedy[discord.Member], *, reason="Cutie snoutie"):
        await functions.interactions(ctx, members, reason, "boop", "so soft", "booped")
    
    @commands.command(brief="Smooch someone", aliases=["kiss"])
    async def smooch(self, ctx, members: commands.Greedy[discord.Member], *, reason="being lovely"):
        await functions.interactions(ctx, members, reason, "smooch", "lovely", "smooched")
        
    @commands.command(brief="Lick someone")
    async def lick(self, ctx, members: commands.Greedy[discord.Member], *, reason="Needed a clean"):
        await functions.interactions(ctx, members, reason, "lick", "tasty", "licked")
    
    @commands.command(brief="Give bellyrubs!")
    async def bellyrub(self, ctx, members: commands.Greedy[discord.Member], *, reason="being lovely"):
        await functions.interactions(ctx, members, reason, "bellyrub", "lovely", "bellyrubbed")

    @commands.command(brief="Cuddle someone")
    async def cuddle(self, ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
        await functions.interactions(ctx, members, reason, "cuddle", "heartwarming", "cuddled")
   
    @commands.command(brief="Feed someone")
    async def feed(self, ctx, members: commands.Greedy[discord.Member], *, reason="Hungwy"):
        await functions.interactions(ctx, members, reason, "feed", "sweet", "fed")

    @commands.command(brief="Glomp someone")
    async def glomp(self, ctx, members: commands.Greedy[discord.Member], *, reason="Love!"):
        await functions.interactions(ctx, members, reason, "glomp", "Cute", "glomped on")

    @commands.command(brief="Highfive someone")
    async def highfive(self, ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
        await functions.interactions(ctx, members, reason, "highfive", "awesome!", "high fived")

    @commands.command(brief="Rawrrrr")
    async def rawr(self, ctx, members: commands.Greedy[discord.Member], *, reason="Rawr!"):
        giflist = gifs.rawr
        gif = random.choice(giflist)
        if not members:
            embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**rawred, cute!**\nFor: " + reason))
            embed.set_image(url=gif)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**rawred at**" + " " + '**,** '.join(x.mention for x in members) + "**, cute!**\nFor: " + reason))
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(brief="Howl to the moon, or someone", aliases=["howl"])
    async def awoo(self, ctx, members: commands.Greedy[discord.Member], *, reason="Awoo!"):
        giflist = gifs.awoo
        gif = random.choice(giflist)
        if not members:
            embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**awoo'd, chilling!**\nFor: " + reason))
            embed.set_image(url=gif)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**howled at**" + " " + '**,** '.join(x.mention for x in members) + "**, chilling!**\nFor: " + reason))
        embed.set_image(url=gif)
        await ctx.send(embed=embed)
        
    @commands.command(brief="Blushies!")
    async def blush(self, ctx, members: commands.Greedy[discord.Member], *, reason="Shy boye"):
        giflist = gifs.blush
        gif = random.choice(giflist)
        if not members:
            embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**blushed**\nFor: " + reason))
            embed.set_image(url=gif)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**blushed because of**" + " " + '**,** '.join(x.mention for x in members) + "**, kyoot!**\nFor: " + reason))
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(brief="Be happy")
    async def happy(self, ctx, members: commands.Greedy[discord.Member]):
        giflist = gifs.happy
        gif = random.choice(giflist)
        if not members:
            embed = discord.Embed(color=config.color, description=f"**{ctx.message.author.display_name}** is happy")
            embed.set_image(url=gif)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(color=config.color, description=f"**{ctx.message.author.display_name}** Is happy because of " + "**" + '**, **'.join(x.display_name for x in members) + "**")
        embed.set_image(url=gif)
        await ctx.send(embed=embed)
    
    @commands.command(brief="wag yer tail")
    async def wag(self, ctx, members: commands.Greedy[discord.Member]):
        giflist = gifs.wag
        gif = random.choice(giflist)
        if not members:
            embed = discord.Embed(color=config.color, description=f"**{ctx.message.author.display_name}** wags their tail")
            embed.set_image(url=gif)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(color=config.color, description=f"**{ctx.message.author.display_name}** wags their tail because of " + "**" + '**, **'.join(x.display_name for x in members) + "**")
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

    @commands.command(brief="pat someone!", aliases=["pet"])
    async def pat(self, ctx, members: commands.Greedy[discord.Member]):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/pat") as r:
                js = await r.json()
                
                if not members:
                    return await ctx.send("Please specify someone to pat.")
                e = discord.Embed(color=config.color, description=f"**{ctx.message.author.display_name} pats** " + "**" + '**,** '.join(x.display_name for x in members) + "**")
                
                manual = gifs.pet
                manual.append(js['link'])
                image = random.choice(manual)
                
                e.set_image(url=image)
                await ctx.send(embed=e)
    
    @commands.command(brief="hug someone!")
    async def hug(self, ctx, members: commands.Greedy[discord.Member]):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/hug") as r:
                js = await r.json()
                
                if not members:
                    return await ctx.send("Please specify someone to hug.")
                e = discord.Embed(color=config.color, description=f"**{ctx.message.author.display_name}** hugs " + "**" + '**, **'.join(x.display_name for x in members) + "**")
                
                manual = gifs.hug
                manual.append(js['link'])
                image = random.choice(manual)
                
                e.set_image(url=image)
                await ctx.send(embed=e)
        
    @commands.command(brief="Gib cookie")
    async def cookie(self, ctx, members: commands.Greedy[discord.Member]):
        if not members:
            return await ctx.send("Please specify at least one cutie to give a cookie to!")
        e = discord.Embed(title='A cookie has been given!', description=f'{ctx.author.mention} gave {members[0].mention} a cookie', color=config.green)
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(social(bot))
