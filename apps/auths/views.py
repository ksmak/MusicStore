from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from auths.models import CustomUser


def registration(
    request: HttpRequest,
    code: str,
    *args: tuple, 
    **kwargs: dict
    ) -> HttpResponse:
    res: QuerySet = CustomUser.objects.filter(
        code=code
    )
    if res:
        user: CustomUser = res.first()
        user.is_active = True
        user.save()
        return HttpResponse("Successfull!")
    
    return HttpResponse("Bad request")
