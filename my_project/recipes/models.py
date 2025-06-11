from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProteinRecipes(models.Model):
    name = models.CharField(max_length=100)
    protein_grams = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

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
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.recipe}"
