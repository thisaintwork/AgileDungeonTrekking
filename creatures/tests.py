from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse
import re


class CreaturesPageTests(TestCase):
    """ Unit test of the Creatures page """
    def setUp(self):
        self.client  = Client()

    def test_creatures_template(self):
        """ Testing creatures page is accessible """
        response = self.client.get('/creatures/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'creatures/creatures.html')

    def test_creatures_management(self):
        """ Testing creture page has the correct form """
        response = self.client.get('/creatures/')
        self.assertContains(response, 'Manage Creatures')