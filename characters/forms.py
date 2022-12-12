import random
from django import forms
from .models import AdtCharacter
import names
from django.core.exceptions import ValidationError

class CharacterForm(forms.ModelForm):
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

    #image = forms.ImageField(required=False, label='Portrait')
    name = forms.CharField(required=False, label='Name', max_length=150, help_text='Leave blank for a random value')
    character_class = forms.ChoiceField(required=False, label='Class', initial='', choices=valid_class)
    race = forms.ChoiceField(required=False, label='Race', initial='', choices=valid_race)
    alignment = forms.ChoiceField(required=False, label='Alignment', initial='', choices=valid_alignment)
    gender = forms.ChoiceField(required=False, initial='', choices=valid_gender)
    age = forms.FloatField(required=False, help_text='Leave blank for a random value')
    charisma = forms.IntegerField(required=False, label='Charisma', help_text='Leave blank for a random value')
    constitution = forms.IntegerField(required=False, help_text='Leave blank for a random value')
    dexterity = forms.IntegerField(required=False, help_text='Leave blank for a random value')
    intelligence = forms.IntegerField(required=False, help_text='Leave blank for a random value')
    strength = forms.IntegerField(required=False, help_text='Leave blank for a random value')
    wisdom = forms.IntegerField(required=False, help_text='Leave blank for a random value')
    level = forms.IntegerField(required=False, help_text='Leave blank for a random value')
    platinum = forms.IntegerField(required=False, label='Platinum Pieces', help_text='Leave blank for a random value')
    gold = forms.IntegerField(required=False, label='Gold Pieces', help_text='Leave blank for a random value')
    silver = forms.IntegerField(required=False, label='Silver Pieces', help_text='Leave blank for a random value')
    copper = forms.IntegerField(required=False, label='Copper Pieces', help_text='Leave blank for a random value')

    def clean_name(self):
        """ Choose random value if blank """
        data = self.cleaned_data['name']
        if not data:
            return names.get_full_name()
        return data

    def clean_character_class(self):
        """ Choose random value if blank """
        data = self.cleaned_data['character_class']
        if not data:
            return random.choice(self.valid_class)
        return data

    def clean_race(self):
        """ Choose random value if blank """
        data = self.cleaned_data['race']
        if not data:
            return random.choice(self.valid_race)
        return data
    def clean_alignment(self):
        """ Choose random value if blank """
        data = self.cleaned_data['alignment']
        if not data:
            return random.choice(self.valid_alignment)
        return data
    def clean_gender(self):
        """ Choose random value if blank """
        data = self.cleaned_data['gender']
        if not data:
            return random.choice(self.valid_gender)
        return data

    def clean_charisma(self):
        """ Choose random value if blank """
        data = self.cleaned_data['charisma']
        if not data:
            return random.randint(3, 18)
        if data < 3 or data > 18:
            raise ValidationError('Invalid value, must be >=3 and <=18')
        return data

    def clean_constitution(self):
        """ Choose random value if blank """
        data = self.cleaned_data['constitution']
        if not data:
            return random.randint(3, 18)
        if data < 3 or data > 18:
            raise ValidationError('Invalid value, must be >=3 and <=18')
        return data

    def clean_dexterity(self):
        """ Choose random value if blank """
        data = self.cleaned_data['dexterity']
        if not data:
            return random.randint(3, 18)
        if data < 3 or data > 18:
            raise ValidationError('Invalid value, must be >=3 and <=18')
        return data

    def clean_intelligence(self):
        """ Choose random value if blank """
        data = self.cleaned_data['intelligence']
        if not data:
            return random.randint(3, 18)
        if data < 3 or data > 18:
            raise ValidationError('Invalid value, must be >=3 and <=18')
        return data

    def clean_strength(self):
        """ Choose random value if blank """
        data = self.cleaned_data['strength']
        if not data:
            return random.randint(3, 18)
        if data < 3 or data > 18:
            raise ValidationError('Invalid value, must be >=3 and <=18')
        return data

    def clean_wisdom(self):
        """ Choose random value if blank """
        data = self.cleaned_data['wisdom']
        if not data:
            return random.randint(3, 18)
        if data < 3 or data > 18:
            raise ValidationError('Invalid value, must be >=3 and <=18')
        return data

    def clean_level(self):
        """ Choose random value if blank """
        data = self.cleaned_data['level']
        if not data:
            return random.randint(1, 20)
        return data

    def clean_age(self):
        """ Choose random value if blank """
        data = self.cleaned_data['age']
        if not data:
            return random.randint(1, 2000)
        return data

    def clean_platinum(self):
        """ Choose random value if blank """
        data = self.cleaned_data['platinum']
        if not data:
            return random.randint(1, 1000)
        return data

    def clean_gold(self):
        """ Choose random value if blank """
        data = self.cleaned_data['gold']
        if not data:
            return random.randint(1, 2000)
        return data

    def clean_silver(self):
        """ Choose random value if blank """
        data = self.cleaned_data['silver']
        if not data:
            return random.randint(1, 20000)
        return data

    def clean_copper(self):
        """ Choose random value if blank """
        data = self.cleaned_data['copper']
        if not data:
            return random.randint(1, 20000)
        return data

    class Meta:
        model = AdtCharacter
        fields = ['name', 'character_class', 'race', 'alignment', 'gender', 'age',
                  'charisma', 'constitution', 'dexterity', 'intelligence', 'strength', 'wisdom',
                  'level', 'platinum', 'gold', 'silver', 'copper']