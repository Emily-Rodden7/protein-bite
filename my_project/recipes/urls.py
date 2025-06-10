from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes, name='recipes'),
    path('login/', views.login, name='login'),
    path('my_account/', views.my_account, name='my_account'),
]
