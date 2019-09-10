from django.forms import ModelForm

from vTrak.models import Squadtable


class SquadtableForm(ModelForm):
    class Meta:
        model = Squadtable
        fields = ['squad']