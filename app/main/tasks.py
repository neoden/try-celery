import time

import dramatiq
from celery.utils.log import get_task_logger

from app.celery import app


logger = get_task_logger(__name__)


@app.task(acks_late=True)
def dummy(fail=False):
    if fail:
        time.sleep(2)
        raise ValueError("This task failed")
    time.sleep(5)
    logger.info('Dummy task finished')


@dramatiq.actor
def dramatiq_dummy(fail=False):
    if fail:
        time.sleep(2)
        raise ValueError("This task failed")
    time.sleep(5)
    logger.info('Dummy task finished')
