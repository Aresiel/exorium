import gifs
import config
import discord
import random
import requests
import logging
import datetime
import discord.ext
from discord.ext import commands
from outsources import functions
from requests.auth import HTTPBasicAuth

mydb = config.DBdata
database = mydb.cursor()
database.execute("CREATE TABLE IF NOT EXISTS warnings (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), reason VARCHAR(255), serverid VARCHAR(255))")
logger = logging.getLogger('discord')

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix=["exo ", "p/"])  # sets the bot prefix
bot.remove_command('help')  # removes the default discord.py help command


@bot.event  # sets the bot status and prints when it has started in console with stats, stats include: The amount of users that are in the total amount of guilds and the discord.py version
async def on_ready():
    activity = discord.Game(name=f'with {len(bot.users)} furs', type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('exorium has started successfully')
    print('-----------')
    print('guilds:')
    print(len(bot.guilds))
    print('-----------')
    print('users:')
    print(len(bot.users))
    print('-----------')
    print('version:')
    print(discord.__version__)
    print('-----------')


@bot.event
async def on_guild_join(guild):
    print(f"I just joined {guild.name}, ID: {guild.id}")
    embed = discord.Embed(title="exorium joined server", color=config.color)
    embed.add_field(name="Server Name", value=guild.name, inline=True)
    embed.add_field(name="Server ID", value=guild.id, inline=True)
    embed.add_field(name="Members", value=len(guild.members), inline=True)
    channel = bot.get_channel(747808767034392626)
    await channel.send(embed=embed)
    embed = discord.Embed(color=config.color)
    embed2.add_field(name="useful information", value="**Thank you for adding exorium to your server <a:shibaheartbeat:755130116316856363>**.\nexorium is a multifunctional bot to fit your needs. <a:glowpaw:755131095032397874>\nFor commands, use the `exo help` command, for more info on commands you can use `exo info {command`.")
    embed2.add_field(name="useful links", value="It's possible that you may find bugs, or errors in ProtoPaw <a:Toothlessuhmwhat:753170277915164672> Or you just want to suggest something, for that you can make an [issue](https://github.com/ThePawKingdom/exorium/issues/new/choose) in our [github repo](https://github.com/ThePawKingdom/exorium).\nFurthermore, if you just need support with exorium, you can join our [support server](https://discord.gg/RQMaHzE)!")
    embed2.set_author(name=guild.name, url="https://cdn.discordapp.com/icons/" + str(guild.id) + "/" + str(guild.icon) + ".webp?size=1024", icon_url="https://cdn.discordapp.com/icons/" + str(guild.id) + "/" + str(guild.icon) + ".webp?size=1024")
    embed2.set_footer(text=f"exorium is now in (len{bot.guilds}) guilds with (len{bot.users} users")
    for channel in guild.channels:
        if await channel.send(embed=embed):
            break
    return


@bot.command(name="ping", aliases=["pong", "latency"], brief="shows the bot's latency.")  # the ping command, simply shows the latency in an embed
async def latency(ctx):
    embed = discord.Embed(color=config.color)
    embed.add_field(name="<a:loadingbounce:753173725263822858> ping", value=f'**{bot.latency:.2f}**s', inline=True)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "ping", bot)


@bot.command(name='test621')
async def test621(ctx):
    embed = discord.Embed(color=config.color)
    embed.add_field(name="__**Table of contents**__", value="[About The Paw Kingdom](https://discordapp.com/channels/715969701771083817/715987980988317737/752170795631116400)\n[Staff members](https://discordapp.com/channels/715969701771083817/715987980988317737/752171831963942962)\n[Channels](https://discordapp.com/channels/715969701771083817/715987980988317737/752173579268915250)\n[Roles](https://discordapp.com/channels/715969701771083817/715987980988317737/752177075095339058)\n[Perks](https://discordapp.com/channels/715969701771083817/715987980988317737/752178791937343560)\n[Bots](https://discordapp.com/channels/715969701771083817/715987980988317737/752178978957164594)\n[Links](https://discordapp.com/channels/715969701771083817/715987980988317737/752179008178749440)", inline=True)
    embed.add_field(name="__**External TPK communities**__", value="[Roblox community](https://www.roblox.com/groups/7604658/TPK-community#!/about)", inline=True)
    await ctx.send(embed=embed)


