from builtins import object
try:
    from django.core.urlresolvers import resolve
except ModuleNotFoundError:
    from django.urls import resolve
from django.urls.exceptions import Resolver404
from django.utils.deprecation import MiddlewareMixin


class RedirectMiddleware(MiddlewareMixin):
    """
        Process the redirect patterns from redirects.urls.
    """
    def process_response(self, request, response):
        if response.status_code != 404:
            # No need to check for a redirect for non-404 responses.
            return response

        path = request.get_full_path()

        try:
            urlconf = 'redirect.urls'
            while True:
                try:
                    redirect, args, kwargs = resolve(path, urlconf=urlconf)
                except Resolver404:
                    break
                path = kwargs.get('url')
            return redirect(request, **kwargs)
        except:
            # No redirect was found. Return the response.
            return response
