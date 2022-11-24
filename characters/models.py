import uuid

from django.db import models
from dnd_character import Character
from dnd_character.classes import CLASSES
from dnd_character.experience import experience_at_level
from django.urls import reverse
from django.utils import timezone

m_names = ['Vindicate',
'Ironside',
'Torpedo',
'Bionic',
'Dynamo',
'Mr. Miraculous',
'Tornado',
'Metal Man',
'Jawbreaker',
'Barrage',
'Amplify',
'Bonfire',
'Monsoon',
'Urchin',
'Firefly']

f_name = ['Ember',
'Twilight',
'Tsunami',
'Miss Mantis',
'Wildfire',
'Radiance',
'Wondrous',
'Starlight',
'Black Magnolia',
'Ivory Wing',
'Coral',
'Waterfall',
'Tempest',
'Lotus']

def CreateCharacter(charClass):
    genChar = Character(
        name="Thor Odinson",
        age="34",
        level=1,
        gender="Male",
        description="Looks like a pirate angel",
        biography="Born on Asgard, God of Thunder",
        classs=CLASSES["fighter"],
    )


class AdtCharacter(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.FloatField()
    charisma = models.IntegerField()
    constitution = models.IntegerField()
    dexterity = models.IntegerField()
    intelligence = models.IntegerField()
    strength = models.IntegerField()
    wisdom = models.IntegerField()
    level = models.PositiveIntegerField()
    character_class = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    alignment = models.CharField(max_length=100)
    platinum = models.IntegerField()
    gold = models.IntegerField()
    silver = models.IntegerField()
    copper = models.IntegerField()
    created_by = models.CharField(max_length=100, default='unknown')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('character', kwargs={'pk': str(self.pk)})

    def generate_attributes(self, **kwargs):
        # call the dnd-character object to generate attributes
        pass
