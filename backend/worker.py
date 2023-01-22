from app.core.celery_app import celery_app
from app.core.config import settings

@celery_app.task(acks_late=True)
def test_celery(word):
    return f'test celery {word}'