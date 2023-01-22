from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from pydantic import ValidationError
from pydantic.networks import EmailStr

from schema import UserCreate, UserUpdate
from schema import User as UserSchema
from models import User as UserModel
from crud import user as crud_user
from api import deps
from core.config import settings

router = APIRouter()

@router.get("/", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db), current_user: UserModel = Depends(deps.get_current_active_admin)) -> Any:
    """
    Retrieve users.
    """
    users = crud_user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db), current_user: UserModel = Depends(deps.get_current_active_admin)) -> Any:
    """
    Create new user.
    """
    user = crud_user.get_by_email(db, email=user.email)
    if user:
        raise HTTPException(status_code=400, detail="The user with this username already exists in the system.")
    user = crud_user.create(db, obj_in=user)
    return user

@router.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(deps.get_db), current_user: UserModel = Depends(deps.get_current_active_admin)) -> Any:
    """
    Update an user.
    """
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="The user with this username does not exist in the system")
    user = crud_user.update(db, db_obj=user, obj_in=user)
    return user


@router.delete("/{user_id}", response_model=UserSchema)
def delete_user(user_id: int, db: Session = Depends(deps.get_db), current_user: UserModel = Depends(deps.get_current_active_admin)) -> Any:
    """
    Delete an user.
    """
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="The user with this username does not exist in the system")
    user = crud_user.remove(db, id=user_id)
    return user

@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(deps.get_db), current_user: UserModel = Depends(deps.get_current_active_admin)) -> Any:
    """
    Get user by ID.
    """
    user = crud_user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud_user.is_admin(current_user):
        raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
    if not user:
        raise HTTPException(status_code=404, detail="The user with this username does not exist in the system")
    return user


@router.get("/me", response_model=UserSchema)
def read_me(current_user: UserModel = Depends(deps.get_current_active_user)) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/open", response_model=UserSchema)
def create_user_open(password: str = Body(...), email: EmailStr = Body(...), username: str = Body(None), db: Session = Depends(deps.get_db)) -> Any:
    """
    Create new user without authentication.
    """
    user = crud.get_user_by_email(db, email=email)
    if user:
        raise HTTPException(status_code=400, detail="The user with this username already exists in the system.")
    user_in = UserCreate(email=email, password=password, username=username)
    user = crud_user.create(db, obj_in=user_in)
    return user
