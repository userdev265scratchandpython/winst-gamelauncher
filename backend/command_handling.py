import wgl_plugins as _Plugins
def start0(gameslist, builtins):
    global plugins, command, comdescs, debug
    debug = debug = builtins.__wlauncher_debug__
    plugins = []
    for name in dir(_Plugins):
        if not callable(getattr(_Plugins, name)):
            if hasattr(getattr(_Plugins, name), "__plugin__"):
                print(f"Loaded plugin : {name}\n"*debug, end="")
                plugins.append(name)

    commands = {}
    comdescs = {}
    for plugin in plugins:
        if hasattr(getattr(_Plugins, plugin), "__command__"):
            if callable(getattr(getattr(_Plugins, plugin), "__command__")):
                commands[plugin] = getattr(
                    getattr(_Plugins, plugin), "__command__")
                comdescs[plugin] = getattr(
                    getattr(_Plugins, plugin), "__command_desc__")()
    gameslist.start0(debug)

def __start__(gameslist, shlex, sys, subprocess):
    if len(sys.argv) < 2:
        print(f"Usage : {sys.argv[0]} [function]")
        print("Official functions: ")
        print("- list          :                                     list games")
        print("- launch <game> :                                    open <game>")
        print("- cinfo <game>  : information about where the game entry is from")
        hasaddons = len(comdescs) > 0
        print("Add-ons: \n"*hasaddons, end="")
        for I in comdescs:
            print(I + " : " + comdescs[I])
        print("Information")
        print("To add games, edit '<homepath>/.winst-gamelauncher/games.txt' or add a formatted file following the wiki in '<homepath>/.winst-gamelauncher/games.d' where '<homepath>' is your user's folder.")
        exit()

    def run_command(command):
        subprocess.run(shlex.split(command))
    gs = {}
    games, gs['fol'], gs['fil'] = gameslist.get_games()

    def cinfo(name=None):
        if name == None:
            print("Please provide a name.")
        else:
            gnames = []
            gsources = []
            for game in games:
                gnames.append(game[0])
            gsources = [gs['fol'], gs['fil']]
            if name in gnames:
                sg = False
                source: 0
                for X in gsources:
                    for I in X:
                        if X == gsources[0]:
                            if name == I:
                                print("Entry source: games list DIR")
                                sg = True
                        elif name in gs['fil']:
                            if name == I:
                                print("Entry source: Games list FILE")
                                sg = True
                if not sg:
                    print("Entry source: Addon")
            else:
                print("Game not found.")
    def list():
        longest = 0
        for I in games:
            if len(I[0]) > longest:
                longest = len(I[0])
        if debug:
            print(games)
        for I in games:
            print(I[0] + str(" "*int(longest+2-len(I[0]))) + I[1])

    def launch(game):
        counter = 0
        matching = []
        for I in games:
            if game.lower() == I[0].lower():
                counter += 1
                matching.append(I)
        if counter > 1:
            print("Multiple instances of game name found.")
            number = 0
            for I in matching:
                number += 1
                print(f"{number}) {I[0]} - {I[1]}")
            a = int(input("launch which one(number, 0 to cancel)? "))
            if a == 0:
                exit()
            else:
                b = a-1
                run_command(matching[b][1])
        elif counter == 1:
            run_command(matching[0][1])
        else:
            print(f"No matches found for : {game}")

    if sys.argv[1] == "list":
        list()
    elif sys.argv[1] == "launch":
        if len(sys.argv) == 2:
            print("Error: command launch requires a game name following it.")
        else:
            launch(sys.argv[2])
    elif sys.argv[1] == "cinfo":
        if len(sys.argv) == 2:
            print("Error: command launch requires a game name following it.")
        else:
            cinfo(sys.argv[2])
    else:
        if sys.argv[1] in commands:
            commands[sys.argv[1]](sys.argv[2:] if len(sys.argv) > 2 else [])
        else:
            print("Invalid option.")
