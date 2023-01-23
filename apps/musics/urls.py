from django.urls import path
from .views import MusicView


urlpatterns = [
    path('', MusicView.as_view()),   
]