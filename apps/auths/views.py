# Django modules
from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect
)
from django.views import View
# Project modules
from .models import MyUser
from abstracts.mixins import HttpResponseMixin
from .forms import UserForm


class UserView(HttpResponseMixin, View):
    """ UserView """
    form = UserForm

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        
        return self.get_http_response(
            request=request,
            template_name='auths/registration_form.html',
            context={
            'ctx_form': self.form()
        }
        )
        
    
    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: list
    ) -> HttpResponse:
        form: UserForm = self.form(
            self.request or None
        )
        breakpoint()
        return HttpResponse("Ok")


def activate_user(request: HttpRequest, activation_code: str):
    current_user = MyUser.objects.filter(activation_code = activation_code).first()
    if current_user:
            current_user.is_active = True
            current_user.save()

            return HttpResponse('Пользователь успешно активирован!')
    
    return HttpResponse('Ошибка активации!')


def register_user(request: HttpRequest):
    if request.method == 'POST':
        user = MyUser()
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.middle_name = request.POST.get('middle_name')
        user.set_password(request.POST.get('password'))
        user.save()

        return HttpResponseRedirect('/')
    

    return render(
        request=request,
        template_name='auths/register_user_page.html',
        context={}
    )
