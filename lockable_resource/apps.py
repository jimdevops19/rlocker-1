from django.apps import AppConfig


class LockableResourceConfig(AppConfig):
    name = "lockable_resource"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        """
        We override the ready method of AppConfig, so the application
            could start listening to the signal we create in signals.py
        :return: None
        """

        import lockable_resource.signals