@bot.command()  # the help command, displays all the commands and the developers in an embed
async def help(ctx):
    embed = discord.Embed(title='Commands | `p/`, `p?`', color=config.color)
    embed.add_field(name="**<a:yoshiban:753151857852940309> Moderation**", value="`ban` `unban` `kick`\n`softban` `warn` `warnings`", inline=True)
    embed.add_field(name="**<a:TPKProtogenDance:728615119910862898> Bot Related**", value="`help` `ping` `invite` `stats` `links` `info`", inline=True)
    embed.add_field(name="**<a:pikaxe:753164460184830013> Utils**", value="`get_id` `avatar` `serverinfo` `random` `poll` `decide` `say` `say2`", inline=True)
    embed.add_field(name="**<a:tacklehug:753169705862430772> Social**", value="`hug` `snuggle` `boop`\n `kiss` `pat` `cuddle`\n `askexo` `lick` `blush`\n`feed` `glomp` `happy`\n`highfive` `wag`", inline=True)
    embed.add_field(name="**<a:Toothlessuhmwhat:753170277915164672> NSFW**", value="`e621`", inline=True)
    embed.add_field(name="**<a:TPK_ProtoBoop:740828362045653073> Developers**", value="[NeoGames#5108](https://github.com/FireGamingYT/)\n[ChosenFate#5108](https://github.com/Chosen-Fate)", inline=True)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Do ?info {command} for command info/usage")
    await ctx.send(embed=embed)
    await functions.logging(ctx, "help", bot)


@bot.command(name="invite", aliases=["inv", "oauth"], brief="Shows the bot ouath link")  # shows the bot invite with hyperlink in an embed
async def invite(ctx):
    embed = discord.Embed(color=config.color)
    embed.add_field(name="Invites", value="[Add exorium to your server](https://discord.com/api/oauth2/authorize?client_id=620990340630970425&permissions=806218999&scope=bot)\n[Join the support & community server](https://discord.gg/k64tAer)")
    await ctx.send(embed=embed)
    await functions.logging(ctx, "invite", bot)


@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")  # shows the bot statistics (total amount of users in total amount of guilds) in an embed
async def statistics(ctx):
    embed = discord.Embed(title="exorium statistics", color=config.color)
    embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
    embed.add_field(name="Total users", value=len(bot.users), inline=False)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "stats", bot)


@bot.command()  # retrieves the ID of a member. Argument can be an ID, just the user's name or the user mention
async def get_id(ctx, member: discord.Member):
    user_id = member.id
    await ctx.send('The user ID is %d.' % user_id)
    await functions.logging(ctx, "get_id", bot)


@bot.command(name='animal', help='Generates a random animal!')
async def animal(ctx):
    r = requests.get(
        'https://pixabay.com/api/',
        params={'key': config.pixabaykey, 'q': "animal", "image_type": 'photo'}
    )
    finalimg = random.choice(r.json()["hits"])["webformatURL"]
    embed = discord.Embed(title='Random animal', color=config.color)
    embed.set_image(url=finalimg)
    embed.set_footer(text='Powered by pixabay.')
    await ctx.send(embed=embed)
    await functions.logging(ctx, "animal", bot)


@bot.command()
async def e621(ctx, *, tags=''):
    if(ctx.channel.is_nsfw() or ctx.channel.id in config.nsfwexceptions):
        response = requests.get(
            'https://e621.net/posts.json',
            params={'tags': tags},
            headers={'User-Agent': config.e621agent},
            auth=HTTPBasicAuth(config.e621username, config.e621key)
        )
        finalimg = random.choice(response.json()["posts"])["file"]["url"]
        embed = discord.Embed(title='Random yiff', color=config.color)
        embed.set_image(url=finalimg)
        embed.set_footer(text='Powered by e621.')
        await ctx.send(embed=embed)
        await functions.logging(ctx, "e621", bot)
    else:
        await ctx.send("Sorry, you can only use e621 commands in an NSFW channel")
        await functions.logging(ctx, "e621_fail", bot)


