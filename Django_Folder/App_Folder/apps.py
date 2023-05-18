from django.apps import AppConfig


class App_FolderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "App_Folder"
    
    def ready(self):
        from .ap_scheduler import start
        start()
