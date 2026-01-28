# config/context_processors.py
from core.models import AppConfig
from django.db.utils import ProgrammingError, OperationalError


def app_settings(request):
    try:
        config, _ = AppConfig.objects.get_or_create(id=1)
    except (ProgrammingError, OperationalError):
        config = None

    return {
        'app_config': config
    }