from django import forms
from Mobiliario.models import Mobiliario

class FormularioMobiliario(forms.ModelForm):
    class Meta:
        model = Mobiliario
        fields = '__all__'