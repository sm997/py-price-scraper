from bs4 import BeautifulSoup

from scraper.scripts import scraping, parsing
from scraper.scripts.parsing import hasElementWithAttr

pageHtml = scraping.getPageHtml("https://www.mimovrste.com/apple-iphone-11?s=iphone%2011&src=sugHist")

productHtmlList = parsing.getProducts(pageHtml, "article")
#print('produkti----->', productHtmlList)

for prHtml in productHtmlList:
    hasEl = hasElementWithAttr(prHtml, "product-availability", "is-available", "1")



