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
from abstracts.mixins import HttpResponseMixin
from .forms import (
    MusicForm
)


class MainView(HttpResponseMixin, View):
    """Main page view."""
    template_name = "musics/home_page.html"

    context = {
        'ctx_title': "Главная страница",
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        self.context['ctx_user'] = request.user
        return self.get_http_response(request)


class MusicView(View, HttpResponseMixin):
    """ View special for Music model """

    form = MusicForm

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        status: list[tuple(str, str)] = Music.STATUS_PATTERN
        genres: QuerySet[Genre] = Genre.objects.all()
        return self.get_http_response(
            request=request,
            template_name='musics/create_music_page.html',
            context={
                'ctx_status': status,
                'ctx_genres': genres,
                'ctx_form': self.form()
            }
        )

    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        data: MusicForm = self.form(
            self.request.POST,
            self.request.FILES
        )

        if not data.is_valid():
            return HttpResponse("BAD")
        
        data.save()

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