from __future__ import unicode_literals

from django.db import models


class Port(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField(max_length=65535)
    protocol = models.CharField(max_length=3)

    @classmethod
    def create(cls, name, number, protocol):
        port = cls(name=name, number=number, protocol=protocol)
        # do something with the port
        return port

# example create
port = Port.create("SSH", 22, "TCP")
