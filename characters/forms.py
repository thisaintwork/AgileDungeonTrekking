from django import forms

class CharacterAddForm(forms.Form):
    """
    Create a new character and add to user's list

    Make sure to bind image data to form:
    https://docs.djangoproject.com/en/4.1/ref/forms/api/#binding-uploaded-files
    """
    valid_race = (('1','dragonborn'),
            ('2','dwarf'),
            ('3','elf'),
            ('4','gnome'),
            ('5','half-elf'),
            ('6','half-orc'),
            ('7','halfling'),
            ('8','human'),
            ('9','tiefling'))

    valid_alignment = (('1','Chaotic Evil'), ('2','Chaotic Good'), ('3','Chaotic Neutral'),
                 ('4','Lawful Evil'), ('5','Lawful Good'), ('6','Lawful Neutral'),
                 ('7','Neutral'), ('8','Neutral Evil'), ('9','Neutral Good'))

    valid_class = (('1','barbarian'), ('2','bard'), ('3','cleric'), ('4','druid'), ('5','fighter'), ('6','monk'),
                 ('7','paladin'), ('8','ranger'), ('9','rogue'), ('10','sorcerer'), ('11','warlock'), ('12','wizard'))

    valid_gender = (('1', 'M'), ('2', 'F'), ('3', 'O'))

    name = forms.CharField(max_length=150)
    character_class = forms.ChoiceField(choices=valid_class)
    race = forms.ChoiceField(choices=valid_race)
    alignment = forms.ChoiceField(choices=valid_alignment)
    gender = forms.ChoiceField(choices=valid_gender)

    age = forms.FloatField()
    charisma = forms.IntegerField()
    constitution = forms.IntegerField()
    dexterity = forms.IntegerField()
    intelligence = forms.IntegerField()
    strength = forms.IntegerField()
    wisdom = forms.IntegerField()
    level = forms.IntegerField()
    experience_points = forms.IntegerField()
    platinum = forms.IntegerField()
    gold = forms.IntegerField()
    silver = forms.IntegerField()
    copper = forms.IntegerField()
    image = forms.ImageField()
    created_by = forms.CharField(max_length=100)
