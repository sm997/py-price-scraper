import json

class Site:
    def __init__(self, configJson):
        self.__dict__ = json.loads(configJson)

    def getQueryUrl(self, query):
        return self.pageUrl.replace(self.replaceKeyword, query)




