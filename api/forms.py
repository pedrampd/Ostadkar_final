from django import forms
from api import models
class OtherForm(forms.ModelForm):
    class Meta:
        model = models.OtherField
        fields = ('other',)

class MainForm(forms.ModelForm):
    class Meta:
        model = models.Main
        exclude = ('other_fk',)
