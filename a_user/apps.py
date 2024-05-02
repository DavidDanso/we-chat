from django.apps import AppConfig


class AUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_user'

    def ready(self):
        import a_user.signals
