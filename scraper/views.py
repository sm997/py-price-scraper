from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def getPageHtml(query):
    URL = 'https://www.mimovrste.com/iskanje?s=' + query
    page = requests.get(URL)

    return page

def getProducts(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all('article')
    res = []
    for product in products:
        price = product.select(".lst-product-item-price-value")[0].get_text().strip()
        productName = product.select(".lst-product-item-title a")[0].get_text().strip()
        res.append([productName, price])
    return res


def index(request):
    result = None
    query = request.GET.get('product') if 'product' in request.GET else None

    if query is not None:
        #scraping
        pageHtml = getPageHtml(query)
        #print(pageHtml.text.count("Zadnji kos!"))
        result = getProducts(pageHtml)



    return render(request, 'index.html', {'result': result})