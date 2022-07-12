# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect

# Custom Library

# Custom Packages
from AthenaTwitchBot.models.bot_methods.bot_command import BotCommand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
bot_commands:dict[str:BotCommand] = {}
bot_tasks = {}

def bot_command(name:str, args:bool=False):
    def decorator(fnc):
        if isinstance(name, list):
            for n in name:
                bot_commands[n] = BotCommand(name=n, callback=fnc, args=args)
        else:
            bot_commands[name] = BotCommand(name=name, callback=fnc, args=args)
    return decorator