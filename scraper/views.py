from django.shortcuts import render
from scraper.scripts.core import getProductsFromAllSites
import time

def index(request):
    result = None
    query = request.GET.getlist('inputSearch')
    excludeWords = request.GET.getlist('excludeWords')
    excludeWords = "" if len(excludeWords) == 0 else excludeWords[0]
    filters = request.GET.getlist('filter')

    if len(query) > 0:
        start_time = time.time()
        result = getProductsFromAllSites(query[0], excludeWords, filters)
        print("--- %s seconds ---" % (time.time() - start_time))




    return render(request, 'index.html', {'result': result})
