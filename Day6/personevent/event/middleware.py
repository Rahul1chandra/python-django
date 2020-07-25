from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

EXEMPT_URLS = ['/', 'signup']
class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            if request.path not in EXEMPT_URLS:
                return HttpResponseRedirect("/")