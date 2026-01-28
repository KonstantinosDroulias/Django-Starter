# core/context_processors.py
from django.conf import settings

def global_settings(request):
    return {
        'APP_NAME': settings.APP_NAME,
        'APP_TAGLINE': settings.TAGLINE,
        'APP_AUTHOR': settings.AUTHOR,
    }