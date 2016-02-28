from django.contrib import admin

from .models import Port
from .models import Application
from .models import Environment
from .models import Host
from .models import DataCenter
from .models import Service


class PortAdmin(admin.ModelAdmin):
    list_display = ('number', 'protocol')


class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class DataCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'host_type', 'environment', 'data_center')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Port, PortAdmin)
admin.site.register(Application)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(DataCenter, DataCenterAdmin)
admin.site.register(Service, ServiceAdmin)
