from django.shortcuts import render
from django.http import HttpResponse
#from .models import characters

def index(request):
    return render(request,
                  'characters/characters.html')

# def create(request):
#     if request.method == 'GET':
#         player_form = Players(request.GET)
#
#         return render(request,
#                     'player/base.html',
#                     {'player_list': player_form})
#     else:
#         player_form = Players()
#     return render(request,
#                   'player/base.html',
#                   {'player_list': player_form})