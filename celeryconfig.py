from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # Executes every morning at 7:00 A.M
    'every-day-at-7': {
        'task': 'tasks.bob',
        'schedule': crontab(hour=13, minute=06),
        'args': (),
    },
}
