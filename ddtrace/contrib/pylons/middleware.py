import logging

from ...ext import http
from ...ext import AppTypes

log = logging.getLogger(__name__)


class PylonsTraceMiddleware(object):

    def __init__(self, app, tracer, service="pylons"):
        self.app = app
        self._service = service
        self._tracer = tracer

        self._tracer.set_service_info(
            service=service,
            app="pylons",
            app_type=AppTypes.web,
        )

    def __call__(self, environ, start_response):
        with self._tracer.trace("pylons.request", service=self._service, span_type=http.TYPE) as span:

            if not span.sampled:
                return self.app(environ, start_response)

            def _start_response(status, *args, **kwargs):
                """ a patched response callback which will pluck some metadata. """
                http_code = int(status.split()[0])
                span.set_tag(http.STATUS_CODE, http_code)
                if http_code >= 500:
                    span.error = 1
                return start_response(status, *args, **kwargs)

            try:
                return self.app(environ, _start_response)
            finally:
                controller = environ.get('pylons.routes_dict', {}).get('controller')
                action = environ.get('pylons.routes_dict', {}).get('action')
                span.resource = "%s.%s" % (controller, action)

                span.set_tags({
                    http.METHOD: environ.get('REQUEST_METHOD'),
                    http.URL: environ.get('PATH_INFO'),
                    "pylons.user": environ.get('REMOTE_USER', ''),
                    "pylons.route.controller": controller,
                    "pylons.route.action": action,
                })