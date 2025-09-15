from django.apps import AppConfig

class MissingchildappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # fix warning
    name = 'MissingChildApp'
