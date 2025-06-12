from django.apps import AppConfig

class ProteinbiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proteinbite'

    def ready(self):
        import proteinbite.signals  # activates signals
