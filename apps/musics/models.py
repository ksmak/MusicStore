from django.db import models
from auths.models import CustomUser
from abstracts.models import AbstractModel
from django.db.models import QuerySet


class AuthorManager(models.Manager):
    def get_author_by_user(
        self,
        user: CustomUser
    ) -> 'Author':
        result: QuerySet = self.filter(
            user=user
        )
        if result.count() > 0:
            return result.first()
    
    def get_author_by_firstname(
        self,
        first_name: str
    ) -> 'Author':
        result: QuerySet = self.filter(
            user__first_name=first_name
        )
        if result.count() > 0:
            return result.first()
    
    def get_author_by_lastname(
        self,
        last_name: str
    ) -> 'Author':
        result: QuerySet = self.filter(
            user__last_name=last_name
        )
        if result.count() > 0:
            return result.first()

class Author(AbstractModel):
    """User but will push music by 5 dollars."""

    datestart_subscribe = models.DateField(
        verbose_name='начало подписки',
        auto_now_add=True
    )

    followers = models.ManyToManyField(
        to=CustomUser,
        related_name='followers',
        verbose_name='подписчики'
    )

    user = models.ForeignKey(
        to=CustomUser,
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
        return (f"{self.user.first_name} "
            f"{self.user.last_name}")


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


class MusicManager(models.Manager):
    def get_by_status(
        self,
        status: int
    ) -> 'Music':
        result: QuerySet =  self.filter(
            status=status
        )
        if result.count() > 0:
            return result.first()

        return None

        
class Music(AbstractModel):
    """Music model"""
    objects = MusicManager()

    STATUSES = [
        (1, 'Предрелиз'),
        (2, 'Релиз')
    ]

    title = models.CharField(
        verbose_name='наименование',
        max_length=200
    )

    status = models.PositiveSmallIntegerField(
        verbose_name='статус',
        choices=STATUSES
    )

    duration = models.IntegerField(
        verbose_name='продолжительность',
        default=0
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

    class Meta:
        ordering = (
            'title',
        )
        verbose_name = 'трек'
        verbose_name_plural = 'треки'

    def __str__(self) -> str:
        return self.title