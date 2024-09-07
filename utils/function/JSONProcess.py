from json import load, dump
from pathlib import Path






def getChannelUrl(channelNumber : int) -> str:
    with open(Path('importantFiles','config.json'), "r") as readJSON:
        return str(load(readJSON)["channelUrl" + str(channelNumber)])
    

def editChannelUrl(channelNumber : int, newURL : str) -> None:
    with open(Path('importantFiles','config.json'), "r") as readJSON:
        dataNow = load(readJSON)
        dataNow["channelUrl" + str(channelNumber)] = newURL

    with open(Path('importantFiles','config.json'), "w") as writeJSON:
        
        dump(dataNow, writeJSON, indent=4)



def getOnlineTestLink():
    with open(Path('importantFiles','config.json'), "r") as readJSON:
        return str(load(readJSON)["onlineTest"])
    




        
    
    
