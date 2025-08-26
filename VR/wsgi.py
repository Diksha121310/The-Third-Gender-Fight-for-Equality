
"""
WSGI config for VR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
import sys, traceback
from django.core.wsgi import get_wsgi_application

try:
    application = get_wsgi_application()
except Exception:
    traceback.print_exc(file=sys.stdout)
    raise

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VR.settings')

application = get_wsgi_application()
