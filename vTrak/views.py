from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicletable, Statustable, Squadtable


def home(request):
    squadinfo = {
        'Squadinfo': Squadtable.objects.all()
    }
    vehinfo = {
        'Vehicleinfo': Vehicletable.objects.all()
    }

    return render(request, 'vTrak/home.html', vehinfo, squadinfo)


def about(request):
    squadinfo = {
        'Squadinfo': Squadtable.objects.all()
    }

    return render(request, 'vTrak/about.html', squadinfo)
