from django.shortcuts import render
from .models import ProteinRecipes


def home(request):
    Recipes = ProteinRecipes.objects.all()
    return render(request, 'Recipes/home.html', {'Recipes': Recipes})


def about(request):
    return render(request, 'Recipes/about.html')
