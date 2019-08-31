from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicletable, Statustable




def home(request):
    vehinfo = {
        'Vehicleinfo': Vehicletable.objects.all()
    }


    return render(request,'vTrak/home.html',vehinfo)
