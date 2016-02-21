from django.http import HttpResponse
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("Index view of infrasee_core")


class VersionView(View):
    def get(self, request):
        return HttpResponse('{"version":"1.0.0-DEV"}')

