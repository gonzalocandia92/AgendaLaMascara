from django.apps import AppConfig


# cuando la aplicación se ejecuta, por defecto me va a cargar el archivo signals

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Perfiles'
    
    def ready(self):
        import accounts.signals