from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'applications', views.ApplicationViewSet)
router.register(r'environments', views.EnvironmentViewSet)
router.register(r'datacenters', views.DataCenterViewSet)
router.register(r'hosts', views.HostViewSet)
router.register(r'ports', views.PortViewSet)


urlpatterns = [
    url(r'^version$', views.VersionView.as_view(), name='version'),
    url(r'^api/', include(router.urls))
]
