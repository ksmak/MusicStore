from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from musics import views
from auths.views import activate_user, register_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('activate/<str:activation_code>', activate_user),
    path('register/', register_user),
    path('musics/', include('musics.urls')),
    path('', views.index),
    path('create-author', views.create_author_view),
    path('create-genre', views.create_genre_view),
    path('create-music', views.create_music_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]