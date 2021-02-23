import discord, config
from discord.ext import commands

class mod(commands.Cog, name="Moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Ban someone")
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        try:
            if member == ctx.message.author:
                return await ctx.send("You can not ban yourself, please try someone else.")
            botmember = ctx.guild.me
            if not botmember.top_role > member.top_role:
                return await ctx.send("My role is too low in the hierarchy. Please move it above the highest role the user you are trying to ban has.")
            await ctx.message.delete()
            messageok = f"You were banned from {ctx.guild.name}\n**reason:** {reason}."
            await member.send(messageok)
            await member.ban(reason=f"Moderator: {ctx.message.author} | Reason: {reason}")
            e = discord.Embed(title=f"{member} was banned | {reason}", color=config.red)
            await ctx.send(embed=e)
        except Exception as e:
            await ctx.send(f"```py\n{e}\n```")

def setup(bot):
    bot.add_cog(mod(bot))
