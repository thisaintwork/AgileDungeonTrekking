import random

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from django.urls import reverse
# from .models import AdtCharacter, Category
# from .forms import CharacterForm
from . import models as m
from . import forms as f

import random_name_generator as rname
from django.core.files.base import ContentFile


class CharactersPageTests(TestCase):
    """ Unit test of the Characters page """

    def setUp(self):
        """ Set up the environment """
        self.client = Client()
        self.user_password_text= 'testpass1234'
        self.user = get_user_model().objects.create_user(username='testuser1',
                                                         email='testuser1@email.com',
                                                         password=self.user_password_text)
        self.user2 = get_user_model().objects.create_user(username='testuser2',
                                                         email='testuser2@email.com',
                                                         password='test12345')
        self.user.save()
        self.user2.save()

        # create scaled down category data
        m.Category.objects.create(name='fighter',slug='fighter').save()
        m.Category.objects.create(name='wizard', slug='wizard').save()

        # create lists of valid values
        self.valid_alignment = ['Chaotic Evil', 'Chaotic Good', 'Chaotic Neutral',
                                'Lawful Evil', 'Lawful Good', 'Lawful Neutral',
                                'Neutral', 'Neutral Evil', 'Neutral Good']
        self.valid_race = ['dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'half-orc', 'halfling',
                           'human', 'tiefling']
        self.valid_class = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                            'sorcerer', 'warlock', 'wizard']
        self.valid_gender = ['M', 'F', 'O']

    def test_character_page_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('characters'))
        self.assertRedirects(response, r'/login/?next=/characters/')

    def test_character_page_is_accessible(self):
        """ Testing character page is accessible """
        self.client.logout()
        login = self.client.login(username=self.user.username, password=self.user_password_text)
        response = self.client.get(reverse('characters'))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, 'Characters')
        self.assertContains(response, 'Categories')

    def create_fighter(self):
        """ Test create fighter character is successful """

        self.fighter_random_name = rname.generate(limit=1)[0]
        self.fighter = m.AdtCharacter()
        self.fighter.name = self.fighter_random_name
        self.fighter.character_class = 'fighter'
        # simulate saving an image
        content = ContentFile(b"these are bytes")
        self.fighter.image.save('image01.jpg', content, save=True)
        self.fighter.category = m.Category.objects.get(name=self.fighter.character_class)
        self.fighter.race = random.choice(self.valid_race)
        self.fighter.alignment = random.choice(self.valid_alignment)
        self.fighter.gender = 'M'
        self.fighter.age = 110
        self.fighter.charisma = 10
        self.fighter.constitution = 11
        self.fighter.dexterity = 12
        self.fighter.intelligence = 13
        self.fighter.strength = 14
        self.fighter.wisdom = 15
        self.fighter.level = 1
        self.fighter.platinum = 100
        self.fighter.gold = 101
        self.fighter.silver = 102
        self.fighter.copper = 103
        self.fighter.created_by = self.user.username

        # save data to database
        self.fighter.save()
        # get the id, so we can retrieve it for further testing
        return self.fighter.id


    def test_fighter_created(self):
        """ Test fighter character can be created """
        fighter_id = self.create_fighter()
        self.assertTrue(fighter_id > 0)

    def test_fighter_is_valid(self):
        """ Test fighter character has valid attributes """
        fighter_id = self.create_fighter()
        character = get_object_or_404(m.AdtCharacter,
                                      id=fighter_id)
        self.assertEqual(character.character_class, 'fighter')
        self.assertTrue(character.name is not None)


    def create_wizard(self):
        """ Test creating a wizard is successful """

        self.wizard_random_name = rname.generate(limit=1)[0]
        self.wizard = m.AdtCharacter()
        self.wizard.name = self.wizard_random_name
        # simulate saving an image
        content = ContentFile(b"these are bytes")
        self.wizard.image.save('image01.jpg', content, save=True)
        self.wizard.character_class = 'wizard'
        self.wizard.category = m.Category.objects.get(name=self.wizard.character_class)
        self.wizard.race = random.choice(self.valid_race)
        self.wizard.alignment = random.choice(self.valid_alignment)
        self.wizard.gender = random.choice(self.valid_gender)
        self.wizard.age = random.randint(1,99999)
        self.wizard.charisma = random.randint(3,18)
        self.wizard.constitution = random.randint(3,18)
        self.wizard.dexterity = random.randint(3,18)
        self.wizard.intelligence = random.randint(3,18)
        self.wizard.strength = random.randint(3,18)
        self.wizard.wisdom = random.randint(3,18)
        self.wizard.level = random.randint(3,18)
        self.wizard.platinum = random.randint(0,99999999)
        self.wizard.gold = random.randint(0,99999999)
        self.wizard.silver = random.randint(0,99999999)
        self.wizard.copper = random.randint(0,99999999)
        self.wizard.created_by = self.user.username

        # save data to database
        self.wizard.save()
        # get the id, so we can retrieve it for further testing
        return self.wizard.id

    def test_wizard_created(self):
        """ Test wizard character can be created """
        wizard_id = self.create_wizard()
        self.assertTrue(wizard_id > 0)

    def test_wizard_is_valid(self):
        """ Test wizard character has valid attributes """
        self.client.logout()
        self.client.login(username=self.user.username, password=self.user_password_text)

        wizard_id = self.create_wizard()
        character = get_object_or_404(m.AdtCharacter,
                                      id=wizard_id)
        self.assertEqual(character.character_class, 'wizard')
        self.assertTrue(character.name is not None)


    def test_wizard_attributes(self):
        """ Test creating a wizard is successful """
        wizard_id = self.create_wizard()
        character = get_object_or_404(m.AdtCharacter,
                                      id=wizard_id)
        self.assertEqual(character.character_class, 'wizard')
        self.assertTrue(character.alignment in self.valid_alignment)
        self.assertTrue(character.race in self.valid_race)
        self.assertTrue(character.gender in self.valid_gender)

    def test_validate_ability_scores(self):
        """ Test wizard has valid ability scores """
        wizard_id = self.create_wizard()
        character = get_object_or_404(m.AdtCharacter,
                                      id=wizard_id)
        self.assertTrue(self.wizard.charisma in range(0, 19))
        self.assertTrue(self.wizard.constitution in range(0, 19))
        self.assertTrue(self.wizard.dexterity in range(0, 19))
        self.assertTrue(self.wizard.intelligence in range(0, 19))
        self.assertTrue(self.wizard.strength in range(0, 19))
        self.assertTrue(self.wizard.wisdom in range(0, 19))

    def test_create_view(self):
        """ Testing a logged in user can create characters """
        self.client.logout()
        self.client.login(username=self.user.username, password=self.user_password_text)
        response = self.client.get(reverse('character_add'))
        self.assertContains(response, "Portrait:")
        self.assertContains(response, "Name:")

    def test_edit_view(self):
        """ Testing the edit page is displayed"""
        self.client.logout()
        login = self.client.login(username=self.user.username, password=self.user_password_text)
        fighter_id = self.create_fighter()
        response = self.client.get(reverse('character_modify', args=[fighter_id]))
        self.assertContains(response, "Portrait:")
        self.assertContains(response, "Name:")

    def test_edit_view_is_accessible(self):
        """ Testing the edit page is accessible"""
        self.client.logout()
        login = self.client.login(username=self.user.username, password=self.user_password_text)
        fighter_id = self.create_fighter()
        response = self.client.get(reverse('character_modify', args=[fighter_id]))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, r'characters/edit.html')

    def test_detail_view(self):
        """ Testing the detail page is displayed"""
        self.client.logout()
        login = self.client.login(username=self.user.username, password=self.user_password_text)
        fighter_id = self.create_fighter()
        character = m.AdtCharacter.objects.get(id=fighter_id)
        response = self.client.get(reverse('character_detail', args=[fighter_id]))
        self.assertContains(response, character.name)

    def test_detail_view_is_accessible(self):
        """ Testing the detail page is accessible"""
        self.client.logout()
        login = self.client.login(username=self.user.username, password=self.user_password_text)
        self.assertTrue(login)

        fighter_id = self.create_fighter()
        response = self.client.get(reverse('character_detail', args=[fighter_id]))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, r'characters/detail.html')


    def test_logout_success(self):
        """ Testing the user can log out """
        self.client.logout()
        login = self.client.login(username=self.user.username, password=self.user_password_text)
        self.assertTrue(login)
        response = self.client.post(path=reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)

class CharacterFormTests(TestCase):
    """ Test the forms associated with characters. """

    def test_character_form_name_label(self):
        form = f.CharacterForm()
        self.assertEqual(form.fields['name'].label, "Name")
        self.assertEqual(form.fields['name'].help_text, "Leave blank for a random value")

    def test_character_form_image_label(self):
        form = f.CharacterForm()
        self.assertEqual(form.fields['image'].label, "Portrait")



