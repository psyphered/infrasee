from django.http import HttpResponse
from django.views.generic import View
from rest_framework import viewsets

from .models import Environment
from .models import Application
from .models import DataCenter
from .models import Host
from .models import Port
from .models import Service
from .serializers import EnvironmentSerializer
from .serializers import ApplicationSerializer
from .serializers import DataCenterSerializer
from .serializers import HostSerializer
from .serializers import PortSerializer
from .serializers import ServiceSerializer


class VersionView(View):
    version = '{"version":"1.0.0-DEV"}'

    def get(self, request):
        # <view logic>
        return HttpResponse(self.version)


class PortViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ports to be viewed or edited.
    """
    queryset = Port.objects.all()
    serializer_class = PortSerializer


class EnvironmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows environments to be viewed or edited.
    """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hosts to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


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
