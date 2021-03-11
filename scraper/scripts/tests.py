

from bs4 import BeautifulSoup

from scraper.scripts import scraping, parsing
from scraper.scripts.parsing import hasElementWithAttr

pageHtml = scraping.getPageHtml("https://www.mimovrste.com/apple-iphone-11?s=iphone%2011&src=sugHist")
#pageHtml = scraping.getPageHtml("https://www.bigbang.si/izdelki/?search_q=apple+watch+nike&securecode=main_search")
#pageHtml = scraping.getPageHtml("https://www.bolha.com/index.php?ctl=search_ads&keywords=iphone&page=4")

productHtmlList = parsing.getProducts(pageHtml, "article")
#print('produkti----->', productHtmlList)

a = ['sanela', 'plava']
b = ['plava', 'bbb']



for prHtml in productHtmlList:

    name  = productName = parsing.getProductName(prHtml, ".lst-product-item-title a")
    print('name',name)
    a =  parsing.getProductThumbnailImg(prHtml, ".lst-product-item-media-img", "data-src")
    print('aaa', a)




