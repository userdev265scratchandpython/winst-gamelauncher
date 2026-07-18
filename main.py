#!/usr/bin/python3
from backend import gameslist, command_handling
import shlex
import sys
import subprocess
import builtins

debug = False

builtins.__wlauncher_debug__ = debug


command_handling.__start__(gameslist, shlex, sys, subprocess)
