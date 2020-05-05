from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Statustable(models.Model):
    status = models.TextField()

    def __str__(self):
        return self.status


class Typetable(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Vehicletable(models.Model):
    vehnum = models.CharField(max_length=3)
    vehtype = models.ForeignKey('Typetable', on_delete=models.PROTECT)
    is_lpr = models.BooleanField()
    isforpatrol = models.BooleanField()
    status = models.ForeignKey('Statustable', on_delete=models.PROTECT)
    is_active = models.BooleanField()
    datetaken = models.DateTimeField(default=timezone.now)
    callsigninuse = models.CharField(max_length=7, default=" ", blank=True)


    def __str__(self):
        return self.vehnum


class Squadtable(models.Model):
    squad = models.CharField(max_length=20)
    squad_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.squad


class Activitytable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    vehnum = models.CharField(max_length=3)
    status = models.ForeignKey('Statustable', on_delete=models.PROTECT)
    callsign = models.CharField(max_length=7)
    squad = models.CharField(max_length=20)
    checkout = models.DateTimeField(auto_now_add=True)
    downtype = models.CharField(max_length=20)
    down_desc = models.CharField(max_length=300)
    # checkin = models.DateTimeField(null=True, blank=True)


class Downtable(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class IntelTypes(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class IntelStorage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, default='Daily Log')
    violation = models.CharField(max_length=250)
    casenumber = models.CharField(max_length=15)
    synopsis = models.TextField()
    arrestinfo = models.CharField(max_length=250)
    susdesc = models.CharField(max_length=250)
    susvehdesc = models.CharField(max_length=250)
    vicinfo = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    dateoccurred = models.CharField(max_length=20)
    witnessinterviewed = models.BooleanField()

    def __str__(self):
        return self.type


class CarActivity(models.Model):
    vehnum = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('Statustable', on_delete=models.PROTECT)
    down_desc = models.CharField(max_length=300)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = "caractivity"
