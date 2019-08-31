from django.db import models
from django.utils import timezone

class Statustable(models.Model):
    status = models.TextField()
    def __str__(self):
        return self.status

class Vehicletable(models.Model):
    vehnum = models.PositiveSmallIntegerField()
    vehtype = models.TextField()
    is_lpr = models.BooleanField(default='False')
    isforpatrol = models.BooleanField(default='False')
    status = models.ForeignKey('Statustable', on_delete=models.PROTECT)
    is_active = models.BooleanField(default='False')
    datetaken = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.vehnum
