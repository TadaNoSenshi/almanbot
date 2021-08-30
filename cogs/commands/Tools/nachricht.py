import datetime
import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument, Bot

from cogs.core.config.config_botchannel import get_botchannel_obj_list, botchannel_check
from config import ICON_URL, THUMBNAIL_URL, FOOTER, WRONG_CHANNEL_ERROR
from cogs.core.functions.functions import (
    get_author,
)
from cogs.core.config.config_prefix import get_prefix_string
from cogs.core.config.config_embedcolour import (
    get_embedcolour,
    get_embedcolour_code,
    embedcolour_check,
)
from cogs.core.config.config_embedcolour import embedcolour_check
from cogs.core.functions.logging import log


class nachricht(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nachricht(
        self, ctx, title, colour, channel: discord.TextChannel, *, message
    ):
        time = datetime.datetime.now()
        user = ctx.author.name
        name = ctx.channel.name
        msg2 = ctx.message
        mention = ctx.author.mention
        if botchannel_check(ctx):
            try:
                if embedcolour_check(colour):
                    colour = get_embedcolour_code(colour)
                else:
                    colour = get_embedcolour(ctx.message)
                embed = discord.Embed(
                    title=f"**{title}**", description=message, colour=colour
                )
                embed.set_footer(
                    text=FOOTER[0]
                    + str(user)
                    + FOOTER[1]
                    + str(get_author())
                    + FOOTER[2]
                    + str(get_prefix_string(ctx.message)),
                    icon_url=ICON_URL,
                )
                await channel.send(embed=embed)
                embed = discord.Embed(
                    title="**Nachricht**", colour=get_embedcolour(ctx.message)
                )
                embed.set_thumbnail(url=THUMBNAIL_URL)
                embed.set_footer(
                    text=FOOTER[0]
                    + str(user)
                    + FOOTER[1]
                    + str(get_author())
                    + FOOTER[2]
                    + str(get_prefix_string(ctx.message)),
                    icon_url=ICON_URL,
                )
                embed.add_field(
                    name="‎",
                    value=f"Die Nachricht wurde erfolgreich in den Channel {channel.mention}"
                    " geschickt!",
                    inline=False,
                )
                await ctx.send(embed=embed)
                log(
                    text=f"{time}: Der Nutzer {user} hat mit dem Befehl {get_prefix_string(ctx.message)}nachricht"
                    f" eine Nachricht in #{channel} gesendet.",
                    guildid=ctx.guild.id,
                )
            except Exception:
                embed = discord.Embed(
                    title="**Fehler**", colour=get_embedcolour(ctx.message)
                )
                embed.set_footer(
                    text=FOOTER[0]
                    + str(user)
                    + FOOTER[1]
                    + str(get_author())
                    + FOOTER[2]
                    + str(get_prefix_string(ctx.message)),
                    icon_url=ICON_URL,
                )
                embed.add_field(
                    name="‎",
                    value="Ich habe nicht die nötigen Berrechtigungen um diesen Befehl auszuführen!",
                    inline=False,
                )
                await ctx.send(embed=embed)
                log(
                    text=str(time)
                    + ": Der Bot hatte nicht die nötigen Berrechtigungen um "
                    + get_prefix_string(ctx.message)
                    + "nachricht auszuführen.",
                    guildid=ctx.guild.id,
                )
        else:
            Bot.dispatch(self.bot, "botchannelcheck_failure", ctx)


########################################################################################################################


def setup(bot):
    bot.add_cog(nachricht(bot))
