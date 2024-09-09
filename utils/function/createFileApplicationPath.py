from os import listdir






def createFilePathToNewApplication(baseDir : str): #Создать файл новой заявки. К количеству заявок прибавляется 1, что-бы избежать повторений
    newId = len(listdir(baseDir)) + 1
    filePath = f"{baseDir}/application-{newId}.txt"

    return filePath

def createFilePathToResultModule(userId, baseDir : str):
    filePath = f"{baseDir}/{userId}.txt"
    return filePath
    


