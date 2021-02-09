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
