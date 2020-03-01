from django.shortcuts import render
from vTrak.forms import ActivityForm, ClearCar
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
    if request.method == "POST":
        setAssigned = ActivityForm(request.POST)
        setClear = ClearCar(request.POST)

        if setAssigned.is_valid():
            assignedcar = setAssigned.cleaned_data['vehnum']
            print("Console Log: Vehicle " + assignedcar + " is being checked out.")
            Vehicletable.objects.filter(vehnum=assignedcar).update(status_id='3', callsigninuse=setAssigned.cleaned_data['callsign'])
            Activitytable.objects.create(**setAssigned.cleaned_data)
            setAssigned = ActivityForm()
        if setClear.is_valid():
            if setClear.backtoclear.check_test:
                Vehicletable.objects.filter(vehnum=setClear.cleaned_data['clearedvehnum']).update(status_id='1')
                print("Vehicle " + setClear.cleaned_data['clearedvehnum'] + " is back in service")
                setClear = ClearCar()

    else:
        setAssigned = ActivityForm(request.POST)
        setClear = ClearCar(request.POST)
    content = {
        'setAssigned': setAssigned,
        'setClear': setClear,
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
