from django.apps import AppConfig


def ready(self):
    import agenda.signals  # importa el archivo para que se activen los signals


class AgendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agenda'
