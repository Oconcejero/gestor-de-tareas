from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    

    class Meta:
        model = Tarea
        fields = [
            'title',
            'user',  
            'description',
            'completed',
            'dateLimit',
            ]
        widgets = {
            'dateLimit': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'input-fecha',
                    'placeholder': 'Selecciona fecha y hora'
                    }),
        }