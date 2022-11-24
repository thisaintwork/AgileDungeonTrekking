from django.shortcuts import render
from django.http import HttpResponse
#from .models import characters

def index(request):
    return render(request,
                  'creatures/creatures.html')