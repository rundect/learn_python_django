from datetime import datetime

from celery import Celery

app = Celery()


@app.task()
def one():
    print('start 1', datetime.now())


@app.task()
def two():
    print('start 2', datetime.now())

    print('end 2', datetime.now())
