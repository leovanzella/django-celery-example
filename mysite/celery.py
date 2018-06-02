from __future__ import absolute_import, unicode_literals

import os
import celery

if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


class Celery(celery.Celery):
    def on_configure(self):
        pass


app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()