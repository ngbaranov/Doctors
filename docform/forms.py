from .models import Reception
from django import forms
from django.contrib.admin import widgets

class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ('date','time','patient_name','patient_info')

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.HiddenInput()