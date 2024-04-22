from django.test import TestCase
from django.urls import reverse


class BasicTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse(''))  #
        self.assertEqual(response.status_code, 200)