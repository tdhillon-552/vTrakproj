from django.contrib import admin
from .models import Vehicletable, Statustable, Typetable, Squadtable

admin.site.register(Vehicletable)
admin.site.register(Statustable)
admin.site.register(Typetable)
admin.site.register(Squadtable)
