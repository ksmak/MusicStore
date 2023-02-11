# Django modules
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)
from django.views import View
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.hashers import make_password

# Project modules
from .models import MyUser
from abstracts.mixins import HttpResponseMixin
from .forms import (
    UserForm,
    UserRegisterForm,
    UserLoginForm,
    ChangePasswordForm
)


class UserRegistrationView(HttpResponseMixin, View):
    """View for registration user."""

    template_name = "auths/user_form.html"

    form = UserRegisterForm

    context = {
        'ctx_title': 'Регистрация',
        'ctx_form': form(),
        'ctx_btn_title': 'Зарегистрировать'
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        return self.get_http_response(request)
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        return self.post_form(
            request=request,
            success_url="/auths/",
        )


class UserLoginView(HttpResponseMixin, View):
    """View for login user."""
    template_name = "auths/user_form.html"

    form = UserLoginForm

    context = {
        'ctx_title': 'Вход в систему',
        'ctx_form': form(),
        'ctx_btn_title': 'Войти'
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        return self.get_http_response(request)
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form = self.form(
            request.POST
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
                login(
                    request=request,
                    user=user
                )
                return HttpResponseRedirect("/")
        
        form.add_error(None, 'Неверный логин или пароль!')
        self.context['ctx_form'] = form

        return self.get_http_response(request)


class UserLogoutView(HttpResponseMixin, View):
    """User logout view."""
    template_name="auths/logout.html"

    context = {
        'ctx_title': "Выход из сайта"
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        logout(request)

        return self.get_http_response(request)
    


class UserProfileView(HttpResponseMixin, View):
    """User profile view."""
    template_name = "auths/user_profile.html"

    form = UserForm

    context = {
        'ctx_title': 'Профиль пользователя',
        'ctx_form': form()
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        self.context['ctx_user'] = request.user

        return self.get_http_response(request)


class UserEditView(HttpResponseMixin, View):
    """User edit view."""
    template_name="auths/user_form.html"

    form=UserForm

    context = {
        'ctx_title': "Редактирование профиля",
        'ctx_btn_title': 'Сохранить'
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        self.context['ctx_form'] = self.form(
            instance=request.user
        )
        
        return self.get_http_response(request)
        
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        
        form = self.form(
            request.POST
        )

        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.middle_name = form.cleaned_data['middle_name']
            user.save(update_fields=(
                'first_name', 'last_name', 'middle_name'
            ))

            return HttpResponseRedirect("/auths/profile/")
        

        self.context['ctx_form'] = form

        return self.get_http_response(request)


class UserChangePasswordView(HttpResponseMixin, View):
    """User change password view."""
    template_name="auths/user_form.html"

    form=ChangePasswordForm

    context = {
        'ctx_title': "Смена пароля",
        'ctx_form': form(),
        'ctx_btn_title': 'Сменить',
        'ctx_error': ''
    }

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        return self.get_http_response(request)
        
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form = self.form(
            request.POST
        )

        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data['password'])
            user.save(update_fields=(
                'password',
            ))

            login(request, user)

            return HttpResponseRedirect("/auths/profile/")
        

        self.context['ctx_form'] = form

        return self.get_http_response(request)



def activate_user(request: HttpRequest, activation_code: str):
    current_user = MyUser.objects.filter(activation_code = activation_code).first()
    if current_user:
            current_user.is_active = True
            current_user.save()

            return HttpResponse('Пользователь успешно активирован!')
    
    return HttpResponse('Ошибка активации!')
