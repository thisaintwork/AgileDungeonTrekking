from dnd_character import Character
from dnd_character.classes import CLASSES
from dnd_character.experience import experience_at_level


class GenerateCharacter():
    """ Helper class that will generate all character attributes using the dnd-character package  """
    def CreateCharacter(**kwargs):
        # character = Character(
        #     name="Thor Odinson",
        #     age="34",
        #     level=1,
        #     gender="Male",
        #     description="Looks like a pirate angel",
        #     biography="Born on Asgard, God of Thunder",
        #     classs=CLASSES["fighter"],
        # )
        character = Character(**kwargs)
        return character
