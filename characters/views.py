import random
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AdtCharacter, Category
from .forms import CharacterForm
import random_name_generator as rname

valid_alignment = ['Chaotic Evil', 'Chaotic Good', 'Chaotic Neutral',
                        'Lawful Evil', 'Lawful Good', 'Lawful Neutral',
                        'Neutral', 'Neutral Evil', 'Neutral Good']
valid_race = ['dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'half-orc', 'halfling',
                   'human', 'tiefling']
valid_class = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                    'sorcerer', 'warlock', 'wizard']
valid_gender = ['M', 'F', 'O']

@login_required
def character_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    characters = AdtCharacter.objects.filter(created_by=request.user.get_username())
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        characters = characters.filter(category=category)
    return render(request,
                  'characters/list.html',
                  {'category': category,
                   'categories': categories,
                   'characters': characters})


@login_required
def character_detail(request, id):
    character = get_object_or_404(AdtCharacter,
                                  id=id)
    return render(request,
                  'characters/detail.html',
                  {'character': character})


@login_required
def character_modify(request, id):
    character = get_object_or_404(AdtCharacter,
                                  id=id)
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # set xp based n level
            # set creadtedBy
            character.name = form.cleaned_data['name']
            character.image = request.FILES['image']
            character.character_class = form.cleaned_data['character_class']
            character.slug = form.cleaned_data['character_class']
            character.race = form.cleaned_data['race']
            character.alignment = form.cleaned_data['alignment']
            character.gender = form.cleaned_data['gender']
            character.age = form.cleaned_data['age']
            character.charisma = form.cleaned_data['charisma']
            character.constitution = form.cleaned_data['constitution']
            character.dexterity = form.cleaned_data['dexterity']
            character.intelligence = form.cleaned_data['intelligence']
            character.strength = form.cleaned_data['strength']
            character.wisdom = form.cleaned_data['wisdom']
            character.level = form.cleaned_data['level']
            character.platinum = form.cleaned_data['platinum']
            character.gold = form.cleaned_data['gold']
            character.silver = form.cleaned_data['silver']
            character.copper = form.cleaned_data['copper']
            character.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('characters'))

    # If this is a GET populate form with existing character data
    else:
        form = CharacterForm(initial={
                            'name': character.name,
                            'image': character.image.url,
                            'character_class': character.character_class,
                            'race': character.race,
                            'alignment': character.alignment,
                            'gender': character.gender,
                            'age': character.age,
                            'charisma': character.charisma,
                            'constitution': character.constitution,
                            'dexterity': character.dexterity,
                            'intelligence': character.intelligence,
                            'strength': character.strength,
                            'wisdom': character.wisdom,
                            'level': character.level,
                            'platinum': character.platinum,
                            'gold': character.gold,
                            'silver': character.silver,
                            'copper': character.copper})

    context = {
        'form': form,
        'character_instance': character,
    }

    return render(request, 'characters/edit.html', context)


@login_required
def character_add(request):

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():

            character = AdtCharacter()
            character.name = rname.generate(limit=1)[0] if not form.cleaned_data['name'] else form.cleaned_data['name']
            character.image = request.FILES['image']
            character.character_class = random.choice(valid_class) if form.cleaned_data['character_class'] is None else form.cleaned_data['character_class']
            character.category = Category.objects.get(name=character.character_class)
            character.race = random.choice(valid_race) if form.cleaned_data['race'] is None else form.cleaned_data['race']
            character.alignment = random.choice(valid_alignment) if form.cleaned_data['alignment'] is None else form.cleaned_data['alignment']
            character.gender = random.choice(valid_gender) if form.cleaned_data['gender'] is None else form.cleaned_data['gender']
            character.age = random.randint(1,9999) if form.cleaned_data['age'] is None else form.cleaned_data['age']
            character.charisma = random.randint(0,18) if form.cleaned_data['charisma'] is None else form.cleaned_data['charisma']
            character.constitution = random.randint(0,18) if form.cleaned_data['constitution'] is None else form.cleaned_data['constitution']
            character.dexterity = random.randint(0,18) if form.cleaned_data['dexterity'] is None else form.cleaned_data['dexterity']
            character.intelligence = random.randint(0,18) if form.cleaned_data['intelligence'] is None else form.cleaned_data['intelligence']
            character.strength = random.randint(0,18) if form.cleaned_data['strength'] is None else form.cleaned_data['strength']
            character.wisdom = random.randint(0,18) if form.cleaned_data['wisdom'] is None else form.cleaned_data['wisdom']
            character.level = random.randint(0,15) if form.cleaned_data['level'] is None else form.cleaned_data['level']
            character.experience_points = character.level * random.randint(100, 1000)
            character.platinum = random.randint(0,9999999) if form.cleaned_data['platinum'] is None else form.cleaned_data['platinum']
            character.gold = random.randint(0,9999999) if form.cleaned_data['gold'] is None else form.cleaned_data['gold']
            character.silver = random.randint(0,9999999) if form.cleaned_data['silver'] is None else form.cleaned_data['silver']
            character.copper = random.randint(0,9999999) if form.cleaned_data['copper'] is None else form.cleaned_data['copper']
            character.created_by = request.user.username
            character.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('characters'))
    else:
        context = {}
        context['form'] = CharacterForm()
        return render(request, 'characters/add.html', context)