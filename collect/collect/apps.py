from django.apps import AppConfig


class CollectConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "collect"
    label = "collect"
    verbose_name = "Collectibles"

    dpy_package = "collect.package"