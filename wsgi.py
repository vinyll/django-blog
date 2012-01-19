import os, sys
from init import *

sys.path.append(PYTHON_PACKAGES_ROOT)
sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
