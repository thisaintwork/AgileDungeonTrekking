from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse
import re
from .models import AdtCharacter

class CharactersPageTests(TestCase):
    """ Unit test of the Characters page """
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser1',
                                                         email='testuser1@email.com',
                                                         password='testpass1234')
        self.user2 = get_user_model().objects.create_user(username='testuser2',
                                                         email='testuser2@email.com',
                                                         password='testpass1234')


    def test_character_template(self):
        """ Testing character page is accessible """
        response = self.client.get('/characters/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'characters/characters.html')

    def test_character_management(self):
        """ Testing character page has the correct form """
        response = self.client.get('/characters/')
        self.assertContains(response, 'Manage Characters')

    def test_list_view(self):
        """ Testing a logged in user sees only their characters """
        self.Fighter_User1 = AdtCharacter(first_name='user1', created_by='testuser1')
        self.Wizard_User2 = AdtCharacter(first_name='user2', created_by='testuser2')
        self.client.login(username='testuser1', password='testpass1234')
        response = self.client.get(reverse('characters'))
        self.assertContains(response, 'user1')
        self.assertNotContains(response, 'user2')


class CharactersTests(TestCase):
    """ Unit testing creating characters """
    def setUp(self):
        self.valid_alignment = ['Chaotic Evil', 'Chaotic Good', 'Chaotic Neutral',
                                'Lawful Evil', 'Lawful Good', 'Lawful Neutral',
                                'Neutral', 'Neutral Evil', 'Neutral Good']
        self.valid_race = ['dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'half-orc', 'halfling',
                           'human', 'tiefling']
        self.valid_class = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                            'sorcerer', 'warlock', 'wizard']
        self.Fighter = AdtCharacter()
        self.Wizard = AdtCharacter()
        self.Unknown = AdtCharacter()

    def test_fighter(self):
        """ Test creating a fighter character is successful """
        self.Fighter.generate_attributes(character_class="fighter");
        self.assertEqual(self.Fighter.character_class, 'fighter')
        self.assertTrue(self.Fighter.alignment in self.valid_alignment)
        self.assertTrue(self.Fighter.race in self.valid_race)

    def test_wizard(self):
        """ Test creating a wizard is successful """
        self.Wizard.generate_attributes(character_class="wizard");
        self.assertEqual(self.Wizard.character_class, 'wizard')
        self.assertTrue(self.Wizard.alignment in self.valid_alignment)
        self.assertTrue(self.Wizard.race in self.valid_race)

    def test_unknown(self):
        """ Test creating an unknown character is not successful """
        self.Unknown.generate_attributes(chracter_class="teacher");
        self.assertFalse(self.Unknown.character_class in self.valid_class)
        self.assertTrue(self.Unknown.alignment in self.valid_alignment)

    def test_wizard_attributes(self):
        """ Test creating a wizard is successful """
        self.Wizard.generate_attributes(character_class="wizard");
        self.assertEqual(self.Wizard.character_class, 'wizard')
        self.assertTrue(self.Wizard.alignment in self.valid_alignment)
        self.assertTrue(self.Wizard.race in self.valid_race)
        self.assertTrue(self.Wizard.gold < 100)


    def test_validate_ability_scores(self):
        """ Test creating a wizard is successful """
        self.assertTrue(self.Wizard.charisma in range(1, 19))
        self.assertTrue(self.Wizard.constitution in range(1, 19))
        self.assertTrue(self.Wizard.dexterity in range(1, 19))
        self.assertTrue(self.Wizard.intelligence in range(1, 19))
        self.assertTrue(self.Wizard.strength in range(1, 19))
        self.assertTrue(self.Wizard.wisdom in range(1, 19))
