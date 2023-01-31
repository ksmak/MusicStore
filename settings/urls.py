from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from auths.views import activate_user, register_user, UserView
from musics.views import index


urlpatterns = [
    path('registration/', UserView.as_view()),
    path('admin/', admin.site.urls),
    path('activate/<str:activation_code>', activate_user),
    path('register/', register_user),
    path('', include('musics.urls')),
    path('', index, name='main-page'),
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]