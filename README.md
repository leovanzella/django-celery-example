# django-celery-example

A simple django app that uses celery for creating ```n```users asyncronously.

```celery -A mysite worker -l info```


Capturing celery task messages:

Receiving the task:

**[INFO/MainProcess] Received task: mysite.core.tasks.create_random_user_accounts[f8b94a1d-6047-4728-96a7-bdce604ed07f]**

And when the task sucessed:

**[INFO/ForkPoolWorker-4] Task mysite.core.tasks.create_random_user_accounts[f8b94a1d-6047-4728-96a7-bdce604ed07f] succeeded in 18.195066804s: '50 random users created with success!'**

Enjoy!
