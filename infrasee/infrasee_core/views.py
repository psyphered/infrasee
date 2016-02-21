from django.http import HttpResponse


def index(request):
    return HttpResponse("Index view of infrasee_core")


def version(request):
    return HttpResponse('{"version":"1.0.0-DEV"}')
