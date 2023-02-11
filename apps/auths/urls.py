# Django
from django.urls import path

# Local
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserEditView,
    UserChangePasswordView,
    UserLogoutView,
)


urlpatterns = [
    path('', UserLoginView.as_view()),   
    path('register/', UserRegistrationView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('edit/', UserEditView.as_view()),
    path('change-password/', UserChangePasswordView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]
