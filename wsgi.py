import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'venv', 'lib', 'python2.6', 'site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
