import os, sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PYTHON_PACKAGES_ROOT = os.path.join(PROJECT_ROOT, 'venv', 'lib', 'python2.6', 'site-packages')

sys.path.append(PYTHON_PACKAGES_ROOT)
sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
