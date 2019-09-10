from django import forms

from vTrak.models import Squadtable


class SquadForm(forms.Form):
    squad = forms.ModelChoiceField(queryset=Squadtable.objects.only('squad'))
