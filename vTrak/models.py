from django.db import models
from django.forms import ModelForm
from django.utils import timezone


class Statustable(models.Model):
    status = models.TextField()

    def __str__(self):
        return self.status


class Typetable(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class Vehicletable(models.Model):
    vehnum = models.CharField(max_length=3)
    vehtype = models.ForeignKey('Typetable', on_delete=models.PROTECT)
    is_lpr = models.BooleanField(default='False')
    isforpatrol = models.BooleanField(default='False')
    status = models.ForeignKey('Statustable', on_delete=models.PROTECT)
    is_active = models.BooleanField(default='False')
    datetaken = models.DateTimeField(default=timezone.now)
    callsigninuse = models.CharField(max_length=7, default=False, blank=True)


    def __str__(self):
        return self.vehnum


class Squadtable(models.Model):
    squad = models.CharField(max_length=20)
    squad_desc = models.CharField(max_length=30)

    def __str__(self):
        return self.squad


class Activitytable(models.Model):
    vehnum = models.CharField(max_length=3)
    callsign = models.CharField(max_length=7)
    squad = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
