
import random
import tempfile

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import AdtCharacter, Category
from .forms import CharacterForm
from django.core.files import File



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
        form = CharacterForm(request.POST, files=request.FILES)
        # Check if the form is valid:
        if form.is_valid():
            #character.name = form.cleaned_data['name']
            #character.image = request.FILES['image']
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
        data = {
                'name': character.name,
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
                'copper': character.copper
        }

        form = CharacterForm(instance=character, files=request.FILES)

    context = {
        'form': form,
        'character': character,
    }

    return render(request, 'characters/edit.html', context)


@login_required
def character_add(request):

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():

            character = AdtCharacter()
            character.name = form.cleaned_data['name']
            character.character_class = form.cleaned_data['character_class']
            character.category = Category.objects.get(name=character.character_class)
            character.slug = character.character_class
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
            character.experience_points = random.randint(1*character.level, 9999*character.level)
            character.platinum = form.cleaned_data['platinum']
            character.gold = form.cleaned_data['gold']
            character.silver = form.cleaned_data['silver']
            character.copper = form.cleaned_data['copper']

            character.created_by = request.user.username
            # if not request.FILES.get('image', False):
            #     from urllib.request import urlopen
            #     url = "https://picsum.photos/id/1/200/300"
            #     img_temp = tempfile.NamedTemporaryFile(delete=True)
            #     img_temp.write(urlopen(url).read())
            #     img_temp.flush()
            #     character.image.save('img.jpg', File(img_temp))
            #
            # else:
            #     character.image = request.FILES['image']
            character.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('characters'))
    else:
        context = {}
        context['form'] = CharacterForm()
        return render(request, 'characters/add.html', context)