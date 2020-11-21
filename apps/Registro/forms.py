from django import forms
from .models import Pack, Cliente

class PackForm(forms.ModelForm):
    class Meta:
        model = Pack
        fields = ['nombre', 'mensualidad']

        labels = {
            'nombre' : 'Nombre',
            'mensualidad' : 'Mensualidad Pesos Chilenos',

        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'mensualidad' : forms.TextInput(attrs={'class': 'form-control'}),
        }

