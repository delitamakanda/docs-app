from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

from fastapi import APIRouter, Depends, HTTPException, status
from core.celery_app import celery_app
from models import User as UserModel
from schema import Msg as MsgSchema
from api import deps

router = APIRouter()

@router.post('/test-celery/', response_model=MsgSchema, status_code=201)
def test_celery(
    msg: MsgSchema,
    current_user: UserModel = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Test Celery.
    """
    celery_app.send_task('app.worker.test_celery', args=[msg.msg])
    return {'msg': 'Celery task started'}
