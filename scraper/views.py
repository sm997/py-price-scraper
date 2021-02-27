from django.shortcuts import render
from scraper.scripts.core import getProductsFromAllSites

def index(request):
    result = None
    query = request.GET.get('product') if 'product' in request.GET else None

    if query is not None:
        result = getProductsFromAllSites(query)

    return render(request, 'index.html', {'result': result})