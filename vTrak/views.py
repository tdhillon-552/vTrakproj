import csv
from django.http import HttpResponse
from django.shortcuts import render
from vTrak.forms import ActivityForm, ClearCarForm, VehSearchForm, DownCarForm, IntelEnterForm
from .models import Vehicletable, Squadtable, Activitytable, Downtable, IntelTypes, IntelStorage


def home(request):
    if request.method == "POST":
        setAssigned = ActivityForm(request.POST)
        setClear = ClearCarForm(request.POST)
        setDown = DownCarForm(request.POST)

        if setAssigned.is_valid():
            assignedcar = setAssigned.cleaned_data['vehnum']
            print("Console Log: Vehicle " + assignedcar + " is being checked out.")
            Vehicletable.objects.filter(vehnum=assignedcar).update(status_id='3',
                                                                   callsigninuse=setAssigned.cleaned_data['callsign'])
            Activitytable.objects.create(**setAssigned.cleaned_data, downtype='None')
            setAssigned = ActivityForm()
        if setClear.is_valid():
            if setClear.backtoclear.check_test:
                Vehicletable.objects.filter(vehnum=setClear.cleaned_data['clearedvehnum']).update(status_id='1',
                                                                                                  callsigninuse='',)
                Activitytable.objects.create(vehnum=setClear.cleaned_data['clearedvehnum'], downtype='None', status_id='1')
                print("Console Log: Vehicle " + setClear.cleaned_data['clearedvehnum'] + " is back in service")
                setClear = ClearCarForm()

        if setDown.is_valid():
            print("Vehicle " + setDown.cleaned_data['downedvehnum'] + " is down")
            Vehicletable.objects.filter(vehnum=setDown.cleaned_data['downedvehnum']).update(status_id='2')
            Activitytable.objects.create(vehnum=setDown.cleaned_data['downedvehnum'], downtype=setDown.cleaned_data['reason'],
                                         status_id='2', down_desc=setDown.cleaned_data['description'])

            setDown = DownCarForm()

    else:
        setAssigned = ActivityForm(request.POST)
        setClear = ClearCarForm(request.POST)
        setDown = DownCarForm(request.POST)

    content = {
        'setAssigned': setAssigned,
        'setClear': setClear,
        'setDown': setDown,
        'Squadinfo': Squadtable.objects.all(),
        'Vehicleinfo': Vehicletable.objects.all(),
        'Downdescription': Activitytable.objects.all()[:1],
        # 'Downdescription': Activitytable.objects.raw('SELECT TOP 1 * WHERE status_id = 2 ORDER BY created DESC'),
    }
    return render(request, 'vTrak/home.html', content)


def about(request):
    if request.method == "POST":
        setAssigned = ActivityForm(request.POST)
        setClear = ClearCarForm(request.POST)
        setDown = DownCarForm(request.POST)

        if setAssigned.is_valid():
            assignedcar = setAssigned.cleaned_data['vehnum']
            print("Console Log: Vehicle " + assignedcar + " is being checked out.")
            Vehicletable.objects.filter(vehnum=assignedcar).update(status_id='3',
                                                                   callsigninuse=setAssigned.cleaned_data['callsign'])
            Activitytable.objects.create(**setAssigned.cleaned_data, downtype='None')
            setAssigned = ActivityForm()
        if setClear.is_valid():
            if setClear.backtoclear.check_test:
                Vehicletable.objects.filter(vehnum=setClear.cleaned_data['clearedvehnum']).update(status_id='1',
                                                                                                  callsigninuse='',)
                Activitytable.objects.create(vehnum=setClear.cleaned_data['clearedvehnum'], downtype='None', status_id='1')
                print("Console Log: Vehicle " + setClear.cleaned_data['clearedvehnum'] + " is back in service")
                setClear = ClearCarForm()

        if setDown.is_valid():
            print("Vehicle " + setDown.cleaned_data['downedvehnum'] + " is down")
            Vehicletable.objects.filter(vehnum=setDown.cleaned_data['downedvehnum']).update(status_id='2')
            Activitytable.objects.create(vehnum=setDown.cleaned_data['downedvehnum'], downtype=setDown.cleaned_data['reason'],
                                         status_id='2', down_desc=setDown.cleaned_data['description'])

            setDown = DownCarForm()

    else:
        setAssigned = ActivityForm(request.POST)
        setClear = ClearCarForm(request.POST)
        setDown = DownCarForm(request.POST)

    content = {
        'setAssigned': setAssigned,
        'setClear': setClear,
        'setDown': setDown,
        'Squadinfo': Squadtable.objects.all(),
        'Vehicleinfo': Vehicletable.objects.all(),
        'Downdescription': Activitytable.objects.all().order_by('-created').filter(status_id__exact=2),
    }
    return render(request, 'vTrak/home.html', content)


def log(request):
    # car = 791
    content = {
        'Vehicleinfo': Vehicletable.objects.all(),
        'Activityinfo': Activitytable.objects.all().order_by('-checkout'),
        # 'anothertest': Activitytable.objects.only('callsign').filter(vehnum=car).order_by('-checkout')[:1],

    }
    return render(request, 'vTrak/log.html', content)


def history(request):
    if request.POST:
        searcher = VehSearchForm(request.POST)

        if searcher.is_valid():
            newsearch = searcher.cleaned_data['vehnum']
            request.session['vehnumtoexport'] = newsearch
            print("Console Log: Vehicle " + newsearch + " is being searched.")
            results = Activitytable.objects.all().filter(vehnum=newsearch).order_by('-checkout')
    else:
        searcher = VehSearchForm(request.POST)
        results = VehSearchForm(request.POST)

    content = {
        'results': results,
        'searcher': searcher,
    }
    return render(request, 'vTrak/history.html', content)


def exportcsv(request):
    vehnumtoexport = request.session.get('vehnumtoexport')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export-' + vehnumtoexport + '.csv"'
    writer = csv.writer(response)
    writer.writerow(['Vehicle Number', 'Call Sign', 'Squad', 'Check out Time'])
    export = Activitytable.objects.values_list('vehnum', 'callsign', 'squad', 'checkout', 'downtype', 'down_desc').filter(
        vehnum=vehnumtoexport).order_by('-checkout')

    for exports in export:
        writer.writerow(exports)

    return response


def intel(request):

    if request.method == "POST":
        print("TEST")
        setdata = IntelEnterForm(request.POST)

        if setdata.is_valid():
            print("Console Log: Log is being sent out")
            IntelStorage.objects.create(**setdata.cleaned_data)
            setdata = IntelEnterForm()
    else:
        setdata = IntelEnterForm(request.POST)
        print("FAIL")

    content = {
        'setdata': setdata,
        'IntelStorage': IntelStorage.objects.all(),
    }

    return render(request, 'vTrak/intel.html', content)
