from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Category, AdtCharacter
from .forms import CharacterForm

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

def character_detail(request, id, slug):
    character = get_object_or_404(AdtCharacter,
                                  id=id,
                                  slug=slug)
    return render(request,
                  'characters/detail.html',
                  {'character': character})


@login_required
def character_edit(request, id):
    character = get_object_or_404(AdtCharacter,
                                  id=id)
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # set xp based n level
            # set creadtedBy
            character.name = form.cleaned_data['name']
            character.image = form.cleaned_data['image']

            character.character_class = form.cleaned_data['image']
            character.race = form.cleaned_data['image']
            character.alignment = form.cleaned_data['image']
            character.gender = form.cleaned_data['name']
            character.age = form.cleaned_data['name']
            character.charisma = form.cleaned_data['name']
            character.constitution = form.cleaned_data['name']
            character.dexterity = form.cleaned_data['name']
            character.intelligence = form.cleaned_data['name']
            character.strength = form.cleaned_data['name']
            character.wisdom = form.cleaned_data['name']
            character.level = form.cleaned_data['name']
            character.platinum = form.cleaned_data['name']
            character.gold = form.cleaned_data['name']
            character.silver = form.cleaned_data['name']
            character.copper = form.cleaned_data['name']
            character.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('list'))

    # If this is a GET populate form with existing character data
    else:

        form = CharacterForm()
        form.name = character.name
        form.image = character.image
        form.character_class = character.character_class
        form.race = character.race
        form.alignment = character.alignment
        form.gender = character.gender
        form.age = character.age
        form.charisma = character.charisma
        form.constitution = character.constitution
        form.dexterity = character.dexterity
        form.intelligence = character.intelligence
        form.strength = character.strength
        form.wisdom = character.wisdom
        form.level = character.level
        form. platinum = character.platinum
        form.gold = character.gold
        form.silver = character.silver
        form.copper = character.copper

    context = {
        'form': form,
        'character_instance': character,
    }

    return render(request, 'characters/edit.html', context)

def character_add(request):
    context = {}
    context['form'] = CharacterForm()
    return render(request,
                  context,
                  'characters/add.html')