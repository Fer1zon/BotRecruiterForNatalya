from json import load, dump
from pathlib import Path






def getChannelUrl(channelNumber : int) -> str:
    with open(Path('importantFiles','config.json'), "r") as readJSON:
        return load(readJSON)["channelUrl" + str(channelNumber)]
    

def editChannelUrl(channelNumber : int, newURL : str) -> None:
    with open(Path('importantFiles','config.json'), "r") as readJSON:
        dataNow = load(readJSON)
        dataNow["channelUrl" + str(channelNumber)] = newURL

    with open(Path('importantFiles','config.json'), "w") as writeJSON:
        
        dump(dataNow, writeJSON, indent=4)



editChannelUrl(1, "PASS1")
editChannelUrl(2, "PASS2")

        
    
    
