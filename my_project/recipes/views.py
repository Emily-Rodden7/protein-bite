from django.shortcuts import render
from .models import ProteinRecipes


def home(request):
    recipes = ProteinRecipes.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def about(request):
    return render(request, 'recipes/about.html')


def recipes(request):
    return render(request, 'recipes/recipes.html')
