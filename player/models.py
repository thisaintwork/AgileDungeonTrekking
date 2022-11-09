from django.db import models
from dnd_character import Character
from dnd_character.classes import CLASSES
from dnd_character.experience import experience_at_level


class Players(models.Model):
    playerList = {}

    def __str__(self):
        return f'Player list'
