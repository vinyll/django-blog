import os, sys

PROJECT_ROOT = sys.path.append(os.path.abspath(os.path.dirname(__file__)))

sys.path.append(
    os.path.join(PROJECT_ROOT, 'venv', 'lib', 'python2.6', 'site-packages'),
    PROJECT_ROOT,
    )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
