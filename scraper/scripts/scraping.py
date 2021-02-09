import requests


def getPageHtml(pageUrl):
    page = requests.get(pageUrl)
    return page