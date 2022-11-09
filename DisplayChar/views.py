from django.shortcuts import render
from dnd_character import Character
from dnd_character.classes import CLASSES

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

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


