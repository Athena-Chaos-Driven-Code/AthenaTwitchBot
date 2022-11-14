# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Callable, Coroutine

# Athena Packages

# Local Imports
from AthenaTwitchBot.commands.command_logic import CommandLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class _CommandMemory:
    all_channels:dict[str:Callable]
    channel_specific:dict[tuple[str, str]:CommandLogic]

    def __init__(self):
        self.all_channels = {}
        self.channel_specific = {}

    def assign_channel_cmd(self,cmd_logic:CommandLogic, channel:str):
        """
        Method to assign a coroutine as to a specific command that is run on a specific channel
        """
        if known_coroutine:=(self.channel_specific.get(cmd_key:=(channel, cmd_logic.name),False)):
            raise KeyError(
                f"The combination of `{cmd_key}` already existed in the mapping,\nwith callback: `{known_coroutine}`"
            )
        # Else:
        self.channel_specific[cmd_key] = cmd_logic

    def assign_global_cmd(self,cmd_logic:CommandLogic):
        """
        Method to assign a coroutine as to a specific command that is allowed to run on all channels
        """
        if known_coroutine:=(self.all_channels.get(cmd_name := cmd_logic.name,False)):
            raise KeyError(
                f"The combination of `{cmd_name}` already existed in the mapping,\nwith callback: `{known_coroutine}`"
            )
        # Else:
        self.all_channels[cmd_name] = cmd_logic

    def get_command_logic(self, channel:str, cmd_name:str) -> CommandLogic|None:
        """
        Fetches the requested coroutine from the memory, corresponding to the channel and command name combination
        If the command name also exists in the "all_channels" mode, it will return that specific CommandLogic instance
        """
        if cmd_logic := (self.all_channels.get(cmd_name, False)):
            # found a coroutine that can be accessed from all chats
            return cmd_logic
        elif cmd_logic := self.channel_specific.get((channel, cmd_name), False):
            # Found a coroutine for a specific channel
            return cmd_logic
        else:
            # Failed to return a coroutine
            return None

# ----------------------------------------------------------------------------------------------------------------------
# Basically a glorified singleton
CommandMemory = _CommandMemory()