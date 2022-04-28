# users/users_controller.py
from locale import delocalize
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from models.users.users_model import DbUser, UserBase

from utils.hash import Hash

# TODO

# Create users
def create_user(db: Session, request: UserBase):
    new_user = DbUser(username=request.username, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get all users
def get_all_user(db: Session):
    return db.query(DbUser).order_by(DbUser.created_date.desc()).all()


# Get user by id
def get_user_by_id(db: Session, user_id: int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()


# update
def update_user(db: Session, user_id: int, requset: UserBase):
    user = db.query(DbUser).filter(DbUser.id == user_id)
    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with {user_id} not found",
        )
    else:
        user.update(
            {
                DbUser.username: requset.username,
                DbUser.password: Hash.bcrypt(requset.password),
            }
        )
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"detail": f"user id {user_id} updated succesful!"},
        )


# delete
def deleted_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user id: {user_id} not found",
        )
    else:
        db.delete(user)
        db.commit()
        return JSONResponse(
            content={"detial": f"user id {user_id} deleted succesful!"},
            status_code=status.HTTP_200_OK,
        )
