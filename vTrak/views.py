from django.shortcuts import render
from django.views.generic import TemplateView
from vTrak.forms import SquadForm, ActivityForm
from .models import Vehicletable, Squadtable


def home(request):
    squadinfo = {
        'Squadinfo': Squadtable.objects.all()
    }
    vehinfo = {
        'Vehicleinfo': Vehicletable.objects.all()
    }

    return render(request, 'vTrak/home.html', vehinfo, squadinfo)


def about(request):
    template_name = 'vTrak/about.html'
    form = ActivityForm(data=request.POST or None)
    print(request)
    content = {'form': form}
    return render(request, template_name, content)
