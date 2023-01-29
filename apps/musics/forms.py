from django import forms
# Local
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


class TempForm(forms.Form):
    """ Music form """

    title = forms.CharField(
        max_length=100,
        label='Заголовок'
    )
    duration = forms.TimeField(
        required=True,
        label='Длительность',
        widget=forms.TimeInput(
            attrs={
                'type': 'time'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='Описание'
    )