@bot.command(aliases=['av'])  # shows the mentioned user's avatar in an embed
async def avatar(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    else:
        user = user
        eA = discord.Embed(title='Avatar', color=config.color)
        eA.set_author(name=user, icon_url=user.avatar_url)
        eA.set_image(url=user.avatar_url)
        await ctx.send(embed=eA)
        await functions.logging(ctx, "avatar", bot)


@bot.command(name='links', brief='Discord related links')  # shows the links related to exorium in an embed
async def links(ctx):
    embed = discord.Embed(title='exorium Links', color=config.color)
    embed.add_field(name="Github", value="[Repo](https://github.com/ThePawKingdom/protogen)\n[Organisation](https://github.com/ThePawKingdom/)", inline=True)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using exorium!")
    await ctx.send(embed=embed)
    await functions.logging(ctx, "links", bot)

    
@bot.command(name="serverinfo", aliases=["servinfo", "sinfo"])  # shows info about the server the command was executed, in an embed. Still being worked on.
async def serverinfo(ctx):
    gu = ctx.guild
    embed = discord.Embed(color=config.color)
    embed.add_field(name="Server Name", value=str(gu.name), inline=True)
    embed.add_field(name="Owner", value=str(gu.owner), inline=True)
    embed.add_field(name="Creation Date", value=f"{gu.created_at.day}/{ctx.guild.created_at.month}/{ctx.guild.created_at.year} {ctx.guild.created_at.hour}:{ctx.guild.created_at.minute}", inline=True)
    embed.add_field(name="Server ID", value=str(gu.id), inline=True)
    embed.add_field(name="Region", value=str(gu.region), inline=True)
    embed.add_field(name="Verification Level", value=str(gu.verification_level), inline=True)
    if ctx.guild.features:
        embed.add_field(name="Server Features", value=str(gu.features), inline=True)
    embed.add_field(name="Afk Channel", value=f"`{str(gu.afk_channel)}`\nTimeout {int(gu.afk_timeout)}s", inline=False)
    embed.set_author(name=ctx.guild.name + " information", url="https://cdn.discordapp.com/icons/" + str(gu.id) + "/" + str(gu.icon) + ".webp?size=1024", icon_url="https://cdn.discordapp.com/icons/" + str(gu.id) + "/" + str(gu.icon) + ".webp?size=1024")
    await ctx.send(embed=embed)
    await functions.logging(ctx, "serverinfo", bot)


@bot.command(name='variable', brief='test variables')  # to test things. Currently a way to bully people who arent a fan of furries.
async def variables(ctx):
    embed = discord.Embed(title='variable tests', color=config.color)
    embed.add_field(name='test:', value="Teh fitnyessgwam pacew test is a muwtistage aewobic capacity test that pwogwessivewy gets mowe difficuwt as it continyues. Teh 20 metew pacew test wiww begin owo in 30 seconds. Wine up at teh stawt. Teh wunnying speed stawts swowwy~ but gets fastew each minyute aftew chu heaw dis signyaw. A singwe wap shouwd be compweted each time chu heaw dis sound. Uwu wemembew uwu to wun owo in a gay winye~ and wun as wong as possibwe. Teh second time chu faiw uwu to compwete a wap befowe teh sound~ ur test is ovew. Teh test wiww begin on teh wowd stawt. On ur mawk~ get weady~ stawt.", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_author(name="The Paw Kingdom Links", url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1", icon_url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    await ctx.send(embed=embed)
    await functions.logging(ctx, "variable", bot)


@bot.command(name='snuggle', brief='Snuggling, how sweet')  # interaction command - snuggle someone. gifs are random!
async def snuggle(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "snuggle", "how cute", "snuggled")
    await functions.logging(ctx, "snuggle", bot)


@bot.command(name='hug', brief='Fandom hug!')  # interaction command - hug someone. gifs are random!
async def hug(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "hug", "how lovely", "hugged")
    await functions.logging(ctx, "hug", bot)


@bot.command(name='pat', brief='Pats, wholesome!')  # interaction command - pat someone. gifs are random!
async def pat(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "pat", "how beautiful", "pat")
    await functions.logging(ctx, "pat", bot)


@bot.command(name='boop', aliases=['bp'], brief='Boop!')  # interaction command - boop someone. gifs are random!
async def boop(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "boop", "so soft", "booped")
    await functions.logging(ctx, "boop", bot)


@bot.command(name='kiss', aliases=['smooch'], brief='Smooch!')  # interaction command - kiss someone. gifs are random!
async def kiss(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "smooch", "lovely", "smooched")
    await functions.logging(ctx, "kiss", bot)


@bot.command(name="lick", brief='Licking, lol')  # interaction command - lick someone. gifs are random!
async def lick(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "lick", "tasty", "licked")
    await functions.logging(ctx, "lick", bot)


@bot.command(name="bellyrub")  # interaction command - bellyrub someone. gifs are random!
async def bellyrub(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "bellyrub", "lovely", "bellyrubbed")
    await functions.logging(ctx, "bellyrub", bot)


@bot.command(name="cuddle")  # interaction command - cuddle someone. gifs are random!
async def cuddle(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "cuddle", "heartwarming", "cuddled")
    await functions.logging(ctx, "cuddle", bot)


@bot.command(name="rawr")  # interaction command - rawr at someone. gifs are random!
async def rawr(ctx, members: commands.Greedy[discord.Member], *, reason="Rawr!"):
    GIFlist = gifs.rawr
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**rawred, cute!**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**rawred at**" + " " + '**,** '.join(x.mention for x in members) + "**, cute!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "rawr", bot)


@bot.command(name="awoo")  # interaction command - awoo at someone. gifs are random!
async def awoo(ctx, members: commands.Greedy[discord.Member], *, reason="Awoo!"):
    GIFlist = gifs.awoo
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**awoo'd, chilling!**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**awoo'd at**" + " " + '**,** '.join(x.mention for x in members) + "**, chilling!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "awoo", bot)


@bot.command(name="blush")  # interaction command - blush (because of) someone. gifs are random!
async def blush(ctx, members: commands.Greedy[discord.Member], *, reason="Makes them kyooter!"):
    GIFlist = gifs.blush
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**blushed**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**blushed because of**" + " " + '**,** '.join(x.mention for x in members) + "**, kyoot!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "blush", bot)


