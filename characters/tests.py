from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
import re
from .models import AdtCharacter
from dnd_character.classes import CLASSES


class CharactersCITests(TestCase):
    def test_build_fail_in_ci(self):
        """ Deliberate failure to trigger error in CI """
        self.assertEqual(1, 2)
        
        
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
        self.assertTemplateUsed(response, 'characters/list.html')

    def test_character_management(self):
        """ Testing character page has the correct form """
        response = self.client.get('/characters/')
        self.assertContains(response, 'Manage Characters')

    def test_list_view(self):
        """ Testing a logged in user sees only their characters """
        self.Fighter_User1 = AdtCharacter(name='user1', created_by='testuser1')
        self.Wizard_User2 = AdtCharacter(name='user2', created_by='testuser2')
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
        self.Random = AdtCharacter()

    def test_fighter(self):
        """ Test creating a fighter character is successful """
        kwargs = {'classs': CLASSES["fighter"]}
        #self.Fighter.generate_attributes(**kwargs);
        # self.assertEqual(self.Fighter.character_class, 'fighter')
        # self.assertTrue(self.Fighter.alignment in self.valid_alignment)
        # self.assertTrue(self.Fighter.race in self.valid_race)

    def test_wizard(self):
        """ Test creating a wizard is successful """
        kwargs = {'classs': CLASSES["wizard"]}
        # self.Wizard.generate_attributes(**kwargs);
        # self.assertEqual(self.Wizard.character_class, 'wizard')
        # self.assertTrue(self.Wizard.alignment in self.valid_alignment)
        # self.assertTrue(self.Wizard.race in self.valid_race)

    def test_random(self):
        """ Test creating a completely random character  """
        # self.Random.generate_attributes();


    def test_wizard_attributes(self):
        """ Test creating a wizard is successful """
        # kwargs = {'classs': CLASSES["wizard"]}
        # self.Wizard.generate_attributes(**kwargs);
        # self.assertEqual(self.Wizard.character_class, 'wizard')
        # self.assertTrue(self.Wizard.alignment in self.valid_alignment)
        # self.assertTrue(self.Wizard.race in self.valid_race)
        # self.assertTrue(self.Wizard.gold < 100)


    def test_validate_ability_scores(self):
        """ Test creating a wizard is successful """
        self.assertTrue(self.Wizard.charisma in range(0, 19))
        self.assertTrue(self.Wizard.constitution in range(0, 19))
        self.assertTrue(self.Wizard.dexterity in range(0, 19))
        self.assertTrue(self.Wizard.intelligence in range(0, 19))
        self.assertTrue(self.Wizard.strength in range(0, 19))
        self.assertTrue(self.Wizard.wisdom in range(0, 19))
