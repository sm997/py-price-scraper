from bs4 import BeautifulSoup


def getProducts(page, element):
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all(element)
    return products

def getPrice(html, element):
    return html.select(element)[0].get_text().strip()

def getProductName(html, element):
    return html.select(element)[0].get_text().strip()