@bot.command(name="feed")  # interaction command - feed someone. Gifs are random
async def feed(ctx, members: commands.Greedy[discord.Member], *, reason="Hungwy"):
    await functions.interactions(ctx, members, reason, "feed", "sweet!", "fed")
    await functions.logging(ctx, "feed", bot)


@bot.command(name="glomp")  # interaction command - glomp someone. gifs are random!
async def glomp(ctx, members: commands.Greedy[discord.Member], *, reason="Love!"):
    GIFlist = gifs.glomp
    GIF = random.choice(GIFlist)
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**glomped on**" + " " + '**,** '.join(x.mention for x in members) + "**, chilling!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "glomp", bot)


@bot.command(name="happy")  # interaction command - be happy (because of someone). gifs are random!
async def happy(ctx, members: commands.Greedy[discord.Member], *, reason="Vibing"):
    GIFlist = gifs.happy
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**Is happy**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**Is happy because of**" + " " + '**,** '.join(x.mention for x in members) + "**, kyoot!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "happy", bot)


@bot.command(name="highfive")  # interaction command - highfive someone. Gifs are random
async def highfive(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "highfive", "awesome!", "high fived")
    await functions.logging(ctx, "highfive", bot)


@bot.command(name="wag")  # interaction command - wag (because of someone). gifs are random!
async def wag(ctx, members: commands.Greedy[discord.Member], *, reason="Rawr!"):
    GIFlist = gifs.wag
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**wags their tail, kyoot!**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**wags their tail because of**" + " " + '**,** '.join(x.mention for x in members) + "**, cute!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "wag", bot)


@bot.command(name="kill")  # interaction command - highfive someone. Gifs are random
async def kill(ctx, members: commands.Greedy[discord.Member], *, reason="not paying attention"):
    await functions.interactions(ctx, members, reason, "kill", "gruesome!", "killed")
    await functions.logging(ctx, "kill", bot)


@bot.command(name='random', brief='Randomness!')  # Let exorium choose for you!
async def randomchoice(ctx, arg1, arg2):
    Arglist = [arg1, arg2]
    await ctx.send(random.choice(Arglist))
    await functions.logging(ctx, "random", bot)


