from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Environment


class EnvironmentModelTests(TestCase):
    def test_environment(self):
        # Given
        input = {'name': 'myName', 'description': 'myDescription'}

        # When
        environment = Environment.objects.create(
            name=input['name'],
            description=input['description']
        );

        # Then
        self.assertEqual(environment.name, input['name']);
        self.assertEqual(environment.description, input['description']);


class EnvironmentApiTests(APITestCase):
    def test_create_environment(self):
        """
        Ensure we can create a new account object.
        """
        # Given
        input = {'name': 'myName', 'description': 'myDescription'}

        # When
        response = self.client.post(reverse('environment-list'), input, format='json')

        # Then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Environment.objects.count(), 1)
        self.assertEqual(Environment.objects.get().name, input['name'])
        self.assertEqual(Environment.objects.get().description, input['description'])

    def test_get_environment(self):
        """
        Ensure we can create a new account object.
        """
        # Given
        input = {'name': 'myName', 'description': 'myDescription'}
        environment = Environment.objects.create(
            name=input['name'],
            description=input['description'],
        );
        environment.save();

        # When
        response = self.client.get(reverse('environment-detail', args=['1']))

        # Then
        self.assertEqual(response.data, {
            'name': input['name'],
            'description': input['description'],
            'host_set': [],
        })
