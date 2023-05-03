from django.apps import AppConfig


class DoctorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctors'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
