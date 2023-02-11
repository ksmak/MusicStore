# Django
from django.urls import path

# Local
from .views import (
    MainView,
    MusicView,
    AuthorView,
    GenreView
)


urlpatterns = [
    path('', MainView.as_view()),
    path('music/', MusicView.as_view()),   
    path('author/', AuthorView.as_view()),
    path('genre/', GenreView.as_view()),
]