@bot.command(name="info")  # Gives information about the mentioned command
async def info(ctx, arg):
    embed = discord.Embed(color=config.color)
    embed.add_field(name=arg, value=getattr(cmds, arg), inline=True)
    embed.add_field(name="Syntax of " + arg, value=getattr(syntax, arg), inline=True)
    embed.add_field(name="Developers:", value="`-` ChosenFate#5108\n`-` NeoGames#5108", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using exorium!")
    await ctx.send(embed=embed)
    await functions.logging(ctx, "info", bot)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please fill in all the required arguments.')  # Shows the command isn't completed
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the sufficient permissions.")  # Shows that you dont have the needed permission for this command
    if isinstance(error, commands.NotOwner):
        await ctx.send('Only bot owners can use this command.')  # Shows when a user executes a bot owner only command while not being a bot owner


@bot.command(name="askexo", aliases=["askexorium"])  # Lets you ask something to exorium, he will answer with a random answer listed in gifs.py
async def askexorium(ctx, *, arg):
    answers = gifs.Askexorium
    answer = random.choice(answers)
    embed = discord.Embed(color=config.color)
    embed.add_field(name=arg, value=f"Exo says {answer}", inline=False)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "askexo", bot)


@bot.command(name="ban")  # Permanently bans the user that was mentioned (user must be in guild)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't ban yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been banned from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.ban(reason=f"{ctx.message.author}: {reason}")
        embed = discord.Embed(title=f"{member} has been casted from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)
        await functions.logging(ctx, "ban", bot)


@bot.command(name='unban')  # Unbans user with a given ID
@commands.has_permissions(ban_members=True)
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    clearname = str(user).split("#")
    embed = discord.Embed(title=f"Unbanned {clearname[0]}", color=config.color)
    embed.set_footer(text=user)
    await ctx.send(embed=embed)
    await functions.logging(ctx, "unban", bot)


@bot.command(name="kick")  # Kicks the mentioned user from the guild
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't kick yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been kicked from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.kick(reason=f"{ctx.message.author}: {reason}")
        embed = discord.Embed(title=f"{member} has been kicked from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)
        await functions.logging(ctx, "kick", bot)


@bot.command(name="softban")  # bans and immediately unbans the user mentioned
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't softban yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been softbanned from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.ban(reason=f"{ctx.message.author}: {reason}")
        await member.unban()
        embed = discord.Embed(title=f"{member} has been softcasted from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)
        await functions.logging(ctx, "softban", bot)


@bot.command(name="poll")  # Makes a poll with up to 10 options, seperate choices with ,
async def poll(ctx, *, arg):
    await ctx.message.delete()
    choice = str(arg).split(",")
    n = 1
    reactionlist = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    embed = discord.Embed(title="Poll", color=config.color)
    for x in choice:
        embed.add_field(name="Option " + reactionlist[n-1], value=f"{x}", inline=False)
        n = n+1
    embed.set_footer(text=f"Poll cast by {ctx.message.author}")
    botmsg = await ctx.send(embed=embed)
    en = 1
    for emoji in reactionlist:
        await botmsg.add_reaction(emoji)
        en = en+1
        if en >= n:
            break
            await functions.logging(ctx, "poll", bot)


@bot.command(name="decide")  # Let people vote for something
async def decide(ctx, *, arg):
    await ctx.message.delete()
    embed = discord.Embed(title=arg, color=config.color)
    embed.set_footer(text=f"Asked by {ctx.message.author}")
    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction("✅")
    await botmsg.add_reaction("❌")
    await functions.logging(ctx, "decide", bot)


@bot.command(name="revive")  # Tags the role that was given with a message.
@commands.has_permissions(manage_messages=True)
async def revive(ctx):
    await ctx.message.delete()
    await ctx.send("<@&738356235841175594>! The chat is dead, we need you now!")
    await functions.logging(ctx, "revive", bot)


@bot.command()  # In an embed repeats what you said and deletes the original command
async def say(ctx, *, sentence):
    await ctx.message.delete()
    embed = discord.Embed(color=config.color)
    embed.add_field(name=sentence, value=f'by {ctx.message.author}')
    await ctx.send(embed=embed)
    await functions.logging(ctx, "say", bot)


@bot.command()  # Repeats what you said and deletes the original command
async def say2(ctx, *, sentence2):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} said:\n{sentence2}")
    await functions.logging(ctx, "say2", bot)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=0):
    if (amount <= 0):
        return await ctx.send("You can't grow younger either, so neither can I purge negative amounts of messages.")
    if (amount <= 1500):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Successfully deleted **{amount}** messages with the purge command.')
        await functions.logging(ctx, f"purge ({amount})", bot)
    if (amount >= 1500):
        await ctx.send("You can only purge 1500 messages at a time.")


@bot.command()
@commands.has_permissions(ban_members=True)
async def warn(ctx, member: discord.Member, *, reason="No reason provided"):
    sql = "INSERT INTO warnings (user, reason, serverid) VALUES (%s, %s, %s)"
    val = (member.id, reason, ctx.message.guild.id)
    database.execute(sql, val)
    mydb.commit()
    await ctx.send(f"Warned {member.mention} for {reason}")
    await functions.logging(ctx, "warn", bot)


@bot.command()
@commands.has_permissions(ban_members=True)
async def delwarn(ctx, caseID):
    database.execute("SELECT * FROM warnings WHERE id = %s AND serverid = %s", [caseID, ctx.message.guild.id])
    results = database.fetchall()
    if results:
        database.execute("DELETE FROM warnings WHERE id = %s AND serverid = %s", [caseID, ctx.message.guild.id])
        mydb.commit()
        await ctx.send(f"Removed warning #{caseID}")
        await functions.logging(ctx, "delwarn", bot)
        return
    await ctx.send("No warning with such an ID exists here. Please check again!")


@bot.command()
@commands.has_permissions(ban_members=True)
async def warnings(ctx, member: discord.Member):
    await functions.logging(ctx, "warnings", bot)
    database.execute("SELECT * FROM warnings WHERE user = %s AND serverid = %s", [member.id, ctx.message.guild.id])
    results = database.fetchall()
    if not results:
        return await ctx.send("⚠️ User has no warnings!")
    totalwarns = " "
    i = 0
    while i < len(results):
        totalwarns += f"{i+1}: Reason: {results[i][2]}\nCase #{results[i][0]}\n"
        i += 1

    await ctx.send(f"The user has a total of {len(results)} warnings")

    embed = discord.Embed(title='Warnings for ' + member.name, description=totalwarns, color=config.color)
    await ctx.send(embed=embed)


@bot.command()    
@commands.is_owner()
async def exoinfo(ctx):
    e = discord.Embed(title='exorium private information', color=config.color)
    e.add_field(name="Guilds list", value=ctx.guild.roles, inline=True)
    await ctx.send(embed=e)
    
        
class cmds:
    hug = "Hugs the pinged person, kyoot!"
    snuggle = "Snuggles the pinged persons, kyoot!"
    boop = "Boops the pinged persons, boop!"
    kiss = "Smooches the pinged persons :*"
    pat = "Pats the pinged persons, good boy!"
    ping = "Displays the latency of the bo -connection lost"
    invite = "Displays the invite link to invite TPKP to your server"
    stats = "Shows some neat stats about TPKP"
    get_id = "Gets a users Discord ID"
    av = "Gets and posts avatar of the pinged person / ID works too"
    links = "Displays some links to get to The Paw Kingdom, this bots home!"
    random = "Can't make a choice? Use the random command! Only 2 options possible at this point"
    info = "You already know what this does, derp"
    honk = "HONK"
    askexorium = "Ask exorium, and he shall give you an answer"
    unban = "Unbans the given user"
    lick = "Licks the pinged persons, yum!"
    ban = "Bans the mentioned person"
    kick = "Kicks the specified person"
    softban = "Softbans (bans and unbans) the specified"
    poll = "Cast a poll if you can't agree about something!"
    decide = "Casts a simple yes / no poll"
    cuddle = "Cuddle the pinged persons"


class syntax:
    hug = "`?hug @user1 @user2...`"
    snuggle = "`?snuggle @user1 @user2...`"
    boop = "`?boop @user1 @user2...`"
    kiss = "`?kiss  @user1 @user2...`"
    pat = "`?pat  @user1 @user2...!`"
    invite = "`?invite`"
    get_id = "`?get_id @user`"
    links = "`links`"
    info = "`?info`"
    honk = "`?honk`"
    askexo = "`?askexo <Question>`"
    lick = "`?lick @user1 @user2..."
    ban = "`?ban @user | ID Reason`"
    kick = "`?kick @user | ID reason`"
    softban = "`?softban @user | ID reason"
    poll = "`?poll choice1, choice2, choice3 [...]`"
    decide = "`?decide <question>"
    cuddle = "?cuddle @user1 @user2...`"


bot.run(config.token)
