from django.apps import AppConfig

# from api.utils import check_database_empty


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

