from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "work_lights.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
