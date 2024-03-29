from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MessagingConfig(AppConfig):
    name = 'schooling.messaging'
    verbose_name = _("Messaging")

    def ready(self):
        try:
            import schooling.messaging.signals  # noqa F401
        except ImportError:
            pass

