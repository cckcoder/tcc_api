from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model import UserBase, UserDisplayBase

from routers.users import users_controller
from utils.oauth2 import access_user_token


router = APIRouter(prefix="/users", tags=["users"])

# POST
@router.post("/")
def register_user(request: UserBase, db: Session = Depends(get_db)):
    return users_controller.create_user(db, request)


# GET
@router.get(
    "/", response_model=List[UserDisplayBase], dependencies=[Depends(access_user_token)]
)
def all_user(db: Session = Depends(get_db)):
    return users_controller.get_all_user(db)


# BET by id
@router.get(
    "/{user_id}",
    response_model=UserDisplayBase,
    dependencies=[Depends(access_user_token)],
)
def user_by_id(user_id: int, db: Session = Depends(get_db)):
    return users_controller.get_user_by_id(db, user_id)


# PUT
@router.put(
    "/{user_id}", response_model=UserBase, dependencies=[Depends(access_user_token)]
)
def user_by_id(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return users_controller.update_user(db, user_id, request)


# DELETE
@router.delete("/{user_id}", dependencies=[Depends(access_user_token)])
def user_by_id(user_id: int, db: Session = Depends(get_db)):
    return users_controller.deleted_user(db, user_id)
