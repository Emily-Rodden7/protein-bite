from django.contrib import admin
from .models import ProteinRecipes

admin.site.register(ProteinRecipes)

from .models import Recipe, Comment
admin.site.register(Comment)