from django import forms
from .models import Hardware

class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = ['sn', 'inventn', 'created', 'model']
