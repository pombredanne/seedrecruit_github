import json

from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase


class TestApiEndpoints(TestCase):

    def setUp(self):
        self.client = Client()

    def test_with_username(self):
        response = self.client.get(reverse('api:user', args=['mikeywaites']))
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertIn('commits', content)
        self.assertIn('languages', content)
        self.assertIn('forked', content)
        self.assertNotIn('error', content)
