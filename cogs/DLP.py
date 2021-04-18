from discord.ext import commands
import config
import discordlists

class DiscordListsPost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = discordlists.Client(self.bot)  # Create a Client instance
        self.api.set_auth("discordextremelist.xyz", config.DELTOKEN) # Set authorisation token for a bot list
        self.api.set_auth("top.gg", config.TOPTOKEN)
        self.api.set_auth("discordbotlist.com", config.DBLTOKEN)
        self.api.start_loop()  # Posts the server count automatically every 30 minutes

    @commands.command()
    @commands.is_owner()
    async def post(self, ctx: commands.Context):
        """
        Manually posts guild count using discordlists.py (BotBlock)
        """
        try:
            result = await self.api.post_count()
        except Exception as e:
            await ctx.send("Request failed: `{}`".format(e))
            return
        await ctx.send("Successfully manually posted server count ({:,}) to {:,} lists."
                       "\nFailed to post server count to {:,} lists.".format(self.api.server_count,
                                                                             len(result["success"].keys()),
                                                                             len(result["failure"].keys())))
def setup(bot):
    bot.add_cog(DiscordListsPost(bot))