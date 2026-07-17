# path:
wgl_plugins/<whatever you want>.py
# attributes exposed
attribute           type            expected return type    description                                                                                 example return
__command__         function        none                    what you run in your module if it gets invoked, optionnal                                   None
__command_desc__    function        string                  description for __command__, required if making __command__                                 "Description of command"
__library__         function        list                    required if you don't make __command__, returns a list of names and commands to run them    [["Name1","Command1"],["Name2","Command2"]]
__plugin__          any             none                    required, lets the tool know your file is a plugin                                          None
