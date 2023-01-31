# Django modules
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone

# Project modules
from auths.models import MyUser
from abstracts.models import AbstractModel, AbstractManager, AbstractQuerySet


class Author(AbstractModel):
    """User but will push music by 5 dollars."""
    datestart_subscribe = models.DateField(
        verbose_name='начало подписки',
        auto_now_add=True
    )

    followers = models.ManyToManyField(
        to=MyUser,
        related_name='followers',
        verbose_name='подписчики'
    )

    user = models.ForeignKey(
        to=MyUser,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Genre(AbstractModel):
    """Music genre"""
    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    class Meta:
        ordering = (
            'title',
        )
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
    
    def __str__(self) -> str:
        return self.title


class MusicManager(AbstractManager):
    def get_music_by_genre(self, title: str) -> QuerySet['Music']:
        id: int = Genre.objects.get(
           title=title
        ).id
        
        return self.filter(
            genre=id
        )

class Music(AbstractModel):
    """Music model"""
    objects = MusicManager()

    STATUS_PATTERN = [
        ('BR', 'Предрелиз'),
        ('R', 'Релиз')
    ]

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=STATUS_PATTERN
    )

    duration = models.TimeField(
        verbose_name='продолжительность',
        default=timezone.now
    )

    author = models.ForeignKey(
        to='Author',
        on_delete=models.RESTRICT,
        verbose_name='автор'
    )

    genre = models.ManyToManyField(
        to='Genre',
        related_name='genres',
        verbose_name='жанр'
    )

    avatar = models.ImageField(
        verbose_name='автарка',
        upload_to='upload',
        null=True,
        blank=True
    )
    
    class Meta:
        ordering = (
            'title',
        )
        verbose_name = 'трек'
        verbose_name_plural = 'треки'

    def __str__(self) -> str:
        return self.title