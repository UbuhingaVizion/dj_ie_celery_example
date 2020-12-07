# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as dj_celery_app

__all__ = ("dj_celery_app",)
