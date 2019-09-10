from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicletable, Statustable, Squadtable


def home(request):
    Squadinfo = {
        'Squadinfo': Squadtable.objects.all()
    }
    vehinfo = {
        'Vehicleinfo': Vehicletable.objects.all()
    }

    return render(request, 'vTrak/home.html', vehinfo, Squadinfo)
