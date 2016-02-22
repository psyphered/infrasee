from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View
from rest_framework import viewsets

from .models import Port
from .models import Environment
from .models import Application
from .models import DataCenter
from .models import Host
from .serializers import EnvironmentSerializer
from .serializers import ApplicationSerializer
from .serializers import DataCenterSerializer
from .serializers import HostSerializer


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


class EnvironmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows environments to be viewed or edited.
    """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class DataCenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows data centers to be viewed or edited.
    """
    queryset = DataCenter.objects.all()
    serializer_class = DataCenterSerializer


class HostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer
