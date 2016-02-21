from __future__ import unicode_literals

from django.db import models


class Port(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField(default=0)
    protocol = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, number, protocol):
        port = cls(name=name, number=number, protocol=protocol)
        # do something with the port
        return port
