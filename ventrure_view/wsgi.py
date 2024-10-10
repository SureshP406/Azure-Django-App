"""
WSGI config for ventrure_view project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ventrure_view.settings')  ##Default/Original setting

settings_module = 'ventrure_view.production' if 'WEBSITE_HOSTNAME' in os.environ else 'ventrure_view.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
