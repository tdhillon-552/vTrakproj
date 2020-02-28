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
        'Activityinfo': Activitytable.objects.all(),
    }
    return render(request, 'vTrak/about.html', content)


def log(request):
    content = {
        'Vehicleinfo': Vehicletable.objects.all(),
        'Activityinfo': Activitytable.objects.all().order_by('-created_on'),
    }
    return render(request, 'vTrak/log.html', content)
