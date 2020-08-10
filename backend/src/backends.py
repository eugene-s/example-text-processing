#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("CELERY_APP", "textanalyzer.celery")
    try:
        from celery.__main__ import main
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Celery. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    sys.exit(main())


if __name__ == '__main__':
    main()
