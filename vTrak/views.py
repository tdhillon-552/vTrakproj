from django.shortcuts import render
from django.views.generic import TemplateView
from vTrak.forms import SquadForm
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
    form = SquadForm(data=request.POST or None)
    if form.is_valid():
        print(form.squad)
        form = SquadForm()
    else:
        print("failed")
    content = {'form': form}
    return render(request, template_name, content)
