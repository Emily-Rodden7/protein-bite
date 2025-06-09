from django.db import models


class ProteinRecipe(models.Model):
    name = models.CharField(max_length=100)
    protein_grams = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
