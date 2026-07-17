#!/usr/bin/python3
import shlex, sys, subprocess
import builtins

debug = False

builtins.__wlauncher_debug__ = debug

from backend import gameslist, command_handling

command_handling.__start__(gameslist, shlex, sys, subprocess)
