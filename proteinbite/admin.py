from django.contrib import admin
from .models import ProteinRecipes, Comment


class ProteinRecipesAdmin(admin.ModelAdmin):
    list_display = ('name', 'protein_grams')
    fields = ('name', 'protein_grams', 'meat_type', 'calories', 'serves', 'description', 'ingredients', 'method', 'image')


admin.site.register(ProteinRecipes, ProteinRecipesAdmin)
admin.site.register(Comment)
