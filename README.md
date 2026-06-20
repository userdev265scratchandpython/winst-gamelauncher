Winst GameLauncher

# Preamble
This software is provided as-is. It does not include any kind of warranty. You are responsible for any consequences of its use. It does not perform any verification of applications, commands or, games you run.

# Version name meaning
Each public version follows this format: <major>.<minor>.<hotfix>.<type(BC - breaking changes, CM - compatibility, SF - security fix, BF - bugfix, 00 - initial release)>.<date of release in DD-MM-YYYY format>
An example(initial release, june 20th 2026) of this model is: 1.0.0.00-20-06-2026
Each public version carries a list of private versions versioned like so: <version base, no date, no type>.<type>.<index, 01-99>
Each private version can be found in releases tab, in changelog.

# usage
This launcher can be used in these ways:
- list    : list games that you added
- launch  : launch a game from the list of games you added

# editing lists(adding or removing games)

Below is the editing guide. Where "<name>" is, it is the name you want to assign to the game, and "<command>" is an absolute path to executable file or binary, with optional arguments following it. If your path contains spaces, it must be wrapped in quotes.
## edit-list(games.txt)
Syntax : 
```
<name> ;; <command>
```
or with spaces as dashes(for visual help, will not work)
```
<name>-;;-<command>
```

## list-dir(game.d/*)
Syntax :
```
name : <name>
bin : <command>
```
or with dashes as spaces(for visual help, will not work)
```
name-:-<name>
bin-:-<command>
```
