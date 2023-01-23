from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from auths.views import activate_user, register_user
from musics.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('activate/<str:activation_code>', activate_user),
    path('register/', register_user),
    path('main/', include('musics.urls')),
    path('', index, name='main-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]