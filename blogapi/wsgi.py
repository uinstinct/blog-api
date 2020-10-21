from pathlib import Path

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogapi.settings')

application = get_wsgi_application()
