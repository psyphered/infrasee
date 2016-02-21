from django.contrib import admin

from .models import Application
from .models import Environment
from .models import Host
from .models import DataCenter

admin.site.register(Application)
admin.site.register(Environment)
admin.site.register(Host)
admin.site.register(DataCenter)
