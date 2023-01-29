# Python modules
import random
# Django modules
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db import models
# Local
from abstracts.models import AbstractModel


class MyUserManager(BaseUserManager):
    """ Custom user model manager"""
    def create_user(self, email, password):
        if not email:
            raise ValueError("Email is invalid!")
        
        if not password:
            raise ValueError("Passwor is invalid!")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin, AbstractModel):
    """ Custom user model """

    MAX_ACTIVATION_CODE_SIZE = 32

    email = models.EmailField(
        verbose_name='почта',
        primary_key=True
    )

    first_name = models.CharField(
        verbose_name='имя',
        max_length=50,
        null=True,
        blank=True
    )
    
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=50,
        null=True,
        blank=True
    )

    middle_name = models.CharField(
        verbose_name='отчество',
        max_length=50,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        verbose_name='активность',
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name='является суперпользователем',
        default=False
    )

    date_joined = models.DateTimeField(
        verbose_name='дата последнего входа',
        auto_now=True
    )

    activation_code = models.CharField(
        verbose_name='код активации',
        max_length=32,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self) -> str:
        return f'{self.email}'

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    def _get_activation_code(self, code_len: int):
        digits = '0123456789'
        alfabet = 'ABCDEFGHJKLMNOPQRSTVWXYZ'
        symbols = digits + alfabet
        code = []
        for _ in range(code_len):
            code.append(symbols[random.randint(0, len(symbols) - 1)])
        
        return ''.join(code)


    def save(self, *args, **kwargs):
        self.activation_code = self._get_activation_code(self.MAX_ACTIVATION_CODE_SIZE)
        super().save(*args, **kwargs)