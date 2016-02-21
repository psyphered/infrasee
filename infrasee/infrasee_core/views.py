from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from .models import Port


class IndexView(View):
    message = "Index view of infrasee_core"

    def get(self, request):
        # <view logic>
        return HttpResponse(self.message)


class VersionView(View):
    version = '{"version":"1.0.0-DEV"}'

    def get(self, request):
        # <view logic>
        return HttpResponse(self.version)


class PortView(View):
    model = Port

    def get(self, request):
        all_ports_list = Port.objects.all()
        return HttpResponse(all_ports_list)


class PortDetailView(View):
    model = Port

    def get(self, request, pk):
        port_details = Port.objects.get(id=pk)

        return HttpResponse(port_details)

    def post(self, request, pk):
        did_some_stuff = "stuff done"
        return HttpResponse(did_some_stuff)
