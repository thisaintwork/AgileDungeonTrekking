from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse
import re


class CreaturesPageTests(TestCase):
    """ Unit test of the Registration page """
    def setUp(self):
        self.client  = Client()

    def test_register_template(self):
        """ Testing creatures page is accessible """
        response = self.client.get('/creatures/')
        self.assertEqual(response.status_code, 200)