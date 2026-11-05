from django import forms
from . import models as mo


class AutorForm(forms.ModelForm):
    class Meta:
        model = mo.Autor
        fields = [
            'nombre',
            'pseudonimo',
            'nacionalidad',
            'fecha_nacimiento',
            'fecha_defuncion',
            'biografia'
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Autor...',
                    'type': 'text'
                }
            ),
            'pseudonimo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pseudónimo Autor...',
                    'type': 'text'
                }
            ),
            'nacionalidad': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'DD/MM/YYYY'
                }
            ),
            'fecha_defuncion': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'placeholder': 'DD/MM/YYYY'
                }
            ),
            'biografia': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nacionalidad'].empty_label = '-- Selecciona una opción --'