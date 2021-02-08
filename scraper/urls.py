from django.urls import path
from scraper import views

urlpatterns = [
    path('', views.index, name='index'),
]