from django.apps import AppConfig

from suit.apps import DjangoSuitConfig

class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    
