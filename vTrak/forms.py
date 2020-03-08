from django import forms

from vTrak.models import Squadtable


class SquadForm(forms.Form):
    squad = forms.ModelChoiceField(queryset=Squadtable.objects.only('squad'))


class ActivityForm(forms.Form):
    vehnum = forms.CharField(max_length=3)
    callsign = forms.CharField(max_length=7)
    squad = forms.ModelChoiceField(queryset=Squadtable.objects.only('squad'))


class ClearCarForm(forms.Form):
    clearedvehnum = forms.CharField(max_length=3)
    backtoclear = forms.CheckboxInput()


class VehSearchForm(forms.Form):
    vehnum = forms.CharField(max_length=3)
