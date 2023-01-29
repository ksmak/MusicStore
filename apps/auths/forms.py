from django import forms
# Local
from .models import MyUser


class UserForm(forms.ModelForm):
    """ User form """

    class Meta:
        model = MyUser
        fields = '__all__'
        exclude = ['username']