from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'applications', views.ApplicationViewSet)
router.register(r'environments', views.EnvironmentViewSet)
router.register(r'datacenters', views.DataCenterViewSet)
router.register(r'hosts', views.HostViewSet)


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^version$', views.VersionView.as_view(), name='version'),
    url(r'^port$', views.PortView.as_view(), name='port'),
    url(r'^port/(?P<pk>[0-9]+)/$', views.PortDetailView.as_view(), name='port_details'),
    url(r'^api/', include(router.urls))
]
