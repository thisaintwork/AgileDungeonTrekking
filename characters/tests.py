from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse
import re
from .models import AdtCharacter

class CharactersPageTests(TestCase):
    """ Unit test of the Registration page """
    def setUp(self):
        self.client  = Client()

    def test_character_template(self):
        """ Testing register page is accessible """
        response = self.client.get('/characters/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/characters.html')


class CharactersTests(TestCase):
    """ Unit testing creating characters """
    def setUp(self):
        adtCharacter = AdtCharacter()


    def test_create_knight(self):
        """ Test creating a user is successful """
        self.adtCharacter.generate_attributes(character_class="knight");
        self.assertEqual(self.adtCharacter.character_class, 'knight')


    def test_create_wizard(self):
        """ Test creating a super user is successful """
        self.adtCharacter.generate_attributes(character_class="wizard");
        self.assertEqual(self.adtCharacter.character_class, 'wizard')

    def test_create_unknown(self):
        """ Test creating an unknown character is not successful """
        self.adtCharacter.generate_attributes(chracter_class="teacher");
        self.assertNotEqual(self.adtCharacter.character_class, 'teacher')
