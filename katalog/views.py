from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'daftar_katalog': data_katalog,
    }
    return render(request, "katalog.html", context) 