from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.db.models import QuerySet
# Project modules
from musics.models import (
    Author,
    Genre,
    Music
)
from auths.models import MyUser

def index(request, *args, **kwargs):
    return render(
        request=request,
        template_name='musics/home_page.html',
        context={}
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


class AuthorView(View):
    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        users: QuerySet[Genre] = MyUser.objects.all()
        return render(
            request=request,
            template_name='musics/create_author_page.html',
            context={
                'ctx_users': users
            }
        )
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        user_email = request.POST.get('user')
        user = MyUser.objects.get(email=user_email)


        followers_emails = request.POST.getlist('followers')

        author = Author.objects.create(
            user=user
        )

        if followers_emails:
            followers = MyUser.objects.filter(email__in=followers_emails)
            author.followers.set(followers)


        return HttpResponse("success")


class GenreView(View):
    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        return render(
            request=request,
            template_name='musics/create_genre_page.html',
            context={}
        )
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        title = request.POST.get('title')
        
        genre = Genre.objects.create(
            title=title
        )
       
        return HttpResponse("success")