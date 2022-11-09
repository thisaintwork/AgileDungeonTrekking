from django.shortcuts import render
from django.http import HttpResponse
from .models import Players

def index(request):
    return HttpResponse("Hello, world. You're at the players page.")

def create(request):
    if request.method == 'GET':
        player_form = Players(request.GET)

        return render(request,
                    'player/base.html',
                    {'player_list': player_form})
    else:
        player_form = Players()
    return render(request,
                  'player/base.html',
                  {'player_list': player_form})