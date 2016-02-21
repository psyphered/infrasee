from __future__ import unicode_literals

from django.db import models


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
