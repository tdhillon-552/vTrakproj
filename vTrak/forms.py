from django import forms
from django.forms import CheckboxInput

from vTrak.models import Squadtable, Statustable, Downtable, IntelStorage, IntelTypes


class SquadForm(forms.Form):
    squad = forms.ModelChoiceField(queryset=Squadtable.objects.only('squad'))


class ActivityForm(forms.Form):
    vehnum = forms.CharField(max_length=3)
    callsign = forms.CharField(max_length=7)
    squad = forms.ModelChoiceField(queryset=Squadtable.objects.only('squad'))
    status = forms.ModelChoiceField(queryset=Statustable.objects.only('status'))


class ClearCarForm(forms.Form):
    clearedvehnum = forms.CharField(max_length=3)
    backtoclear = forms.CheckboxInput()


class VehSearchForm(forms.Form):
    vehnum = forms.CharField(max_length=3)


class DownCarForm(forms.Form):
    downedvehnum = forms.CharField(max_length=3)
    reason = forms.ModelChoiceField(queryset=Downtable.objects.only('type'))
    description = forms.CharField(widget=forms.Textarea, max_length=300)


class IntelEnterForm(forms.Form):
    type = forms.ModelChoiceField(queryset=IntelTypes.objects.only('type'), label='Intel Type')
    dateoccurred = forms.CharField(max_length=20, label='Date Occurred')
    violation = forms.CharField(max_length=250, label='Violation')
    casenumber = forms.CharField(max_length=15, label='Case Number')
    arrestinfo = forms.CharField(max_length=250, label='Arrest Information', required=False)
    susdesc = forms.CharField(max_length=250, label='Suspect Description', required=False)
    susvehdesc = forms.CharField(max_length=250, label='Suspect Vehicle Description', required=False)
    vicinfo = forms.CharField(max_length=250, label='Victim Information', required=False)
    location = forms.CharField(max_length=250, label='Location')
    synopsis = forms.CharField(widget=forms.Textarea, label='Synopsis')
    witnessinterviewed = forms.BooleanField(widget=CheckboxInput, label='Witness Interviewed?', required=False)
