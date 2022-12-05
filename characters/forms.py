from django import forms


class IntegerOrBlankField(forms.IntegerField):
    """ Custom validation method to allow blank values """
    def validate(self, value):
        """Custom field to allow None or integer values"""
        if not value:
            return value
        super().validate(value)


class FloatOrBlankField(forms.FloatField):
    """ Custom validation method to allow blank values """
    def validate(self, value):
        """Custom field to allow None or float values"""
        if not value:
            return value
        super().validate(value)


class CharacterForm(forms.Form):
    """
    Create a new character and add to user's list

    Make sure to bind image data to form:
    https://docs.djangoproject.com/en/4.1/ref/forms/api/#binding-uploaded-files
    """
    valid_race = (('1', 'dragonborn'),
                  ('2', 'dwarf'),
                  ('3', 'elf'),
                  ('4', 'gnome'),
                  ('5', 'half-elf'),
                  ('6', 'half-orc'),
                  ('7', 'halfling'),
                  ('8', 'human'),
                  ('9', 'tiefling'),
                  )

    valid_alignment = (('1', 'Chaotic Evil'),
                       ('2', 'Chaotic Good'),
                       ('3', 'Chaotic Neutral'),
                       ('4', 'Lawful Evil'),
                       ('5', 'Lawful Good'),
                       ('6', 'Lawful Neutral'),
                       ('7', 'Neutral'),
                       ('8', 'Neutral Evil'),
                       ('9', 'Neutral Good'),
                       )

    valid_class = (('1', 'barbarian'),
                   ('2', 'bard'),
                   ('3', 'cleric'),
                   ('4', 'druid'),
                   ('5', 'fighter'),
                   ('6', 'monk'),
                   ('7', 'paladin'),
                   ('8', 'ranger'),
                   ('9', 'rogue'),
                   ('10', 'sorcerer'),
                   ('11', 'warlock'),
                   ('12', 'wizard'),
                   )

    valid_gender = (('1', 'M'), ('2', 'F'), ('3', 'O'),)

    image = forms.ImageField(required=False, label='Portrait')
    name = forms.CharField(required=False, label='Name', max_length=150, help_text='Leave blank for a random value')
    character_class = forms.ChoiceField(required=False, label='Class', initial='', choices=valid_class, help_text='Leave blank for a random value')
    race = forms.ChoiceField(required=False, label='Race', initial='', choices=valid_race, help_text='Leave blank for a random value')
    alignment = forms.ChoiceField(required = False, label='Alignment', initial='', choices=valid_alignment, help_text='Leave blank for a random value')
    gender = forms.ChoiceField(required=False, initial='', choices=valid_gender, help_text='Leave blank for a random value')
    age = FloatOrBlankField(help_text='Leave blank for a random value')
    charisma = IntegerOrBlankField(help_text='Leave blank for a random value')
    constitution = IntegerOrBlankField(help_text='Leave blank for a random value')
    dexterity = IntegerOrBlankField(help_text='Leave blank for a random value')
    intelligence = IntegerOrBlankField(help_text='Leave blank for a random value')
    strength = IntegerOrBlankField(help_text='Leave blank for a random value')
    wisdom = IntegerOrBlankField(help_text='Leave blank for a random value')
    level = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    platinum = IntegerOrBlankField(required=False, label='Platinum Pieces', help_text='Leave blank for a random value')
    gold = IntegerOrBlankField(required=False, label='Gold Pieces', help_text='Leave blank for a random value')
    silver = IntegerOrBlankField(required=False, label='Silver Pieces', help_text='Leave blank for a random value')
    copper = IntegerOrBlankField(required=False, label='Copper Pieces', help_text='Leave blank for a random value')

