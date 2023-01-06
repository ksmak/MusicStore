from django.shortcuts import render
from musics.models import (
    Author,
    Genre,
    Music
)

def index(request, *args, **kwargs):
    return render(
        request=request,
        template_name='musics/home_page.html',
        context={}
    )

def create_author_view(request, *args, **kwargs):
    items = Author.objects.all()
    return render(
        request=request,
        template_name='musics/create_author_page.html',
        context={
            "items": items
        }
    )

def create_genre_view(request, *args, **kwargs):
    items = Genre.objects.all()
    return render(
        request=request,
        template_name='musics/create_genre_page.html',
        context={
            "items": items
        }
    )

def create_music_view(request, *args, **kwargs):
    items = Music.get_all()
    return render(
        request=request,
        template_name='musics/create_music_page.html',
        context={
            "items": items
        }
    )