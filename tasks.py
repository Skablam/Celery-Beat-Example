from celery import Celery
import os

celery = Celery('tasks', broker=os.environ['REDIS_URL'])
celery.config_from_object('celeryconfig')

@celery.task(name="tasks.bob")
def gather_markets():
    print("markets_gathered")
