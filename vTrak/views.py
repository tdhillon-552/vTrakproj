from django.shortcuts import render
from vTrak.forms import ActivityForm
from .models import Vehicletable, Squadtable, Activitytable


def home(request):

    form = ActivityForm(request.POST or None)
    if form.is_valid():
        print("Console Log: Vehicle " + form.cleaned_data['vehnum'] + " is being checked out.")
        Vehicletable.objects.filter(vehnum=form.cleaned_data['vehnum']).update(status_id='3')
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


def log(request):
    template_name = 'vTrak/log.html'
    form = ActivityForm()
    content = {'form': form}
    return render(request, template_name, content)
