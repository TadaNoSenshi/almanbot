import os

import discord
from discord.ext import commands
from discord.ext.commands import Bot

from cogs.core.config.config_botchannel import botchannel_check
from cogs.core.config.config_embedcolour import get_embedcolour
from cogs.core.config.config_general import resetconfig
from cogs.core.defaults.defaults_embed import get_embed_footer, get_embed_thumbnail


class adminresetconfig(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def adminresetconfig(self, ctx, guildid):
        path = os.path.join("data", "configs", f"{guildid}.json")
        if botchannel_check(ctx):
            if resetconfig(path):
                embed = discord.Embed(
                    title="**Reset Config**",
                    description=f"Die Config vom Server mit der ID```{guildid}```"
                    "wurde erfolgreich zurückgesetzt.",
                    colour=get_embedcolour(ctx.message),
                )
                embed._footer = get_embed_footer(ctx)
                embed._thumbnail = get_embed_thumbnail()
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(
                    title="**Fehler**",
                    description=f"Die Config vom Server mit der ID```{guildid}```"
                    "konnte nicht zurückgesetzt werden.",
                    colour=get_embedcolour(ctx.message),
                )
                embed._footer = get_embed_footer(ctx)
                embed._thumbnail = get_embed_thumbnail()
                await ctx.send(embed=embed)
                return
        else:
            Bot.dispatch(self.bot, "botchannelcheck_failure", ctx)


########################################################################################################################


def setup(bot):
    bot.add_cog(adminresetconfig(bot))
