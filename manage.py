#!/usr/bin/env python
import os, sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'venv', 'lib', 'python2.7', 'site-packages'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
