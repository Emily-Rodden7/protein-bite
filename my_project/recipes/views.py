from django.shortcuts import render
from .models import ProteinRecipe


def home(request):
    snacks = ProteinRecipe.objects.all()
    return render(request, 'snacks/home.html', {'snacks': snacks})


def about(request):
    return render(request, 'Recipes/about.html')
