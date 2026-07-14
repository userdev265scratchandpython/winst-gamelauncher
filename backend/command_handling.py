def __start__(gameslist, shlex, sys, subprocess):
    if len(sys.argv) < 2:
        print(f"Usage : {sys.argv[0]} [function]")
        print("Functions : ")
        print("- list          :  list games")
        print("- launch <game> : open <game>")
        print("To add games, edit '<homepath>/.winst-gamelauncher/games.txt' or add a formatted file following the wiki in '<homepath>/.winst-gamelauncher/games.d' where '<homepath>' is your user's folder.")
        exit()

    def run_command(command):
        subprocess.run(shlex.split(command))

    games = gameslist.get_games()

    def list():
        longest = 0
        for I in games:
            if len(I[0]) > longest:
                longest = len(I[0])
        for I in games:
            print(I[0] + str(" "*int(longest+2-len(I[0]))) + I[1])

    def launch(game):
        counter = 0
        matching = []
        for I in games:
            if game.lower() == I[0].lower():
                counter+=1
                matching.append(I)
        if counter > 1:
            print("Multiple instances of game name found.")
            number = 0
            for I in matching:
                number+=1
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
