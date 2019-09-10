from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from vTrak.forms import SquadtableForm
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
    return render(request, 'vTrak/about.html', {})


class CreateMyFormView(CreateView):
    model = Squadtable
    form_class = SquadtableForm
    template_name = 'vTrak/about.html'
    success_url = 'vTrak/success.html'



