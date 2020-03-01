from django.shortcuts import render
from vTrak.forms import ActivityForm
from .models import Vehicletable, Squadtable, Activitytable


def home(request):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        print("Console Log: Vehicle " + form.cleaned_data['vehnum'] + " is being checked out.")
        Vehicletable.objects.filter(vehnum=form.cleaned_data['vehnum']).update(status_id='3')
        Activitytable.objects.create(**form.cleaned_data)
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
        assignedcar = form.cleaned_data['vehnum']
        print("Console Log: Vehicle " + assignedcar + " is being checked out.")
        Vehicletable.objects.filter(vehnum=assignedcar).update(status_id='3', callsigninuse=form.cleaned_data['callsign'])
        Activitytable.objects.create(**form.cleaned_data)
        form = ActivityForm()

    content = {
        'form': form,
        'Squadinfo': Squadtable.objects.all(),
        'Vehicleinfo': Vehicletable.objects.all(),
    }
    return render(request, 'vTrak/about.html', content)


def log(request):
    car = 791
    content = {
        'Activityinfo': Activitytable.objects.all().order_by('-created_on'),
        'anothertest': Activitytable.objects.only('callsign').filter(vehnum=car).order_by('-created_on')[:1],

    }
    return render(request, 'vTrak/log.html', content)
