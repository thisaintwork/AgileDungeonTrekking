from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, AdtCharacter
from .forms import CharacterAddForm

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


def character_edit(request, id):
    character = get_object_or_404(AdtCharacter,
                                  id=id)
    context = {}
    context['form'] = CharacterAddForm()
    return render(request,
                  'characters/edit.html', context,
                  {'character': character})

def character_add(request):
    context = {}
    context['form'] = CharacterAddForm()
    return render(request,
                  context,
                  'characters/add.html')