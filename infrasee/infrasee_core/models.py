from __future__ import unicode_literals

from django.db import models


class Port(models.Model):
    HOST_TYPE_CHOICES = (
        ('0', 'TCP'),
        ('1', 'UDP'),
    )
    name = models.CharField(max_length=256)
    number = models.IntegerField(default=0)
    protocol = models.CharField(max_length=1, choices=HOST_TYPE_CHOICES)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, number, protocol):
        port = cls(name=name, number=number, protocol=protocol)
        # do something with the port
        return port


class Application(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Environment(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Host(models.Model):
    HOST_TYPE_CHOICES = (
        ('0', 'physical'),
        ('1', 'virtual'),
    )
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    host_type = models.CharField(max_length=1, choices=HOST_TYPE_CHOICES)

    def __str__(self):
        return self.name


class DataCenter(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
