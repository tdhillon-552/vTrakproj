from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='vTrak-home'),
    path('down', views.down, name='vTrak-down'),
    path('log', views.log, name='vTrak-log'),
    path('history', views.history, name='vTrak-history'),
    path('report', views.exportcsv, name='vTrak-exportcsv'),
    path('intel', views.intel, name='vTrak-intel'),
    path('datahistory', views.datahistory, name='vTrak-datahistory')


]
