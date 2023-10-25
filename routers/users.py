from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from services.db_service import get_db

from schemas.user_schema import CreateUser, ShowUser
from database.models import User
from services.passwords import pwd_context

user_router = APIRouter()

@user_router.get("/{id}", response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with the id of {id} is not avilable")
    
    return user


@user_router.post("/", response_model=ShowUser)
def create_a_user(user: CreateUser, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    new_user = User(first_name=user.first_name, last_name=user.last_name, username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user