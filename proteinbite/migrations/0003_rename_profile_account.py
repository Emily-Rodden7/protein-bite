# Generated by Django 4.2.22 on 2025-06-10 17:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proteinbite', '0002_rename_proteinrecipe_proteinrecipes_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='account',
        ),
    ]
