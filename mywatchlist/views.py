from re import M
from django.shortcuts import render
from .models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data = MyWatchList.objects.all()
    watched = MyWatchList.objects.filter(watched=True).count()
    not_watched = MyWatchList.objects.filter(watched=False).count()
    menonton = "Selamat, kamu sudah banyak menonton!"
    if not_watched > watched:
        menonton = "Wah, kamu masih sedikit menonton!"
    context = {
        'my_watchlist': data,
        'menonton': menonton,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml") 

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")