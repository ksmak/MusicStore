# Django
from django.core.handlers.wsgi import WSGIRequest
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.template import (
    loader,
    Template,
)
from django.forms import ModelForm


class HttpResponseMixin:
    """Mixin from http handlers."""

    content_type = 'text/html'

    def get_http_response(
            self,
            request: WSGIRequest
        ) -> HttpResponse:
        template: Template =\
            loader.get_template(
                self.template_name
            )

        return HttpResponse(
            template.render(
                context=self.context,
                request=request
            ),
            content_type=self.content_type
        )

    def post_form(
        self,
        request: WSGIRequest,
        success_url: str
    ) -> HttpResponse:
        post_form: ModelForm = self.form(
            request.POST
        )
        
        self.context['ctx_form'] = post_form

        if not post_form.is_valid():
            return self.get_http_response(request)
        
        post_form.save()
        
        return HttpResponseRedirect(success_url)
