from django.contrib import admin
from .models import Vehicletable, Statustable, Typetable, Squadtable, Downtable

admin.site.register(Vehicletable)
admin.site.register(Statustable)
admin.site.register(Typetable)
admin.site.register(Squadtable)
admin.site.register(Downtable)
