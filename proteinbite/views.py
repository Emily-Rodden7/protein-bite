from django.shortcuts import render, redirect
from .models import ProteinRecipes
from .models import Account
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404

def home(request):
    recipes = ProteinRecipes.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})

def about(request):
    return render(request, 'recipes/about.html')

def recipes(request):
    recipe_list = ProteinRecipes.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipe_list})

# register account
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

        # Log the user in immediately
        login(request, user)

        messages.success(request, "Account created successfully!")
        return redirect('account')  # Redirect them to their account page
    else:
        return render(request, 'recipes/register.html')

from django.contrib import messages

#login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('account')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'recipes/login.html')
    return render(request, 'recipes/login.html')

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

@login_required
def account(request):
    return render(request, 'recipes/account.html')

#  adding comments to recipes

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(ProteinRecipes, id=recipe_id)
    comments = recipe.comments.all().order_by('-created_at')

    if request.user.is_authenticated and request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        comment_form = CommentForm()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form
    })