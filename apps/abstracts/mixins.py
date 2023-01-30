from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template import (
    loader,
    Template,
)


class HttpResponseMixin:
    """Mixin from http handlers."""

    content_type = 'text/html'

    def get_http_response(
        self,
        request: WSGIRequest,
        template_name: str,
        context: dict = {}
    ) -> HttpResponse:
        context['ctx_title'] = 'Music store'
        
        template: Template =\
            loader.get_template(
                template_name
            )

        return HttpResponse(
            template.render(
                context=context,
                request=request
            ),
            content_type=self.content_type
        )