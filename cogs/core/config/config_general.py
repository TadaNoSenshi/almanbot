import json
import os
from shutil import copyfile
from config import (
    DEFAULT_PREFIX,
    DEFAULT_EMBEDCOLOUR,
    DEFAULT_MEMESOURCE,
    DEFAULT_TRIGGER,
    DEFAULT_TRIGGER_LIST,
    DEFAULT_BUTTONCOLOUR,
)
from discord.ext import commands


class config_general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# general Config things


def get_defaultconfig():
    data = {
        "prefix": DEFAULT_PREFIX,
        "blacklist": [],
        "botchannel": [],
        "memechannel": [],
        "autoroles": [],
        "memesource": DEFAULT_MEMESOURCE,
        "embedcolour": DEFAULT_EMBEDCOLOUR,
        "buttoncolour": DEFAULT_BUTTONCOLOUR,
        "deactivated_commands": [],
        "trigger": {
            "triggerlist": DEFAULT_TRIGGER_LIST,
            "triggermsg": DEFAULT_TRIGGER,
        },
        "errors": {
            "commandnotfound": False,
            "missing_permissions": True,
            "missing_argument": True,
            "wrong_channel": True,
            "badargument": True,
        },
        "welcome_messages": {"active": False, "channel": None},
        "leave_messages": {"active": False, "channel": None},
        "tags": {"list": [], "tagmsg": {}},
        "levelling": {
            "messages": False,
            "spam_allowed": False,
            "activated": False,
        },
    }
    return data


def config_check(guildid):
    path = os.path.join("data", "configs", f"{guildid}.json")
    if os.path.isfile(path):
        return True
    return False


def config_fix(guildid):
    path = os.path.join("data", "configs", f"{guildid}.json")
    pathcheck = os.path.join("data", "configs", "deleted", f"{guildid}.json")
    if os.path.isfile(pathcheck):
        copyfile(pathcheck, path)
        os.remove(pathcheck)
        return
    data = get_defaultconfig()
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def resetconfig(path):
    os.remove(path=path)
    with open(path, "w") as f:
        data = get_defaultconfig()
        json.dump(data, f, indent=4)
    return True


########################################################################################################################


def setup(bot):
    bot.add_cog(config_general(bot))
