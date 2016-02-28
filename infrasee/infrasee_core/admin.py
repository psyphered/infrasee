from django.contrib import admin

from .models import Port
from .models import Application
from .models import Environment
from .models import Host
from .models import DataCenter
from .models import Service

class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'host_type', 'environment', 'data_center')

admin.site.register(Port)
admin.site.register(Application)
admin.site.register(Environment)
admin.site.register(Host, HostAdmin)
admin.site.register(DataCenter)
admin.site.register(Service)
