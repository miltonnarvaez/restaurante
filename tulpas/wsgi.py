"""
WSGI config for tulpas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tulpas.settings')
if os.environ.get('RENDER') == 'true':
    from tulpas.create_superuser import *  # cambia esto por la ruta real
  
application = get_wsgi_application()
