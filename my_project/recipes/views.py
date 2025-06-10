from django.shortcuts import render, redirect
from .models import ProteinRecipes
from .models import Account
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    recipes = ProteinRecipes.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})


def about(request):
    return render(request, 'recipes/about.html')


def recipes(request):
    return render(request, 'recipes/recipes.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1)
        user.save()
        messages.success(request,
                         "Account created successfully! Please log in.")
        return redirect('login')
    else:
        return render(request, 'recipes/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
    return render(request, 'recipes/login.html')


def account(request):
    return render(request, 'recipes/account.html')


@login_required
def edit_account(request):
    user = request.user

    account_obj, created = Account.objects.get_or_create(user=user)

    if request.method == 'POST':
        account_obj.address = request.POST.get('address', '')
        account_obj.phonenumber = request.POST.get('phonenumber', '')
        account_obj.save()
        return redirect('account')

    return render(request, 'recipes/edit_account.html', {
        'account': account_obj
    })
