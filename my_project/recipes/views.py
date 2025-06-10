from django.shortcuts import render, redirect
from .models import ProteinRecipes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


def home(request):
    recipes = ProteinRecipes.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def about(request):
    return render(request, 'recipes/about.html')


def recipes(request):
    return render(request, 'recipes/recipes.html')


def login(request):
    form = UserCreationForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/login.html', {'form': form})


def my_account(request):
    return render(request, 'recipes/my_account.html')
