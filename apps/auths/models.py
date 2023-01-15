# Python modules
from typing import Any, Iterable, Optional
from random import randrange

# Django modules
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet

# Project modules
from abstracts.models import AbstractModel

class CustomUserManager(BaseUserManager):
    """ Менеджер пользователя """

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':
        if not email:
            raise ValidationError("Не указана почта")

        user: CustomUser = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':
        if not email:
            raise ValidationError("Не указана почта")

        user: CustomUser = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(
    AbstractBaseUser,
    PermissionsMixin,
    AbstractModel
):
    email = models.EmailField(
        verbose_name="почта",
        unique=True
    )

    first_name = models.CharField(
        verbose_name='first_name',
        max_length=60,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        verbose_name='last_name',
        max_length=70,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        verbose_name="активность",
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name="является суперпользователем",
        default=False
    )

    is_staff = models.BooleanField(
        verbose_name='является сотрудником',
        default=False
    )

    CODE_SIZE = 32

    code = models.CharField(
        verbose_name='код активации',
        max_length=CODE_SIZE,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def generate_code(self) -> str:
        digits = '0123456789'
        alphabit = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
        spec = '@#$%&()-+='
        txt = digits + alphabit
        res = []
        for _ in range(self.CODE_SIZE):
            res.append(txt[randrange(0, len(txt))])
        
        return ''.join(res)

    def save(
        self,
        *args: Any,
        **kwargs: Any
    ) -> None:
        self.code = self.generate_code()
        super().save(*args, **kwargs)

    class Meta:
        ordering = (
            'email',
        )
        verbose_name = "пользователи"
        verbose_name_plural = "пользователи"