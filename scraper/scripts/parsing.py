from bs4 import BeautifulSoup


def getProducts(page, element):
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.select(element)
    return products

def getPrice(html, element):
    return html.select(element)[0].get_text().strip()

def getProductName(html, element):
    return html.select(element)[0].get_text().strip()

def getProductUrl(html, element):
    return html.select(element)[0]["href"].strip()

def hasElement(html, element):
    return len(html.select(element)) > 0

def hasElementWithAttr(html, element, attrName, attrValue):
    komp = html.select(element)
    if len(komp) > 0:
        return str(komp[0][attrName]) == str(attrValue)
    else:
        return False


