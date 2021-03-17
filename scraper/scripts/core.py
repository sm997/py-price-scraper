from scraper.scripts import scraping, parsing
from scraper.scripts.helpers import readFilesInDir, textToFile
from scraper.scripts.models.site import Site
from scraper.scripts.parsing import hasElementWithAttr, hasElement


def getProductsFromAllSites(query, excludeWords, filters):
    siteJsons = readFilesInDir('../sites', '.json')
    sites = map(lambda x: Site(x), siteJsons)
    allProducts = {}
    excluded = []
    if len(excludeWords) > 0:
        clearInput = excludeWords.replace(" ", "")
        excluded = list(map(str.lower, clearInput.split(",")))  # split excluded words and put them all to lowercae


    for site in sites:
        isSlovene = checkIsSlovene(site)
        isClassified = checkIsClassified(site)

        products = getProductsFromSite(site, query, excluded, filters, isSlovene, isClassified)
        allProducts[site.pageName] = products

    return allProducts

def getProductsFromSite(site, query, excluded, filters, isSlovene, isClassified):
    pageHtml = scraping.getPageHtml(site.getQueryUrl(query))
    textToFile('../tmp', site.pageName + '.txt', pageHtml.text)
    productHtmlList = parsing.getProducts(pageHtml, site.productHtmlEl)

    res = []
    for productHtml in productHtmlList:
        price = parsing.getPrice(productHtml, site.priceHtmlEl)
        productName = parsing.getProductName(productHtml, site.productNameHtmlEl)
        productUrl = parsing.getProductUrl(productHtml, site.productUrlHtmlHref)

        inStock =  checkStock(productHtml, site)

        if site.pageName == "Bolha":
            productThumbnail = ""
        else:
            productThumbnail = parsing.getProductThumbnailImg(productHtml, site.productThumbnailHtmlEl, site.productThumbnailHtmlAttribute)

        if ("stock" in filters and inStock) or ("stock" not in filters):
            if len(excluded)<1 or checkIfWordInList(excluded, productName):
                res.append([productName, price, productUrl, productThumbnail, inStock])


    return res

def checkStock(html, site):
    if site.inStockMethod ==  "hasElementWithAttr":
        return hasElementWithAttr(html, site.inStockEl, site.inStockAttrName, site.inStockAttrValue)
    elif site.inStockMethod ==  "hasElement":
        return hasElement(html, site.inStockEl)
    else:
        return True

def checkIfWordInList(excludedWords, title):
    clearTitle = title.replace(" ", "").lower()
    for word in excludedWords:
        if word in clearTitle:
            return False

    return True

def checkIsSlovene(site):
    if 'SLO' in site.country:
        return True
    return False

def checkIsClassified(site):
    if site.isClassifieds:
        return True
    return False




