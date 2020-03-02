from django.shortcuts import render
from vTrak.forms import ActivityForm, ClearCar, VehSearchForm
from .models import Vehicletable, Squadtable, Activitytable


def home(request):
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
        'Vehicleinfo': Vehicletable.objects.all(),
        'Activityinfo': Activitytable.objects.all().order_by('-created_on'),
        'anothertest': Activitytable.objects.only('callsign').filter(vehnum=car).order_by('-created_on')[:1],

    }
    return render(request, 'vTrak/log.html', content)


def history(request):

    if request.method == "POST":
        searcher = VehSearchForm(request.POST)

        if searcher.is_valid():
            newsearch = searcher.cleaned_data['vehnum']
            print("Console Log: Vehicle " + newsearch + " is being searched.")
            results = Activitytable.objects.all().filter(vehnum=newsearch).order_by('-created_on')
            searcher = VehSearchForm()

    else:
        searcher = VehSearchForm(request.POST)
        results = None

    content = {
        'results': results,
        'searcher': searcher,
        'Vehicleinfo': Vehicletable.objects.all(),
        'Activityinfo': Activitytable.objects.all().order_by('-created_on'),

    }
    return render(request, 'vTrak/history.html', content)
