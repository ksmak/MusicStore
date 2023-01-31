# Django modules
from django import forms

# Project modules
from .models import Music


class MusicForm(forms.ModelForm):
    """ Music form """

    class Meta:
        model = Music
        fields = '__all__'
        widgets = {
            'duration': forms.TimeInput(
                attrs={'type': 'time'}
            )
        }
