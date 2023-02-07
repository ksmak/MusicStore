# Django modules
from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate

# Project modules
from .models import MyUser
from abstracts.mixins import HttpResponseMixin
from .forms import (
    UserForm,
    UserRegisterForm,
    UserLoginForm
)


class UserRegistrationView(HttpResponseMixin, View):
    """View for registration user."""
    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form = UserRegisterForm()

        return self.get_http_response(
            request=request,
            template_name='auths/user_form.html',
            context={
                'ctx_title': 'Регистрация',
                'ctx_form': form
            }
        )
        
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form = UserRegisterForm(
            self.request.POST
        )
        
        if form.is_valid():
            user: MyUser = form.save(
                commit=False
            )

            user.password = make_password(
                user.password
            )

            user.save()

            login(request=request, user=user)

            return HttpResponseRedirect("/")

        return self.get_http_response(
            request=request,
            template_name='auths/user_form.html',
            context={
                'ctx_title': 'Регистрация',
                'ctx_form': form
            }
        )


class UserLoginView(HttpResponseMixin, View):
    """View for login user."""
    
    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form: UserLoginForm = UserLoginForm()

        return self.get_http_response(
            request=request,
            template_name='auths/user_form.html',
            context={
                'ctx_title': 'Вход в систему',
                'ctx_form': form
            }
        )
        
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form: UserLoginForm = UserLoginForm(
            self.request.POST
        )

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        
            user = authenticate(
                request=request,
                username=email,
                password=password
            )

            if user:
                login(request=request, user=user)

                return HttpResponseRedirect("/")

        return self.get_http_response(
            request=request,
            template_name='auths/user_form.html',
            context={
                'ctx_title': 'Вход в систему',
                'ctx_form': form,
                'ctx_form_error': 'Ошибка! Логин или пароль не верны!'
            }
        )



def activate_user(request: HttpRequest, activation_code: str):
    current_user = MyUser.objects.filter(activation_code = activation_code).first()
    if current_user:
            current_user.is_active = True
            current_user.save()

            return HttpResponse('Пользователь успешно активирован!')
    
    return HttpResponse('Ошибка активации!')