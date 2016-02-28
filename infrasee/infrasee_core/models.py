from __future__ import unicode_literals

from django.db import models


class Port(models.Model):
    HOST_TYPE_CHOICES = (
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
    )
    name = models.CharField(max_length=256)
    number = models.IntegerField(default=0)
    protocol = models.CharField(max_length=3, choices=HOST_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)
    environments = models.ManyToManyField(Environment, blank=True)
    # services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.name


class DataCenter(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.name


class Host(models.Model):
    HOST_TYPE_CHOICES = (
        ('0', 'physical'),
        ('1', 'virtual'),
    )
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)
    host_type = models.CharField(max_length=1, choices=HOST_TYPE_CHOICES)
    environment = models.ForeignKey(Environment, blank=True, null=True, on_delete=models.SET_NULL)
    data_center = models.ForeignKey(DataCenter, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)
    ports = models.ManyToManyField(Port, blank=True)

    def __str__(self):
        return self.name
