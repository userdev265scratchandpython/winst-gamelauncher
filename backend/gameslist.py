from os import path as osp
import builtins
from pathlib import Path as plibp
from os import listdir, mkdir, remove
from shutil import rmtree
import shlex, subprocess, builtins
import wgl_plugins as _Plugins

debug = builtins.__wlauncher_debug__

plugins = []
for name in dir(_Plugins):
    if not callable(getattr(_Plugins, name)):
        if hasattr(getattr(_Plugins, name), "__plugin__"):
            print(f"Loaded plugin : {name}\n"*debug, end="")
            plugins.append(name)

addonslist = []
for plugin in plugins:
    if hasattr(getattr(_Plugins, plugin), "__library__"):
        if callable(getattr(getattr(_Plugins, plugin), "__library__")):
           for I in getattr(getattr(_Plugins, plugin), "__library__")():
               addonslist.append(I)




home = str(plibp.home())

games = addonslist

if osp.exists(f"{home}/.winst-gamelauncher/games.txt") and osp.exists(f"{home}/.winst-gamelauncher/games.d") and not osp.isfile(f"{home}/.winst-gamelauncher/games.d"):
    with open(f"{home}/.winst-gamelauncher/games.txt") as file:
        for I in file.read().splitlines():
            info = I.split(" ;; ")
            if len(info) != 2:
                print(f"games.txt - line invalid : {I}\n"*debug, end="")
            else:
                print(f"found {info[0]} at {info[1]}\n"*debug, end="")
                games.append(info)
        for I in listdir(f"{home}/.winst-gamelauncher/games.d"):
            if osp.isfile(f"{home}/.winst-gamelauncher/games.d/{I}"):
                with open(f"{home}/.winst-gamelauncher/games.d/{I}") as file:
                    name = ""
                    binary = ""
                    for Y in file.read().splitlines():
                        if not Y.strip():
                            continue
                        phrazedl = Y.split(" : ")
                        if len(phrazedl) != 2:
                            print(f"games.d/{I} - line invalid {Y}\n"*debug, end="")
                        else:
                            key = phrazedl[0].strip()
                            val = phrazedl[1].strip()
                            if key == "bin":
                                binary = val
                                print(f"binary set to {val}\n"*debug, end="")
                            elif key == "name":
                                name = val
                                print(f"name set to {val}\n"*debug, end="")
                            else:
                                print(f"games.d/{I} - invalid line {Y}\n"*debug, end="")
                    if name == "":
                        print(f"no name provided for {I}, skipping\n"*debug, end="")
                    elif binary == "":
                        print(f"no binary provided for {I}, skipping\n"*debug, end="")
                    else:
                        if osp.exists(shlex.split(binary)[0]):
                            games.append([name, binary])
                        else:
                            print(f"binary of {I}({binary}) does NOT exist\n"*debug, end="")
else:
    Done = False
    fol = False
    file = False
    while not Done:
        if osp.exists(f"{home}/.winst-gamelauncher") and not osp.isfile(f"{home}/.winst-gamelauncher"):
            if osp.exists(f"{home}/.winst-gamelauncher/games.d") and osp.isdir(f"{home}/.winst-gamelauncher/games.d"):
                fol = True
            else:
                print("make dir")
                if not osp.exists(f"{home}/.winst-gamelauncher/games.d"):
                    mkdir(f"{home}/.winst-gamelauncher/games.d")
                else:
                    remove(f"{home}/.winst-gamelauncher/games.d")
            if osp.exists(f"{home}/.winst-gamelauncher/games.txt") and osp.isfile(f"{home}/.winst-gamelauncher/games.txt"):
                file = True
            else:
                print("make file")
                if not osp.exists(f"{home}/.winst-gamelauncher/games.txt"):
                    with open(f"{home}/.winst-gamelauncher/games.txt", "w") as file:
                        continue
                else:
                    rmtree(f"{home}/.winst-gamelauncher/games.txt")
        else:
            mkdir(f"{home}/.winst-gamelauncher")
        if file:
            if fol:
                Done = True
            
def get_games():
    return games
