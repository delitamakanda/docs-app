from typing import Any, Dict, List, Optional, Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api import deps
from schema import Post, PostCreate, PostUpdate
from crud import post, user
from models import User


router = APIRouter()

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_active_user)):
    """
    Retrieve posts.
    """
    if user.is_admin(current_user):
        posts = post.get_multi(db, skip=skip, limit=limit)
    else:
        posts = post.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)
    return posts


@router.post("/", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_active_user)):
    """
    Create a new post.
    """
    if not user.is_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action."
        )
    post = post.create_with_owner(db=db, obj_in=post, owner_id=current_user.id)
    return post


@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_active_user)):
    """
    Update a post.
    """
    if not user.is_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action."
        )
    post = post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The post with this id does not exist in the system."
        )
    post = post.update(db=db, db_obj=post, obj_in=post)
    return post

@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_active_user)):
    """
    Get a post.
    """
    post = post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The post with this id does not exist in the system."
        )
    if not user.is_admin(current_user) and (post.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action."
        )
    return post


@router.delete("/{post_id}", response_model=Post)
def delete_post(post_id: int, db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_active_user)):
    """
    Delete a post.
    """
    post = post.get(db=db, id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The post with this id does not exist in the system."
        )
    if not user.is_admin(current_user) and (post.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to perform this action."
        )
    post = post.remove(db=db, id=post_id)
    return post
