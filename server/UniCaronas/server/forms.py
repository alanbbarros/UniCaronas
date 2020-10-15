from django import forms
from server.models import Vehicle

attrs = {
    'TextInput': {"class": "form-control"}
}


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('model', 'maker', 'color', 'board')
        widgets = {
            'model': forms.TextInput(attrs=attrs['TextInput']),
            'maker': forms.TextInput(attrs=attrs['TextInput']),
            'color': forms.TextInput(attrs=attrs['TextInput']),
            'board': forms.TextInput(attrs=attrs['TextInput']),
        }
