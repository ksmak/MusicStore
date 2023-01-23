from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.db.models import QuerySet

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
    items = Music.objects.all()
    return render(
        request=request,
        template_name='musics/create_music_page.html',
        context={
            "items": items
        }
    )

class MusicView(View):
    """ View special for Music model """

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        status: list[tuple(str, str)] = Music.STATUS_PATTERN
        genres: QuerySet[Genre] = Genre.objects.all()
        return render(
            request=request,
            template_name='musics/create_music_page.html',
            context={
                'ctx_status': status,
                'ctx_genres': genres
            }
        )

    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        status = request.POST.get('status')
        title = request.POST.get('title')
        duration = request.POST.get('duration', 0)
        genre_ids = request.POST.getlist('genre')

        author = Author.objects.get(id=request.user.id)
        
        music = Music.objects.create(
            status=status,
            title=title,
            duration=duration,
            author=author
        )

        if genre_ids:
            genres = Genre.objects.filter(id__in=genre_ids)
        
        music.genre.set(genres)


        return HttpResponse("success")