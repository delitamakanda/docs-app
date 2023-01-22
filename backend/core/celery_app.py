from celery import Celery

celery_app = Celery('core', broker='redis://localhost:6379/0')

celery_app.conf.task_routes = {
    'app.worker.test_celery': 'low-priority',
}