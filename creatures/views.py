from django.shortcuts import render
from django.http import HttpResponse
#from .models import characters

def index(request):
    return HttpResponse("Hello, world. You're at the creatures page.")