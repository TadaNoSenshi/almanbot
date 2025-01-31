import datetime

import discord
from discord.ext import commands
from discord.ext.commands import Bot

from cogs.core.config.config_botchannel import botchannel_check
from cogs.core.config.config_embedcolour import embedcolour_check
from cogs.core.config.config_embedcolour import (
    get_embedcolour,
    get_embedcolour_code,
)
from cogs.core.config.config_prefix import get_prefix_string
from cogs.core.defaults.defaults_embed import get_embed_thumbnail, get_embed_footer
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
        if botchannel_check(ctx):
            try:
                if embedcolour_check(colour):
                    colour = get_embedcolour_code(colour)
                else:
                    colour = get_embedcolour(ctx.message)
                embed = discord.Embed(
                    title=f"**{title}**", description=message, colour=colour
                )
                embed._footer = get_embed_footer(ctx)
                await channel.send(embed=embed)
                embed = discord.Embed(
                    title="**Nachricht**", colour=get_embedcolour(ctx.message)
                )
                embed._footer = get_embed_footer(ctx)
                embed._thumbnail = get_embed_thumbnail()
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
                embed._footer = get_embed_footer(ctx)
                embed._thumbnail = get_embed_thumbnail()
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
