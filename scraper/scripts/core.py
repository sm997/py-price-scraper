from scraper.scripts import scraping, parsing
from scraper.scripts.helpers import readFilesInDir, textToFile
from scraper.scripts.models.site import Site
from scraper.scripts.parsing import hasElementWithAttr, hasElement


def getProductsFromAllSites(query, excludeWords):
    siteJsons = readFilesInDir('../sites', '.json')
    sites = map(lambda x: Site(x), siteJsons)
    allProducts = {}

    for site in sites:
        products = getProductsFromSite(site, query, excludeWords)
        allProducts[site.pageName] = products

    print(allProducts)
    return allProducts

def getProductsFromSite(site, query, excludeWords):
    pageHtml = scraping.getPageHtml(site.getQueryUrl(query))
    textToFile('../tmp', site.pageName + '.txt', pageHtml.text)
    productHtmlList = parsing.getProducts(pageHtml, site.productHtmlEl)


    res = []
    for productHtml in productHtmlList:
        if checkStock(productHtml, site):
            price = parsing.getPrice(productHtml, site.priceHtmlEl)
            productName = parsing.getProductName(productHtml, site.productNameHtmlEl)
            productUrl = parsing.getProductUrl(productHtml, site.productUrlHtmlHref)
            if str(excludeWords) not in productName:
                res.append([productName, price, productUrl])

    return res

def checkStock(html, site):
    if site.inStockMethod ==  "hasElementWithAttr":
        return hasElementWithAttr(html, site.inStockEl, site.inStockAttrName, site.inStockAttrValue)
    elif site.inStockMethod ==  "hasElement":
        return hasElement(html, site.inStockEl)
    else:
        return True

