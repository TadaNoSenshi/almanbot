import json
import os
from main import client
from discord.ext import commands


class config_botchannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Botchannel


def botchannel_check(ctx):
    channelid = ctx.channel.id
    message = ctx.message
    ids = get_botchannel(message=message)
    if channelid in ids or ids == []:
        return True
    return False


def get_botchannel(message):
    path = os.path.join("data", "configs", f"{message.guild.id}.json")
    with open(path, "r") as f:
        data = json.load(f)
    if not isinstance(data["botchannel"], list):
        data["botchannel"] = []
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    return data["botchannel"]


def get_botchannel_obj_list(ctx):
    list = get_botchannel(ctx.message)
    string = "".join([client.get_channel(id).mention + ", " for id in list])[:-2]
    return str(string)


########################################################################################################################


def setup(bot):
    bot.add_cog(config_botchannel(bot))
