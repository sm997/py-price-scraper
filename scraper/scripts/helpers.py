import io
import os

def readFile(fileName):
    file = open(fileName, mode='r')
    content = file.read()
    file.close()
    return content

def readFilesInDir(dir, ext):
    scriptDir = os.path.dirname(__file__)
    absDirPath = os.path.join(scriptDir, dir)
    res = []
    for file in os.listdir(absDirPath):
        if file.endswith(ext):
            content = readFile(os.path.join(absDirPath, file))
            res.append(content)
    return res

def textToFile(dir, file, text):
    scriptDir = os.path.dirname(__file__)
    absDirPath = os.path.join(scriptDir, dir)
    with open(os.path.join(absDirPath, file), "w", encoding="utf-8") as f:
        f.write(text)
        f.close()

