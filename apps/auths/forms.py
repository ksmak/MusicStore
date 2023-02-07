# Django 
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

# Local
from .models import MyUser


class UserForm(forms.ModelForm):
    """ User form """

    class Meta:
        model = MyUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'is_active',
            'is_superuser'
        )


class UserRegisterForm(forms.ModelForm):
    EMAIL_SERVICES = (
        'gmail.com',
        'mail.ru',
        'yahoo.com',
        'outlook.com'
    )

    ERROR_EMAIL_INVALID = "Client's email is invalid"
    ERROR_EMAIL_TOO_LONG = "Client's email is too long"
    ERROR_EMAIL_TOO_SHORT = "Client's email is too short"
    ERROR_PASSWORD_INVALID = 'Password is invalid'
    ERROR_PASSWORD_TOO_LONG = "Password is too long"
    ERROR_PASSWORD_TOO_SHORT = "Password is too short"
    ERROR_PASSWORD_NOT_SAME = "Passwords is not same"

    EMAIL_MIN_LENGTH = 10
    EMAIL_MAX_LENGTH = 50

    PASSWORD_MIN_LENGTH = 12
    PASSWORD_MAX_LENGTH = 24

    DIGITS = "0123456789"
    SYMBOLS = "~!@#$%^&*()-+="
    ALPHABET = "abcdefghijklmnopqrstvwxyz"
    
    email = forms.EmailField(
        label='Почта'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Повторите пароль'
    )

    class Meta:
        model = MyUser
        fields = (
            'email',
            'password',
        )

    def clean(self) -> None:
        super().clean()
        
        email: str = self.cleaned_data['email']
        password: str = self.cleaned_data['password']
        password2: str = self.cleaned_data['password2']

        password = password.lower()
        password2 = password2.lower()

        # 0
        if password != password2:
            raise ValidationError(self.ERROR_PASSWORD_NOT_SAME)

        # 1
        email_parts: list[str] = email.split('@')
        if not (len(email_parts) == 2 and email_parts[1] in self.EMAIL_SERVICES):
            raise ValidationError(self.ERROR_EMAIL_INVALID)
        
        # 2
        if len(email) < self.EMAIL_MIN_LENGTH:
            raise ValidationError(self.ERROR_EMAIL_TOO_SHORT)
        
        if len(email) > self.EMAIL_MAX_LENGTH:
            raise ValidationError(self.ERROR_EMAIL_TOO_LONG)
        
        # 3
        if email[0] in self.DIGITS:
            raise ValidationError(self.ERROR_EMAIL_INVALID)
        
        count = 0
        for s in email_parts[0]:
            if s in self.DIGITS:
                count += 1
                if count > 1:
                    raise ValidationError(self.ERROR_EMAIL_INVALID)
        
        # 4
        if len(password) < self.PASSWORD_MIN_LENGTH:
            raise ValidationError(self.ERROR_PASSWORD_TOO_SHORT)
        
        if len(password) > self.PASSWORD_MAX_LENGTH:
            raise ValidationError(self.ERROR_PASSWORD_TOO_LONG)
        
        # 5
        is_digit = False
        for s in password:
            if s in self.DIGITS:
                is_digit = True
                break
        
        is_symbol = False
        for s in password:
            if s in self.SYMBOLS:
                is_symbol = True
                break
        
        is_alphabet = False
        for s in password:
            if s in self.ALPHABET:
                is_alphabet = True
                break
        
        if not (is_digit and is_symbol and is_alphabet):
            raise ValidationError(self.ERROR_PASSWORD_INVALID)


class UserLoginForm(forms.Form):
    """User login form."""
    email = forms.EmailField(
        label='Почта'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль'
    )

    class Meta:
        model = MyUser
        fields = (
            'email',
            'password',
        )        