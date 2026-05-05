#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # The project root holds the dead_code_salon package; the inner directory
    # holds the apps (core, etc.) so both need to be on sys.path.
    here = os.path.dirname(os.path.abspath(__file__))
    inner = os.path.join(here, 'dead_code_salon')
    if inner not in sys.path:
        sys.path.insert(0, inner)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dead_code_salon.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed: pip install django"
        ) from exc
    execute_from_command_line(sys.argv)
