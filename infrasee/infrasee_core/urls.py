from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^version$', views.VersionView.as_view(), name='version'),
    url(r'^port$', views.PortView.as_view(), name='port'),
    url(r'^port/(?P<pk>[0-9]+)/$', views.PortDetailView.as_view(), name='port_details'),
]
