from scraper.scripts import scraping, parsing
from scraper.scripts.helpers import readFilesInDir, textToFile
from scraper.scripts.models.site import Site


def getProductsFromAllSites(query):
    siteJsons = readFilesInDir('../sites', '.json')
    sites = map(lambda x: Site(x), siteJsons)

    for site in sites:
        products = getProductsFromSite(site, query)
        print(site.pageName)
        for p in products: print(p)

def getProductsFromSite(site, query):
    pageHtml = scraping.getPageHtml(site.getQueryUrl(query))
    textToFile('../tmp', site.pageName + '.txt', pageHtml.text)
    productHtmlList = parsing.getProducts(pageHtml, site.productHtmlEl)


    res = []
    for productHtml in productHtmlList:
        price = parsing.getPrice(productHtml, site.priceHtmlEl)
        productName = parsing.getProductName(productHtml, site.productNameHtmlEl)
        res.append([productName, price])

    return res