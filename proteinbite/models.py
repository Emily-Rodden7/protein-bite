from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProteinRecipes(models.Model):
    name = models.CharField(max_length=100)
    protein_grams = models.IntegerField()
    calories = models.IntegerField(null=True, blank=True)
    serves = models.CharField(max_length=100, blank=True)
    meat_type = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    image = models.ImageField(upload_to='media/recipe_images/', blank=True, null=True)

    class Meta:
        verbose_name = "Protein Recipe"
        verbose_name_plural = "Protein Recipes"

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phonenumber = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Account"


@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()


class Comment(models.Model):
    recipe = models.ForeignKey(ProteinRecipes, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # logged-in user
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recipe.name}'
