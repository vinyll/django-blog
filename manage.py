#!/usr/bin/env python
import os, sys
from init import *

sys.path.append(PYTHON_PACKAGES_ROOT)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
