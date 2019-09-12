from django.shortcuts import render
from django.views.generic import TemplateView
from vTrak.forms import SquadForm, ActivityForm
from .models import Vehicletable, Squadtable, Activitytable


def home(request):

    form = ActivityForm(request.POST or None)
    if form.is_valid():
        dbsave = Activitytable.objects.create(**form.cleaned_data)
        form = ActivityForm()
    content = {
        'form': form,
        'Squadinfo': Squadtable.objects.all(),
        'Vehicleinfo': Vehicletable.objects.all(),
    }
    return render(request, 'vTrak/home.html', content)


def about(request):
    template_name = 'vTrak/about.html'
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        dbsave = Activitytable.objects.create(**form.cleaned_data)
        form = ActivityForm

    content = {'form': form}
    return render(request, template_name, content)
