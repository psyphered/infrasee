from django.test import TestCase

from .models import Environment


class EnvironmentModelTests(TestCase):
    def test_environment(self):
        environment = Environment.objects.create(name="myName", description="myDescription");
        self.assertEqual(environment.name, "myName");
        self.assertEqual(environment.description, "myDescription");
