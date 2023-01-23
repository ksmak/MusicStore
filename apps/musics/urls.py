from django.urls import path
from .views import (
    MusicView,
    AuthorView,
    GenreView
)


urlpatterns = [
    path('music/', MusicView.as_view()),   
    path('author/', AuthorView.as_view()),
    path('genre/', GenreView.as_view())
]