from pathlib import Path




def getCommandsList():
    path = Path("utils","messageContent","startMessageContent","adminCommands.txt")

    with open(path, "r", encoding="utf-8") as file:
        return file.read()