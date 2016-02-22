from rest_framework import serializers

from .models import Environment
from .models import Application
from .models import DataCenter
from .models import Host


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    host_set = serializers.HyperlinkedRelatedField(many=True,
        view_name='host-detail', read_only=True)

    class Meta:
        model = Environment
        fields = ('name', 'description', 'host_set')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    environments = serializers.HyperlinkedRelatedField(many=True, 
        view_name='environment-detail', read_only=True)

    class Meta:
        model = Application
        fields = ('name', 'description', 'environments')


class DataCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataCenter
        field = ('name', 'description')


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        field = ('name', 'description', 'host_type', 'environment',
            'data_center')
