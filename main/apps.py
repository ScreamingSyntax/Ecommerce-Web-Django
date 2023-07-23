from django.apps import AppConfig
# from main import signals>

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    def ready(self):
        import main.signals
