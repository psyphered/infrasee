from django.core import serializers
from django.http import HttpResponse
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
        data = serializers.serialize("json", all_ports_list)
        return HttpResponse(data, content_type='application/json')


class PortDetailView(View):
    model = Port

    def get(self, request, pk):
        port_details = Port.objects.all().filter(id=pk)
        data = serializers.serialize("json", port_details)
        return HttpResponse(data, content_type='application/json')

    def post(self, request, pk):
        did_some_stuff = "stuff done"
        return HttpResponse(did_some_stuff)
