# Generated by Django 4.1.5 on 2023-01-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('first_name', models.CharField(blank=True, max_length=60, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=70, null=True, verbose_name='last_name')),
                ('is_active', models.BooleanField(default=False, verbose_name='активность')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='является суперпользователем')),
                ('is_staff', models.BooleanField(default=False, verbose_name='является сотрудником')),
                ('code', models.CharField(blank=True, max_length=32, null=True, verbose_name='код активации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователи',
                'verbose_name_plural': 'пользователи',
                'ordering': ('email',),
            },
        ),
    ]
