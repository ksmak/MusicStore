# Generated by Django 4.1.5 on 2023-01-28 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('datestart_subscribe', models.DateField(auto_now_add=True, verbose_name='начало подписки')),
                ('followers', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='подписчики')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('title', models.CharField(max_length=200, verbose_name='наименование')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('title', models.CharField(max_length=200, verbose_name='наименование')),
                ('status', models.CharField(choices=[('BR', 'Предрелиз'), ('R', 'Релиз')], max_length=3, verbose_name='статус')),
                ('duration', models.TimeField(default=django.utils.timezone.now, verbose_name='продолжительность')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='musics.author', verbose_name='автор')),
                ('genre', models.ManyToManyField(related_name='genres', to='musics.genre', verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'трек',
                'verbose_name_plural': 'треки',
                'ordering': ('title',),
            },
        ),
    ]
