from __future__ import absolute_import, unicode_literals

import os
import celery
from celery.schedules import crontab


if os.environ.get('DJANGO_SETTINGS_MODULE') is None:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


class Celery(celery.Celery):
    def on_configure(self):
        pass


app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# disable UTC so that Celery can use local time
app.conf.enable_utc = False

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10', expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=4, minute="*"),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)