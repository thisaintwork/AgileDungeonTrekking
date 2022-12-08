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
    valid_race = (('dragonborn', 'dragonborn'),
                  ('dwarf', 'dwarf'),
                  ('elf', 'elf'),
                  ('gnome', 'gnome'),
                  ('half-elf', 'half-elf'),
                  ('half-orc', 'half-orc'),
                  ('halfling', 'halfling'),
                  ('human', 'human'),
                  ('tiefling', 'tiefling'),
                  )

    valid_alignment = (('Chaotic Evil', 'Chaotic Evil'),
                       ('Chaotic Good', 'Chaotic Good'),
                       ('Chaotic Neutral', 'Chaotic Neutral'),
                       ('Lawful Evil', 'Lawful Evil'),
                       ('Lawful Good', 'Lawful Good'),
                       ('Lawful Neutral', 'Lawful Neutral'),
                       ('Neutral', 'Neutral'),
                       ('Neutral Evil', 'Neutral Evil'),
                       ('Neutral Good', 'Neutral Good'),
                       )

    valid_class = (('barbarian', 'barbarian'),
                   ('bard', 'bard'),
                   ('cleric', 'cleric'),
                   ('druid', 'druid'),
                   ('fighter', 'fighter'),
                   ('monk', 'monk'),
                   ('paladin', 'paladin'),
                   ('ranger', 'ranger'),
                   ('rogue', 'rogue'),
                   ('sorcerer', 'sorcerer'),
                   ('warlock', 'warlock'),
                   ('wizard', 'wizard'),
                   )

    valid_gender = (('M', 'M'), ('F', 'F'), ('O', 'O'),)

    image = forms.ImageField(required=False, label='Portrait')
    name = forms.CharField(required=False, label='Name', max_length=150, help_text='Leave blank for a random value')
    character_class = forms.ChoiceField(required=False, label='Class', initial='', choices=valid_class, help_text='Leave blank for a random value')
    race = forms.ChoiceField(required=False, label='Race', initial='', choices=valid_race, help_text='Leave blank for a random value')
    alignment = forms.ChoiceField(required=False, label='Alignment', initial='', choices=valid_alignment, help_text='Leave blank for a random value')
    gender = forms.ChoiceField(required=False, initial='', choices=valid_gender, help_text='Leave blank for a random value')
    age = FloatOrBlankField(required=False, help_text='Leave blank for a random value')
    charisma = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    constitution = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    dexterity = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    intelligence = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    strength = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    wisdom = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    level = IntegerOrBlankField(required=False, help_text='Leave blank for a random value')
    platinum = IntegerOrBlankField(required=False, label='Platinum Pieces', help_text='Leave blank for a random value')
    gold = IntegerOrBlankField(required=False, label='Gold Pieces', help_text='Leave blank for a random value')
    silver = IntegerOrBlankField(required=False, label='Silver Pieces', help_text='Leave blank for a random value')
    copper = IntegerOrBlankField(required=False, label='Copper Pieces', help_text='Leave blank for a random value')

