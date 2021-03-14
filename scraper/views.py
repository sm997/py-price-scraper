from django.shortcuts import render
from scraper.scripts.core import getProductsFromAllSites

def index(request):
    result = None
    query = request.GET.getlist('inputSearch')
    excludeWords = request.GET.getlist('excludeWords')
    excludeWords = "" if len(excludeWords) == 0 else excludeWords[0]
    filters = request.GET.getlist('filter')
    print("aads", query)

    if len(query) > 0:
        result = getProductsFromAllSites(query[0], excludeWords, filters)

    return render(request, 'index.html', {'result': result})